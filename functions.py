#!/usr/bin/env python3

import os
import shutil
import yaml
import libtorrent as lt
import ftplib
import re


def checkMimes(file, allowed_extensions):
    """Check if the file is in the correct extensions list, if not, return False"""
    if os.path.splitext(file)[1] in allowed_extensions:
        file_valid = True
    else:
        file_valid = False
    return file_valid


def checkIfFolder(path):
    if os.path.splitext(path)[1] == "":
        is_Folder = True
    else:
        is_Folder = False
    return is_Folder


def torrentIdentifier(directory):
    torrents = []
    with os.scandir(directory) as localdir:
        for entry in localdir:
            # check if file is correct type
            if entry.is_file() and checkMimes(entry, ".torrent"):
                # print(f"Found torrent file ::: {entry.name}")
                torrents.append(entry)
    return torrents


def getDiffList(a, b):
    """get members of a not present in b, return list of members"""
    difflist = [x for x in a if x not in b]
    return difflist


# TODO: handle file already exists
def moveManager(torrents, torrent_dir):
    for torrent in torrents:
        try:
            shutil.move(torrent.path, torrent_dir)
        except Exception as e:
            raise Exception(e)


def yamlDataExtract(config_file="config.yaml"):
    with open("config.yaml", "r") as config:
        try:
            data = yaml.safe_load(config)
            return data
        except yaml.YAMLError as exc:
            print(exc)


def getTorrentDiffList(torrent_dir, target_dir):
    """return a list of all the torrents in torrent_dir not present in target_dir"""
    torrents = getDiffList(
        torrentIdentifier(torrent_dir), torrentIdentifier(target_dir)
    )
    return torrents


def getFileNamefromTorrent(torrent):
    """must be a direntry item. Gets the name of the torrent's finished folder from the .torrent file."""
    torrent_info = lt.torrent_info(torrent.path)
    return torrent_info.name()


###############################################################################
#                           Below needs integration.                          #
###############################################################################


def _is_ftp_dir(ftp_handle, name, guess_by_extension=True):
    """simply determines if an item listed on the ftp server is a valid directory or not"""

    # if the name has a "." in the fourth to last position, its probably a file extension
    # this is MUCH faster than trying to set every file to a working directory, and will work 99% of time.
    if guess_by_extension is True:
        if len(name) >= 4:
            if name[-4] == ".":
                return False

    original_cwd = ftp_handle.pwd()  # remember the current working directory
    try:
        ftp_handle.cwd(name)  # try to set directory to new name
        ftp_handle.cwd(original_cwd)  # set it back to what it was
        return True

    except ftplib.error_perm as e:
        print(e)
        return False

    except Exception as e:
        print(e)
        return False


def _make_parent_dir(fpath):
    """ensures the parent directory of a filepath exists"""
    dirname = os.path.dirname(fpath)
    while not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
            print("created {0}".format(dirname))
        except OSError as e:
            print(e)
            _make_parent_dir(dirname)


def _download_ftp_file(ftp_handle, name, dest, overwrite):
    """downloads a single file from an ftp server"""
    _make_parent_dir(dest.lstrip("/"))
    if not os.path.exists(dest) or overwrite is True:
        try:
            with open(dest, "wb") as f:
                ftp_handle.retrbinary("RETR {0}".format(name), f.write)
            print("downloaded: {0}".format(dest))
        except FileNotFoundError:
            print("FAILED: {0}".format(dest))
    else:
        print("already exists: {0}".format(dest))


def _file_name_match_patern(pattern, name):
    """returns True if filename matches the pattern"""
    if pattern is None:
        return True
    else:
        return bool(re.match(pattern, name))


def _mirror_ftp_dir(ftp_handle, name, overwrite, guess_by_extension, pattern):
    """replicates a directory on an ftp server recursively"""
    for item in ftp_handle.nlst(name):
        if _is_ftp_dir(ftp_handle, item, guess_by_extension):
            _mirror_ftp_dir(ftp_handle, item, overwrite, guess_by_extension, pattern)
        else:
            if _file_name_match_patern(pattern, name):
                _download_ftp_file(ftp_handle, item, item, overwrite)
            else:
                # quietly skip the file
                pass


def download_ftp_tree(
    ftp_handle,
    path,
    destination,
    pattern=None,
    overwrite=False,
    guess_by_extension=True,
):
    path = path.lstrip("/")
    original_directory = (
        os.getcwd()
    )  # remember working directory before function is executed
    os.chdir(destination)  # change working directory to ftp mirror directory

    _mirror_ftp_dir(
        ftp_handle,
        path,
        pattern=pattern,
        overwrite=overwrite,
        guess_by_extension=guess_by_extension,
    )

    os.chdir(
        original_directory
    )  # reset working directory to what it was before function exec
