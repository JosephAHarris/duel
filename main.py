#This is my attempt at working out the dueling mechanic for a game I'm working on. When an officer attacks the other,
#a duel is triggered. The two officers battle each other until one is fully beaten. 
#Every officer will have 3 attacks. Thrust, Strike, and Smash. They will also have 3 defensive options. Parry, Block, and Dodge
#A duel will work like Rock, Paper, Scissors.
#Thrust and Dodge are Paper.
#Strike and Parry are Scissors.
#Smash and Block are Rock.
#If the attacker loses the matchup, there is no damage. For instance, Thrust is countered by Parry.
#If the defender loses the matchup, there is double damage. For instance, Thrust deals double damage vs Dodge
#If neither win, the attacker deals normal damage, for instance, Thrust being used against Block.
#The two officer exchange blows. The attacker in round 1 is the defender in round 2. 
#Each player draws 1 of each type of card. 
#The cards will have a power between 1 and 9. Higher is better.
#Each officer will have a number assigned to each type of attack. For instance, Sir Frederick wields a mace.
#He has 5 Smash, 3 Strike, and 1 Thrust as base damage.
#If Sir Frederick uses a 9 power Smash card, his smash stat will be 14. 
#This also means he should be using more Smash and Strike attacks than Thrust.
#Defense card power will reduce the power of the attack, but only a successful matchup can negate all damage.
#The minimum power of a successful attack is 1. If a 2 power attack is met by a 9 power defense, the damage will still be 1.
import random
import copy
import roster
from draw_card import draw_attack_cards, draw_defense_cards
from turn import take_turn
from input import get_input

def get_character(character):
    match character:
        case 1:
            return copy.deepcopy(roster.char_kumayari)
        case 2:
            return copy.deepcopy(roster.char_sir_frederick)
        case 3:
            return copy.deepcopy(roster.char_kiln)
        case 4: 
            return copy.deepcopy(roster.char_sint_drage)
    
#do_battle should loop between attack and defense phases for the player and the computer until one of defeated, then return the conclusion of the battle.
def do_battle(user, opp):
    while True:
        print(f"{user.name} has {user.health} left.\n{opp.name} has {opp.health} left.")
        take_turn(user, opp)
        if opp.health < 1:
            return(f"{opp.name} has been defeated!")
        take_turn(opp, user)
        if user.health < 1:
            return(f"{user.name} has been defeated!")

            

def main():
    #Choosing a warrior returns a copy of the character, allowing mirror matches.
    print("Choose your warrior!\n1. Kumayari, the Samurai\n2. Sir Frederick, the Knight\n3. Kiln, the Adventurer\n4. Sint Drage, the Dragon Warrior")
    player_choice = get_input(1, 4)
    player_character = get_character(player_choice)
    player_character.player = True

    print("Choose your opponent!\n1. Kumayari, the Samurai\n2. Sir Frederick, the Knight\n3. Kiln, the Adventurer\n4. Sint Drage, the Dragon Warrior")
    opponent_choice = get_input(1, 4)
    opponent_character = get_character(opponent_choice)

    #do_battle should loop until either the player or the computer character's health drops below 1, hen print 
    print(f"The battle between {player_character.name} and {opponent_character.name} begins!")
    conclusion = do_battle(player_character, opponent_character)
    print(conclusion)
main()

