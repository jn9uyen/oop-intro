'''
program.py
Object-oriented programing intro
https://realpython.com/inheritance-composition-python/
Joe Nguyen | 01 Sep 2020
'''

import sys
import importlib

import hr
import productivity
import employees


importlib.reload(sys.modules['hr'])
importlib.reload(sys.modules['productivity'])
importlib.reload(sys.modules['employees'])


# c = fn.MyClass()
# dir(c)

# o = object()
# dir(o)

# raise fn.MyError()

# Payroll system
salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

# Error case
# employee = employees.Employee(1, 'Invalid')
# ^TypeError: Can't instantiate abstract class Employee with abstract methods
# calculate_payroll

payroll_system = hr.PayrollSystem()
employee_ls = [
    salary_employee,
    hourly_employee,
    commission_employee,
    # employee,
]
payroll_system.calculate_payroll(employee_ls)
# ^AttributeError: 'Employee' object has no attribute 'calculate_payroll'

# Payroll and productivty
manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
employee_ls = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employee_ls, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employee_ls)


# method resolution order
# employees.TemporarySecretary.__mro__
employees.Manager.__mro__
