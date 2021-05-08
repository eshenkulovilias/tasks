class WashingMachine:
    def __init__(self):
        self.powder = 1000
        self.conditioner = 1000

    def wash_clothes(self, powder=int(input('Введите количество порошка: ')),
                     conditioner=int(input('Введите количество ополаскивателя: '))):
        if powder > self.powder and conditioner > self.conditioner:
            print(f'Пополните запасы порошка на {(powder - self.powder)} гр\n'
                  f'И ополаскивателя на {(conditioner - self.conditioner)} мл')
        elif powder > self.powder:
            print(f'Пополните запасы порошка на {(powder - self.powder)} гр')
        elif conditioner > self.conditioner:
            print(f'Пополните запасы ополаскивателя на {(conditioner - self.conditioner)} мл')
        else:
            self.subtract_powder(powder)
            self.subtract_conditioner(conditioner)
            print('Стирка завершена')
            print(f'Порошка осталось {self.powder}гр')
            print(f'Ополаскивателя осталось {self.conditioner}мл')

    def subtract_powder(self, powder):
        self.powder -= powder

    def subtract_conditioner(self, conditioner):
        self.conditioner -= conditioner


w = WashingMachine()
w.wash_clothes()
