__author__ = 'Eleanor Mehlenbacher'

import urllib
import subprocess

jenkinsInstances = "etc/jenkins.txt"
jenkinsWAR = "~/jenkins-2.0/usr/share/jenkins/jenkins.war"

def checkRunning(instance):
    register = urllib.urlopen(instance).getcode()
    if register is not "404":
        return True

def startLocalInstance():
    subprocess.call(['java', '-jar', 'jenkinsWAR'])

def main():
    f = open(jenkinsInstances, 'r')
    instances = f.readlines()
    f.close()

    # for instance in instances:
        # print checkRunning(instance)


main()
startLocalInstance()
