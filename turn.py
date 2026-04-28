from draw_card import draw_attack_cards, draw_defense_cards
import random
from input import get_input

#take_turn draws cards for both and checks to see which side the player is on, and allows the player to choose a card.
def take_turn(attack, defense):
    attack.cards = draw_attack_cards()
    defense.cards = draw_defense_cards()
    if attack.player == True:
        print(attack.cards)
        user_input = get_input(1 , 3)
        attack.cards = attack.cards[user_input - 1]
    else:
        attack.cards = opp_attack_logic(attack.cards)

    if defense.player == True:
        print(defense.cards)
        user_input = get_input(1 , 3)
        defense.cards = defense.cards[user_input - 1]
    else:
        defense.cards = opp_defense_logic(defense.cards)
    
    do_attack(attack, defense)

#do_attack matches the card types together, then works out what happens based on the power of the cards and the base attacking stat of the character.
def do_attack(attacker, defender):
    damage = 0
    match attacker.cards[0]:
        case "Thrust":
            match defender.cards[0]:
                case "Parry":
                    print(f"{defender.name} successfully parries {attacker.name}'s thrust!")
                
                case "Dodge":
                    if (attacker.thrust + attacker.cards[1]) - defender.cards[1] < 1:
                        damage = 1
                    else:
                        damage = (attacker.thrust + attacker.cards[1]) - defender.cards[1]

                    defender.health -= damage
                    print(f"{attacker.name} thrusts and stabs {defender.name} for {damage} damage!\n")
                
                case "Block":
                    if (((attacker.thrust + attacker.cards[1]) - defender.cards[1]) *2) < 2:
                        damage = 2
                    else:
                        damage = ((attacker.thrust + attacker.cards[1]) - defender.cards[1]) *2
                    defender.health -= damage
                    print(f"{attacker.name} thrusts past {defender.name}'s block and skewers him for {damage} damage!")
        
        case "Strike":
            match defender.cards[0]:
                case "Block":
                    print(f"{defender.name} successfully blocks {attacker.name}'s strike!")

                case "Parry":
                    if (attacker.strike + attacker.cards[1]) - defender.cards[1] < 1:
                        damage = 1
                    else:
                        damage = (attacker.strike + attacker.cards[1]) - defender.cards[1]
                    defender.health -= damage
                    print(f"{attacker.name} strikes {defender.name} for {damage} damage!")

                case "Dodge":
                    if (((attacker.strike + attacker.cards[1]) - defender.cards[1]) *2) < 2:
                        damage = 2
                    else:
                        damage = ((attacker.strike + attacker.cards[1]) - defender.cards[1]) *2

                    defender.health -= damage
                    print(f"{attacker.name} lands a mighty strike on {defender.name} for {damage} damage!")

        case "Smash":
            match defender.cards[0]:
                case "Dodge":
                    print(f"{defender.name} successfully dodges {attacker.name}'s smash!")

                case "Block":
                    if (attacker.smash + attacker.cards[1]) - defender.cards[1] < 1:
                        damage = 1
                    else:
                        damage = (attacker.smash + attacker.cards[1]) - defender.cards[1]

                    defender.health -= damage
                    print(f"{attacker.name} smashes his weapon into {defender.name} for {damage} damage!")

                case "Parry":
                    if (((attacker.smash + attacker.cards[1]) - defender.cards[1]) *2) < 2:
                        damage = 2
                    else:
                        damage = ((attacker.smash + attacker.cards[1]) - defender.cards[1]) * 2

                    defender.health -= damage
                    print(f"{attacker.name} smashes through {defender.name}'s parry for {damage} damage!")


#I intend to work on these more later. Right now, I'm more interested in getting the rest of the program set up. 
def opp_defense_logic(opp_cards):
    choice = random.randint(0,2)
    return opp_cards[choice]


def opp_attack_logic(opp_cards):
    choice = random.randint(0,2)
    return opp_cards[choice]