__author__ = 'Eleanor Mehlenbacher'

import urllib, urllib2, json, base64
from datetime import datetime

# ping jenkins instance
# save json content from jenkins instance
# if jenkins instance doesn't return anything, start it up
# analyze json content --- for now just choose executed builds
# if executed builds are 0, shut it down (for now)

# later on will add some kind of ping from jenkins json
# to python routes.py that will add the server to HAProxy config

jenkins = "http://localhost:8080"
username = "admin"
password = "admin"

class jenkinsMethods():

    def checkRunning(self, instance):
        check = urllib.urlopen(instance).getcode()
        if check is 404:
            return False
        else:
            return True


    # pull down JSON of instance info from Jenkins
    def getJenkinsJSON(self, instance, username, password):
        request = urllib2.Request(instance + "/api/json")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)
        data = json.load(urllib2.urlopen(request))
        return data


    # need to get crumb for POST requests because of CSRF protection
    def getJenkinsCrumb(self, instance, username, password):
        request = urllib2.Request(instance + "/crumbIssuer/api/json")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)
        data = json.load(urllib2.urlopen(request))

        crumb = [data['crumbRequestField'],data['crumb']]
        return crumb


    # use Monitoring plugin external API to find latest HTTP hit
    def getLastHit(self, instance, username, password):
        request = urllib2.Request(instance + "/monitoring?format=json&period=tout")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)
        data = json.load(urllib2.urlopen(request))

        # put all date items from JSON into list
        dates = []
        for line in data["list"]:
            date = datetime.strptime(line["startDate"].split(" ")[0], '%Y-%m-%d')
            dates.append(date)

        # find most recent date of HTTP hit
        youngest = max(dates)
        return youngest


    # POST request to jenkins/safeRestart to restart instance
    # in safe mode to put Jenkins into quiet mode, then restart
    def restartInstance(self, instance, username, password, crumb):
        method = "POST"
        handler = urllib2.HTTPHandler()
        opener = urllib2.build_opener(handler)
        data = urllib.urlencode({'':''})
        base64string = base64.b64encode('%s:%s' % (username, password))

        request = urllib2.Request(instance + "/safeRestart", data=data)
        request.add_header("Content-Type", 'application/json')
        request.add_header("Authorization", "Basic %s" % base64string)
        request.add_header(crumb[0], crumb[1])
        request.get_method = lambda: method

        try:
            connection = opener.open(request)
        except urllib2.HTTPError,e:
            connection = e


    # POST request to jenkins/safeExit to stop instance
    # in safe mode to put Jenkins into quiet mode, then stop
    def stopInstance(self, instance, username, password, crumb):
        method = "POST"
        handler = urllib2.HTTPHandler()
        opener = urllib2.build_opener(handler)
        data = urllib.urlencode({'':''})
        base64string = base64.b64encode('%s:%s' % (username, password))

        request = urllib2.Request(instance + "/safeExit", data=data)
        request.add_header("Content-Type", 'application/json')
        request.add_header("Authorization", "Basic %s" % base64string)
        request.add_header(crumb[0], crumb[1])
        request.get_method = lambda: method

        try:
            connection = opener.open(request)
        except urllib2.HTTPError,e:
            connection = e



if __name__ == '__main__':
    jenkinsMethods = jenkinsMethods()
    # crumb = jenkinsMethods.getJenkinsCrumb(jenkins, username, password)
    # jenkinsMethods.stopInstance(jenkins, username, password, crumb)
