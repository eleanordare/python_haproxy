__author__ = 'Eleanor Mehlenbacher'

import urllib

jenkinsInstances = "etc/jenkins.txt"

def checkRunning(instance):
    register = urllib.urlopen(instance).getcode()
    if register is not "404":
        return True


def main():
    f = open(jenkinsInstances, 'r')
    instances = f.readlines()
    f.close()

    for instance in instances:
        print checkRunning(instance)

main()
