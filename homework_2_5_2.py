from random import randint

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

random_name = names[randint(0, len(names)) - 1]
print(random_name)
with open(random_name, 'w') as new_file:
    pass


def func(file_names: list):
    for i in file_names:
        try:
            with open(i, 'r+') as f:
                f.write('Ilias')
        except FileNotFoundError:
            print(f'Файла {i} не существует')


func(names)
