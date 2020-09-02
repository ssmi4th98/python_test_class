import unittest
from employee import employee

## this shows how to use a class statement to go across the entire class now just each test setup.
## Note: cannot alter the value of the names because of its definition as class (not flexible)


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nSetUpClass')
        cls.emp1 = employee('Ralph','Smith',50000,['Java'])
        cls.emp2 = employee('Janis','Robins',75000,['Scala'])

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("\ntearDown")

    def test_mail(self):

        print("\nmail")
        self.assertEqual(self.emp1.email,'Ralph.Smith@xyz.com')
        self.assertEqual(self.emp2.email,'Janis.Robins@xyz.com')

    def test_full_name(self):

        print("\nfullname")
        self.assertEqual(self.emp1.fullname,'Ralph Smith')
        self.assertEqual(self.emp2.fullname,'Janis Robins')

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