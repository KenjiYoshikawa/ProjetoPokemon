__author__ = 'kenji'

from enum import Enum

class Tipo(Enum):
    Normal = 0
    Fighting = 1
    Flying = 2
    Poison = 3
    Ground = 4
    Rock = 5
    Bird = 6
    Bug = 7
    Ghost = 8
    Fire = 9
    Water = 10
    Grass = 11
    Electric = 12
    Psychic = 13
    Ice = 14
    Dragon = 15
    Blank = 16

    def get_tipo(nome_tipo):
        lista_tipo = list(Tipo)
        for tipo in lista_tipo:
            if (tipo.name == nome_tipo):
                return tipo
        return None