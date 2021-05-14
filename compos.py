# * У каждого пользователя есть логин, пароль и его роль
# * У ученика есть количество пройденных занятий, группа и его средний бал
# * У учителя есть список групп в которых он работает
# * У администратора есть доступ к ученикам состоящим в группах и учителям, которые в них ведут

class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role


class Student(User):
    def __init__(self, login, password, num_lesson, group, average_point):
        super().__init__(login, password, role='Student')
        self.num_lesson = num_lesson
        self.group = group
        self.average_point = average_point


class Teacher(User):
    def __init__(self, login, password, lst_group):
        super().__init__(login, password, role='Teacher')
        self.lst_group = lst_group


class Group:
    def __init__(self, name, admin, teacher, list_of_students):
        self.name = name
        self.admin = admin
        self.admin.group.append(self)
        self.teacher = teacher
        self.list_of_students = list_of_students


class Admin(User):
    def __init__(self, login, password):
        super().__init__(login, password, role='Admin')

    group = []

    def together(self):
        for i in self.group:
            print(i.name)


stdnt1 = Student('Valera', 'valer123', 12, 1, 5.5)
stdnt2 = Student('Ers', 'ers23', 9, 1, 4.5)
stdnt3 = Student('Sula', 'sula2468', 11, 2, 3.6)
teacher = Teacher('Genadii.V', 'biology1', 'All groups')
admin = Admin('AdminLog', 'AdminPass')
group1 = Group('Python21', admin, teacher, list_of_students=[stdnt1, stdnt2])
group2 = Group('Python21', admin, teacher, list_of_students=[stdnt3])
group3 = Group('Python21', admin, teacher, list_of_students=[stdnt2])
# admin.group.append(group1)
# admin.group.append(group2)
for i in admin.group:
    print(i.name)
