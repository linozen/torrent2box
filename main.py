#!/usr/bin/env python3

import functions
import connectionhandler


# Handle the config file
config = functions.yamlDataExtract()

TORRENT_DIR = config["torrent_dir"]  # this
TARGET_DIR = config["target_dir"]
SEEDBOX_ADDR = config["seedbox_addr"]
SEEDBOX_LOGIN = config["seedbox_login"]
SEEDBOX_PW = config["seedbox_pw"]


# create list of torrent files present in from_torrents, not present in to_torrents
torrents = functions.getTorrentDiffList(TARGET_DIR, TORRENT_DIR)

num_torrents = len(torrents)

if num_torrents > 0:
    print(f"Found {num_torrents} new torrents")
    # functions.moveManager(torrents, TORRENT_DIR)
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
for torrent in torrents:
    sftp.testUpload(torrent)
# disconnect
sftp.disconnect()

# move torrents into the torrent dir
functions.moveManager(torrents, TORRENT_DIR)
