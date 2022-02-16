import pygame
pygame.init()
x = 400
y = 300
velocidade = 10

fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carro.png')
janela = pygame.display.set_mode((605, 500))
pygame.display.set_caption('Criando um jogo em python')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        comandos = pygame.key.get_pressed() #Se pressionado uma tecla fazer...

    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade

    # janela.fill((0, 0, 0)) #Mudar para a cor preta automatico quando se mover o objeto.
    janela.blit(fundo, (0, 0))
    pygame.draw.circle(janela, (0, 255, 0), (x, y), 50) # Cor, posicao de inicio e tamanho do objeto.
    pygame.display.update()

pygame.quit()