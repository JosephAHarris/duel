class Warrior():
    def __init__(self, name, thrust, strike, smash, health, cards):
        self.name = name
        self.thrust = thrust
        self.strike = strike
        self.smash = smash
        self.health = health
        self.cards = cards


char_kumayari = Warrior("Kumayari", 5, 3, 2, 300, [])
char_sir_frederick = Warrior("Sir Frederick", 1, 3, 6, 300, [])
char_kiln = Warrior("Kiln", 4, 3, 3, 300, [])
char_sint_drage = Warrior("Sint Drage", 4, 5, 1, 300, [])
char_testudo_iratus = Warrior("Testudo Iratus", 4, 4, 2, 300, [])