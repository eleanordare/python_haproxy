__author__ = 'Eleanor Mehlenbacher'

import subprocess

class updateHAProxy():

    def update(self):
        newConfig = "result.txt"
        haproxyConfig = "/etc/haproxy/haproxy.cfg"

        f = open(newConfig, 'r')
        lines = f.readlines()
        f.close()

        f = open(haproxyConfig, 'w')
        for line in lines:
            f.write(line)
        f.close()

    def restart(self):
        command = ['service', 'haproxy', 'restart']
        subprocess.call(command, shell=False)
