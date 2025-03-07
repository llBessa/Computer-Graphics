import pygame, math
from Ponto import Ponto

# algoritmos de rasterização de linhas

class Renderizador:
    def __init__(self, superficie, cor, escala):
        self.superficie = superficie
        self.cor = cor
        self.escala = escala
        self.largura_tela = superficie.get_width()
        self.altura_tela = superficie.get_height()
    
    def pinta_pixel(self, x, y):
        y = self.altura_tela/2 - (y + 1) * self.escala
        x = x * self.escala + self.largura_tela/2

        pygame.draw.rect(self.superficie, self.cor, pygame.Rect(x, y , self.escala, self.escala), 1)
    
    def pega_pixel(self, x, y):
        y = self.altura_tela/2 - (y + 1) * self.escala
        x = x * self.escala + self.largura_tela/2

        return self.superficie.get_at((int(x), int(y)))


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
    


# def criaFiguraA(cor, superficie, escala):
#     dda2(Ponto(abs(30*escala), abs(30*escala)), Ponto(abs(60*escala), abs(10*escala)), cor, superficie)
#     dda2(Ponto(abs(60*escala), abs(10*escala)), Ponto(abs(95*escala), abs(35*escala)), cor, superficie)
#     dda2(Ponto(abs(95*escala), abs(35*escala)), Ponto(abs(85*escala), abs(45*escala)), cor, superficie)
#     dda2(Ponto(abs(85*escala), abs(45*escala)), Ponto(abs(35*escala), abs(60*escala)), cor, superficie)
#     dda2(Ponto(abs(35*escala), abs(60*escala)), Ponto(abs(40*escala), abs(40*escala)), cor, superficie)
#     dda2(Ponto(abs(40*escala), abs(40*escala)), Ponto(abs(30*escala), abs(30*escala)), cor, superficie)