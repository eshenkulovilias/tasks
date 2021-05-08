class SchoolMember:
    """Представляет любого человека в школе."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        """Вывести информацию."""
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Представляет преподавателя."""

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        super().tell()
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        super().tell()
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()  # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print('I am breathing')

    def grow(self):
        print('I am growing')


class Unicellular(Animal):
    cell_count = 1


class Multicellular(Animal):
    def __init__(self, cell_count):
        super().__init__(name)
        self.cell_count = cell_count


class Amphibian(Multicellular):
    pass

