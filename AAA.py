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



pygame.init()

tela = pygame.display.set_mode((800, 600))


# botão
img_jogar_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\jogar_padrao_resized.png")
img_jogar_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\jogar_indicado_resized.png")
btn_jogar = Botao(tela, "Jogar padrão", (400, 400),img_jogar_padrao, img_jogar_indicado, 0)


img_creditos_padrao = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\creditos_padrao_resized.png")
img_creditos_indicado = pygame.image.load(r"C:\Users\ruben\Documentos\IntroGame\Imagens\Botôes\creditos_indicado_resized.png")
btn_creditos = Botao(tela, "{variavel}", (400, 520), img_creditos_padrao, img_creditos_indicado, 1)

img_{variavel}_padrao = pygame.image.load(r"Caminho")
img_{variavel}_indicado = pygame.image.load(r"Caminho")
btn_{variavel} = Botao(tela, "{variavel}", (400, 520), img_{variavel}_padrao, img_{variavel}_indicado, endereço=int)


botoes = []
indice = 0
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                if indice < 1:
                    indice += 1
                else:
                    indice = 0
            if evento.key == pygame.K_s:
                if indice > 0:
                    indice -= 1
                else:
                    indice = 1

    # desenhar
        for botao in botoes:
            if indice == botao.endereco:
                botao._indicado()
            else:
                botao._nao_indicado()
            botao._desenhar()

    pygame.display.update()

pygame.quit()