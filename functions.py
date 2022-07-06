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
    """Check if a path is a folder or a file."""
    if os.path.splitext(path)[1] == "":
        is_Folder = True
    else:
        is_Folder = False
    return is_Folder


def torrentIdentifier(directory):
    """generates a list of torrents - if torrent is file and ends in .torrent, add it to list."""
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
    """move files (expects posix) from target directory to torrent directory"""
    for torrent in torrents:
        try:
            shutil.move(torrent.path, torrent_dir)
        except Exception as e:
            raise Exception(e)


def yamlDataExtract(config_file="config.yaml"):
    """Handle the yaml data, load it into the space safely."""
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
