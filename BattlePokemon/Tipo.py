__author__ = 'kenji'

from enum import Enum
from Validacao import Validacao

class Tipo(Enum):
    Normal = 0
    Fight = 1
    Flying = 2
    Poison = 3
    Ground = 4
    Rock = 5
    Bug = 6
    Ghost = 7
    Fire = 8
    Water = 9
    Grass = 10
    Electric = 11
    Psychic = 12
    Ice = 13
    Dragon = 14
    Blank = 15

    def get_tipo(nome_tipo):

        nome_tipo = Validacao(nome_tipo, str).validar()

        lista_tipo = list(Tipo)
        for tipo in lista_tipo:
            if (tipo.name == nome_tipo):
                return tipo
        print (nome_tipo, "não é um tipo válido")
        raise TypeError

    def get_type_multiplier(tipo_ataca, tipo_defende):

        tipo_ataca = Validacao(tipo_ataca, Tipo).validar()
        tipo_defende = Validacao(tipo_defende, Tipo).validar()

        type_multiplier = list()
        #[Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Blank]

        normal = [1, 1, 1, 1, 1, 1/2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        type_multiplier.append(normal)

        fight = [2, 1, 1/2, 1/2, 1, 2, 1/2, 0, 1, 1, 1, 1, 1/2, 2, 1, 1]
        type_multiplier.append(fight)

        flying = [1, 2, 1, 1, 1, 1/2, 2, 1, 1, 1, 2, 1/2, 1, 1, 1, 1]
        type_multiplier.append(flying)

        poison = [1, 1, 1, 1/2, 1/2, 1/2, 1, 1/2, 1, 1, 2, 1, 1, 1, 1, 1]
        type_multiplier.append(poison)

        ground = [1, 1, 0, 2, 1, 2, 1/2, 1, 2, 1, 1/2, 2, 1, 1, 1, 1]
        type_multiplier.append(ground)

        rock = [1, 1/2, 2, 1, 1/2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1]
        type_multiplier.append(rock)

        bug = [1, 1/2, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 2, 1, 2, 1, 1, 1]
        type_multiplier.append(bug)

        ghost = [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
        type_multiplier.append(ghost)

        fire = [1, 1, 1, 1, 1, 1/2, 2, 1, 1/2, 1/2, 2, 1, 1, 2, 1/2, 1]
        type_multiplier.append(fire)

        water = [1, 1, 1, 1, 2, 2, 1, 1, 2, 1/2, 1/2, 1, 1, 1, 1/2, 1]
        type_multiplier.append(water)

        grass = [1, 1, 1/2, 1/2, 2, 2, 1/2, 1, 1/2, 2, 1/2, 1, 1, 1, 1/2, 1]
        type_multiplier.append(grass)

        electric = [1, 1, 2, 1, 0, 1, 1, 1, 1, 2, 1/2, 1/2, 1, 1, 1/2, 1]
        type_multiplier.append(electric)

        psychic = [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1]
        type_multiplier.append(psychic)

        ice = [1, 1, 2, 1, 2, 1, 1, 1, 1/2, 1/2, 2, 1, 1, 1/2, 2, 1]
        type_multiplier.append(ice)

        dragon = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
        type_multiplier.append(dragon)

        blank = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        type_multiplier.append(blank)

        return type_multiplier[tipo_ataca.value][tipo_defende.value]