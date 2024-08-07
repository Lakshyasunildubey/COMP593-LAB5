'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main(pokemon):
   
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    pokemon = str(pokemon_name).strip().lower()
    print(f"Getting information on {pokemon}.")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched Pokémon Info")
        return response()
    else:
        print(f"Failed to fetch Pokémon. Status code: {response.status_code}")
        return None
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    
    return

if __name__ == '__main__':
    main()