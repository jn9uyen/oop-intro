'''
employee.py
Object-oriented programing intro: functions library
https://realpython.com/inheritance-composition-python/
Joe Nguyen | 01 Sep 2020
'''

from abc import ABC, abstractmethod

from hr import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from productivity import (
    ManagerRole,
    SecretaryRole,
    SalesPersonRole,
    FactoryWorkerRole
)


class Employee(ABC):
    '''Base class: abstract (base) class that can't be instantiated'''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(self, id, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(self, id, name)


class SalaryEmployee(Employee):
    '''Derived class: extends `Employee`
    implements `calculate_payroll()`'''

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    '''Derived class: extends `Employee`
    implements `calculate_payroll()`'''

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    '''Derived class; extends `SalaryEmployee`
    implements `calculate_payroll()`'''

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
