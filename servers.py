#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

import re
import os
import sys
import fileinput
import glob
import urllib, json

class serverMethods():

    # looks for server name in frontend
    # returns True if server is found
    def checkIfExistingInFrontend(self, domainsFile, server):
        with open(domainsFile, 'r') as f:
            for line in f:
                if server["text"] in line:
                    return True
        return False

    # looks for server name in backend
    # returns True if server is found
    def checkIfExistingInBackend(self, backendsFile, server):
        with open(backendsFile, 'r') as f:
            for line in f:
                if server["text"] in line:
                    return True
        return False

    # checks if server is in frontend file
    # adds default server configuration to frontend setup
    def addServerToFrontend(self, domainsFile, server):
        if not self.checkIfExistingInFrontend(domainsFile, server):
            domains = open(domainsFile, 'a')
            domains.write("/" + server["text"] + "  " + server["text"] + "\n")
            domains.close()

    # checks if server is in backend file
    # adds default server configuration to backend setup
    def addServerToBackend(self, backendsFile, server):
        if not self.checkIfExistingInBackend(backendsFile, server):
            backends = open(backendsFile, 'a')
            backends.write("\nbackend " + server["text"] + "\n  balance roundrobin" + "\n  mode http" + "\n  server " + server["text"] + " " + str(server["ip"]) + ":" + str(server["port"]) + " check\n  server " + server["text"] + "Backup " + str(server["ip"]) + ":" + str(server["port"]) + " check backup\n\n")
            backends.close()

    # looks for server name in frontend
    # removes lines associated with server in files
    def removeServerFromFrontend(self, domainsFile, server):
        f = open(domainsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(domainsFile, 'w')
        for line in lines:
            if server["text"] not in line:
                f.write(line)
        f.close()

    # looks for server name in backend
    # removes lines associated with server in files
    def removeServerFromBackend(self, backendsFile, server):
        f = open(backendsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(backendsFile, 'w')
        ignoreLines = False
        for line in lines:
            if server["text"] in line:
                ignoreLines = True
            if not ignoreLines:
                f.write(line)
            if "backup" in line:
                ignoreLines = False
        f.close()

    # checks if new server info already exists
    # if not, rewrites frontend/backend with new server info
    def changeServerInFrontend(self, domainsFile, server1, server2):
        if self.checkIfExistingInFrontend(domainsFile, server2):
            return

        filedata = None
        with open(domainsFile, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace(server1["text"], server2["text"])
        with open(domainsFile, 'w') as file:
            file.write(filedata)

    # checks if new server info already exists
    # if not, rewrites frontend/backend with new server info
    def changeServerInBackend(self, backendsFile, server1, server2):
        if self.checkIfExistingInBackend(backendsFile, server2):
            return

        filedata = None
        with open(backendsFile, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace(server1["text"], server2["text"])
        filedata = filedata.replace(server1["ip"], server2["ip"])
        filedata = filedata.replace(str(server1["port"]), str(server2["port"]))
        with open(backendsFile, 'w') as file:
            file.write(filedata)

    # combines existing defaults, frontend, and backend files
    # produces complete haproxy config file
    def combineConfig(self):
        combined = sorted(glob.glob('configs/*.txt'))
        with open("result.txt", "wb") as outfile:
            for f in combined:
                with open(f, "rb") as infile:
                    outfile.write(infile.read() + "\n")


if __name__ == '__main__':
    defaultsFile = "configs/1_default.txt"
    frontendsFile = "configs/2_frontends.txt"
    backendsFile = "configs/3_backends.txt"
    domainsFile = "configs/domain2backend.map"
    serverMethods = serverMethods()

    # data = [{"id":7,"text":"third","ip":"localhost","port":8080},{"id":9,"text":"second","ip":"localhost","port":9090}]
    # serverMethods.addServerToBackend(backendsFile, data[0])
