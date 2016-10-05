__author__ = 'Eleanor Mehlenbacher'

import unittest
import urllib, json
import re
from servers import serverMethods

frontendsFile = "test/test_frontends.txt"
backendsFile = "test/test_backends.txt"
domainsFile = "test/test_domain2backend.map"

addFrontendsFile = "test/test_frontends_add.txt"
addBackendsFile = "test/test_backends_add.txt"
addDomainsFile = "test/test_domain2backend_add.map"

removeFrontendsFile = "test/test_frontends_remove.txt"
removeBackendsFile = "test/test_backends_remove.txt"
removeDomainsFile = "test/test_domain2backend_remove.map"

changeFrontendsFile = "test/test_frontends_change.txt"
changeBackendsFile = "test/test_backends_change.txt"
changeDomainsFile = "test/test_domain2backend_change.map"

data = [{"id":7,"text":"first","ip":"localhost","port":8080},{"id":9,"text":"second","ip":"localhost","port":9090}]

serverMethods = serverMethods()


class testAddServerToFrontend(unittest.TestCase):
    def setUp(self):
        serverMethods.addServerToFrontend(domainsFile, data[1])

    def test_add_server_to_frontend(self):
        # reads content from expected result file
        expected = None
        with open(addDomainsFile, 'r') as file:
            expected = file.read()

        # reads content from changed frontend file
        changed = None
        with open(domainsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(domainsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(domainsFile, 'w')
        ignoreLines = False
        for line in lines:
            if "second" in line:
                ignoreLines = True
            if not ignoreLines:
                f.write(line)
        f.close()


class testAddServerToBackend(unittest.TestCase):
    def setUp(self):
        serverMethods.addServerToBackend(backendsFile, data[1])

    def test_add_server_to_backend(self):
        # reads content from expected result file
        expected = None
        with open(addBackendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(backendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test backend file
    def tearDown(self):
        f = open(backendsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(backendsFile, 'w')
        ignoreLines = False
        for line in lines:
            if "second" in line:
                ignoreLines = True
            if not ignoreLines:
                f.write(line)
        f.close()


class testRemoveServerFromFrontend(unittest.TestCase):
    def setUp(self):
        serverMethods.removeServerFromFrontend(domainsFile, data[0])

    def test_remove_server_from_frontend(self):
        # reads content from expected result file
        expected = None
        with open(removeDomainsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(domainsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(domainsFile, 'a')
        f.write("/first  first\n")
        f.close()


class testRemoveServerFromBackend(unittest.TestCase):
    def setUp(self):
        serverMethods.removeServerFromBackend(backendsFile, data[0])

    def test_remove_server_from_backend(self):
        # reads content from expected result file
        expected = None
        with open(removeBackendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(backendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(backendsFile, 'a')
        f.write("\nbackend first\n  balance roundrobin\n  mode http\n  server first localhost:8080 check\n  server firstBackup localhost:8080 check backup\n\n")
        f.close()


class testChangeServerInFrontend(unittest.TestCase):
    def setUp(self):
        serverMethods.changeServerInFrontend(domainsFile, data[0], data[1])

    def test_change_server_in_frontend(self):
        # reads content from expected result file
        expected = None
        with open(changeDomainsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(domainsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(domainsFile, 'w')
        f.write("#domainname  backendname\n")
        f.write("/first  first\n")
        f.close()


class testChangeServerInBackend(unittest.TestCase):
    def setUp(self):
        serverMethods.changeServerInBackend(backendsFile, data[0], data[1])

    def test_change_server_in_backend(self):
        # reads content from expected result file
        expected = None
        with open(changeBackendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(backendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(backendsFile, 'w')
        f.write("\nbackend first\n  balance roundrobin\n  mode http\n  server first localhost:8080 check\n  server firstBackup localhost:8080 check backup\n\n")
        f.close()



if __name__ == '__main__':
    unittest.main()
