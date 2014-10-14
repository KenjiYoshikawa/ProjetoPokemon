__author__ = 'kenji'

from Tipo import Tipo
from Ataque import Ataque
from Atributo import Atributo

class Pokemon():
    def __init__(self, pokemon_detail):

        #Parse do arquivo da especificação do pokemon
        pokemon_detail = pokemon_detail.read().split('\n')
        pokemon_detail.reverse()

        self.nome = pokemon_detail.pop()
        self.level = pokemon_detail.pop()

        #atributos
        HP = pokemon_detail.pop()
        ATK = pokemon_detail.pop()
        DEF = pokemon_detail.pop()
        SPD = pokemon_detail.pop()
        SPC = pokemon_detail.pop()

        self.atributo = Atributo(HP, ATK, DEF, SPD, SPC)

        #tipos
        tipo1 = pokemon_detail.pop()
        tipo2 = pokemon_detail.pop()

        self.tipo1 = Tipo.get_tipo(tipo1)
        self.tipo2 = Tipo.get_tipo(tipo2)

        #ataques
        numero_de_ataques = pokemon_detail.pop()
        lista_ataques = list()
        for i in range(0, int(numero_de_ataques)):
            nome_ataque = pokemon_detail.pop()
            tipo_ataque = pokemon_detail.pop()
            acuracia_ataque = pokemon_detail.pop()
            poder_ataque = pokemon_detail.pop()
            pontos_ataque = pokemon_detail.pop()

            ataque = Ataque(nome_ataque, tipo_ataque, acuracia_ataque, poder_ataque, pontos_ataque)
            lista_ataques.append(ataque)

        self.lista_ataques = lista_ataques