import random
def draw_attack_cards():
    thrust_cards = [("Thrust", 1), ("Thrust", 2), ("Thrust", 3), ("Thrust", 4), ("Thrust", 5), ("Thrust", 6), ("Thrust", 7), ("Thrust", 8), ("Thrust", 9)]
    strike_cards = [("Strike", 1), ("Strike", 2), ("Strike", 3), ("Strike", 4), ("Strike", 5), ("Strike", 6), ("Strike", 7), ("Strike", 8), ("Strike", 9)]
    smash_cards = [("Smash", 1), ("Smash", 2), ("Smash", 3), ("Smash", 4), ("Smash", 5), ("Smash", 6), ("Smash", 7), ("Smash", 8), ("Smash", 9)]
    draw_thrust_card = random.sample(thrust_cards, k=1)
    draw_strike_card = random.sample(strike_cards, k=1)
    draw_smash_card = random.sample(smash_cards, k=1)
    return draw_thrust_card + draw_strike_card + draw_smash_card

def draw_defense_cards():
    parry_cards = [("Parry", 1), ("Parry", 1), ("Parry", 2), ("Parry", 3), ("Parry", 4), ("Parry", 5), ("Parry", 6), ("Parry", 7), ("Parry", 8), ("Parry", 9)]
    block_cards = [("Block", 1), ("Block", 1), ("Block", 2), ("Block", 3), ("Block", 4), ("Block", 5), ("Block", 6), ("Block", 7), ("Block", 8), ("Block", 9)]
    dodge_cards = [("Dodge", 1), ("Dodge", 1), ("Dodge", 2), ("Dodge", 3), ("Dodge", 4), ("Dodge", 5), ("Dodge", 6), ("Dodge", 7), ("Dodge", 8), ("Dodge", 9)]
    draw_parry_card = random.sample(parry_cards, k=1)
    draw_block_card = random.sample(block_cards, k=1)
    draw_dodge_card = random.sample(dodge_cards, k=1)
    return draw_parry_card + draw_block_card + draw_dodge_card