import unittest

## this is to demostrate the use of test suites with python using a test runner.


class TestString(unittest.TestCase):
    def runTest(self):
        self.assertEqual('a'*4, 'aaaa')

class TestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual('gama'.upper(), "GAMA")

# to run both classes together, instatiate the test suite.

if __name__=='__main__':
    suite = unittest.TestSuite([TestString(),TestCase()])
    unittest.TextTestRunner().run(suite)  #This is the runner function built into unitttest

