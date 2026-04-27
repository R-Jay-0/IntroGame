import pygame
from Botao import Botao
from imagens import *
from var_universais import *

# função para gerenciar a tela de menu
def _menu(display):
    display.fill((0, 0, 0))

    # Fundo
    display.blit(fundo_menu, (0, 0)) # por a imagem de fundo do menu

    # botões
    btn_jogar = Botao(display, "Jogar padrão", ((1024//4) - 30, 410), img_jogar, 0) # criando e posicionando o botão de jogar
    
    btn_tutorial = Botao(display,"Voltar Seta", ((1024//4) - 30, 480), img_tutorial, 1) # criando e posicionando o botão de tutorial

    btn_sair = Botao(display, "Sair", ((1024//4) - 30, 550), img_sair, 2)   # criando e posicionando o botão de sair

    botoes = [btn_jogar, btn_tutorial, btn_sair]    # lista com botões criaddos anteriormente
    indice = 0      # índice para identificar qualbotão está sendo indicado
    relogio = pygame.time.Clock()
    executando = True
    # loop para tratar os inputs e atualizações da tela
    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            # tratar dos eventos de clique do teclado
            if event.type == pygame.KEYDOWN:
                # levar para a tela correspondente ao botão indicado
                if event.key == pygame.K_j:
                    if indice == 1:
                        return 2
                    elif indice == 0:
                        return 1
                    else:
                        return -1
                # estrutura circular para controlar qual botão está sendo indicado
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

            # não faço ideia do porque os botões só funcionam direito com essa ilha de código 
            display.fill((0, 0, 0))
            display.blit(fundo_menu, (0, 0))

            for botao in botoes:
                if indice == botao.endereco:
                    botao._indicado()
                else:
                    botao._nao_indicado()
                botao._desenhar()

        # Atualização 

        # Renderização
        pygame.display.update()
        relogio.tick(FPS)
    pygame.quit()
    return -1