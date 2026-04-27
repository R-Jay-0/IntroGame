import pygame
from Botao import Botao
from imagens import *
from var_universais import *
from Personagens import aliados

class Ficha:
    def __init__(self, display, personagem, img_fundo, img_escolhido, endereco, tela):
        self.personagem = personagem    # nome do personagem
        self.img_fundo = img_fundo  # imagem da ficha do peronagem
        self.img_escolhido = img_escolhido  # imagem da "fotinha" do personagem
        self.display = display  # tela na qual está ocorrendo o jogo
        self.selecionado = False    # booleano para identificar se o personagem foi ecolhido
        self.endereco = endereco    # endereço do botão indicado atualmente
        self.tela = tela    #   endereço da ficha do personagem (para comparar com a variável tela)

    # método para desenhar a tela baseada no índice dos botões
    def _mostrar_ficha(self, indice):
        self.display.fill((0, 0, 0))
        self.display.blit(self.img_fundo, (0, 0))
    
        if (indice != self.endereco) or self.selecionado:           
            self.display.blit(carimbo_abaixado, (705, 140))         # desenha o carimbo abaixado ou
        else:                                                       # flutuando dependendo do
            self.display.blit(carimbo_flutuando, (750, 120))        # indice / botão indicado

        # desenha o selo de aprovado caso selecionado = True
        if self.selecionado:
            self.display.blit(selo_aprovado, (220, 280))
    
    # o índice aqui é diferente do índice dos botões, é apenas para mostrar os escolhidos da forma correta
    def _mostrar_fotinha(self, indice):
        if indice == 0:
            self.display.blit(self.img_escolhido, (320, 250))
        else:
            self.display.blit(self.img_escolhido, (530, 250))

    # método para selecionar o personagem correspondente e rodar a animação do carimbo
    def _selecionar(self, indice):
        inicio = pygame.time.get_ticks()
        duracao = 800  # 0,8 segundos

        # executará enquanto a subtração entre a contagem de frames atuais 
        # com a contagem inicial for menor que a duração.
        while pygame.time.get_ticks() - inicio < duracao:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display.fill((0, 0 , 0)) 
            self.display.blit(self.img_fundo, (0, 0))
            self.display.blit(carimbo_abaixado, (160, 210))

            pygame.display.update()

        self.selecionado = True
        self._mostrar_ficha(indice)

# Retorna o objeto da classe Ficha ao qual foi selecionado em caso de não ter sido selecionado ainda
# além de usar a função de selecionar para rodar a animação de selecionar 
def _analisar_confirmacao(display, fichas, indice, tela):
    for ficha in fichas:
        if tela == ficha.tela:
            if not ficha.selecionado:
                ficha._selecionar(indice)
                return ficha

# Retorna o objeto da classe Ficha ao qual foi cancelada a seleção além de
# resetar a ficha correspondente
def _analisar_cancelamento(display, fichas, indice, tela):
    for ficha in fichas:
        if tela == ficha.tela:
            if ficha.selecionado:
                ficha.selecionado = False
                ficha._mostrar_ficha(indice)
                return ficha

