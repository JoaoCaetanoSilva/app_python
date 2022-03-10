import pygame
from random import randint
pygame.init()

principal_x = 280
principal_y = 200

policia_x = 280
policia_y = 800

vermelho_x = 180
vermelho_y = 800

mesclado_x = 380
mesclado_y = 800

time = 0
time_segundo = 0

rodando = 0
pausado = 1

velocidade = 10
velocidade_policia = 14
velocidade_vermelho = 5
velocidade_misto = 8

fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carro.png')
carro2 = pygame.image.load('carro2.png')
carro3 = pygame.image.load('carro3.png')
policia = pygame.image.load('policia.png')

fonte = pygame.font.SysFont('arial black', 20)  # If 'True' printará a mensagem dentro de uma caixa de texto.
texto = fonte.render(' Tempo: ', True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
posicao = texto.get_rect()
posicao.center = (55, 25)

janela = pygame.display.set_mode((604, 500))
pygame.display.set_caption('Criando um jogo em python')

jogo = rodando

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50) # Delay para continuar aberto o game... Tambem indica a velocidade de jogo.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        comandos = pygame.key.get_pressed() #Se pressionado uma tecla fazer...

    if comandos[pygame.K_DOWN] and principal_y <= 410:
        principal_y += velocidade - 2
    if comandos[pygame.K_UP] and principal_y >= 30:
        principal_y -= velocidade
    if comandos[pygame.K_RIGHT] and principal_x <= 395:
        principal_x += velocidade
    if comandos[pygame.K_LEFT] and principal_x >= 171:
        principal_x -= velocidade
    if comandos[pygame.K_RETURN]:  # Tecla enter.
        if jogo != pausado:
            fonte = pygame.font.SysFont('arial black', 20)  # If 'True' printará a mensagem dentro de uma caixa de texto.
            texto = fonte.render(' pausado ', True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
            posicao = texto.get_rect()
            posicao.center = (300, 200)
            jogo = pausado
        else:
            jogo = rodando

    if jogo == pausado:
        pygame.display.flip()
        continue

    # Detecta colisao.
    if ((principal_x - 30 < vermelho_x and principal_y + 90 > vermelho_y)) and ((principal_y - 75 < vermelho_y)): # Colisao lado esquerdo.

        if jogo != pausado:
            fonte = pygame.font.SysFont('arial black', 20)  # If 'True' printará a mensagem dentro de uma caixa de texto.
            texto = fonte.render(' game over ', True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
            posicao = texto.get_rect()
            posicao.center = (300, 200)
            jogo = pausado
        else:
            jogo = rodando

        if jogo == pausado:
            pygame.display.flip()
            continue

    if ((principal_x + 30 > policia_x and principal_y + 90 > policia_y)) and ((principal_x - 30 < policia_x and principal_y + 90 > policia_y)) and ((principal_y - 75 < policia_y)): # Colisao no meio.

        if jogo != pausado:
            fonte = pygame.font.SysFont('arial black', 20)  # If 'True' printará a mensagem dentro de uma caixa de texto.
            texto = fonte.render(' game over ', True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
            posicao = texto.get_rect()
            posicao.center = (300, 200)
            jogo = pausado
        else:
            jogo = rodando

        if jogo == pausado:
            pygame.display.flip()
            continue

    if ((principal_x + 30 > mesclado_x and principal_y + 90 > mesclado_y)) and ((principal_y - 75 < mesclado_y)): # Colisao lado direito.

        if jogo != pausado:
            fonte = pygame.font.SysFont('arial black', 20)  # If 'True' printará a mensagem dentro de uma caixa de texto.
            texto = fonte.render(' game over ', True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
            posicao = texto.get_rect()
            posicao.center = (300, 200)
            jogo = pausado
        else:
            jogo = rodando

        if jogo == pausado:
            pygame.display.flip()
            continue

    if (policia_y <= -200):
        policia_y = randint(600, 1200)

    if (vermelho_y <= -200):
        vermelho_y = randint(600, 850)

    if (mesclado_y <= -200):
        mesclado_y = randint(600, 800)

    if time < 20:
        time += 1
    else:
        time_segundo += 1
        texto = fonte.render(' Tempo: ' + str(time_segundo), True, (255, 255, 255), (0, 0, 0))  # 255 cor da Letra. 0 cor do fundo.
        time = 0

    policia_y -= velocidade_policia
    vermelho_y -= velocidade_vermelho
    mesclado_y -= velocidade_misto

    # janela.fill((0, 0, 0)) #Mudar para a cor preta automatico quando se mover o objeto.
    # pygame.draw.circle(janela, (0, 255, 0), (x, y), 25) ::::: # Cor, posicao de inicio e tamanho do objeto.
    janela.blit(fundo, (0, 0))
    janela.blit(carro, (principal_x, principal_y))
    janela.blit(carro2, (vermelho_x, vermelho_y))
    janela.blit(carro3, (mesclado_x, mesclado_y))
    janela.blit(policia, (policia_x, policia_y))
    janela.blit(texto, posicao)

    pygame.display.update()

pygame.quit()