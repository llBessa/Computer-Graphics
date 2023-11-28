import pygame
from Renderizador import Renderizador
from Ponto import Ponto
from Terminal import Terminal
while True:
    print("RASTERIZAÇÃO DE LINHAS\n\n")
    print("qual algoritmo deseja utilizar ?\n")
    print("[0] Sair\n[1] parametrico\n[2] Bresenham\n[3] Incremental\n")
    escolha = int(input())
    print("\n")

    if(escolha not in [1, 2, 3]): break
    escala = int(input("Digite o valor da escala : "))
    raio = int(input("Digite o raio da circunferencia : "))

    # inicia o pygame
    pygame.init()

    terminal = Terminal()

    # cria uma janela com a resolução especificada
    largura = 500
    altura = 500
    superficie = pygame.display.set_mode((largura, altura))

    centro = Ponto(0, 0)

    # cor vermelha
    cor = (255, 0, 0)

    renderizador = Renderizador(superficie, cor, escala)

    algoritmos = [renderizador.parametrica, renderizador.circunferenciaBresenham, renderizador.incremental]
    executar = algoritmos[escolha - 1]
    executar(raio, centro)

    pygame.display.set_caption("Rasterização de circunferencias")

    # renderiza a imagem
    pygame.display.flip()
    terminal.mantem_janela()