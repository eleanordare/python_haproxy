import unittest
import serverMethods

frontendsFile = "test_frontends.txt"
backendsFile = "test_backends.txt"

addFrontendsFile = "test_frontends_add.txt"
addBackendsFile = "test_backends_add.txt"

server = ['name','localhost','8080']


class testServerMethods(unittest.TestCase):

    def test_add(frontendsFile, backendsFile, server):
        serverMethods.addServer(frontendsFile, backendsFile, server)

        # reads content from expected result file
        filedata = None
        with open(addFrontendsFile, 'r') as file:
            filedata = file.read()

        # compares result file with expected result
        with open(frontendsFile) as f:
            for x in f:
                for y in filedata:
                    assertIs(x, y)


    def test_change(self):
        return

    def test_remove(self):
        return


    def test_combine(self):
        return



class testConfig(unittest.TestCase):

    def test_update(self):
        return


if __name__ == '__main__':
    unittest.main()
