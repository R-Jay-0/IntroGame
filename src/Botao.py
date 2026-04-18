import pygame

class Botao:
    def __init__(self, tela, nome, posicao, img, endereco):
        self.nome = nome    # nome do botão
        self.posicao = posicao  # posição do botão
        self.tela = tela    # tela em que deve ser desenhada o botão
        self.endereco = endereco    # endereço do botão (para comparar com o índice)

        # cria cópias da imagem
        self.img_padrao = img.convert_alpha().copy()
        self.img_indicado = img.convert_alpha().copy()

        # aplica transparência separadamente
        self.img_padrao.set_alpha(100)
        self.img_indicado.set_alpha(255)

        self.img_atual = self.img_padrao

        self.rect = self.img_atual.get_rect(center=self.posicao)

    def _desenhar(self):
        self.tela.blit(self.img_atual, self.rect)

    def _nao_indicado(self):
        self.img_atual = self.img_padrao

    def _indicado(self):
        self.img_atual = self.img_indicado