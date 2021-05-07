class WashingMachine:
    def __init__(self):
        self.powder = 1000
        self.conditioner = 1000

    def wash_clothes(self, powder=int(input('Введите количество порошка: ')),
                     conditioner=int(input('Введите количество ополаскивателя: '))):
        if powder < self.powder and conditioner < self.conditioner:
            self.subtract_powder(powder)
            self.subtract_conditioner(conditioner)
            print('Стирка завершена')
        else:
            print('Пополните запасы!')

    def subtract_powder(self, powder):
        self.powder -= powder

    def subtract_conditioner(self, conditioner):
        self.conditioner -= conditioner


w = WashingMachine()
w.wash_clothes()
print(w.powder)
print(w.conditioner)
