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

    @property
    def acuracia(self): return self.__acuracia

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
    def __init__(self, poke_file):
        self.__lista_ataques = list()

        print("Número de ataques: ")
        numero_de_ataques = Validacao(int(poke_file.readline()), int).validar()
        id_ataque = 0
        for i in range(0, numero_de_ataques):
            print("Nome do ataque: ")
            nome_ataque = Validacao(poke_file.readline().strip(), str).validar()
            print("Tipo do ataque: ")
            tipo_ataque = Tipo.get_tipo(Validacao(poke_file.readline().strip(), str).validar())
            print("Acurácia do ataque: ")
            acuracia_ataque = Validacao(int(poke_file.readline()), int).validar()
            print("Poder do ataque: ")
            poder_ataque = Validacao(int(poke_file.readline()), int).validar()
            print("Pontos do ataque: ")
            pontos_ataque = Validacao(int(poke_file.readline()), int).validar()

            self.__lista_ataques.append(Ataque(i+1, nome_ataque, tipo_ataque, acuracia_ataque, poder_ataque, pontos_ataque))

    @property
    def list(self):
        return self.__lista_ataques