import unittest
import urllib, json
import re
from servers import serverMethods

frontendsFile = "test/test_frontends.txt"
backendsFile = "test/test_backends.txt"

addFrontendsFile = "test/test_frontends_add.txt"
addBackendsFile = "test/test_backends_add.txt"

removeFrontendsFile = "test/test_frontends_remove.txt"
removeBackendsFile = "test/test_backends_remove.txt"

changeFrontendsFile = "test/test_frontends_change.txt"
changeBackendsFile = "test/test_backends_change.txt"

url = "http://localhost:3000/api/v1/todos"
response = urllib.urlopen(url)
data = json.loads(response.read())

serverMethods = serverMethods()


class testAddServerToFrontend(unittest.TestCase):
    def setUp(self):
        serverMethods.addServerToFrontend(frontendsFile, data[1])

    def test_add_server_to_frontend(self):
        # reads content from expected result file
        expected = None
        with open(addFrontendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed frontend file
        changed = None
        with open(frontendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(frontendsFile, 'r')
        lines = f.readlines()
        f.close()

        f = open(frontendsFile, 'w')
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
        serverMethods.removeServerFromFrontend(frontendsFile, data[0])

    def test_remove_server_from_frontend(self):
        # reads content from expected result file
        expected = None
        with open(removeFrontendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(frontendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(frontendsFile, 'a')
        f.write("  acl url_first path_beg /first\n")
        f.write("  use_backend first if url_first\n")
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
        f.write("\nbackend first\n  balance roundrobin\n  mode http\n  server first localhost:8080 check\n\n")
        f.close()


class testChangeServerInFrontend(unittest.TestCase):
    def setUp(self):
        serverMethods.changeServerInFrontend(frontendsFile, data[0], data[1])

    def test_change_server_in_frontend(self):
        # reads content from expected result file
        expected = None
        with open(changeFrontendsFile, 'r') as file:
            expected = file.read()

        # reads content from changed backend file
        changed = None
        with open(frontendsFile, 'r') as file:
            changed = file.read()

        expected = expected.replace('\n', '')
        changed = changed.replace('\n', '')

        self.assertEqual(expected, changed)

    # restore test frontend file
    def tearDown(self):
        f = open(frontendsFile, 'w')
        f.write("frontend main\n")
        f.write("  bind localhost:8081\n")
        f.write("  mode http\n")
        f.write("  default_backend name\n")
        f.write("  acl url_first path_beg /first\n")
        f.write("  use_backend first if url_first\n")
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
        f.write("\nbackend first\n  balance roundrobin\n  mode http\n  server first localhost:8080 check\n\n")
        f.close()



if __name__ == '__main__':
    unittest.main()
