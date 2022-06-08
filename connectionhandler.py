#!/usr/bin/env python3
import ftplib
from pathlib import Path
import os
import sys

###############################################################################
# https://sftptogo.com/blog/python-sftp/                                       #
###############################################################################


class SeedboxFTP:
    def __init__(self, hostname, username, password, port=22):
        """Constructor Method"""
        # Set connection object to None (initial value)
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        try:
            self.connection = ftplib.FTP(self.hostname, self.username, self.password)
        except Exception as e:
            raise Exception(e)
            print("FTP connection failed.")
        finally:
            print(f"Connected sucessfully to {self.hostname} as {self.username}.")

    def disconnect(self):
        """Close the FTP connection"""
        self.connection.close()
        print(f"Disconnected from {self.hostname} sucessfully.")

    def changeWorkingDirectory(self, remotePath):
        try:
            self.connection.cwd(remotePath)
            print(f"changed remote directory to {remotePath}")
        except Exception as e:
            raise Exception(e)

    def printWorkingDirectory(self):
        self.connection.dir()

    # This is the upload function. Very unstable as it stands, and has no proper error handling.
    # The issue I am having is that there is a both a list of posix files (localFile) and the directory
    # in which those files are to be found. it seems odd to set both. Ideally you just feed it the main file.

    def testUpload(self, localFile):
        fileObject = open(localFile, "rb")
        file2BeSavedAs = localFile.name
        ftpCommand = "STOR %s" % file2BeSavedAs
        ftpResponseMessage = self.connection.storbinary(ftpCommand, fp=fileObject)
        print(ftpResponseMessage)
        fileObject.close()

    def testDownload(self, remoteFile):
        """Download file to location of execution. this needs to be amended to allow for choice of location."""
        fileObject = open(remoteFile, "wb")
        ftpcommand = "RETR %s" % remoteFile
        ftpResponseMessage = self.connection.retrbinary(ftpcommand, fileObject.write)
        print(ftpResponseMessage)
        fileObject.close()

    def downloadFiles(self, path, destination):
        # path & destination are str of the form "/dir/folder/something/"
        # path should be the abs path to the root FOLDER of the file tree to download
        try:
            self.connection.cwd(path)
            # clone path to destination
            os.chdir(destination)
            os.mkdir(destination[0 : len(destination) - 1] + path)
            print(destination[0 : len(destination) - 1] + path + " built")
        except OSError:
            # folder already exists at destination
            pass
        except ftplib.error_perm:
            # invalid entry (ensure input form: "/dir/folder/something/")
            print("error: could not change to " + path)
            sys.exit("ending session")

        # list children:
        filelist = self.connection.nlst()

        for file in filelist:
            try:
                # this will check if file is folder:
                self.connection.cwd(path + file + "/")
                # if so, explore it:
                downloadFiles(path + file + "/", destination)
            except ftplib.error_perm:
                # not a folder with accessible content
                # download & return
                os.chdir(destination[0 : len(destination) - 1] + path)
                # possibly need a permission exception catch:
                with open(os.path.join(destination, file), "wb") as f:
                    self.connection.retrbinary("RETR " + file, f.write)
                print(file + " downloaded")
        return
