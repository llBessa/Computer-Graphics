import sys
import pygame
import os
from Ponto import Ponto
from Renderizador import Renderizador
from Terminal import Terminal

def interacao_escolha_algoritmo():
    print("RASTERIZAÇÃO DE LINHAS\n\n")
    print("qual algoritmo deseja utilizar ?\n")
    print("[0] Sair\n[1] Analitico\n[2] DDA\n[3] Bresenham\n")
    escolha = int(input())
    print("\n")

    if(escolha not in [1, 2, 3]): sys.exit()

    while True:
        try:
            # input de valores
            x, y = input("Digite as coordenada do ponto 1 : ").split(" ")
            ponto1 = Ponto(x, y)
            x, y = input("Digite as coordenadas do ponto 2 : ").split(" ")
            ponto2 = Ponto(x, y)

            return (escolha, ponto1, ponto2)
        except:
            print("ocorreu um erro ao escolher as coordenadas")

# cor vermelha para os pixels
cor = (255, 0, 0)

# escala utilizada para os pixels
escala = 10

terminal = Terminal()

# inicia o pygame
pygame.init()
pygame.display.set_caption("Rasterização de linhas")

while True:  
    escolha, ponto1, ponto2 = interacao_escolha_algoritmo()

    try:
        # cria uma janela com a resolução especificada
        superficie = pygame.display.set_mode((500, 500))
        renderizador = Renderizador(superficie, cor, escala)

        algoritmos = [renderizador.analitico, renderizador.dda2, renderizador.linhaBresenham]
        executar = algoritmos[escolha - 1]

        executar(ponto1, ponto2)
        pygame.display.flip()
        terminal.mantem_janela()
    except:
        os.system("cls")
        print("ocorreu um erro ao executar algoritmo")

