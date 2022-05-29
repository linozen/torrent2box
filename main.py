#!/usr/bin/env python3

import os
import sys
import ftplib  # this package allows for ftp login.
import shutil
import functions
import argparse  # this package allows for arg parsing

# TODO first, get name of From folder and Too folder
# argv = sys.argv

## Directories
# This is where you want the torrents to be managed
# TORRENT_DIR = "~/org/projects/Dev/Python/seed_dl/torrentfiles/"

# This is the directory where the torrent files are dumped by the browser
# TARGET_DIR = "~/Downloads/"

#     ftp.dir("watch")

# check local directory for torrent files, and move them to torrentdir
# functions.handleLocalTorrents(
#     torrent_dir=TORRENT_DIR, initial_dir=TARGET_DIR, move_file=False
# )

config = functions.yamlDataExtract()

TORRENT_DIR = config["torrent_dir"]
TARGET_DIR = config["target_dir"]
SEEDBOX_ADDR = config["seedbox_addr"]
SEEDBOX_LOGIN = config["seedbox_login"]
SEEDBOX_PW = config["seedbox_pw"]

seedbox_ftp = ftplib.FTP(SEEDBOX_ADDR, SEEDBOX_LOGIN, SEEDBOX_PW)

seedbox_ftp.encoding = "utf-8"
seedbox_ftp.cwd("watch")
functions.putFile("test.torrent", seedbox_ftp)

# TARGET_DIR, TORRENT_DIR =
from_torrents = functions.torrentIdentifier(TARGET_DIR)
to_torrents = functions.torrentIdentifier(TORRENT_DIR)

# create list of torrent files present in from_torrents, not present in to_torrents
torrents = functions.getDiffList(from_torrents, to_torrents)


if len(torrents) > 0:
    print(f"Found {len(torrents)} new torrents")
    functions.moveManager(torrents, TORRENT_DIR)
else:
    print("No new torrents found.")


for entry in torrents:
    print(f"Found torrent file ::: {entry.name}")


# TODO check that the files are in the correct format.
