import unittest
from employee import employee

class TestEmployee(unittest.TestCase):
    def test_mail(self):
        emp1 = employee('Ralph','Smith',50000,['Java'])
        emp2 = employee('Janis','Robins',75000,['Scala'])

        self.assertEqual(emp1.email,'Ralph.Smith@xyz.com')
        self.assertEqual(emp2.email,'Janis.Robins@xyz.com')

        emp1.first = 'Martin'
        emp2.first = 'Alice'

        self.assertEqual(emp1.email,'Martin.Smith@xyz.com')
        self.assertEqual(emp2.email,'Alice.Robins@xyz.com')

    def test_full_name(self):

        emp1 = employee('Ralph','Smith',50000,['Java'])
        emp2 = employee('Janis','Robins',75000,['Scala'])

        self.assertEqual(emp1.fullname,'Ralph Smith')
        self.assertEqual(emp2.fullname,'Janis Robins')

        emp1.first = 'Martin'
        emp2.first = 'Alice'

        self.assertEqual(emp1.fullname,'Martin Smith')
        self.assertEqual(emp2.fullname,'Alice Robins')

    def test_salary(self):

        emp1 = employee('Ralph','Smith',50000,['Java'])
        emp2 = employee('Janis','Robins',75000,['Scala'])

        emp1.increase_salary()
        emp2.increase_salary()

        self.assertEqual(emp1.salary, 52500)
        self.assertEqual(emp2.salary, 78750)

    def test_skills(self):

        emp1 = employee('Ralph','Smith',50000,['Java'])
        emp2 = employee('Janis','Robins',75000,['Scala'])

        emp1.add_skills('Go')

        self.assertEqual(emp1.skills, ['Java','Go'])

if __name__ == '__main__':
    unittest.main()




