'''
program.py
Object-oriented programing intro
https://realpython.com/inheritance-composition-python/
Joe Nguyen | 01 Sep 2020
'''

import sys
import importlib

from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employees import EmployeeDatabase

importlib.reload(sys.modules['hr'])
importlib.reload(sys.modules['productivity'])
importlib.reload(sys.modules['employees'])

# ------------------------------------------------
# policy-based design
# ------------------------------------------------
productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

# list comphrension to get employee attributes
employees = employee_database.employees

# Manager changes to a temporary employee (hourly rate)
manager = employees[0]
manager.payroll = HourlyPolicy(55)

# for loop to calculate .track()
productivity_system.track(employees, 40)
# for loop to calculate .calculate_payroll()
payroll_system.calculate_payroll(employees)
