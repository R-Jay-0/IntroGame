import pygame
from Botao import *
from menu import _menu
from selecao import _selecao
from batalha import _batalhar
from var_universais import *

########## COMEÇO PROGRAMA #############

pygame.init()

tela = pygame.display.set_mode((1024, 720))

pygame.display.set_caption("Nome do joojj")

'''
As funções retornam um número e cada número corresponde a uma "tela" do jogo¬

-1: O programa deve ser interrompido
0: Tela inicial de menu
1: Tela de seleção de personagens
2: Tela de Tutorial
3: Tela de batalha
'''

cenario = 0
executando = True
while executando:
    
    if cenario == -1:
        executando = False
    elif cenario == 0:
        cenario = _menu(tela)
    elif cenario == 1:
        cenario = _selecao(tela)
    elif cenario == 2:
        print("Tutorial")
        executando = False
    elif cenario == 3:
        cenario = _batalhar_1(tela, aliados_selecionados)
        
pygame.quit()