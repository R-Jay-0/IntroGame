import random

class Habilidade:
    def __init__(self, nome, poder, custo, acerto):
        self.nome = nome
        self.dano = poder
        self.custo = custo
        self.acerto = acerto

    def _roletar_acerto(self):
        resultado = random.choice(range(1, 101))
        if resultado in range(1, self.acerto+1):
            return True
        else:
            return False