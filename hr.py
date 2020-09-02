
class MyClass:
    pass


class MyError(Exception):
    pass


class PayrollSystem:
    '''Implements a `calculate_payroll()` method (interface) common to every
    employee class
    The `IPayrollCalculator` interface requires each employee object passed
    contain an `id`, `name` and `calculate_payroll()` method
    '''

    def calculate_payroll(self, employees):
        print('\nCalculating payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for employee: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}\n')


class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
