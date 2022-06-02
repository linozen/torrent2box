#!/usr/bin/env python3

import os
import sys
import ftplib  # this package allows for ftp login.
import shutil
import functions
import argparse  # this package allows for arg parsing
import ftplib

import connectionhandler

# import pysftp

# TODO first, get name of From folder and Too folder
# argv = sys.argv

# Handle the config file
config = functions.yamlDataExtract()

TORRENT_DIR = config["torrent_dir"]
TARGET_DIR = config["target_dir"]
SEEDBOX_ADDR = config["seedbox_addr"]
SEEDBOX_LOGIN = config["seedbox_login"]
SEEDBOX_PW = config["seedbox_pw"]

# fileObject = open(
#     "Eric Dolphy - Iron Man - 1971 (Vinyl - FLAC - 24bit Lossless)-1671921.torrent",
#     "rb",
# )
# file2BeSavedAs = (
#     "Eric Dolphy - Iron Man - 1971 (Vinyl - FLAC - 24bit Lossless)-1671921.torrent"
# )

# sys.exit("SCRIPT TERMINATED BY BREAKER")
# TARGET_DIR, TORRENT_DIR =
from_torrents = functions.torrentIdentifier(TARGET_DIR)
to_torrents = functions.torrentIdentifier(TORRENT_DIR)

# create list of torrent files present in from_torrents, not present in to_torrents
torrents = functions.getDiffList(from_torrents, to_torrents)

num_torrents = len(torrents)
if num_torrents > 0:
    print(f"Found {num_torrents} new torrents")
    functions.moveManager(torrents, TORRENT_DIR)
else:
    print("No new torrents found.")


for entry in torrents:
    print(f"Found torrent file ::: {entry.name}")


# initiate the connection
sftp = connectionhandler.SeedboxFTP(SEEDBOX_ADDR, SEEDBOX_LOGIN, SEEDBOX_PW)

sftp.connect()

# set CWD to Watch folder
sftp.changeWorkingDirectory(remotePath="watch")

# loop through torrent list, and send them to the seedbox
# for torrent in torrents:
#     sftp.testUpload(torrent)
print(os.getcwd())
# disconnect
sftp.disconnect()
