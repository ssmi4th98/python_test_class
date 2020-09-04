import unittest

#this demonstrates how to initialize a series of tests within a test case

class TestMultiplication(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3*5), 12)


class TestAddition(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3+5), 8)


class TestDivision(unittest.TestCase):
    def runTest(self):
        self.assertEqual((6/0), 3)
#above is all same as in test_suite_add

class SimpleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    @unittest.skip('Skip this test') # decorator to skip the test
    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    suite = unittest.makeSuite(SimpleTest, 'test')
    suite.addTests([TestMultiplication(),TestAddition(),TestDivision()])
    result = unittest.TextTestRunner(verbosity=2).run(suite) # capture the results of the runner in result and then display
                        # turn on verbosity in the test runner itself with value of 2 (1 is minumum).


    print('Errors: ', result.errors)
    print("\nFailures: ", result.failures)
    print("\nSkipped Tests: ", result.skipped)
    print("\nNo. of Tests: ", result.testsRun)
    print("\nWas it a successful test? ", result.wasSuccessful())