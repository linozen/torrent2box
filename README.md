
# Table of Contents

1.  [torrent2box](#org5c5ca0e)
    1.  [Introduction](#orgd08bfad)
    2.  [Disclaimer](#orge728a94)
    3.  [Installation](#org79515d6)
    4.  [Configuration](#orgf77b150)
    5.  [Outstanding tasks](#orge755908)
        1.  [Local file management](#org54dcc8a)
        2.  [Seedbox file management](#org57aadce)



<a id="org5c5ca0e"></a>

# torrent2box


<a id="orgd08bfad"></a>

## Introduction

I found browsing tracker sites, dragging and dropping torrents into my seedbox,
waiting for the download to complete, and then using SFTP to get the downloaded
file back locally annoying, so this script is designed to make that less
annoying. This is a WIP program to scan a directory (normally your `Downloads` directory)
for `.torrent` files and SFTP them into a seedbox. Then, when that file has been
downloaded, get it back from the seedbox.


<a id="orge728a94"></a>

## Disclaimer

This currently **does not work**.


<a id="org79515d6"></a>

## TODO Installation

Don&rsquo;t bother: Currently not functioning. Just made it public to motivate myself to finish the
damn thing.


<a id="orgf77b150"></a>

## Configuration

Fill out the config<sub>example.yaml</sub> file, and rename it to config.yaml.


<a id="orge755908"></a>

## Outstanding tasks


<a id="org54dcc8a"></a>

### Local file management

1.  DONE parse config

2.  DONE diff .torrent files in local DL and torrents folder

3.  TODO place downloaded file in correct location


<a id="org57aadce"></a>

### Seedbox file management

1.  TODO SFTP .torrent files to seedbox

2.  TODO check if download is complete

3.  TODO pull file to local machine

