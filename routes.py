__author__ = 'Eleanor Mehlenbacher'

from bottle import get, post, request, put, delete, run, route
from servers import serverMethods
from update import updateHAProxy
import json

serverMethods = serverMethods()
updateHAProxy = updateHAProxy()

defaultsFile = "configs/1_default.txt"
frontendsFile = "configs/2_frontends.txt"
backendsFile = "configs/3_backends.txt"

# content on page
@route('/hello')
def addPage():
    return "Hi there."

# adding a new server
@post('/hello')
def add():
    # retrieves server information from body of request
    content = json.load(request.body)
    server = content[0]

    # adds server to frontend and backend files
    serverMethods.addServerToFrontend(frontendsFile, server)
    serverMethods.addServerToBackend(backendsFile, server)

    # combines frontend and backend files
    # updates local config and restarts haproxy
    serverMethods.combineConfig()
    updateHAProxy.update()
    updateHAProxy.restart()

# changing an existing server
@put('/hello')
def update():
    # retrieves server information from body of request
    content = json.load(request.body)
    server1 = content[0]
    server2 = content[1]

    # update server in frontend and backend files
    serverMethods.changeServerInFrontend(frontendsFile, server1, server2)
    serverMethods.changeServerInBackend(backendsFile, server1, server2)

    # combines frontend and backend files
    # updates local config and restarts haproxy
    serverMethods.combineConfig()
    updateHAProxy.update()
    updateHAProxy.restart()

# delete an existing server
@delete('/hello')
def delete():
    # retrieves server information from body of request
    content = json.load(request.body)
    server = content[0]

    # remove server from frontend and backend files
    serverMethods.removeServerFromFrontend(frontendsFile, server)
    serverMethods.removeServerFromBackend(backendsFile, server)

    # combines frontend and backend files
    # updates local config and restarts haproxy
    serverMethods.combineConfig()
    updateHAProxy.update()
    updateHAProxy.restart()



run(host='localhost', port=5000, debug=True)
