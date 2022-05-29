#!/usr/bin/env python3

import os
import shutil
import yaml


def checkMimes(file, allowed_extensions):
    """Check if the file is in the correct extensions list, if not, return False"""
    if os.path.splitext(file)[1] in allowed_extensions:
        file_valid = True
    else:
        file_valid = False
    return file_valid


def handleLocalTorrents(torrent_dir, initial_dir, move_file=False):
    """move .torrent files to initial_dir"""
    torrents_found = 0

    with os.scandir(initial_dir) as localdir:
        for entry in localdir:
            # check if file is correct type
            if entry.is_file() and checkMimes(entry, ".torrent"):
                print(f"Found torrent file ::: {entry.name}")
                torrents_found += 1
                if move_file:
                    shutil.move(entry, torrent_dir)
                    print(f"Moved to {torrent_dir}")
        if torrents_found == 0:
            print(f"No torrent files found to process in {initial_dir}")
        else:
            print(f"proceesed {os.path(initial_dir)}")


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


def moveManager(torrents, torrent_dir):
    for torrent in torrents:
        shutil.move(torrent, torrent_dir)


def yamlDataExtract(config_file="config.yaml"):

    with open("config.yaml", "r") as config:
        try:
            data = yaml.safe_load(config)
            return data
        except yaml.YAMLError as exc:
            print(exc)


def putFile(filename, ftp):
    """open file filename and put on ftp server. assumes connection is open."""
    with open(filename, "rb") as binary:
        ftp.storbinary(f"STOR {filename}", filename)
