class Warrior():
    def __init__(self, name, thrust, strike, smash, health, cards, player):
        self.name = name
        self.thrust = thrust
        self.strike = strike
        self.smash = smash
        self.health = health
        self.cards = cards
        self.player = player

#player = false is overwritten when the user chooses their character. It is used in take_turn to identify which character the player is using.
#cards is blank because cards are drawn in draw_card,
char_kumayari = Warrior("Kumayari", 5, 3, 2, 100, [], False)
char_sir_frederick = Warrior("Sir Frederick", 1, 3, 6, 100, [], False)
char_kiln = Warrior("Kiln", 4, 3, 3, 100, [], False)
char_sint_drage = Warrior("Sint Drage", 4, 5, 1, 100, [], False)
char_testudo_iratus = Warrior("Testudo Iratus", 4, 4, 2, 100, [], False)