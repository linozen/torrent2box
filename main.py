#!/usr/bin/env python3

import sys
import argparse
import functions
import connectionhandler

# handle argument parsing
parser = argparse.ArgumentParser(
    description="This tool finds .torrent files in your download folder\
    and gives the option to move them directly into a shared seedbox via\
    FTP. it also allows for download of that file, as well as moving the\
    .torrent files somewhere convenient after processing."
)
# only upload files to seedbox.io,
parser.add_argument(
    "--upload",
    "-u",
    action="store_true",
    help="upload files to seedbox.io using the\
    credentials in the config",
)
parser.add_argument(
    "--print",
    "-p",
    action="store_true",
    help="print files in inbound torrent folder",
)
parser.add_argument(
    "--move",
    "-m",
    action="store_true",
    help="move files in inbound folder to outbound torrent folder",
)  # move torrent files locally
# parser.add_argument(
#     "--download",
#     "-d",
#     action="store_true",
#     help="Download torrents from seedbox.io to the specified folder.",
# )  # download torrents
args = parser.parse_args()


# Handle the config file
config = functions.yamlDataExtract()

TORRENT_DIR = config["torrent_dir"]
TARGET_DIR = config["target_dir"]
SEEDBOX_ADDR = config["seedbox_addr"]
SEEDBOX_LOGIN = config["seedbox_login"]
SEEDBOX_PW = config["seedbox_pw"]


# create list of torrent files present in from_torrents, not present in to_torrents
torrents = functions.getTorrentDiffList(TARGET_DIR, TORRENT_DIR)

num_torrents = len(torrents)

if num_torrents == 0:
    print(f"Aborting because no torrents were found in {TARGET_DIR}")
    sys.exit()

if args.print or args.download or args.upload is True:
    for entry in torrents:
        print(f"Found torrent file ::: {entry.name}")

if args.upload is True:

    sftp = connectionhandler.SeedboxFTP(SEEDBOX_ADDR, SEEDBOX_LOGIN, SEEDBOX_PW)

    print(f"attempting to connect to {SEEDBOX_ADDR}")
    sftp.connect()

    print(f"attempting to upload {num_torrents} to {SEEDBOX_ADDR}.")
    # set CWD to Watch folder
    sftp.changeWorkingDirectory(remotePath="watch")

    # loop through torrent list, and send them to the seedbox
    for torrent in torrents:
        sftp.testUpload(torrent)
    # disconnect
    sftp.disconnect()

if args.download is True:

    sftp.changeWorkingDirectory(remotePath="/files/Completed Downloads")

    for torrent in torrents:
        torrentfile = functions.getFileNamefromTorrent(torrent)
        print(f"processing {torrentfile}")
        sftp.downloadRemoteDir(
            torrentfile,
            destination=TARGET_DIR,
        )
    sftp.disconnect()

if args.move is True:
    print(f"moving torrents to {TORRENT_DIR}")
    functions.moveManager(torrents, TORRENT_DIR)
