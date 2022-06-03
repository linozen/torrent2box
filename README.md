
# Table of Contents

1.  [torrent2box](#org35366fb)
    1.  [Introduction](#org75eed89)
    2.  [Status](#org8170d01)
    3.  [Installation](#org7ed272a)
    4.  [Configuration](#org78ef7ce)
    5.  [Outstanding tasks](#orgf778da6)
        1.  [Local file management](#orgec4759b)
        2.  [Seedbox file management](#org8435719)



<a id="org35366fb"></a>

# torrent2box


<a id="org75eed89"></a>

## Introduction

I found browsing tracker sites, dragging and dropping torrents into my seedbox,
waiting for the download to complete, and then using SFTP to get the downloaded
file back locally annoying, so this script is designed to make that less
annoying. This is a WIP program to scan a directory (normally your `Downloads` directory)
for `.torrent` files and SFTP them into a seedbox. Then, when that file has been
downloaded, get it back from the seedbox.


<a id="org8170d01"></a>

## Status

this is very alpha, and only works for seedbox.io. it might work for other
RuTorrent based shared seedboxes, but I cannot test that. The only functionality
that is currently made available through this script is:

-   check for torrent files in `targetdir`, probably your downloads folder.
-   move them to `torrentdir`.
-   upload new torrents in `torrentdir` to Seedbox.io&rsquo;s `watch` folder. Here,
    Rutorrent automatically starts the torrent download.


<a id="org7ed272a"></a>

## Installation

-   download prerequisites, `git` and `python`.
-   Clone this repo.
    
        git clone
-   Create a directory to store your `.torrent` files.
    
        mkdir torrentfiles
-   configure the YAML file with your login details and the location of the
    directory you created.
-   To run the script, execute
    
        python main.py


<a id="org78ef7ce"></a>

## Configuration

Fill out the `config\_example.yaml` file, and rename it to `config.yaml`.


<a id="orgf778da6"></a>

## Outstanding tasks


<a id="orgec4759b"></a>

### Local file management

1.  DONE parse config

2.  DONE diff .torrent files in local DL and torrents folder

3.  DONE place downloaded file in correct location


<a id="org8435719"></a>

### Seedbox file management

1.  DONE SFTP .torrent files to seedbox

2.  TODO check if download is complete

3.  TODO pull file to local machine

