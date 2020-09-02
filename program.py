'''
program.py
Object-oriented programing intro
https://realpython.com/inheritance-composition-python/
Joe Nguyen | 01 Sep 2020
'''

import sys
import importlib
import json

from hr import calculate_payroll2, LTDPolicy
from productivity import track
from employees import employee_database, Employee

importlib.reload(sys.modules['hr'])
importlib.reload(sys.modules['productivity'])
importlib.reload(sys.modules['employees'])


def print_dict(d):
    print(json.dumps(d, indent=2))


# ------------------------------------------------
# Factory method: assign singleton classes
# ------------------------------------------------
employee_ls = employee_database.employees

track(employee_ls, 40)
calculate_payroll2(employee_ls)

Employee(1)
Employee.__mro__
# Employee(1).

# dir(Employee)
temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())


sales_employee = employee_ls[2]
ltd_policy = LTDPolicy()

# Apply existing policy to new policy (ltd_policy) and then set
# existing policy as ltd_policy
sales_employee.apply_payroll_policy(ltd_policy)
sales_employee

track(employee_ls, 10)
calculate_payroll2(employee_ls)
