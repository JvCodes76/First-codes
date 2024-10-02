import pygame
pygame.init()

def fazer_triangulo(superficie, centroBase, altura):
    x, y = centroBase
    ponto1 = (x, y)
    ponto2 = (x - altura // 2, y + altura)
    ponto3 = (x + altura // 2, y + altura)

    pygame.draw.polygon(superficie, (0, 1, 1), [ponto1, ponto2, ponto3])

def fazer_nuvem(surface, x, y):
    pygame.draw.ellipse(surface, WHITE, [x, y, 100, 60])
    pygame.draw.ellipse(surface, WHITE, [x+20, y-30, 80, 60])
    pygame.draw.ellipse(surface, WHITE, [x+40, y-20, 100, 60])
    pygame.draw.ellipse(surface, WHITE, [x+60, y, 60, 40])

def fazer_folha(surface, x, y):
    pygame.draw.ellipse(surface, [50, 200, 50], [x, y, 100, 60])
    pygame.draw.ellipse(surface, [50, 200, 50], [x+20, y-30, 80, 60])
    pygame.draw.ellipse(surface, [50, 200, 50], [x+40, y-20, 100, 60])
    pygame.draw.ellipse(surface, [50, 200, 50], [x+60, y, 60, 40])
        
win_width = 600
win_height = 500
game_window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Movimento da nuvem')
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (50, 200, 50)
obj_width = 60
obj_height = 60
obj_x = -100
obj_y = 100
lua_x = 1000
sol_x = 30
obj_speed = 5
game_window.fill(BLUE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    obj_x+=obj_speed
    sol_x += 1
    lua_x -= 2
    clock.tick(60)
    pygame.draw.circle(game_window, [255, 255, 0], (sol_x, 100), 40)
    pygame.draw.circle(game_window, WHITE, (lua_x, 100), 40)
    fazer_nuvem(game_window, obj_x, obj_y)
    pygame.draw.rect(game_window, [200, 50, 50], [250, 300, 100, 100])
    pygame.draw.rect(game_window, [255, 255, 255], [265, 325, 25, 25])
    pygame.draw.rect(game_window, [255, 255, 255], [315, 325, 25, 25])
    pygame.draw.rect(game_window, [200, 150, 0], [295, 375, 15, 25])
    pygame.draw.rect(game_window, GREEN, [0, 400, 600, 100])
    fazer_triangulo(game_window, (300, 200), 100)
    pygame.draw.rect(game_window, [200, 150, 50], [435, 275, 40, 130])
    pygame.draw.rect(game_window, [200, 150, 50], [105, 275, 40, 130])
    fazer_folha(game_window, 70, 225)
    fazer_folha(game_window, 400, 225)
    
    pygame.display.flip()
    game_window.fill(BLUE)
    sol_x += 2

    if sol_x > 650:
        game_window.fill((100, 70, 220))
pygame.quit()
