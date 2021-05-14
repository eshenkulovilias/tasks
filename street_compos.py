class Street:
    amount_of_yards = 0
    list_of_yards = []

    def __init__(self, name):
        self.name = name

    def add_yard(self, *yards):
        for yard in yards:
            self.list_of_yards.append(yard)
            self.amount_of_yards += 1
            yard.street = self


class Yard:
    amount_of_houses = 0
    list_of_houses = []
    street = None

    def __init__(self, name):
        self.name = name
        # street.list_of_yards.append(self)
        # street.amount_of_yards += 1

    def add_house(self, *houses):
        for house in houses:
            self.list_of_houses.append(house)
            self.amount_of_houses += 1
            house.address = f'Улица {self.street.name}, Двор {self.name}'


class House:
    address = ''

    def __init__(self, number):
        self.number = number
        # yard.list_of_houses.append(self)
        # yard.amount_of_houses += 1


h1 = House(1)
h2 = House(2)
h3 = House(3)

y1 = Yard('first')

s1 = Street('qwe')

s1.add_yard(y1)

y1.add_house(h1, h2, h3)

print(y1.amount_of_houses)

for i in y1.list_of_houses:
    print(f'Дом {i.number}')

print(h1.address)
