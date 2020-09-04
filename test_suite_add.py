import unittest


class TestMultiplication(unittest.TestCase):
    def runTest(self):    #runTest is an attribute for the object and must be there.
        self.assertEqual((3*5), 15)


class TestAddition(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3+5), 8)


class TestDivision(unittest.TestCase):
    def runTest(self):
        self.assertEqual((6/2), 3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMultiplication()) # addTest is used to add a single test to the suite
    suite.addTests([TestAddition(),TestDivision()])  #addTests is used to do multiple tests
    unittest.TextTestRunner().run(suite)

#The order in which the tests are added determines the order the tests are run.
#Here tests can be added or subtracted based upon results of other tests.