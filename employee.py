from typing import Any

import datetime

class employee():


    increase_amount = 1.05

    def __init__(self,first,last,salary,skills):
        self.first = first
        self.last = last
        self.salary = salary
        self.skills = skills


    @property
    def email(self):
        return self.first + "." + self.last + "@xyz.com"

    @property
    def fullname(self):
        return self.first + " " + self.last


    def display_info(self):
        print("""
        ******
        ******
        ******
        Employee Info

        First Name: {}

        Last Name: {}

        Salary: {}

        Skills: {}


        """.format(self.first,self.last,self.salary,self.skills))

    def increase_salary(self):
        self.salary = int(self.salary * self.increase_amount)

    def add_skills(self,new_skills):
        self.skills.append(new_skills)

    @classmethod
    def set_increase_amount(cls,amount):
        cls.increase_amount = amount

    @staticmethod
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True