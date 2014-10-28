__author__ = 'kenji'
from Validacao import Validacao

class Atributo():

    @property
    def HP(self):return  self.__HP

    @property
    def ATK(self):return  self.__ATK

    @property
    def DEF(self):return  self.__DEF

    @property
    def SPD(self):return  self.__SPD

    @property
    def SPC(self):return  self.__SPC

    def __init__(self, poke_file):
        print("HP: ")
        self.__HP = Validacao(int(poke_file.readline()), int).validar()
        print("ATK: ")
        self.__ATK = Validacao(int(poke_file.readline()), int).validar()
        print("DEF: ")
        self.__DEF = Validacao(int(poke_file.readline()), int).validar()
        print("SPD: ")
        self.__SPD = Validacao(int(poke_file.readline()), int).validar()
        print("SPC: ")
        self.__SPC = Validacao(int(poke_file.readline()), int).validar()

    def receber_dano(self, damage):
        damage = Validacao(damage, int).validar()
        self.__HP -= damage

        if(self.__HP <= 0): return False
        else: return True