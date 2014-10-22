__author__ = 'kenji'


class Validacao():
    def __init__(self, valor, tipo):
        self.__valor = valor
        self.__tipo = tipo

    def validar(self):
        if(isinstance(self.__valor, self.__tipo)):
            return self.__valor
        else:
            print ("O parametro", self.__valor, "não é do tipo esperado", self.__tipo)
            raise TypeError