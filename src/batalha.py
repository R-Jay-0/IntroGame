import pygame
from Botao import Botao
from imagens import *

class Batalha:
    def __init__(self):
        pass









def _batalhar_1(display, lista_personagens):
    display.fill((0, 0, 0))

    display.blit(fundo_B1, (0, 0))

    rodada = 0
    turno_indice = 0

    botoes = []
    relogio = pygame.time.Clock()
    executando = True
    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if indice == 1:
                        return 2
                    elif indice == 0:
                        return 1
                    else:
                        return -1
                elif event.key == pygame.K_w:
                    if indice == 0:
                        indice = 2
                    else:
                        indice -= 1
                elif event.key == pygame.K_s:
                    if indice == 2:
                        indice = 0
                    else:
                        indice += 1

            display.fill((0, 0, 0))  # limpa a tela a cada ação
            display.blit(fundo_B1, (0, 0))


            for botao in botoes:
                if indice == botao.endereco:
                    botao._indicado()
                else:
                    botao._nao_indicado()
                botao._desenhar()

        # Atualização 

        # Renderização
        pygame.display.update()
        relogio.tick(60)
    pygame.quit()
    return -1
