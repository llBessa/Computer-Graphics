import pygame, math

class Ponto:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

# algoritmos de rasterização de linhas

def analitico(ponto1 : Ponto, ponto2 : Ponto, cor, superficie):
    # swap das variaveis caso x1 > x2 e/ou y1 > y2
    if(ponto1.x > ponto2.x): ponto1.x , ponto2.x = ponto2.x, ponto1.x
    if(ponto1.y > ponto2.y): ponto1.y , ponto2.y = ponto2.y, ponto1.y
    
    if(ponto1.x == ponto2.x):
        for y in range(ponto1.y,ponto2.y):
            superficie.set_at((ponto1.x, y),cor)
    else:
        m = (ponto2.y - ponto1.y)/(ponto2.x - ponto1.x)
        b = ponto2.y - m*ponto2.x
        for x in range(ponto1.x, ponto2.x):
            y = m*x + b
            superficie.set_at((x,round(y)), cor)

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
            superficie.set_at((round(x),y), cor)
            x += incremento

def dda2(ponto1 : Ponto,ponto2 : Ponto, cor, superficie):
    dy = ponto2.y - ponto1.y
    dx = ponto2.x - ponto1.x

    delta = max(abs(dx), abs(dy))

    x = ponto1.x
    y = ponto1.y

    incrementoX = dx / delta
    incrementoY = dy / delta

    for i in range(delta):
        superficie.set_at((round(x),round(y)), cor)
        x += incrementoX
        y += incrementoY

def linhaBresenham(ponto1 : Ponto, ponto2 : Ponto, cor, superficie):
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
        for x in range(ponto1.x, ponto2.x):
            if(fazTroca):
                superficie.set_at((y,-x), cor)
            else:
                superficie.set_at((y,x), cor)

            if(parametro < 0):
                parametro += 2*dy
            else:
                y += 1
                parametro += 2*(dy - dx)
    else:
        y = ponto1.y

        parametro = 2*dy - dx
        for x in range(ponto1.x, ponto2.x):
            if(fazTroca):
                superficie.set_at((x,-y), cor)
            else:
                superficie.set_at((x,y), cor)

            if(parametro < 0):
                parametro += 2*dy
            else:
                y += 1
                parametro += 2*(dy - dx)

# algoritmos de rasterização de circunferencias

def parametrica(raio, centro : Ponto, cor, superficie):
    x = centro.x + raio
    y = centro.y
    for t in range(0, 361):
        superficie.set_at((round(x), round(y)), cor)
        x = centro.x + raio*math.cos((t*math.pi)/180)
        y = centro.y + raio*math.sin((t*math.pi)/180)

def circunferenciaBresenham(raio, centro : Ponto, cor, superficie):
    x = 0
    y = raio
    parametro = 1 - raio

    while(x <= y):
        superficie.set_at((centro.x + x, centro.y + y), cor)
        superficie.set_at((centro.x - x, centro.y + y), cor)
        superficie.set_at((centro.x + x, centro.y - y), cor)
        superficie.set_at((centro.x - x, centro.y - y), cor)
        superficie.set_at((centro.x + y, centro.y + x), cor)
        superficie.set_at((centro.x - y, centro.y + x), cor)
        superficie.set_at((centro.x + y, centro.y - x), cor)
        superficie.set_at((centro.x - y, centro.y - x), cor)

        if(parametro < 0):
            parametro += 2*x + 3
            x += 1
        else:
            y -= 1
            parametro += 2*x - 2*y + 5
            x += 1

# algoritmos de preenchimento

def floodFill(x, y, cor, novaCor, superficie):
    if(superficie.get_at((x,y)) == cor):
        superficie.set_at((x,y), novaCor)
        floodFill(x + 1, y, cor, novaCor, superficie)
        floodFill(x, y + 1, cor, novaCor, superficie)
        floodFill(x - 1, y, cor, novaCor, superficie)
        floodFill(x, y - 1, cor, novaCor, superficie)

def varreduraRetangulo(inicio : Ponto, largura, altura, cor, superficie):
    maxY = inicio.y + altura + 1
    maxX = inicio.x + largura + 1
    for y in range(inicio.y, maxY):
        for x in range(inicio.x, maxX):
            superficie.set_at((x, y), cor)

def varreduraCircunferencia(centro: Ponto, raio, cor, superficie):
    for y in range(centro.y - raio, centro.y + raio):
        x1 = centro.x - math.sqrt(raio**2 - (y - centro.y)**2)
        x2 = centro.x + math.sqrt(raio**2 - (y - centro.y)**2)

        for x in range(round(x1), round(x2)):
            superficie.set_at((x, y), cor)

def criaFiguraA(cor, superficie, escala):
    dda2(Ponto(abs(30*escala), abs(30*escala)), Ponto(abs(60*escala), abs(10*escala)), cor, superficie)
    dda2(Ponto(abs(60*escala), abs(10*escala)), Ponto(abs(95*escala), abs(35*escala)), cor, superficie)
    dda2(Ponto(abs(95*escala), abs(35*escala)), Ponto(abs(85*escala), abs(45*escala)), cor, superficie)
    dda2(Ponto(abs(85*escala), abs(45*escala)), Ponto(abs(35*escala), abs(60*escala)), cor, superficie)
    dda2(Ponto(abs(35*escala), abs(60*escala)), Ponto(abs(40*escala), abs(40*escala)), cor, superficie)
    dda2(Ponto(abs(40*escala), abs(40*escala)), Ponto(abs(30*escala), abs(30*escala)), cor, superficie)

def keepWindowAlive():
    running = True
    while running:
        # itera na fila de eventos
        for event in pygame.event.get():
            # se o evento de quit for identificado a condição de parada é setada
            if event.type == pygame.QUIT:
                running = False