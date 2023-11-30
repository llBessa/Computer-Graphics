import pygame, math
from Ponto import Ponto
import numpy as np

# algoritmos de rasterização de linhas

class Renderizador:
    def __init__(self, superficie, cor, escala):
        self.superficie = superficie
        self.cor = cor
        self.escala = escala
        self.largura_tela = superficie.get_width()
        self.altura_tela = superficie.get_height()
        self.pontos_controle = []
    
    def pinta_pixel(self, x, y):
        y = self.altura_tela/2 - (y + 1) * self.escala
        x = x * self.escala + self.largura_tela/2

        pygame.draw.rect(self.superficie, self.cor, pygame.Rect(x, y , self.escala, self.escala), 1)
    
    def pega_pixel(self, x, y):
        y = self.altura_tela/2 - (y + 1) * self.escala
        x = x * self.escala + self.largura_tela/2

        return self.superficie.get_at((int(x), int(y)))
    
    def limpa_tela(self):
        pygame.draw.rect(self.superficie, (0, 0, 0), pygame.Rect(0, 0 , self.largura_tela, self.altura_tela), 0)


    def analitico(self, ponto1 : Ponto, ponto2 : Ponto):
        # swap das variaveis caso x1 > x2 e/ou y1 > y2
        if(ponto1.x > ponto2.x): ponto1.x , ponto2.x = ponto2.x, ponto1.x
        if(ponto1.y > ponto2.y): ponto1.y , ponto2.y = ponto2.y, ponto1.y
        
        if(ponto1.x == ponto2.x):
            for y in range(ponto1.y, ponto2.y + 1):
                self.pinta_pixel(ponto1.x, y)
        else:
            m = (ponto2.y - ponto1.y)/(ponto2.x - ponto1.x)
            b = ponto2.y - m*ponto2.x
            for x in range(ponto1.x, ponto2.x + 1):
                y = m*x + b
                self.pinta_pixel(x, round(y))

    def dda(ponto1 : Ponto, ponto2 : Ponto, cor, superficie):
        # swap das variaveis caso x1 > x2 e/ou y1 > y2
        if(ponto1.x > ponto2.x): ponto1.x , ponto2.x = ponto2.x, ponto1.x
        if(ponto1.y > ponto2.y): ponto1.y , ponto2.y = ponto2.y, ponto1.y

        dy = ponto2.y - ponto1.y
        dx = ponto2.x - ponto1.x
        
        if(abs(dx) > abs(dy)):
            incremento = dy/dx
            y = ponto1.y

            for x in range(ponto1.x, ponto2.x + 1):
                superficie.set_at((x, round(y)), cor)
                y += incremento
        else:
            incremento = dx/dy
            x = ponto1.x

            for y in range(ponto1.y, ponto2.y + 1):
                superficie.set_at((round(x), y), cor)
                x += incremento

    def dda2(self, ponto1 : Ponto, ponto2 : Ponto):
        dy = ponto2.y - ponto1.y
        dx = ponto2.x - ponto1.x

        delta = max(abs(dx), abs(dy))

        x = ponto1.x
        y = ponto1.y

        incrementoX = dx / delta
        incrementoY = dy / delta

        for i in range(delta + 1):
            self.pinta_pixel(round(x), round(y))
            x += incrementoX
            y += incrementoY

    def linhaBresenham(self, ponto1 : Ponto, ponto2 : Ponto):
        if(ponto1.x > ponto2.x): ponto1, ponto2 = ponto2, ponto1

        fazTroca = False

        if(ponto1.y >= ponto2.y):
            ponto1.y = -ponto1.y
            ponto2.y = -ponto2.y
            fazTroca = True
        
        dy = ponto2.y - ponto1.y
        dx = ponto2.x - ponto1.x

        if(abs(dy) > abs(dx)):
            ponto1.x, ponto1.y = ponto1.y, ponto1.x
            ponto2.x, ponto2.y = ponto2.y, ponto2.x

            dy = ponto2.y - ponto1.y
            dx = ponto2.x - ponto1.x

            y = ponto1.y

            parametro = 2*dy - dx
            for x in range(ponto1.x, ponto2.x + 1):
                if(fazTroca):
                    self.pinta_pixel(y, -x)
                else:
                    self.pinta_pixel(y, x)

                if(parametro < 0):
                    parametro += 2*dy
                else:
                    y += 1
                    parametro += 2*(dy - dx)
        else:
            y = ponto1.y

            parametro = 2*dy - dx
            for x in range(ponto1.x, ponto2.x + 1):
                if(fazTroca):
                    self.pinta_pixel(x, -y)
                else:
                    self.pinta_pixel(x, y)

                if(parametro < 0):
                    parametro += 2*dy
                else:
                    y += 1
                    parametro += 2*(dy - dx)

    # algoritmos de rasterização de circunferencias

    def parametrica(self, raio, centro : Ponto):
        x = centro.x + raio
        y = centro.y
        for t in range(0, 361):
            self.pinta_pixel(round(x), round(y))
            x = centro.x + raio*math.cos((t*math.pi)/180)
            y = centro.y + raio*math.sin((t*math.pi)/180)
    
    def incremental(self, raio, centro: Ponto):
        teta = 1/raio
        cosseno = math.cos(teta*math.pi/180)
        seno = math.sin(teta*math.pi/180)

        x = raio + centro.x
        y = centro.y

        while(x >= y):
            self.pinta_pixel(round(x), round(y))
            self.pinta_pixel(round(x), round(-y))
            self.pinta_pixel(round(-x), round(y))
            self.pinta_pixel(round(-x), round(-y))
            self.pinta_pixel(round(y), round(x))
            self.pinta_pixel(round(y), round(-x))
            self.pinta_pixel(round(-y), round(x))
            self.pinta_pixel(round(-y), round(-x))

            x = x * cosseno - y * seno
            y = y * cosseno + x * seno


    def circunferenciaBresenham(self, raio, centro : Ponto):
        x = 0
        y = raio
        parametro = 1 - raio

        while(x <= y):
            self.pinta_pixel(centro.x + x, centro.y + y)
            self.pinta_pixel(centro.x - x, centro.y + y)
            self.pinta_pixel(centro.x + x, centro.y - y)
            self.pinta_pixel(centro.x - x, centro.y - y)
            self.pinta_pixel(centro.x + y, centro.y + x)
            self.pinta_pixel(centro.x - y, centro.y + x)
            self.pinta_pixel(centro.x + y, centro.y - x)
            self.pinta_pixel(centro.x - y, centro.y - x)

            if(parametro < 0):
                parametro += 2*x + 3
                x += 1
            else:
                y -= 1
                parametro += 2*x - 2*y + 5
                x += 1

    # algoritmos de preenchimento

    def floodFill(self, x, y, corFundo):
        if(self.pega_pixel(x, y) == corFundo):
            self.pinta_pixel(x, y)
            self.floodFill(x + 1, y, corFundo)
            self.floodFill(x, y + 1, corFundo)
            self.floodFill(x - 1, y, corFundo)
            self.floodFill(x, y - 1, corFundo)

    def varreduraRetangulo(self, inicio : Ponto, largura, altura):
        maxY = inicio.y + altura + 1
        maxX = inicio.x + largura + 1
        for y in range(inicio.y, maxY):
            for x in range(inicio.x, maxX):
                self.pinta_pixel(x, y)

    def varreduraCircunferencia(self, centro: Ponto, raio):
        for y in range(centro.y - raio, centro.y + raio):
            x1 = centro.x - math.sqrt(raio**2 - (y - centro.y)**2)
            x2 = centro.x + math.sqrt(raio**2 - (y - centro.y)**2)

            for x in range(round(x1), round(x2)):
                self.pinta_pixel(x, y)
    
    def curvaBezier(self, quantidade_pontos_curva: int = 100):
        quantidade_pontos_controle = self.pontos_controle.__len__() - 1
        if(quantidade_pontos_controle >= 1):
            parametros_curva = np.linspace(0, 1, quantidade_pontos_curva)
            for parametro in parametros_curva:
                ponto = Ponto(0, 0)

                for i in range(quantidade_pontos_controle + 1):
                    ponto.x += math.comb(quantidade_pontos_controle, i) * (parametro ** i) * ((1 - parametro) ** (quantidade_pontos_controle - i)) * self.pontos_controle[i][0]
                    ponto.y += math.comb(quantidade_pontos_controle, i) * (parametro ** i) * ((1 - parametro) ** (quantidade_pontos_controle - i)) * self.pontos_controle[i][1]
                
                self.superficie.set_at((round(ponto.x), round(ponto.y)), self.cor)
    
    def ponto_medio(self, ponto1, ponto2):
        x = (ponto1[0] + ponto2[0])/2
        y = (ponto1[1] + ponto2[1])/2

        return x, y
    
    def curvaCasteljau(self, profundidade: int):
        if len(self.pontos_controle) == 4:
            pontos_curva = self.pontos_controle.copy()

            def divide_pontos_curva(pontos, profundidade_atual):
                if profundidade_atual == 0:
                    return pontos
                else:
                    m01 = self.ponto_medio(pontos[0], pontos[1])
                    m12 = self.ponto_medio(pontos[1], pontos[2])
                    m23 = self.ponto_medio(pontos[2], pontos[3])

                    m012 = self.ponto_medio(m01, m12)
                    m123 = self.ponto_medio(m12, m23)

                    ponto_medio_curva = self.ponto_medio(m012, m123)

                    pontos_curva1 = [pontos[0], m01, m012, ponto_medio_curva]
                    pontos_curva2 = [ponto_medio_curva, m123, m23, pontos[::-1][0]]

                    pontos_curva1 = divide_pontos_curva(pontos_curva1, profundidade_atual - 1)
                    pontos_curva2 = divide_pontos_curva(pontos_curva2, profundidade_atual - 1)

                    return pontos_curva1 + pontos_curva2

            pontos_curva = divide_pontos_curva(pontos_curva, profundidade)
            pygame.draw.lines(self.superficie, self.cor, False, pontos_curva)
    
    def calcula_intersecao(self, ponto1, ponto2, lado_recorte: int):
        if ponto2[0] - ponto1[0] == 0:
            # Lidar com linha vertical (evitar divisão por zero)
            x = ponto1[0]
            match lado_recorte:
                case 0: # topo
                    y = self.ymaximo
                case 1: # direita
                    y = ponto1[1] + (self.xmaximo - ponto1[0])
                case 2: # piso
                    y = self.yminimo
                case 3: # esquerda
                    y = ponto1[1] + (self.xminimo - ponto1[0])
        else:
            m = (ponto2[1] - ponto1[1]) / (ponto2[0] - ponto1[0])

            match lado_recorte:
                case 0: # topo
                    x = ponto1[0] + (self.ymaximo - ponto1[1]) / m
                    y = self.ymaximo
                case 1: # direita
                    y = ponto1[1] + (self.xmaximo - ponto1[0]) * m
                    x = self.xmaximo
                case 2: # piso
                    x = ponto1[0] + (self.yminimo - ponto1[1]) / m
                    y = self.yminimo
                case 3: # esquerda
                    y = ponto1[1] + (self.xminimo - ponto1[0]) * m
                    x = self.xminimo

        return x, y

    
    def verifica_ponto_dentro(self, ponto, lado_recorte):
        match lado_recorte:
            case 0: # topo
                return ponto[1] <= self.ymaximo
            case 1: # direita
                return ponto[0] <= self.xmaximo
            case 2: # piso
                return ponto[1] >= self.yminimo
            case 3: # esquerda
                return ponto[0] >= self.xminimo
    
    def recorteSutherlandHogman(self, janela_recorte):
        # inicializa o array de pontos do poligono
        poligono_recortado = self.pontos_controle.copy()
        poligono_recortado.append(self.pontos_controle[0])

        self.xminimo = janela_recorte[0][0]
        self.xmaximo = janela_recorte[0][0]
        self.yminimo = janela_recorte[0][1]
        self.ymaximo = janela_recorte[0][1]

        # Logica para definir os pontos máximos e minimos da janela de recorte
        for ponto in janela_recorte:
            if(ponto[0] < self.xminimo): self.xminimo = ponto[0]
            if(ponto[0] > self.xmaximo): self.xmaximo = ponto[0]
            if(ponto[1] < self.yminimo): self.yminimo = ponto[1]
            if(ponto[1] > self.ymaximo): self.ymaximo = ponto[1]
        
        for lado_recorte in range(4):
            novo_poligono = []

            for i in range(len(poligono_recortado) - 1):
                ponto1_dentro = self.verifica_ponto_dentro(poligono_recortado[i], lado_recorte)
                ponto2_dentro = self.verifica_ponto_dentro(poligono_recortado[i + 1], lado_recorte)
                
                # caso 1
                if(ponto1_dentro and ponto2_dentro): novo_poligono.append(poligono_recortado[i + 1])
                # caso 2
                elif(ponto1_dentro and not ponto2_dentro): novo_poligono.append(self.calcula_intersecao(poligono_recortado[i], poligono_recortado[i + 1], lado_recorte))
                # no caso 3 nada é feito
                # caso 4
                elif(not ponto1_dentro and ponto2_dentro):
                    novo_poligono.append(self.calcula_intersecao(poligono_recortado[i], poligono_recortado[i + 1], lado_recorte))
                    novo_poligono.append(poligono_recortado[i + 1])
                
            novo_poligono.append(novo_poligono[0])
            poligono_recortado = novo_poligono.copy()
        
        self.pontos_controle = poligono_recortado.copy()