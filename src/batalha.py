import pygame
from Botao import Botao
from var_universais import *
from imagens import *

class Batalha:
    def __init__(self, display, aliados_lista, inimigos_lista):
        self.aliados_inico = aliados_lista
        self.aliados_vivos = aliados_lista
        self.inimigos_inico = inimigos_lista
        self.inimigos_vivos = inimigos_lista
        self.display = display

        self.alvo_ataque = None
        self.habilidade_escolhida = None
        self.personagens_alvos = []

        self.ordem_turnos = aliados_lista + inimigos_lista
        self.ordem_turnos.sort(key=lambda obj: obj.velocidade, reverse=True)

        self.tela = 0

        self.indice = 0
        self.max_indice = None
        self.min_indice = None
        self.horizontal_variacao = None
        self.vertical_variacao = None

        # rodadas e turnos #
        self.turno_atual_personagem = self.ordem_turnos[0]
        self.turno_atual_indice = 0

        self.rodada = 0

        # botões #
        self.btn_atacar = Botao(self.display, "botão atacar", ((LARGURA - LARGURA//5) - 120, (ALTURA - ALTURA//6 + 18)), 
            img_atacar, 0
        )
        self.btn_defender = Botao(self.display, "botão defender", ((LARGURA - LARGURA//5) + 80, (ALTURA - ALTURA//6 + 18)), 
            img_defender, 1
        )

        self.btn_vazio_0 = Botao(self.display, "Botão vazio 0", ((LARGURA - LARGURA//5) - 120, (ALTURA - ALTURA//6 - 20)), 
            img_vazio, 2
        )
        self.btn_vazio_1 = Botao(self.display, "Botão vazio 1", ((LARGURA - LARGURA//5) + 80, (ALTURA - ALTURA//6 - 20)), 
            img_vazio, 3
        )
        self.btn_vazio_2 = Botao(self.display, "Botão vazio 2", ((LARGURA - LARGURA//5) - 120, (ALTURA - ALTURA//6 + 60)), 
            img_vazio, 4
        )
        self.btn_vazio_3 = Botao(self.display, "Botão vazio 3", ((LARGURA - LARGURA//5) + 80, (ALTURA - ALTURA//6 + 60)), 
            img_vazio, 5
        )

        self.botoes = [self.btn_atacar, self.btn_defender]
        
    def _posicionar_aliados(self, aliados, inimigos):
        count = 0
        fonte_status = pygame.font.Font(r"fontes\PressStart2P-Regular.ttf", 8)
        for aliado in aliados:
            vida = "vida:" + str(aliado.vida_atual) + "/" + str(aliado.vida_max)
            energia = "enrg.:" + str(aliado.energia_atual) + "/" + str(aliado.energia_max)
            if count == 0:
                # status #
                self.display.blit(fundo_status_aliados, (30, 30))
                self.display.blit(aliado.fotinha, (42, 43)) # foto #

                vida_aliado_1 = fonte_status.render(vida, True, BRANCO)
                self.display.blit(vida_aliado_1, (103, 45))

                energia_aliado_1 = fonte_status.render(energia, True, BRANCO)
                self.display.blit(energia_aliado_1, (103, 60))
                
                #boneco #
                self.display.blit(aliado.corpo_inteiro, (140, 180))
            elif count == 1:
                # status #
                self.display.blit(fundo_status_aliados, (230, 30))
                self.display.blit(aliado.fotinha, (242, 43)) # foto #

                vida_aliado_2 = fonte_status.render(vida, True, BRANCO)
                self.display.blit(vida_aliado_2, (303, 45))
                energia_aliado_2 = fonte_status.render(energia, True, BRANCO)
                self.display.blit(energia_aliado_2, (303, 60))
                
                # boneco #
                self.display.blit(aliado.corpo_inteiro, (240, 220))
            else:
                # status #
                self.display.blit(fundo_status_aliados, (30, 130))
                self.display.blit(aliado.fotinha, (42, 143)) # foto #

                vida_aliado_2 = fonte_status.render(vida, True, BRANCO)
                self.display.blit(vida_aliado_2, (103, 145))
                energia_aliado_2 = fonte_status.render(energia, True, BRANCO)
                self.display.blit(energia_aliado_2, (103, 160))

                # boneco #
                self.display.blit(aliado.corpo_inteiro, (40, 260))
            count += 1

    def _definir_turno_atual(self):
        fonte_turno_rodada = pygame.font.Font(r"fontes\PressStart2P-Regular.ttf", 13)
        if self.tela == 0:
            turno_txt = "Turno de: " + str(self.turno_atual_personagem.nome)
            turno_txt = fonte_turno_rodada.render(turno_txt, True, BRANCO)
            self.display.blit(turno_txt, (30, (ALTURA - ALTURA//6 - 20)))

        rodada_txt = "Rodada atual: " + str(self.rodada)
        rodada_txt = fonte_turno_rodada.render(rodada_txt, True, BRANCO)
        self.display.blit(rodada_txt, (30, (ALTURA - ALTURA//6 + 70)))

        if self.turno_atual_personagem.fim_turno:
            self.turno_atual_personagem.fim_turno = False
            self.turno_atual_indice += 1
            if self.turno_atual_indice >= len(self.ordem_turnos):
                self.rodada += 1
                self.turno_atual_indice = 0
                for personagem in self.ordem_turnos:
                    print(personagem.nome, personagem.defendendo)
                    personagem.defendendo = False
                    print(personagem.nome, personagem.defendendo)
            self.turno_atual_personagem = self.ordem_turnos[self.turno_atual_indice]

    def _mudar_tela(self):
        if self.tela == 0:
            self.indice = 0
            self.max_indice = 1
            self.min_indice = 0
            self.horizontal_variacao = 1
            self.botoes = [self.btn_atacar, self.btn_defender]
        elif self.tela == 1:
            self.indice = 2
            self.max_indice = 5
            self.min_indice = 2
            self.vertical_variacao = 2
            self.botoes = [self.btn_vazio_0, self.btn_vazio_1, self.btn_vazio_2, self.btn_vazio_3]

        else:
            self.min_indice = 6 
            self.max_indice = self.min_indice + len(self.personagens_alvos)
            self.vertical_variacao = 1
            self.indice = self.min_indice
            self.botoes = [self.btn_vazio_0, self.btn_vazio_1, self.btn_vazio_2, self.btn_vazio_3]
        
    def _escrever_tela_habilidades(self):
        fonte_descricao = pygame.font.Font(r"fontes\PressStart2P-Regular.ttf", 12)
        index = 0
        
        idx = self.indice - 2

        if 0 <= idx < len(self.turno_atual_personagem.habilidades):
            descricao_habilidade = self.turno_atual_personagem.habilidades[idx].descricao
            count = 0
            for linha in descricao_habilidade:
                linha = fonte_descricao.render(linha, True, BRANCO)
                self.display.blit(linha, (30, ALTURA - ALTURA//6 - 30 + count))
                count += 30

        for habilidade in self.turno_atual_personagem.habilidades:
            nome_habilidade = habilidade.nome
            nome_habilidade = fonte_descricao.render(nome_habilidade, True, PRETO)

            if index == 0:
                self.display.blit(nome_habilidade, ((LARGURA - LARGURA//5) - 170, (ALTURA - ALTURA//6 - 23)))
                
            if index == 1:
                self.display.blit(nome_habilidade, ((LARGURA - LARGURA//5) + 60, (ALTURA - ALTURA//6 - 23)))

            if index == 2:
                self.display.blit(nome_habilidade, ((LARGURA - LARGURA//5) - 170, (ALTURA - ALTURA//6 + 55)))

            if index == 3:
                self.display.blit(nome_habilidade, ((LARGURA - LARGURA//5) + 60, (ALTURA - ALTURA//6 + 55)))
            
            index += 1


    def _batalhar(self):
        self.indice = 0
        self.max_indice = 1
        self.min_indice = 0
        self.horizontal_variacao = 1
        self.vertical_variacao = 1
        relogio = pygame.time.Clock()
        executando = True
        while executando:
            # Entrada / Inputs / Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    executando = False

                elif event.type == pygame.KEYDOWN:
                    # navegação entre os botões #
                    if event.key == pygame.K_d:
                        self.indice += self.horizontal_variacao
                        if self.indice > self.max_indice:
                            self.indice = self.min_indice

                    elif event.key == pygame.K_a:
                        self.indice -= self.horizontal_variacao
                        if self.indice < self.min_indice:
                            self.indice = self.max_indice

                    elif event.key == pygame.K_s:
                        if self.tela == 1:
                            self.indice += self.vertical_variacao
                            if self.indice > self.max_indice:
                                self.indice = self.min_indice

                    elif event.key == pygame.K_w:
                        if self.tela == 1:
                            self.indice -= self.vertical_variacao
                            if self.indice < self.min_indice:
                                self.indice = self.max_indice


                    # confirmação e return #
                    if event.key == pygame.K_j:
                        if self.tela == 0:
                            if self.indice == 0:
                                self.tela = 1
                                self._mudar_tela()
                            else:
                                self.turno_atual_personagem._defender()
                                self.turno_atual_personagem._finalizar_turno()
                        elif self.tela == 1:
                            self.tela = 2
                            self._mudar_tela()
                           
                            idx = self.indice - 2
                            if 0 <= idx < len(self.turno_atual_personagem.habilidades):
                                self.habilidade_escolhida = self.turno_atual_personagem.habilidades[idx]
                            
                            if self.habilidade_escolhida.tipo == "ataque":
                                self.personagens_alvos = self.inimigos_vivos.copy()

                            elif self.habilidade_escolhida.tipo == "buff_aliado":
                                aliados = self.aliados_vivos.copy()
                                if self.turno_atual_personagem in aliados:
                                    aliados.remove(self.turno_atual_personagem)
                                self.personagens_alvos = aliados

                            else:
                                self.personagens_alvos = [self.turno_atual_personagem]

                        else:
                            if 0 <= (self.indice - 2) < len(self.personagens_alvos):
                                self.alvo_ataque = self.personagens_alvos[self.indice - 2]


                    if event.key == pygame.K_k:
                        if self.tela == 1:
                            self.tela = 0
                            self._mudar_tela()
                        if self.tela == 2:
                            self.tela = 1
                            self._mudar_tela()


                self.display.fill((0, 0, 0))
                self.display.blit(fundo_B1, (0, 0))

                if self.turno_atual_personagem in self.aliados_vivos:
                    for botao in self.botoes:
                        botao._indicado() if self.indice == botao.endereco else botao._nao_indicado()
                        botao._desenhar()
                if self.tela != 0:
                    self._escrever_tela_habilidades()

                self._posicionar_aliados(self.aliados_vivos, self.inimigos_vivos)

            # Atualização

            self._definir_turno_atual()

            # Renderização
            pygame.display.update()
            relogio.tick(FPS)
                


def _batalhar_1(display, lista_aliados):
    display.fill((0, 0, 0))
    display.blit(fundo_B1, (0, 0))

    batalha_1 = Batalha(display, lista_aliados, [])

    batalha_1._batalhar()

    pygame.quit()
    return -1
