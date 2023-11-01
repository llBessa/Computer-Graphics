import sys
import os
import pygame
from Ponto import Ponto
from Renderizador import Renderizador

class Terminal:
    def __init__(self):
        pygame.init()
        self.cor = (255, 0, 0) # vermelho
        self.corFundo = (0, 0, 0) # preto

    def interacao_peenchimento(self):
        while True:
            os.system("cls") # Limpa a Tela

            # Apresenta as opções
            print("ALGORITMOS DE PREENCHIMENTO\n\n")
            print("qual algoritmo deseja utilizar ?\n")
            print("[0] Sair")
            print("[1] FloodFill com Circunferência")
            print("[2] FloodFill com Retângulo")
            print("[3] Varredura com Circunferência")
            print("[4] Varredura com Retângulo")
            print("\n")

            escolha = int(input())

            self.executa_algoritmo_preenchimento(escolha)
            pygame.display.flip()
            self.mantem_janela()
    
    def configura_janela(self, nome: str, largura: int, altura: int):
        self.superficie = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(nome)
    
    def mantem_janela(self):
        running = True
        while running:
            # itera na fila de eventos
            for event in pygame.event.get():
                # se o evento de quit for identificado a condição de parada é setada
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
    
    def executa_algoritmo_preenchimento(self, escolha: int):
        match escolha:
            case 1:
                # inputs do algortimo
                escala = int(input("Digite o valor da escala : "))
                raio = int(input("Digite o raio da circunferência : "))
                x, y = input("Digite as coordenadas da semente do floodfill : ").split(" ")

                x = int(x)
                y = int(y)

                centro = Ponto(0, 0)

                self.configura_janela("FloodFill com Circunferência", 500, 500)
                renderizador = Renderizador(self.superficie, self.cor, escala)
                renderizador.circunferenciaBresenham(raio, centro)
                renderizador.floodFill(x, y, self.corFundo)
            
            case 2:
                escala = int(input("Dgite o valor da escala : "))
                inicio_x, inicio_y = input("Digite as coordenadas do inicio do retângulo : ").split(" ")
                largura, altura = input("Digite a largura e a altura do retângulo : ").split(" ")
                x, y = input("Digite as coordenadas da semente do floodfill : ").split(" ")

                inicio = Ponto(int(inicio_x), int(inicio_y))
                x = int(x)
                y = int(y)

                largura = int(largura)
                altura = int(altura)

                self.configura_janela("FloodFill com Retângulo", 500, 500)
                renderizador = Renderizador(self.superficie, self.cor, escala)

                # cria o retângulo
                renderizador.linhaBresenham(inicio, Ponto(inicio.x + largura, inicio.y))
                renderizador.linhaBresenham(Ponto(inicio.x + largura, inicio.y), Ponto(inicio.x + largura, inicio.y + altura))
                renderizador.linhaBresenham(inicio, Ponto(inicio.x, inicio.y + altura))
                renderizador.linhaBresenham(Ponto(inicio.x, inicio.y + altura), Ponto(inicio.x + largura, inicio.y + altura))

                renderizador.floodFill(x, y, self.corFundo)
            
            case 3:
                # inputs do algortimo
                escala = int(input("Digite o valor da escala : "))
                raio = int(input("Digite o raio da circunferência : "))

                centro = Ponto(0, 0)

                self.configura_janela("Varredura em Circunferência", 500, 500)
                renderizador = Renderizador(self.superficie, self.cor, escala)
                renderizador.varreduraCircunferencia(centro, raio)

            case 4:
                escala = int(input("Dgite o valor da escala : "))
                inicio_x, inicio_y = input("Digite as coordenadas do inicio do retângulo : ").split(" ")
                largura, altura = input("Digite a largura e a altura do retângulo : ").split(" ")

                inicio = Ponto(int(inicio_x), int(inicio_y))

                largura = int(largura)
                altura = int(altura)

                self.configura_janela("Varredura em Retângulo", 500, 500)
                renderizador = Renderizador(self.superficie, self.cor, escala)
                renderizador.varreduraRetangulo(inicio, largura, altura)
            case _:
                sys.exit()
                