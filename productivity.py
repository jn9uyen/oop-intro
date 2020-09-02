
class ProductivitySystem:
    def track(self, employees, hours):
        print('\nTracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')


class ManagerRole:
    def work(self, hours):
        print(f'screams and yells for {hours} hours.')


class SecretaryRole:
    def work(self, hours):
        print(f'expends {hours} hours doing office paperwork.')


class SalesPersonRole:
    def work(self, hours):
        print(f'expends {hours} hours on the phone.')


class FactoryWorkerRole:
    def work(self, hours):
        print(f'manufactures gadgets for {hours} hours.')


# class TemporarySecretary(Secretary, HourlyEmployee):
#     pass
