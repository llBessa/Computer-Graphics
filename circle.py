import pygame
from graphics import keepWindowAlive

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.draw.circle(tela, (255, 0, 0), (500, 500), 30)

pygame.display.flip()
keepWindowAlive()