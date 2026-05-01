from draw_card import draw_attack_cards, draw_defense_cards
import random
from input import get_input

#take_turn draws cards for both and checks to see which side the player is on, and allows the player to choose a card.
def take_turn(attack, defense):
    attack.cards = draw_attack_cards()
    defense.cards = draw_defense_cards()
    if attack.player == True:
        print("Choose your attack!")
        print(f"1. {attack.cards[0][0]} {attack.cards[0][1]} ({attack.cards[0][1] + attack.thrust} total power)\n2. {attack.cards[1][0]} {attack.cards[1][1]} ({attack.cards[1][1] + attack.strike} total power)\n3. {attack.cards[2][0]} {attack.cards[2][1]} ({attack.cards[2][1] + attack.smash} total power)\n")
        user_input = get_input(1 , 3)
        attack.cards = attack.cards[user_input - 1]
    else:
        attack.cards = opp_attack_logic(attack.cards)

    if defense.player == True:
        print("Choose your defense!")
        print(f"1. {defense.cards[0][0]} {defense.cards[0][1]}\n2. {defense.cards[1][0]} {defense.cards[1][1]}\n3. {defense.cards[2][0]} {defense.cards[2][1]}")
        user_input = get_input(1 , 3)
        defense.cards = defense.cards[user_input - 1]
    else:
        defense.cards = opp_defense_logic(defense.cards)
    
    do_attack(attack, defense)

#do_attack matches the card types together, then works out what happens based on the power of the cards and the base attacking stat of the character.
def do_attack(attacker, defender):
    print(f"{attacker.name} attacks with a {attacker.cards[0]} of {attacker.cards[1]} power!\n{defender.name} answers with a {defender.cards[0]} of {defender.cards[1]} power!\n")
    damage = 0
    match attacker.cards[0]:
        case "Thrust":
            match defender.cards[0]:
                case "Parry":
                    print(f"{defender.name} successfully parries {attacker.name}'s thrust!\n")
                
                case "Dodge":
                    if (attacker.thrust + attacker.cards[1]) - defender.cards[1] < 1:
                        damage = 1
                    else:
                        damage = (attacker.thrust + attacker.cards[1]) - defender.cards[1]

                    defender.health -= damage
                    print(f"{attacker.name} thrusts and stabs {defender.name} for {damage} damage!\n")
                
                case "Block":
                    if (((attacker.thrust + attacker.cards[1]) - defender.cards[1]) +10) < 10:
                        damage = 10
                    else:
                        damage = ((attacker.thrust + attacker.cards[1]) - defender.cards[1]) +10
                    defender.health -= damage
                    print(f"{attacker.name} thrusts past {defender.name}'s block and skewers him for {damage} damage!\n")
        
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
                    print(f"{attacker.name} strikes {defender.name} for {damage} damage!\n")

                case "Dodge":
                    if (((attacker.strike + attacker.cards[1]) - defender.cards[1]) +10) < 10:
                        damage = 2
                    else:
                        damage = ((attacker.strike + attacker.cards[1]) - defender.cards[1]) +10

                    defender.health -= damage
                    print(f"{attacker.name} lands a mighty strike on {defender.name} for {damage} damage!\n")

        case "Smash":
            match defender.cards[0]:
                case "Dodge":
                    print(f"{defender.name} successfully dodges {attacker.name}'s smash!\n")

                case "Block":
                    if (attacker.smash + attacker.cards[1]) - defender.cards[1] < 1:
                        damage = 1
                    else:
                        damage = (attacker.smash + attacker.cards[1]) - defender.cards[1]

                    defender.health -= damage
                    print(f"{attacker.name} smashes his weapon into {defender.name} for {damage} damage!\n")

                case "Parry":
                    if (((attacker.smash + attacker.cards[1]) - defender.cards[1]) + 10) < 10:
                        damage = 10
                    else:
                        damage = ((attacker.smash + attacker.cards[1]) - defender.cards[1]) + 10

                    defender.health -= damage
                    print(f"{attacker.name} smashes through {defender.name}'s parry for {damage} damage!\n")


#I intend to work on these more later. Right now, I'm more interested in getting the rest of the program set up. 
def opp_defense_logic(opp_cards):
    choice = random.randint(0,2)
    return opp_cards[choice]


def opp_attack_logic(opp_cards):
    choice = random.randint(0,2)
    return opp_cards[choice]