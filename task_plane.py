class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'Brand: {self.brand}\nModel: {self.model}')


class Destroyer(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.can_fire = True

    def fire(self):
        print('I am firing')


class Stelth(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.is_visible = False

    def hide(self):
        print('I am hiding')


class Kukuruznik(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.can_fertilize = True

    def fertilize(self):
        print('I am fertilizing')


d = Destroyer('AS', '12-23')
print(d.can_fire)
d.fire()

s = Stelth('YT', '15-29')
print(s.is_visible)
s.hide()

k = Kukuruznik('QE', '32-18')
print(k.can_fertilize)
k.fertilize()
