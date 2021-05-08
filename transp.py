class Transport:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def travel(self):
        print(f'Travelling from point {self.a} to point {self.b}')


class Car(Transport):
    def travel(self):

        super().travel()
        print(f'Travelling by road')


class Plane(Transport):
    def travel(self):
        super().travel()
        print(f'Travelling by air')


class Boat(Transport):
    def travel(self):
        super().travel()
        print(f'Travelling by water')


class Motorcycle(Car):
    def travel(self):
        super().travel()
        print(f'Very fast')


m = Motorcycle('A', 'B')
m.travel()
