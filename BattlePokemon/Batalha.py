__author__ = 'kenji'
from Pokemon import Pokemon
from Ataque import Ataque
from Validacao import Validacao
from random import random, uniform
import sys

class Batalha():

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def start_battle(self):
        spd1 = self.pokemon1.atributo.SPD
        spd2 = self.pokemon2.atributo.SPD

        #retorna uma lista com o Pokemon mais rápido na primeira posição
        return [self.pokemon1, self.pokemon2] if spd1 > spd2 else [self.pokemon2, self.pokemon1]

    def ataque(self, pokemon_ataca, id_ataque, pokemon_defende):

        #Validações
        pokemon_ataca = Validacao(pokemon_ataca, Pokemon).validar()
        pokemon_defende = Validacao(pokemon_defende, Pokemon).validar()
        id_ataque = Validacao(id_ataque, int).validar()
        ataque = pokemon_ataca.find_ataque(id_ataque)

        if (ataque):
            if(ataque.usar_ataque()):
                damage = int(self.calcular_dano(pokemon_ataca, pokemon_defende, ataque))
                if(pokemon_defende.atributo.receber_dano(damage)):
                    self._print_result_ataque(pokemon_ataca, ataque)

                else:
                    self._print_result_ataque(pokemon_ataca, ataque)
                    self._print_end_battle(pokemon_ataca, pokemon_defende)
                return True
            else:
                print("{ataque} não possui mais PPs, escolha outro ataque".format(ataque=ataque.nome))
                return False
        else:
            print("Índice incorreto, digite o número de um ataque válido")
            return False

    def calcular_dano(self, pokemon_ataca, pokemon_defende, ataque):
        ataque = Validacao(ataque, Ataque).validar()
        STAB = 1.5 if (pokemon_ataca.tipo1 == ataque.tipo or pokemon_ataca.tipo2 == ataque.tipo)  else 1

        #TODO calcular o type corretamente
        type = 1

        #Other não implementado
        other = 1

        modifier = STAB * type * self._critical_multiplier(pokemon_ataca) * other * uniform(0.85, 1)

        damage = ( (2 * pokemon_ataca.level + 10)/250 * (pokemon_ataca.atributo.ATK/pokemon_defende.atributo.DEF) * ataque.poder + 2) * modifier

        return damage

    def _critical_multiplier(self, pokemon):

        if(self._critical_prob(pokemon.atributo.SPD)):
            return (2*pokemon.level + 5)/(pokemon.level + 5)

        else: return 1

    def _critical_prob(self, SPD):
        prob = SPD/512
        if(random() < SPD): return True
        else: return False

    def _print_result_ataque(self, pokemon, ataque):
        print("************************************")
        print("\t{pokemon} usou {ataque} !!!".format(pokemon = pokemon.nome, ataque = ataque.nome))
        print("************************************")
        print()

    def _print_end_battle(self, pokemon_ataca, pokemon_defende):
        print("************************************")
        print("\t{} foi derrotado".format(pokemon_defende.nome))
        print("\t{} venceu!!!".format(pokemon_ataca.nome))
        print("************************************")
