__author__ = 'kenji'

from Tipo import Tipo
from Ataque import Ataques_List
from Atributo import Atributo
from Validacao import Validacao


class Pokemon():

    @property
    def nome(self): return self.__nome

    @property
    def level(self): return self.__level

    @property
    def atributo(self): return self.__atributo

    @property
    def tipo1(self): return self.__tipo1

    @property
    def tipo2(self): return self.__tipo2

    def __init__(self, poke_file):
        try:
            print("Nome: ")
            self.__nome = Validacao(poke_file.readline(), str).validar()
            print("Level: ")
            self.__level = Validacao(int(poke_file.readline()), int).validar()
            self.__atributo = Atributo(poke_file)
            print("Tipo1: ")
            self.__tipo1 = Validacao(Tipo.get_tipo(poke_file.readline().strip()), Tipo).validar()
            print("Tipo2: ")
            self.__tipo2 = Validacao(Tipo.get_tipo(poke_file.readline().strip()), Tipo).validar()
            self.__lista_ataques = Ataques_List(poke_file).list

        except IndexError:
            print ("Arquivo de configuração do pokemon incorreto")

        except:
            raise

    def print_all_status(self):
        print("Turno: ", self.__nome)
        print("HP: ", self.__atributo.HP)
        print()
        self.print_ataques_pokemon()

    def parse_pokemon_file(self, pokemon_file):
        pokemon_file = pokemon_file.read().split('\n')
        pokemon_file.reverse()
        return pokemon_file

    def find_ataque(self, id):
        for ataque in self.__lista_ataques:
            if(ataque.id == id): return ataque
        return False

    def print_ataques_pokemon(self):
        for ataque in self.__lista_ataques:
            ataque.print_ataque()
        print()