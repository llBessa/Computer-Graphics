import pygame
from graphics import keepWindowAlive, floodFill, parametrica, Ponto, varreduraRetangulo, varreduraCircunferencia, criaFiguraA

# inicia o pygame
pygame.init()

# cria uma janela com a resolução especificada
largura = 500
altura = 500
superficie = pygame.display.set_mode((largura, altura))

# cor vermelha
cor = (255, 0, 0)
corFundo = (0,0,0)

# ================ Testes de flood fill ==================

# para CIRCUNFERÊNCIA

# define o centro da circunferencia
raio = 20
centro = (250, 250)
pygame.draw.circle(superficie, cor, centro, raio, 1)
floodFill(250, 250, corFundo, cor, superficie)

# para RETANGULO

# pygame.draw.rect(superficie, cor, pygame.Rect(250, 250, 40, 40), 1)
# floodFill(260, 260, corFundo, cor, superficie)

# ================ Testes de varredura =====================

# para CIRCUNFERÊNCIA

# define o centro da circunferencia
# raio = 250
# centro = Ponto(250, 250)
# varreduraCircunferencia(centro, raio, cor, superficie)

# para RETANGULO

# varreduraRetangulo(Ponto(0, 0), 500, 500, cor, superficie)

# ============== Testes de Figuras ================
# escala = 1/5
# criaFiguraA(cor, superficie, 1)
# floodFill(60/5, 30/5, corFundo, cor, superficie)


pygame.display.flip()
pygame.display.set_caption("Algoritmos de peenchimento")
keepWindowAlive()