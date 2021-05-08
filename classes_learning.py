# class Cube:
#     def __init__(self, length, height, width):
#         self.length = length
#         self.height = height
#         self.width = width
#
#     def calculate_cube_volume(self):
#         return f'My volume is {self.length * self.height * self.width}'
#
#
# cube_1 = Cube(12, 2, 3)
# cube_2 = Cube(4, 8, 2)
# cube_3 = Cube(2, 3, 4)
#
# print(cube_1.calculate_cube_volume())
# print(cube_2.calculate_cube_volume())
# print(cube_3.calculate_cube_volume())

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f'My name is {self.name}\nI am {self.age} years old\nMy gender is {self.gender}')

    def come_to_lesson(self):
        print('Пришел на урок')

    def do_homework(self):
        print('Сделал домашнее задание')


student_1 = Student('John', 23, 'male')
student_2 = Student('Alice', 19, 'female')

student_1.show_info()
student_1.come_to_lesson()
print()

student_2.show_info()
student_2.do_homework()
