#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

import subprocess

class updateHAProxy():

    def update(self):
        newConfig = "result.txt"
        haproxyConfig = "/etc/haproxy/haproxy.cfg"

        newMap = "configs/domain2backend.map"
        localMap = "/etc/haproxy/domain2backend.map"

        f = open(newConfig, 'r')
        lines = f.readlines()
        f.close()

        f = open(haproxyConfig, 'w')
        for line in lines:
            f.write(line)
        f.close()

        f = open(newMap, 'r')
        lines = f.readlines()
        f.close()

        f = open(localMap, 'w')
        for line in lines:
            f.write(line)
        f.close()

    def restart(self):
        command = ['service', 'haproxy', 'restart']
        subprocess.call(command, shell=True)
        return
