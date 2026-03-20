import random

class Personagem:
    def __init__(self, nome, vida, dano_base, mana, defesa, habilidades, chance_critico):
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.dano_base = dano_base
        self.mana_max = mana
        self.mana_atual = mana
        self.defesa = defesa
        self.habilidades = habilidades
        self.defendendo = False
        self.chance_crit = chance_critico

    def _calc_dano(self, ataque_escolhido, alvo):
        dano_bruto = ataque_escolhido.dano + self.dano_base
        if alvo.defendendo: 
            if dano_bruto < alvo.defesa*1.5:
                return 0
            else:
                return round(dano_bruto - alvo.defesa*1.5)
        else:
            resultado = random.choice(range(1, 101))
            if resultado in range(1, self.chance_crit+1):
                dano_bruto *= 1.2
                dano_total = dano_bruto - alvo.defesa/2
                if dano_total < 0:
                    return 0 
                else: 
                    return round(dano)
            else:
                dano_total = dano_bruto - alvo.defesa
                if dano_total < 0:
                    return 0
                else:
                    return round(dano_total)

    def _atacar(self, ataque_escolhido, alvo):
        if ataque_escolhido._roletar_acerto():
            dano = self._calc_dano(ataque_escolhido, alvo)
            alvo.vida_atual -= dano
            print(f"{alvo.nome} Tomou {dano} de dano!")
        else:
            print(f"{self.nome} Errou o ataque!")

    def _resetar(self):
        self.mana_atual = self.mana_max
        self.vida_atual = self.vida_max
        self.defendendo = False