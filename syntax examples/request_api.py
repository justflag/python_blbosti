#How to ocnnect to an API using python
import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(name):
    url = f"{base_url}/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print("Data retrieved")
        pokemon_data = response.json()
        #print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to fetch data {response.status_code}")

pokemon_name = "charizard"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

