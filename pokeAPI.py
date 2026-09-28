import requests

def get_pokemon(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except requests.exceptions.RequestException:
        print('Connection Error: Could not connect to Pokemon API')


def pokemon_types(data):
    types = []
    for type_info in data["types"]:
        types.append(type_info['type']['name'].capitalize())
    return "Type: " + ", ".join(types)


def pokemon_abilities(data):
    abilities = []
    hidden_abilities = []
    for ability in data["abilities"]:
        if ability["is_hidden"]:
            hidden_abilities.append("Hidden Ability: " + ability["ability"]['name'].capitalize())
        else:
            abilities.append(ability["ability"]['name'].capitalize())
    return "Abilities: " + ", ".join(abilities) + '\n' + "".join(hidden_abilities)


def pokemon_stats(data):
    full_stats_names = []
    full_stats_values = []

    for stat_info in data["stats"]:
        full_stats_names.append(stat_info['stat']['name'].capitalize())
        full_stats_values.append(stat_info['base_stat'])

    total_bst = []
    formatted_stats = []

    for stats_names, stats_values in zip(full_stats_names, full_stats_values):
        total_bst.append(stats_values)
        formatted_stats.append(f"{stats_names}:{stats_values}")

    return formatted_stats, sum(total_bst)

def main():

    pokemon_search = input("Search Pokemon Name: ")

    data = get_pokemon(pokemon_search)

    if data is not None:

        my_pokemon_type = pokemon_types(data)
        my_pokemon_ability = pokemon_abilities(data)
        poke_stats, poke_bst = pokemon_stats(data)

        print(pokemon_search.capitalize().center(40, '-'))
        print("Name: " + data["name"].capitalize())

        print("-" * 40)
        print("National Pokedex No. " + str(data["id"]))
        print(my_pokemon_type)
        print(my_pokemon_ability)
        print("Height: " + str(round((((data["height"]) / 10) * 39.701), 1)) + " inches")
        print("Weight: " + str(round(((data["weight"]) * 0.220462), 1)) + " lbs")

        print((pokemon_search.capitalize() + ' ' + "Stats").center(40, '-'))

        for stat in poke_stats:
            print(stat)

        print("BaseStatTotal:" + str(poke_bst))
        print("-" * 40)

    else:
        print("Pokemon not found. Make sure it's spelled correctly.")

if __name__ == "__main__":
    while True:
        main()
        answer = input("Search Next Pokemon(Y or N): ").capitalize()

        while answer != 'Y' and answer != 'N':
            answer = input("Please Enter Y or N: ").capitalize()

        if answer == "N":
            print('-' * 40)
            break

