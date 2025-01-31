import pygame
pygame.init()

# Configurar a tela
screen = pygame.display.set_mode((800, 600))

# Carregar imagens
image1 = pygame.image.load('gfg-gg-logo.svg')
image2 = pygame.image.load('OIP.jpeg')

# Configurar a fonte e o texto
font = pygame.font.SysFont('Arial', 30)
text1 = font.render('Texto 1', True, (255, 255, 255))
text2 = font.render('Texto 2', True, (255, 255, 255))

# Configurar o relógio
clock = pygame.time.Clock()

# Variáveis de controle
current_image = image1
current_text = text1
change_time = 2000  # Tempo em milissegundos para mudar a imagem/texto
last_change = pygame.time.get_ticks()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar se é hora de mudar a imagem/texto
    current_time = pygame.time.get_ticks()
    if current_time - last_change > change_time:
        if current_image == image1:
            current_image = image2
            current_text = text2
        else:
            current_image = image1
            current_text = text1
        last_change = current_time

    # Limpar a tela
    screen.fill((0, 0, 0))

    # Desenhar a imagem e o texto
    screen.blit(current_image, (100, 100))
    screen.blit(current_text, (100, 300))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(60)

pygame.quit()
