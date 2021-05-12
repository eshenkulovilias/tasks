class Team:
    def __init__(self, name, list_of_members):
        self.name = name
        self.list_of_members = list_of_members


class Hero:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


hero1 = Hero('Tor', 'hammer')
hero2 = Hero('Iron Man', 'fly')
hero3 = Hero('Spider man', 'spiderweb')
list_of_heroes = [hero1, hero2, hero3]
team1 = Team('Avengers', list_of_heroes)
for i in team1.list_of_members:
    print(i.name)
