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

    def __init__(self, pokemon_detail):
        try:
            pokemon_detail = self.parse_pokemon_file(pokemon_detail)

            self.__nome = Validacao(pokemon_detail.pop(), str).validar()
            self.__level = Validacao(int(pokemon_detail.pop()), int).validar()
            self.__atributo = Atributo(pokemon_detail)
            self.__tipo1 = Tipo.get_tipo(pokemon_detail.pop())
            self.__tipo2 = Tipo.get_tipo(pokemon_detail.pop())
            self.__lista_ataques = Ataques_List(pokemon_detail).list

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