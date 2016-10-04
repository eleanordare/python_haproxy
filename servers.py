__author__ = 'Eleanor Mehlenbacher'

import re
import os
import sys
import fileinput
import glob
import urllib, json

class serverMethods():

    url = "http://localhost:3000/api/v1/todos"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    defaultsFile = "configs/1_default.txt"
    frontendsFile = "configs/2_frontends.txt"
    backendsFile = "configs/3_backends.txt"

    # looks for server name in both frontend and backend
    # returns True if server is found
    def checkIfExisting(self, server):
        with open(frontendsFile) as f:
            for line in f:
                if server["text"] in line:
                    return True

        with open(backendsFile) as f:
            for line in f:
                if server["text"] in line:
                    return True

        return False

    # checks if server is in frontend file
    # adds default server configuration to frontend setup
    def addServerToFrontend(self, frontendsFile, server):
        # if not checkIfExisting(server):
        frontends = open(frontendsFile, 'a')
        frontends.write("  acl url_" + server["text"] + " path_beg /" + server["text"] + "\n")
        frontends.write("  use_backend " + server["text"] + " if url_" + server["text"] + "\n")
        frontends.close()

    # checks if server is in backend file
    # adds default server configuration to backend setup
    def addServerToBackend(self, backendsFile, server):
        # if not checkIfExisting(server):
        backends = open(backendsFile, 'a')
        backends.write("\nbackend " + server["text"] + "\n  balance roundrobin" + "\n  mode http" + "\n  server " + server["text"] + " " + str(server["ip"]) + ":" + str(server["port"]) + " check\n\n")
        backends.close()

    # looks for server name in frontend
    # removes lines associated with server in files
    def removeServerFromFrontend(self, frontendsFile, server):
        f = open(frontendsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(frontendsFile, 'w')
        for line in lines:
            if server["text"] in line and "default_backend" in line:
                print "Please change your default backend before removing this server."
                return
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
            if "check" in line:
                ignoreLines = False
        f.close()


    # checks if new server info already exists
    # if not, rewrites frontend/backend with new server info
    def changeServerInFrontend(self, frontendsFile, server1, server2):
        # if checkIfExisting(server2):
        #     return

        filedata = None
        with open(frontendsFile, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace(server1["text"], server2["text"])
        with open(frontendsFile, 'w') as file:
            file.write(filedata)


    # checks if new server info already exists
    # if not, rewrites frontend/backend with new server info
    def changeServerInBackend(self, backendsFile, server1, server2):
        # if checkIfExisting(server2):
        #     return

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
        with open("../result.txt", "wb") as outfile:
            for f in combined:
                with open(f, "rb") as infile:
                    outfile.write(infile.read() + "\n")


if __name__ == '__main__':
    url = "http://localhost:3000/api/v1/todos"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    defaultsFile = "configs/1_default.txt"
    frontendsFile = "configs/2_frontends.txt"
    backendsFile = "configs/3_backends.txt"
    serverMethods = serverMethods()
    # serverMethods.addServerToFrontend(frontendsFile, data[1])
    # addServer(frontendsFile, backendsFile, data[0])
