
# Table of Contents

1.  [torrent2box](#orgf501309)
    1.  [Introduction](#org7d4f9fa)
    2.  [Disclaimer](#orgf3451ff)
    3.  [Installation](#org1dde8b1)
    4.  [Configuration](#org75a3abf)
    5.  [Outstanding tasks](#orge7c8bfd)
        1.  [Local file management](#orgc28e1a0)
        2.  [Seedbox file management](#orge642d23)



<a id="orgf501309"></a>

# torrent2box


<a id="org7d4f9fa"></a>

## Introduction

I found browsing tracker sites, dragging and dropping torrents into my seedbox,
waiting for the download to complete, and then using SFTP to get the downloaded
file back locally annoying, so this script is designed to make that less
annoying. This is a WIP program to scan a directory (normally your `Downloads` directory)
for `.torrent` files and SFTP them into a seedbox. Then, when that file has been
downloaded, get it back from the seedbox.


<a id="orgf3451ff"></a>

## Disclaimer

This currently **does not work**.


<a id="org1dde8b1"></a>

## Installation

Don&rsquo;t bother: Currently not functioning. Just made it public to motivate myself to finish the
damn thing.


<a id="org75a3abf"></a>

## Configuration

Fill out the `config\_example.yaml` file, and rename it to config.yaml.


<a id="orge7c8bfd"></a>

## Outstanding tasks


<a id="orgc28e1a0"></a>

### Local file management

1.  DONE parse config

2.  DONE diff .torrent files in local DL and torrents folder

3.  TODO place downloaded file in correct location


<a id="orge642d23"></a>

### Seedbox file management

1.  TODO SFTP .torrent files to seedbox

2.  TODO check if download is complete

3.  TODO pull file to local machine

