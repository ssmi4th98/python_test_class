import unittest
from employee import employee

## setUp and tearDown are referred to as fixtures as they are "fixed" for all tests


class TestEmployee(unittest.TestCase):

    def setUp(self):

        print("\nsetUp")  ## print statements added in order to show order - done in alphabetical order.
        self.emp1 = employee('Ralph','Smith',50000,['Java'])
        self.emp2 = employee('Janis','Robins',75000,['Scala'])

    def tearDown(self):
        print("\ntearDown")
        pass

    def test_mail(self):

        print("\nmail")
        self.assertEqual(self.emp1.email,'Ralph.Smith@xyz.com')
        self.assertEqual(self.emp2.email,'Janis.Robins@xyz.com')

        self.emp1.first = 'Martin'
        self.emp2.first = 'Alice'

        self.assertEqual(self.emp1.email,'Martin.Smith@xyz.com')
        self.assertEqual(self.emp2.email,'Alice.Robins@xyz.com')

    def test_full_name(self):

        print("\nfullname")
        self.assertEqual(self.emp1.fullname,'Ralph Smith')
        self.assertEqual(self.emp2.fullname,'Janis Robins')

        self.emp1.first = 'Martin'
        self.emp2.first = 'Alice'

        self.assertEqual(self.emp1.fullname,'Martin Smith')
        self.assertEqual(self.emp2.fullname,'Alice Robins')

    def test_salary(self):

        print("\nsalary")
        self.emp1.increase_salary()
        self.emp2.increase_salary()

        self.assertEqual(self.emp1.salary, 52500)
        self.assertEqual(self.emp2.salary, 78750)

    def test_skills(self):

        print("\nskills")
        self.emp1.add_skills('Go')

        self.assertEqual(self.emp1.skills, ['Java','Go'])

if __name__ == '__main__':
    unittest.main()
