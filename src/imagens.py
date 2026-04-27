import pygame
from var_universais import *

### Fundos principais ¬ ###
fundo_menu = pygame.image.load(r"Imagens\fundos\menu.png")
fundo_menu = pygame.transform.scale(fundo_menu, (LARGURA, ALTURA))

fundo_B1 = pygame.image.load(r"Imagens\fundos\batalhas\F_B1.png")
fundo_B1 = pygame.transform.scale(fundo_B1, (LARGURA, ALTURA))


### imagens personagens ¬ ###
# Protagonista #
fotinha_vincent = pygame.image.load(r"Imagens\personagens\Ronaldo\foto_vincent.png")
fotinha_vincent = pygame.transform.scale(fotinha_vincent, (175, 215))

prota_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Ronaldo\prota_CI_padrao.png")
prota_corpo_inteiro = pygame.transform.scale(prota_corpo_inteiro, (150, 230))

sprites_prota = [prota_corpo_inteiro, fotinha_vincent]

# Albert Camus #
fundo_camus = pygame.image.load(r"Imagens\fundos\Seleção\Camus_analisando.png")
fundo_camus = pygame.transform.scale(fundo_camus, (LARGURA, ALTURA))

fotinha_camus = pygame.image.load(r"Imagens\personagens\Camus\foto_camus.png")
fotinha_camus = pygame.transform.scale(fotinha_camus, (175, 215))

camus_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Camus\corpo_inteiro.png")
camus_corpo_inteiro = pygame.transform.scale(camus_corpo_inteiro, (160, 235))

sprites_camus = [camus_corpo_inteiro, fotinha_camus]

# Nikola Tesla #
fundo_tesla = pygame.image.load(r"Imagens\fundos\Seleção\Tesla_analisando.png")
fundo_tesla = pygame.transform.scale(fundo_tesla, (LARGURA, ALTURA))

fotinha_tesla = pygame.image.load(r"Imagens\personagens\Tesla\tesla_foto.png")
fotinha_tesla = pygame.transform.scale(fotinha_tesla, (175, 215))

tesla_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Tesla\corpo_inteiro.png")
tesla_corpo_inteiro = pygame.transform.scale(tesla_corpo_inteiro, (130, 225))

sprites_tesla = [tesla_corpo_inteiro, fotinha_tesla]

# Nicolau COpérnico #
fundo_copernico = pygame.image.load(r"Imagens\fundos\Seleção\Copérnico_analisando.png")
fundo_copernico = pygame.transform.scale(fundo_copernico, (LARGURA, ALTURA))

fotinha_copernico = pygame.image.load(r"Imagens\personagens\Copérnico\copernico_foto.png")
fotinha_copernico = pygame.transform.scale(fotinha_copernico, (175, 215))

copernico_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Copérnico\corpo_inteiro.png")
copernico_corpo_inteiro = pygame.transform.scale(copernico_corpo_inteiro, (160, 240))

sprites_copernico = [copernico_corpo_inteiro, fotinha_copernico]

# Marie Curie #
fundo_curie = pygame.image.load(r"Imagens\fundos\Seleção\Curie_analisando.png")
fundo_curie = pygame.transform.scale(fundo_curie, (LARGURA, ALTURA))

fotinha_curie = pygame.image.load(r"Imagens\personagens\Curie\foto_curie.png")
fotinha_curie = pygame.transform.scale(fotinha_curie, (175, 215))

curie_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Curie\corpo_inteiro.png")
curie_corpo_inteiro = pygame.transform.scale(curie_corpo_inteiro, (145, 220))

sprites_curie = [curie_corpo_inteiro, fotinha_curie]

# Sêneca #
fundo_seneca = pygame.image.load(r"Imagens\fundos\Seleção\Sêneca_analisando.png")
fundo_seneca = pygame.transform.scale(fundo_seneca, (LARGURA, ALTURA))

fotinha_seneca = pygame.image.load(r"Imagens\personagens\Sêneca\seneca_foto.png")
fotinha_seneca = pygame.transform.scale(fotinha_seneca, (175, 215))

seneca_corpo_inteiro = pygame.image.load(r"Imagens\personagens\Sêneca\corpo_inteiro.png")
seneca_corpo_inteiro = pygame.transform.scale(seneca_corpo_inteiro, (185, 250))

sprites_seneca = [seneca_corpo_inteiro, fotinha_seneca]

### Botões ¬ ###
img_jogar = pygame.image.load(r"imagens\Botôes\jogar.png")

img_tutorial = pygame.image.load(r"Imagens\Botôes\Tutorial.png")
img_tutorial = pygame.transform.scale(img_tutorial, (233, 50))

img_sair = pygame.image.load(r"Imagens\Botôes\sair.png")

img_return = pygame.image.load(r"Imagens\Botôes\return.png")
img_return = pygame.transform.scale(img_return, (150, 32))

img_atacar = pygame.image.load(r"Imagens\Botôes\atacar.png")
img_atacar = pygame.transform.scale(img_atacar, (160, 40))

img_defender = pygame.image.load(r"Imagens\Botôes\defender.png")
img_defender = pygame.transform.scale(img_defender, (160, 40))

img_vazio = pygame.image.load(r"Imagens\Botôes\btn_vazio.png")
img_vazio = pygame.transform.scale(img_vazio, (160, 40))

### elementos gráficos ¬ ###
fundo_status_aliados = pygame.image.load(r"Imagens\Elementos_graficos\fundo_status_aliado.png")
fundo_status_aliados = pygame.transform.scale(fundo_status_aliados, (200, 95))

fundo_status_inimigos = pygame.image.load(r"Imagens\Elementos_graficos\fundo_status_inimigos.png")
fundo_status_inimigos = pygame.transform.scale(fundo_status_inimigos, (200, 95))

carimbo_abaixado =  pygame.image.load(r"Imagens\Elementos_graficos\carimbo_abaixado.png")
carimbo_abaixado = pygame.transform.scale(carimbo_abaixado, (230, 200))

carimbo_flutuando = pygame.image.load(r"Imagens\Elementos_graficos\Carimbo_flutuando.png")
carimbo_flutuando = pygame.transform.scale(carimbo_flutuando, (240, 160))

selo_aprovado = pygame.image.load(r"Imagens\Elementos_graficos\Selo_aproved.png")
selo_aprovado = pygame.transform.scale(selo_aprovado, (120, 65))

base_verificar_selecao = pygame.image.load(r"Imagens\Elementos_graficos\base_verificar_selecao.png")
base_verificar_selecao = pygame.transform.scale(base_verificar_selecao, (500, 500))