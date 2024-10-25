import pygame, sys
import random

def reset_da_bola(contador):
    contador += 1
    bola.center = (screen_width/2, screen_height/2)
    velocidade_bola_x = -20
def contagem_vidas():
    quantidadeDeVidas = 3
    quantidadeDeVidas -= contador
    t = sys_font.render(f"{quantidadeDeVidas} Vida(s)", False, (255,255,255))
    x = 20
    y = 10
   
    screen.blit(t, t.get_rect(top = y, left=x))
pygame.init()
clock = pygame.time.Clock()

contador = 0
sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
bola = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10, 140)
cinza = (200, 200, 200)
velocidade_bola_x = -20
velocidade_bola_y = 7
velocidade_player = 0
quantidadeDeVidas = 3
velocidade1 = 5
velocidade2 = 10
velocidade3 = 20

while True:
    for event in pygame.event.get():
        if quantidadeDeVidas <= -1:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocidade_player -= 7
            if event.key == pygame.K_DOWN:
                velocidade_player += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidade_player += 7
            if event.key == pygame.K_DOWN:
               velocidade_player  -= 7
                

    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y
    player.y += velocidade_player

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    if bola.top <= 0 or bola.bottom >= screen_height:
        velocidade_bola_y *= -1
        if random.randint(0, 3) == 0:
            velocidade_bola_x = velocidade1
        if random.randint(0, 3) == 1:
            velocidade_bola_x = velocidade2
        if random.randint(0, 3) == 2:
            velocidade_bola_x = velocidade3
    if bola.left <= 0:
        velocidade_bola_x *= -1
        if random.randint(0, 3) == 0:
            velocidade_bola_x = velocidade1
        if random.randint(0, 3) == 1:
            velocidade_bola_x = velocidade2
        if random.randint(0, 3) == 2:
            velocidade_bola_x = velocidade3
        
    if bola.right >= screen_width:
        reset_da_bola(contador)
        contador += 1
        velocidade_bola_x = -20
        velocidade_bola_y += random.randint(0, 5)

    if bola.colliderect(player):
        velocidade_bola_x *= -1
        velocidade_bola_y += random.randint(0, 5)
    screen.fill('grey12')
    pygame.draw.rect(screen, cinza, player)
    pygame.draw.ellipse(screen, cinza, bola)
    pygame.draw.aaline(screen, cinza, (screen_width/2, 0),(screen_width/2, screen_height))
    quantidadeDeVidas = 3
    quantidadeDeVidas -= contador
    t = sys_font.render(f"{quantidadeDeVidas} Vida(s)", False, (255,255,255))
    x = 20
    y = 10
    screen.blit(t, t.get_rect(top = y, left=x))

    pygame.display.flip()
    clock.tick(60)
