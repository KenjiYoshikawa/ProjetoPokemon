# -*- coding: utf-8 -*-
__author__ = 'kenji'

import
from Pokemon import Pokemonos

def main():
    PATH_POKEMON_LIST = os.path.abspath("PokemonList") + "/"

    while True:
        try:
            first_pokemon = input("Digite o nome do primeiro Pokemon: ")
            first_pokemon_detail = open(PATH_POKEMON_LIST + first_pokemon)
            first_pokemon = Pokemon(first_pokemon_detail)
            break

        except OSError:
            print ("Pokemon não encontrado, digite um Pokemon válido")

if __name__ == "__main__":
    main()