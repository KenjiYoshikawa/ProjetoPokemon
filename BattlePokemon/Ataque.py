__author__ = 'kenji'

class Ataque():
    def __init__(self, id, nome, tipo, acuracia, poder, pontos):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.acuracia = acuracia
        self.poder = poder
        self.pontos = pontos
        self.pontos_atual = pontos

    def print_ataque(self):
        print ("{id} - {nome} ({pontos_atual}/{pontos_total})"
               .format(id = self.id,
                       nome = self.nome,
                       pontos_atual = self.pontos_atual,
                       pontos_total = self.pontos)
        )

    #Retorna True caso o ataque possa ser realizado, diminuindo seus pontos em 1.
    def usar_ataque(self):
        if(self.pontos_atual > 0):
            self.pontos_atual -= 1
            return True
        else: return False
