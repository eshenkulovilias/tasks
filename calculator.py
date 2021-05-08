class Calculator:
    def __init__(self, brand, model, number_1, number_2):
        self.brand = brand
        self.model = model
        self.number_1 = number_1
        self.number_2 = number_2

    def show_info(self):
        try:
            return f'Brand: {self.brand}\nModel: {self.model}'
        except TypeError:
            return 'Вы должны вводить числа'

    def plus(self):
        try:
            return f'{self.number_1} + {self.number_2} = {self.number_1 + self.number_2}'
        except TypeError:
            return 'Вы должны вводить числа'

    def minus(self):
        try:
            return f'{self.number_1} - {self.number_2} = {self.number_1 - self.number_2}'
        except TypeError:
            return 'Вы должны вводить числа'

    def product(self):
        try:
            if type(self.number_1) == str or type(self.number_2) == str:
                raise TypeError
            else:
                return f'{self.number_1} * {self.number_2} = {self.number_1 * self.number_2}'
        except TypeError:
            return 'Вы должны вводить числа'

    def division(self):
        try:
            return f'{self.number_1} / {self.number_2} = {self.number_1 / self.number_2}'
        except ZeroDivisionError:
            return 'Нельзя делить на 0'
        except TypeError:
            return 'Вы должны вводить числа'


calculator_1 = Calculator('Canon', 'as-2020', 'qwe', 2)
print(calculator_1.show_info())
print(calculator_1.plus())
print(calculator_1.minus())
print(calculator_1.product())
print(calculator_1.division())
