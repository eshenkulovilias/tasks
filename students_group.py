class Group:
    count = 0

    def __init__(self, name, journal):
        self.name = name
        self.journal = journal
        Group.count += 1

    def add_student(self, student):
        self.journal.append(student)

    def show_info(self):
        print(f'Group\'s name: {self.name}\nStudents: {self.journal}')

    def __del__(self):
        Group.count -= 1
        print('Удаляю группу')


group_1 = Group('PTN1-W21', ['Alice'])
group_1.add_student('John')
group_1.add_student('Tom')
group_1.show_info()

# group_2 = Group('PTN2-W21', ['Ron'])
