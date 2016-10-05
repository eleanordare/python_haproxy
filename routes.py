from bottle import get, post, request, put, delete, run, route
from servers import serverMethods
from update import updateConfig

serverMethods = serverMethods()
updateConfig = updateConfig()

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
    server = {"text":request.forms.get('name'),
                "ip":request.forms.get('ip'),
                "port":request.forms.get('port')}
                
    # adds server to frontend and backend files
    serverMethods.addServerToFrontend(frontendsFile, server)
    serverMethods.addServerToBackend(backendsFile, server)

    # combines frontend and backend files, updates local config
    serverMethods.combineConfig()
    updateConfig.update()

# changing an existing server
@put('/hello')
def update():
    server1 = {"text":request.forms.get('name1'),
                "ip":request.forms.get('ip1'),
                "port":request.forms.get('port1')}
    server2 = {"text":request.forms.get('name2'),
                "ip":request.forms.get('ip2'),
                "port":request.forms.get('port2')}
    serverMethods.changeServerInFrontend(frontendsFile, server1, server2)
    serverMethods.changeServerInBackend(backendsFile, server1, server2)

    serverMethods.combineConfig()
    updateConfig.update()

# delete an existing server
@delete('/hello')
def delete():
    server = {"text":request.forms.get('name'),
                "ip":request.forms.get('ip'),
                "port":request.forms.get('port')}
    serverMethods.removeServerFromFrontend(frontendsFile, server)
    serverMethods.removeServerFromBackend(backendsFile, server)

    serverMethods.combineConfig()
    updateConfig.update()



run(host='localhost', port=5000, debug=True)
