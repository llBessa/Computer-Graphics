import pygame
from graphics import analitico, keepWindowAlive, linhaBresenham, dda2, Ponto

print("RASTERIZAÇÃO DE LINHAS\n\n")
print("qual algoritmo deseja utilizar ?\n")
print("[1] Analitico\n[2] DDA\n[3] Bresenham\n")
escolha = int(input())
print("\n")

# input de valores
x, y = input("Digite as coordenada do ponto 1 : ").split(" ")
ponto1 = Ponto(x, y)
x, y = input("Digite as coordenadas do ponto 2 : ").split(" ")
ponto2 = Ponto(x, y)

# cor vermelha para os pixels
cor = (255, 0, 0)

# inicia o pygame
pygame.init()

# cria uma janela com a resolução especificada
superficie = pygame.display.set_mode((500, 500))

algoritmos = [analitico, dda2, linhaBresenham]
executar = algoritmos[escolha - 1]
executar(ponto1, ponto2, cor, superficie)

pygame.display.set_caption("Rasterização de linhas")
pygame.display.flip()
keepWindowAlive()