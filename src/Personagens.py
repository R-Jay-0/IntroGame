import random
from imagens import *
from Habilidades import *

class Personagem:
    def __init__(self, nome, sprites_personagem, vida, dano_base, energia, defesa, habilidades, chance_critico, speed):
        # Status
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.dano_base = dano_base
        self.energia_max = energia
        self.energia_atual = energia
        self.defesa = defesa
        self.habilidades = habilidades
        self.chance_crit = chance_critico
        self.velocidade = speed
        # Sprites
        self.corpo_inteiro = sprites_personagem[0]
        self.fotinha = pygame.transform.scale(sprites_personagem[1], (58, 70))
        # Situações
        self.defendendo = False
        self.fim_turno = False

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
                dano_bruto *= 1.3
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

    def _defender(self):
        self.defendendo = True

    def _resetar(self):
        self.energia_atual = self.energia_max
        self.vida_atual = self.vida_max
        self.defendendo = False
    
    def _esta_vivo(self):
        if self.vida <= 0:
            return False
        return True
    
    def _finalizar_turno(self):
        self.fim_turno = True


aliados = [
    Personagem("Albert Camus", sprites_camus, 100, 10, 50, 5, habilidades_camus, 25, 10),
    Personagem("Nicolau Copérnico", sprites_copernico, 110, 10, 60, 5, habilidades_copernico, 25, 20),
    Personagem("Marie Curie", sprites_curie, 120, 10, 70, 5, habilidades_curie, 5, 30),
    Personagem("Sêneca", sprites_seneca, 130, 10, 80, 5, habilidades_seneca, 5, 40),
    Personagem("Nikola Tesla", sprites_tesla, 140, 10, 90, 5, habilidades_tesla, 5, 50),
    Personagem("Vincent", sprites_prota, 150, 10, 100, 5, habilidades_prota, 5, 60)
]

inimigos = [

]