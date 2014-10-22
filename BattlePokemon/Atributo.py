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

    def __init__(self, atributo_detail):
        self.__HP = Validacao(int(atributo_detail.pop()), int).validar()
        self.__ATK = Validacao(int(atributo_detail.pop()), int).validar()
        self.__DEF = Validacao(int(atributo_detail.pop()), int).validar()
        self.__SPD = Validacao(int(atributo_detail.pop()), int).validar()
        self.__SPC = Validacao(int(atributo_detail.pop()), int).validar()

    def receber_dano(self, damage):
        damage = Validacao(damage, int).validar()
        self.__HP -= damage

        if(self.__HP <= 0): return False
        else: return True