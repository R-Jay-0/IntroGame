import pygame

class Botao:
    def __init__(self, tela, nome, posicao, imagem_padrao, imagem_indicado, endereco):
        self.nome = nome
        self.posicao = posicao
        self.imagem_padrao = imagem_padrao
        self.imagem_indicado = imagem_indicado
        self.imagem_atual = imagem_padrao
        self.endereco = endereco
        self.tela = tela

        self.rect = self.imagem_atual.get_rect(center=self.posicao)

    def _desenhar(self):
        self.tela.blit(self.imagem_atual, self.rect)

    def _nao_indicado(self):
        self.imagem_atual = self.imagem_padrao

    def _indicado(self):
        self.imagem_atual = self.imagem_indicado

def _creditos(display):
    display.fill((0, 0, 0))

    # Fundo
    imagem_fundo = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\fundo_creditos.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1024, 720))
 
    relogio = pygame.time.Clock()
    indice = 0
    executando = True
    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    _menu(display)

        # Atualização
            display.blit(imagem_fundo, (0, 0))

        # Renderização
        pygame.display.update()

        relogio.tick(60)

    pygame.quit()

def _menu(display):
    display.fill((0, 0, 0))

    # Fundo
    imagem_menu = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\fundo_menu.png")
    imagem_menu = pygame.transform.scale(imagem_menu, (1024, 720))

    # botões
    img_jogar_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\jogar_padrao_resized.png")
    img_jogar_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\jogar_indicado_resized.png")
    btn_jogar = Botao(display, "Jogar padrão", (1024/2, 300),img_jogar_padrao, img_jogar_indicado, 0)

    img_creditos_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\creditos_padrao_resized.png")
    img_creditos_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\creditos_indicado_resized.png")
    btn_creditos = Botao(display, "Créditos", (1024/2, 450), img_creditos_padrao, img_creditos_indicado, 1)

    img_sair_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\sair_padrao.png")
    img_sair_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\sair_indicado.png")
    btn_sair = Botao(display, "Sair", (1024/2, 600), img_sair_padrao, img_sair_indicado, 2)

    botoes = [btn_jogar, btn_creditos, btn_sair]
    indice = 0
    relogio = pygame.time.Clock()
    executando = True

    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    executando = False
                    if indice == 1:
                        _creditos(display)
                    elif indice == 0:
                        _pre_selecao(display)
                if event.key == pygame.K_w:
                    if indice == 0:
                        indice = 2
                    else:
                        indice -= 1
                if event.key == pygame.K_s:
                    if indice == 2:
                        indice = 0
                    else:
                        indice += 1

        # Atualização
            display.blit(imagem_menu, (0, 0))
            for botao in botoes:
                if indice == botao.endereco:
                    botao._indicado()
                else:
                    botao._nao_indicado()
                botao._desenhar()


        # Renderização
        pygame.display.update()
        relogio.tick(60)
    pygame.quit()

def _pre_selecao(display):
    display.fill((0, 0, 0))

    # Fundo
    imagem_fundo = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\fundo_pre_select.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1024, 720))

    # botões
    img_tutorial_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\Tutorial_padrao.png")
    img_tutorial_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\Tutorial_indicado.png")
    btn_tutorial = Botao(display, "Jogar", (1024/4, 720/2),img_tutorial_padrao, img_tutorial_indicado, 0)

    img_iniciar_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\Iniciar_padrao.png")
    img_iniciar_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\Iniciar_indicado.png")
    btn_iniciar = Botao(display, "Iniciar", (3*1024/4, 720/2), img_iniciar_padrao, img_iniciar_indicado, 1)

    botoes = [btn_tutorial, btn_iniciar]
    indice = 0
    relogio = pygame.time.Clock()
    executando = True
    while executando:
        # Entrada / Inputs / Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if indice == 1:
                        print("Está jogando")
                    else:
                        print("Está no Tutorial")
                elif event.key == pygame.K_a:
                    if indice > 0:
                        indice = 0
                    else:
                        indice = 1
                elif event.key == pygame.K_d:
                    if indice == 1:
                        indice = 0
                    else:
                        indice = 1
                elif event.key == pygame.K_k:
                    executando = False
                    _menu(display)

        # Atualização
            display.blit(imagem_fundo, (0, 0))
            for botao in botoes:
                if indice == botao.endereco:
                    botao._indicado()
                else:
                    botao._nao_indicado()
                botao._desenhar()

        # Renderização
        pygame.display.update()

        relogio.tick(60)

    pygame.quit()


########## COMEÇO PROGRAMA #############

pygame.init()

tela = pygame.display.set_mode((1024, 720))

pygame.display.set_caption("Nome do joojj")

_menu(tela)