# função para gerenciar a tela de seleção de personagens
def _selecao(display):
    display.fill((0, 0, 0)) # limpar a tela

    # Iniciar a tela de seleção com o personagem "Albert Camus"
    camus = Ficha(display, "Albert Camus", fundo_camus, fotinha_camus, 0, 0)
    camus._mostrar_ficha(0)

    # Gerando as fichas dos peronagens
    copernico = Ficha(display, "Nicolau Copérnico", fundo_copernico, fotinha_copernico, 0, 1)
    curie = Ficha(display, "Marie Curie", fundo_curie, fotinha_curie, 0, 2)
    seneca = Ficha(display, "Sêneca", fundo_seneca, fotinha_seneca, 0, 3)
    tesla = Ficha(display, "Nikola Tesla", fundo_tesla, fotinha_tesla, 0, 4)

    # criando o botão de return que leva para a tela anterior (menu)
    btn_return = Botao(display, "Return", (900, 620), img_return, 1)

    overlay = pygame.Surface(display.get_size(), pygame.SRCALPHA)   # Cria quadrado cobrindo toda a tela
    overlay.fill((0, 0, 0, 170)) # Deixa o quadrado preto e transparente

    # retângulo da imagem de verificação dos personagens selecionados
    rect_verificador = base_verificar_selecao.get_rect(center=(1024//2, 720//2))

    aliados_selecionados.append(aliados[5]) # Adiciona o protagonista na party automaticamente

    supostos_selecionados = []
    fichas = [camus, copernico, curie, seneca, tesla]   # lista com todas as fichas já criadas
    botoes = [btn_return]   # lista com os botões já criados
    tela = 0    # variável para identificar qual ficha deve ser exibida
    indice = 0  # vaiável para identificar se está no botão return ou no carimbo
    relogio = pygame.time.Clock()   # relógio para controlar os fps
    executando = True   # variável para continuar o loop enquanto estiver na tela de seleção
    # loop para lidar com eventos e atualizações na tela
    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            # impede as ações em caso de já ter selecionado os 2 personagens
            if len(aliados_selecionados) != 3:
                # verifica se o evento é uma tecla que foi clicada
                if event.type == pygame.KEYDOWN:
                    # estrutura circular para controlar a tela (qual personagem está sendo exibido)
                    if event.key == pygame.K_d:
                        if tela < 4:
                            tela += 1
                        else:
                            tela = 0
                    elif event.key == pygame.K_a:
                        if tela > 0:
                            tela -= 1
                        else:
                            tela = 4

                    # estrutura circular para controlar o índice dos botões (return ou carimbo indicado)
                    elif event.key == pygame.K_w:
                        if indice == 1:
                            indice = 0
                        else:
                            indice =1
                    elif event.key == pygame.K_s:
                        if indice == 1:
                            indice = 0
                        else:
                            indice = 1

                    # estrutura para tratar o input de confirmação do jogo
                    elif event.key == pygame.K_j:
                        # se estiver com índice correspondente ao endereço do carimbo
                        if indice == 0:
                            # identificar qual personagem foi selecionado e adicionar a lista de aliados_selecionados
                            selecionado = _analisar_confirmacao(display, fichas, indice, tela)
                            if selecionado != None:
                                for personagem in aliados:
                                    if selecionado.personagem == personagem.nome:
                                        aliados_selecionados.append(personagem)
                                        supostos_selecionados.append(selecionado)
                        # se o índice estiver no botão return então volta para a tela de menu
                        else:
                            aliados_selecionados.clear()
                            return 0

                    # estrutura para cancelar a seleção caso o persongaem já tenha sido selecionado
                    elif event.key == pygame.K_k:
                        # identificar qual personagem foi cancelado e retirar da lista de aliados_selecionados
                        cancelado = _analisar_cancelamento(display, fichas, indice, tela)
                        if cancelado != None:
                            aliados_selecionados.pop(1)
                            supostos_selecionados.pop(0)

                # desenha a ficha correspondente na tela de acordo com a variável tela
                for ficha in fichas:
                    if ficha.tela == tela:
                        ficha._mostrar_ficha(indice)
                        break
                # desenha os botões da lista de botões
                for botao in botoes:
                    if indice == botao.endereco:
                        botao._indicado()
                    else:
                        botao._nao_indicado()
                    botao._desenhar()

            # caso a quantidade mínima de personagens tenham sido alcançada:
            else:
                # desenha a ficha correspondente na tela de acordo com a variável tela
                for ficha in fichas:
                    if ficha.tela == tela:
                        ficha._mostrar_ficha(indice)
                        break
                # desenha os botões da lista de botões
                for botao in botoes:
                    if indice == botao.endereco:
                        botao._indicado()
                    else:
                        botao._nao_indicado()
                    botao._desenhar()

                # Desenha a verificação de seleção
                display.blit(overlay, (0, 0)) 
                display.blit(base_verificar_selecao, rect_verificador)
                # estrutura para desenhar a "fotinha" de cada personagem selecionado
                if supostos_selecionados != None:
                    for i in range(2):
                        supostos_selecionados[i]._mostrar_fotinha(i)

                # lidar com os eventos de clique dos botões do teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:     # ir para a tela de batalha caso confirmar o time
                        return 3
                    if event.key == pygame.K_k:     # re-selecionar os personagens
                        aliados_selecionados.clear()
                        return 1

        # Atualização 


        # Renderização
        pygame.display.update()
        relogio.tick(FPS)
    pygame.quit()
    return -1