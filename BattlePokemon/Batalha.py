__author__ = 'kenji'

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

        #TODO Calcular o ataque com base na fórmula dada

        ataque = pokemon_ataca.find_ataque(id_ataque)
        