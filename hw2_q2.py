"""
Author: Noa Kirschbaum
Assignment / Part: HW9 - Q2 and Q3
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def add_battle_stats(battle_dict, hp, attack, defense, sp_attack, sp_defense, speed):
    battle_dict = {'HP': hp, 'Attack': attack, 'Defense': defense, 'Sp. Atk': sp_attack, 'Sp. Def': sp_defense, 'Spd': speed}
    return battle_dict

def create_entry(number, name, type_1, type_2, health_points, attack, defense, special_attack, special_defense, speed, generation, is_legendary):
    if len(type_2) > 0:
        ty_list = [type_1, type_2]
    else:
        ty_list = [type_1, None]

    poke_dict = {'Number': number, 'Name': name, 'Type': tuple(ty_list), 'Battle Stats': {}, 'Generation': generation, 'Legendary': is_legendary}

    poke_dict['Battle Stats'] = add_battle_stats(poke_dict['Battle Stats'], health_points, attack, defense, special_attack, special_defense, speed)

    return poke_dict



def main():
    a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel", 25, 35, 70, 95, 55, 45, 1, False)
    for key in a_random_pokemon.keys():
        print("{}: {}".format(key, a_random_pokemon[key]))

main()




