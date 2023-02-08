class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase

    def print_name(self):
        print(self.name)

    def health_2(self):
        self.health_points *= 2
        print(f"Updated health points: {self.health_points}")

    def __str__(self):
        return f"Nickname -> {self.nickname} \n" \
               f"SuperPower -> {self.superpower} \n" \
               f"Health -> {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


barbie = SuperHero("Aijamal", "aijamal.08", "Screaming", 200, "Baidoolot Yilak")

barbie.print_name()
barbie.health_2()
print(barbie)
print(len(barbie))
print()


class AirHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health_2(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')

class CosmicHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health_2(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')

airHero = AirHero('SuperMan', 'S', 'Devil Eyes', 500, 'Batman is so weak!!!', 100)
print(airHero)
airHero.health_2()
airHero.method_fly()
print()

cosmicHero = CosmicHero('Blast', 'Bl', 'Teleport', 700, 'Saitamaaaa!', 150)
print(cosmicHero)
cosmicHero.health_2()
cosmicHero.method_fly()
print()

class Villain(CosmicHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return hero.damage ** 2


villain = Villain('Garou', 'Gaara', 'Beast', 1000, 'All heroes must to die!!!')
print(villain.crit(airHero))