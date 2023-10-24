import sys
import pygame
from Renderizador import Renderizador

class Terminal:
    def __init__(self) :
        pygame.init()

    def interacao_peenchimento(self):
        print("ALGORITMOS DE PREENCHIMENTO\n\n")
        print("qual algoritmo deseja utilizar ?\n")
        print("[0] Sair")
        print("[1] FloodFill com Circunferência")
        print("[2] FloodFill com Retângulo")
        print("[3] Varredura com Circunferência")
        print("[4] Varredura com Retângulo")
        self.escolha = int(input())
        print("\n")

        self.escala = int(input("Dgite o valor da escala (int) :"))

        # finaliza a execução do programa se a escolha for diferente das opções apresentadas
        if(self.escolha not in [1, 2, 3, 4]): sys.exit()

        if(self.escolha in [2, 4]):
            self.largura, self.altura = input("Digite a largura e a altura do retângulo : ").split(" ")
        else:
            self.raio = int(input("Digite o raio da circunferência : "))
    
    def configura_janela(self, nome: str, largura: int, altura: int):
        self.superficie = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(nome)
    
    def mantem_janela():
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
                pass