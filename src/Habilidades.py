import random

class Habilidade:
    def __init__(self, nome, poder, custo, acerto, tipo, descricao):
        self.nome = nome
        self.custo = custo
        self.acerto = acerto
        self.descricao = descricao
        self.tipo = tipo

    def _roletar_acerto(self):
        resultado = random.choice(range(1, 101))
        if resultado in range(1, self.acerto+1):
            return True
        else:
            return False

habilidades_prota = [
    Habilidade("Bengalada", 5, 0, 100, "ataque", [
        "Vincent usa sua bengala para",
        "atacar o inimigo.",
        "dano: 5, energ.: 0; acerto: 100"
    ]), 
    Habilidade("fumar", 25, 20, 100, "cura", [
        "Vincent bafora seu caximbo.",
        "cura: 25; energ.: 20; acerto: 100"
    ]),
    Habilidade("solar bean", 50, 50, 80, "ataque", [
        "Vincent explode um inimigo.", 
        "dano: 50; energ.: sim; acerto: 80"
    ]),
    Habilidade("AAA", 50, 50, 80, "ataque", [
        "AAAAAAAAAAAAAAAAA", 
        "dano: 100; energ.: 70; acerto: 100"
    ])
]
habilidades_camus = [

]
habilidades_copernico = [

]
habilidades_curie = [

]
habilidades_seneca = [

]
habilidades_tesla = [

]