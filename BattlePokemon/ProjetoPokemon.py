# -*- coding: utf-8 -*-
__author__ = 'kenji'

import os
from Pokemon import Pokemon
from Batalha import Batalha
import fileinput
import sys

def main():

    poke_file = fileinput.input()
    while True:
        try:
            print("Insira os dados do primeiro Pokémon")
            first_pokemon = Pokemon(poke_file)
            break

        except OSError:
            print ("Pokemon não encontrado, digite um Pokemon válido")
    print()

    while True:
        try:
            print ("Insira os dados do segundo Pokémon")
            second_pokemon = Pokemon(poke_file)
            break

        except OSError:
            print ("Pokemon não encontrado, digite um Pokemon válido")

    batalha = Batalha(first_pokemon, second_pokemon)
    batalha_pokemon = batalha.start_battle()

    print ("\nBatalha Pokemon!")
    print (batalha_pokemon[0].nome, "inicia a batalha!\n")

    while True:
        try:
            while True:
                batalha_pokemon[0].print_all_status()
                id_ataque = input("Digite o número do ataque: ")
                print()
                if(id_ataque.isnumeric()):
                    if(batalha.ataque(batalha_pokemon[0], int(id_ataque), batalha_pokemon[1])): break
                else:
                    print("Entrada incorreta, informe o número do ataque")

            if (batalha_pokemon[0].atributo.HP <= 0 or batalha_pokemon[1].atributo.HP <= 0): break

            while True:
                batalha_pokemon[1].print_all_status()
                id_ataque = input("Digite o número do ataque: ")
                print()
                if(id_ataque.isnumeric()):
                    if(batalha.ataque(batalha_pokemon[1], int(id_ataque), batalha_pokemon[0])): break
                else:
                    print("Entrada incorreta, informe o número do ataque")

            if (batalha_pokemon[0].atributo.HP <= 0 or batalha_pokemon[1].atributo.HP <= 0): break
        except:
            raise

    print("Final da batalha!!!!")

if __name__ == "__main__":
    main()