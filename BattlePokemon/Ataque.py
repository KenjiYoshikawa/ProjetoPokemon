__author__ = 'kenji'

from Validacao import Validacao
from Tipo import Tipo

class Ataque():

    @property
    def id(self): return self.__id

    @property
    def tipo(self): return self.__tipo

    @property
    def nome(self): return self.__nome

    @property
    def poder(self): return self.__poder

    def __init__(self, id, nome, tipo, acuracia, poder, pontos):
        self.__id = id
        self.__nome = nome
        self.__tipo = tipo
        self.__acuracia = acuracia
        self.__poder = poder
        self.__pontos = pontos
        self.__pontos_atual = pontos

    def print_ataque(self):
        print ("{id} - {nome} ({pontos_atual}/{pontos_total})"
               .format(id = self.__id,
                       nome = self.__nome,
                       pontos_atual = self.__pontos_atual,
                       pontos_total = self.__pontos)
        )

    #Retorna True caso o ataque possa ser realizado, diminuindo seus pontos em 1.
    def usar_ataque(self):
        if(self.__pontos_atual > 0):
            self.__pontos_atual -= 1
            return True
        else: return False

class Ataques_List():
    def __init__(self, ataques_detail):
        numero_de_ataques = Validacao(int(ataques_detail.pop()), int).validar()
        self.__lista_ataques = list()

        id_ataque = 0
        for i in range(0, int(numero_de_ataques)):
            nome_ataque = Validacao(ataques_detail.pop(), str).validar()
            tipo_ataque = Tipo.get_tipo(Validacao(ataques_detail.pop(), str).validar())
            acuracia_ataque = Validacao(int(ataques_detail.pop()), int).validar()
            poder_ataque = Validacao(int(ataques_detail.pop()), int).validar()
            pontos_ataque = Validacao(int(ataques_detail.pop()), int).validar()

            self.__lista_ataques.append(Ataque(i+1, nome_ataque, tipo_ataque, acuracia_ataque, poder_ataque, pontos_ataque))

    @property
    def list(self):
        return self.__lista_ataques