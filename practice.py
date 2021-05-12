class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role


class Student(User):
    def __init__(self, login, password, count_of_lessons, group, avg):
        super().__init__(login, password, role='Student')
        self.count_of_lessons = count_of_lessons
        self.group = group
        self.avg = avg


class Teacher(User):
    def __init__(self, login, password, list_of_groups):
        super().__init__(login, password, role='Teacher')
        self.list_of_groups = list_of_groups


class Admin(User):
    def __init__(self, login, password, list_of_groups):
        super().__init__(login, password, role='Admin')
        self.list_of_groups = list_of_groups


class Group:
    def __init__(self, name, admin, teacher, list_of_students):
        self.name = name
        self.teacher = teacher
        self.admin = admin
        self.list_of_students = list_of_students


student1 = Student('admin', 'admin', 15, 'ptn', 4)
student2 = Student('admin', 'admin', 10, 'ptn', 3)
student3 = Student('admin', 'admin', 12, 'ptn', 5)
list_of_groups = []
teacher = Teacher('admin', 'admin', list_of_groups)
list_of_students = [student1, student2, student3]
group1 = Group(teacher, list_of_students)
print(group1.teacher.list_of_groups)
for i in group1.list_of_students:
    print(i.count_of_lessons)
