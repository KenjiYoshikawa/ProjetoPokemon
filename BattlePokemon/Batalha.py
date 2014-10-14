__author__ = 'kenji'

class Batalha():

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def start_battle(self):
        spd1 = self.pokemon1.atributo.SPD
        spd2 = self.pokemon2.atributo.SPD

        return self.pokemon1 if spd1 > spd2 else self.pokemon2