# Tasks
# Chukwudi Ajoku 14th Dec. 2020

import requests
import json
import os.path


def act2():
    if os.path.exists("pokemon_data.json"):
        pok()
    else:
        pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        if pokemon.status_code == requests.codes.ok:
            pokemon_data = pokemon.json()
            with open("pokemon_data.json", "w") as f:
                json.dump(pokemon_data, f, indent=2)
                pok()


def pok():
    pokemon_names = []
    with open("pokemon_data.json") as file:
        pokemon = json.load(file)
        for i in range(len(pokemon["results"])):
            pokemon_names.append(pokemon["results"][i]["name"])

    search = ""
    guess = ""
    while guess != "yes":
        letter = input("Enter the name of the Pokemon one letter at a time: " ).lower()
        search = search + letter
        matching_names = [s for s in pokemon_names if str(search) in s]
        if len(search) <= 3:
            if len(matching_names) > 1:
                print("\nMy guesses are:")
            elif len(matching_names) == 1:
                print("My final guess is: ")
            else:
                raise Exception("Sorry, nothing")
            print(*matching_names, sep=" or ")
            guess = input("Is this correct?: ").lower()
            if guess == "yes"
                print("Sure thing")
        else:
            raise Exception("Sorry, no pokemon has that name")



act2()