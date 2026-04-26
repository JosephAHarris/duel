#This is my attempt at working out the dueling mechanic for a game I'm working on. When an officer attacks the other,
#a duel is triggered. The two officers battle each other until one is fully beaten. 
#Every officer will have 3 attacks. Thrust, Strike, and Smash. They will also have 3 defensive options. Parry, Block, and Dodge
#A duel will work like Rock, Paper, Scissors.
#Thrust and Block are paper.
#Strike and Dodge are Rock.
#Smash and Parry are Scissors.
#If the attacker loses the matchup, there is no damage. For instance, Thrust is countered by Parry.
#If the defender loses the matchup, there is double damage. For instance, Thrust deals double damage vs Dodge
#If neither win, the attacker deals normal damage, for instance, Thrust being used against Block.
#The two officer exchange blows. The attacker in round 1 is the defender in round 2. 
#Each player draws 3 of each type of card. 
#The attacker gets 3 Thrust, 3 Strike, and 3 Smash cards.
#The defender gets 3 Parry, 3 Block, and 3 Dodge cards.
#The cards will have a power between 1 and 9. Higher is better.
#Each officer will have a number assigned to each type of attack. For instance, Sir Frederick wields a mace.
#He has 5 Smash, 3 Strike, and 1 Thrust as base damage.
#If Sir Frederick uses a 9 power Smash card, his smash stat will be 14. 
#This also means he should be using more Smash and Strike attacks than Thrust.
#Defense card power will reduce the power of the attack, but only a successful matchup can negate all damage.
#The minimum power of a successful attack is 1. If a 2 power attack is met by a 9 power defense, the damage will still be 1.
import random
import roster

def get_input(min, max):
    while True:
        try:
            choice = int(input())
            if choice < min or choice > max:
                print(f"Please choose a number from {min} to {max} ")
            else:
                return choice
        except ValueError:
            print(f"Please choose a number from {min} to {max} ")

def draw_attack_cards():
    thrust_cards = [("Thrust", 1), ("Thrust", 1), ("Thrust", 2), ("Thrust", 3), ("Thrust", 4), ("Thrust", 5), ("Thrust", 6), ("Thrust", 7), ("Thrust", 8), ("Thrust", 9)]
    strike_cards = [("Strike", 1), ("Strike", 1), ("Strike", 2), ("Strike", 3), ("Strike", 4), ("Strike", 5), ("Strike", 6), ("Strike", 7), ("Strike", 8), ("Strike", 9)]
    smash_cards = [("Smash", 1), ("Smash", 1), ("Smash", 2), ("Smash", 3), ("Smash", 4), ("Smash", 5), ("Smash", 6), ("Smash", 7), ("Smash", 8), ("Smash", 9)]
    draw_thrust_cards = random.sample(thrust_cards, k=3)
    draw_strike_cards = random.sample(strike_cards, k=3)
    draw_smash_cards = random.sample(smash_cards, k=3)
    return draw_thrust_cards + draw_strike_cards + draw_smash_cards

def draw_defense_cards():
    parry_cards = [("Parry", 1), ("Parry", 1), ("Parry", 2), ("Parry", 3), ("Parry", 4), ("Parry", 5), ("Parry", 6), ("Parry", 7), ("Parry", 8), ("Parry", 9)]
    block_cards = [("Block", 1), ("Block", 1), ("Block", 2), ("Block", 3), ("Block", 4), ("Block", 5), ("Block", 6), ("Block", 7), ("Block", 8), ("Block", 9)]
    dodge_cards = [("Dodge", 1), ("Dodge", 1), ("Dodge", 2), ("Dodge", 3), ("Dodge", 4), ("Dodge", 5), ("Dodge", 6), ("Dodge", 7), ("Dodge", 8), ("Dodge", 9)]
    draw_parry_cards = random.sample(parry_cards, k=3)
    draw_block_cards = random.sample(block_cards, k=3)
    draw_dodge_cards = random.sample(dodge_cards, k=3)
    return draw_parry_cards + draw_block_cards + draw_dodge_cards

def get_character(character):
    match character:
        case 1:
            return roster.char_kumayari
        case 2:
            return roster.char_sir_frederick
        case 3:
            return roster.char_kiln
        case 4: 
            return roster.char_sint_drage

def player_turn(user, opp):
    user.cards = draw_attack_cards()
    opp.cards = draw_defense_cards()
    opp_defense = opp_logic(opp.cards, user)
    print(user.cards)
    user_card = get_input(1 , 9)
    

def do_battle(user, opp):
    while True:
        if opp.health < 1:
            return f"{user.name} is the victor!"
        if user.health < 1:
            return f"{opp.name} is the victor!"
        else:
            player_turn(user, opp)
            opponent_turn(user, opp)
                

def opp_logic(cards, opponent):
    for card in cards:


def main():

    print("Choose your warrior!\n1. Kumayari, the Samurai\n2. Sir Frederick, the Knight\n3. Kiln, the Adventurer\n4. Sint Drage, the Dragon Warrior")
    player_choice = get_input(1, 4)
    player_character = get_character(player_choice)

    print("Choose your opponent!\n1. Kumayari, the Samurai\n2. Sir Frederick, the Knight\n3. Kiln, the Adventurer\n4. Sint Drage, the Dragon Warrior")
    opponent_choice = get_input(1, 4)
    opponent_character = get_character(opponent_choice)

    print(f"The battle between {player_character.name} and {opponent_character.name} begins!")
    winner = do_battle(player_character, opponent_character)
    print(winner)
main()

