# -*- coding: utf-8 -*-
__author__ = 'kenji'

import os
from Pokemon import Pokemon
from Batalha import Batalha

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

    while True:
        try:
            second_pokemon = input("Digite o nome do segundo Pokemon: ")
            second_pokemon_detail = open(PATH_POKEMON_LIST + second_pokemon)
            second_pokemon = Pokemon(second_pokemon_detail)
            break

        except OSError:
            print ("Pokemon não encontrado, digite um Pokemon válido")

    batalha = Batalha(first_pokemon, second_pokemon)
    batalha_pokemon = batalha.start_battle()

    print ("\nBatalha Pokemon!")
    print (batalha_pokemon[0].nome, "inicia a batalha!")

    while True:
        try:
            batalha_pokemon[0].print_ataques_pokemon()

            id_ataque = input("Digite o número do ataque")

        except:
            raise


if __name__ == "__main__":
    main()