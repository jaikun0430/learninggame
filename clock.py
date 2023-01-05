import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('My game','False','Black')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,235))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos == 0:
        snail_x_pos = 600
    screen.blit(snail_surface,(snail_x_pos,250))
    pygame.display.update()
    clock.tick(60)
