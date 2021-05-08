class Employee:
    def __init__(self, name, college_graduate):
        self.name = name
        self.college_graduate = college_graduate

    def work(self):
        print('I am working as employee')

class Manager:
    def __init__(self, name, college_graduate):
        self.name = name
        self.college_graduate = college_graduate

    def work(self):
        print('I am working as manager')


class Secretary:
    def __init__(self, name, college_graduate):
        self.name = name
        self.college_graduate = college_graduate

    def work(self):
        print('I am working as secretary')


class HourlyPaidEmployee(Employee, Manager, Secretary):
    def work(self):
        super.work()
        print('I am doing any work')


h = HourlyPaidEmployee('qwe', True)
h.work()
