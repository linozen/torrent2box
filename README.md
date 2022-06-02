
# Table of Contents

1.  [torrent2box](#org2a6dd7f)
    1.  [Introduction](#org86fa481)
    2.  [Disclaimer](#orgd654583)
    3.  [Installation](#org3b80ab5)
    4.  [Configuration](#org0b91e49)
    5.  [Outstanding tasks](#org6129fd8)
        1.  [Local file management](#org29f8a52)
        2.  [Seedbox file management](#orgf718594)



<a id="org2a6dd7f"></a>

# torrent2box


<a id="org86fa481"></a>

## Introduction

I found browsing tracker sites, dragging and dropping torrents into my seedbox,
waiting for the download to complete, and then using SFTP to get the downloaded
file back locally annoying, so this script is designed to make that less
annoying. This is a WIP program to scan a directory (normally your `Downloads` directory)
for `.torrent` files and SFTP them into a seedbox. Then, when that file has been
downloaded, get it back from the seedbox.


<a id="orgd654583"></a>

## Disclaimer

This currently **does not work**.


<a id="org3b80ab5"></a>

## Installation

Don&rsquo;t bother: Currently not functioning. Just made it public to motivate myself to finish the
damn thing.


<a id="org0b91e49"></a>

## Configuration

Fill out the `config\_example.yaml` file, and rename it to `config.yaml`.


<a id="org6129fd8"></a>

## Outstanding tasks


<a id="org29f8a52"></a>

### Local file management

1.  DONE parse config

2.  DONE diff .torrent files in local DL and torrents folder

3.  TODO place downloaded file in correct location


<a id="orgf718594"></a>

### Seedbox file management

1.  TODO SFTP .torrent files to seedbox

2.  TODO check if download is complete

3.  TODO pull file to local machine

