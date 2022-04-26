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

def create_pokedex(filepath):

    dex_dict = {}

    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return dex_dict

    file.readline()

    x = 0
    for line in file:
        entry = line.strip().split(',')
        dex_dict[entry[1]] = create_entry(entry[0], entry[1], entry[2], entry[3], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], entry[12])

    file.close()

    return dex_dict




def main():
    filepath = "pokemon.csv"
    pokedex = create_pokedex(filepath)
    pokemon_key = "Charizard"

    try:
        my_favorite_pokemon = pokedex[pokemon_key]
    except KeyError:
        print("ERROR: Pokemon {} does not exist!".format(pokemon_key))
    else:
        print("PRINTING {}'S INFORMATION..." .format(pokemon_key))
        for key in my_favorite_pokemon.keys():
            print("{}: {}".format(key, my_favorite_pokemon[key]))
main()



