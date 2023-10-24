import pygame
from Renderizador import Renderizador
from Ponto import Ponto
from Terminal import Terminal

print("RASTERIZAÇÃO DE LINHAS\n\n")
print("qual algoritmo deseja utilizar ?\n")
print("[1] parametrico\n[2] Bresenham\n")
escolha = int(input())
print("\n")

raio = int(input("Digite o raio da circunferencia : "))

# inicia o pygame
pygame.init()

# cria uma janela com a resolução especificada
largura = 500
altura = 500
superficie = pygame.display.set_mode((largura, altura))

escala = 1

posicaoX = 250/escala
posicaoY = 250/escala
centro = Ponto(posicaoX, posicaoY)

# cor vermelha
cor = (255, 0, 0)

renderizador = Renderizador(superficie, cor, escala)

algoritmos = [renderizador.parametrica, renderizador.circunferenciaBresenham]
executar = algoritmos[escolha - 1]
executar(raio, centro, cor, superficie, escala)

pygame.display.set_caption("Rasterização de circunferencias")

# renderiza a imagem
pygame.display.flip()
Terminal.mantem_janela()