__author__ = 'Eleanor Mehlenbacher'

newConfig = "result.txt"
haproxyConfig = "/etc/haproxy/haproxy.cfg"

def updateConfig(newConfig):
    f = open(newConfig, 'r')
    lines = f.readlines()
    f.close()

    f = open(haproxyConfig, 'w')
    for line in lines:
        f.write(line)
    f.close()

updateConfig(newConfig)
