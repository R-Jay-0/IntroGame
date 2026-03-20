import random

class Ataque:
    def __init__(self, nome, dano, custo, acerto):
        self.nome = nome
        self.dano = dano
        self.custo = custo
        self.acerto = acerto

    def _roletar_acerto(self):
        resultado = random.choice(range(1, 101))
        if resultado in range(1, self.acerto+1):
            return True
        else:
            return False

ataques = {
    "mordida" : Ataque("Mordida", 10, 0, 100)    
}
