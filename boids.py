import random, pygame, math, sys

pygame.init()
pygame.font.init
font = pygame.font.SysFont ( "comicsansms", 20)
size = largura, altura = 1200, 650
PRETO = 0, 0, 0
AZUL = 77, 77, 255
AMARELO = 255, 255, 0
ROSA = 235,199,158

velMax = 10
numBoids = 50
boids = []
boids1 = []
boids2 = []

class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidadeX = random.randint(1, 10) / 10.0
        self.velocidadeY = random.randint(1, 10) / 10.0
    # Retorna a sua de outro boid

    def distancia(self, boid):
        distX = self.x - boid.x
        distY = self.y - boid.y
        return math.sqrt(distX * distX + distY * distY)

    def moveCloser(self, boids):
        if len(boids) < 1:
            return

        avgX = 0
        avgY = 0
        for boid in boids:
            if boid.x == self.x and boid.y == self.y:
                continue

            avgX += (self.x - boid.x)
            avgY += (self.y - boid.y)

        avgX /= len(boids)
        avgY /= len(boids)

        distancia = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0

        self.velocidadeX -= (avgX / 100)
        self.velocidadeY -= (avgY / 100)

    def moveWith(self, boids):
        if len(boids) < 1:
            return

        avgX = 0
        avgY = 0

        for boid in boids:
            avgX += boid.velocidadeX
            avgY += boid.velocidadeY

        avgX /= len(boids)
        avgY /= len(boids)

        self.velocidadeX += (avgX / 40)
        self.velocidadeY += (avgY / 40)

    def moveAway(self, boids, minDistancia):
        if len(boids) < 1:
            return

        distanciaX = 0
        distanciaY = 0
        numClose = 0

        for boid in boids:
            distancia = self.distancia(boid)
            if distancia < minDistancia:
                numClose += 1
                xdiff = (self.x - boid.x)
                ydiff = (self.y - boid.y)

                if xdiff >= 0: xdiff = math.sqrt(minDistancia) - xdiff
                elif xdiff < 0: xdiff = -math.sqrt(minDistancia) - xdiff

                if ydiff >= 0: ydiff = math.sqrt(minDistancia) - ydiff
                elif ydiff < 0: ydiff = -math.sqrt(minDistancia) - ydiff

                distanciaX += xdiff
                distanciaY += ydiff

        if numClose == 0:
            return

        self.velocidadeX -= distanciaX / 5
        self.velocidadeY -= distanciaY / 5

    def move(self):
        if abs(self.velocidadeX) > velMax or abs(self.velocidadeY) > velMax:
            scaleFactor = velMax / max(abs(self.velocidadeX), abs(self.velocidadeY))
            self.velocidadeX *= scaleFactor
            self.velocidadeY *= scaleFactor

        self.x += self.velocidadeX
        self.y += self.velocidadeY

    def newBoid(self, coord):
        x, y = coord
        boids.append(Boid(x, y))
    def newBoid1(self, coord):
        x, y = coord
        boids1.append(Boid(x, y))
    def newBoid2(self, coord):
        x, y = coord
        boids2.append(Boid(x, y))

screen = pygame.display.set_mode(size)

bola = pygame.image.load("bola.png")
ballrect = bola.get_rect()

for i in range(1):
    boids1.append(Boid(random.randint(0, largura), random.randint(0, altura)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            boid.newBoid(coord)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                coord = pygame.mouse.get_pos()
                boid.newBoid1(coord)
            if event.key == pygame.K_c:
                coord = pygame.mouse.get_pos()
                boid.newBoid2(coord)

    for boid in boids:
        closeBoids = []
        for outroBoid in (boids + boids2):
            if outroBoid == boid: continue
            distancia = boid.distancia(outroBoid)
            if distancia < 200:
                closeBoids.append(outroBoid)

        boid.moveCloser(closeBoids)
        boid.moveWith(closeBoids)
        boid.moveAway(closeBoids, 20)

        border = 25

        if boid.x < border and boid.velocidadeX < 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.x > largura - border and boid.velocidadeX > 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.y < border and boid.velocidadeY < 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()
        if boid.y > altura - border and boid.velocidadeY > 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()

        boid.move()


    for boid in boids1:
        closeBoid = []

        #---esse for foi alterado para arrmar bug
        for outroBoid in (boids + boids1):
            if outroBoid == boid: continue
            distancia = boid.distancia(outroBoid)
            if distancia < 200:
                closeBoid.append(outroBoid)

        boid.moveCloser(closeBoid)
        boid.moveWith(closeBoid)
        boid.moveAway(closeBoid, 20)

        border = 25

        if boid.x < border and boid.velocidadeX < 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.x > largura - border and boid.velocidadeX > 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.y < border and boid.velocidadeY < 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()
        if boid.y > altura - border and boid.velocidadeY > 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()

        boid.move()

    for boid in boids2:
        closeBoid = []

        #---esse for foi alterado para arrmar bug
        for outroBoid in (boids2 + boids1):
            if outroBoid == boid: continue
            distancia = boid.distancia(outroBoid)
            if distancia < 200:
                closeBoid.append(outroBoid)

        boid.moveCloser(closeBoid)
        boid.moveWith(closeBoid)
        boid.moveAway(closeBoid, 20)

        border = 25

        if boid.x < border and boid.velocidadeX < 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.x > largura - border and boid.velocidadeX > 0:
            boid.velocidadeX = -boid.velocidadeX * random.random()
        if boid.y < border and boid.velocidadeY < 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()
        if boid.y > altura - border and boid.velocidadeY > 0:
            boid.velocidadeY = -boid.velocidadeY * random.random()

        boid.move()

    screen.fill(PRETO)
    for boid in boids:
        boidRect = pygame.Rect(ballrect)
        boidRect.x = boid.x
        boidRect.y = boid.y
        pygame.draw.circle(screen, AZUL, (int(boid.x), int(boid.y)), 10)

    for boid in boids1:
        boidRect = pygame.Rect(ballrect)
        boidRect.x = boid.x
        boidRect.y = boid.y
        pygame.draw.circle(screen, AMARELO, (int(boid.x), int(boid.y)), 10)

    for boid in boids2:
        boidRect = pygame.Rect(ballrect)
        boidRect.x = boid.x
        boidRect.y = boid.y
        pygame.draw.circle(screen, ROSA, (int(boid.x), int(boid.y)), 10)

    boids1_cont = font.render(str(len(boids1)), True, AMARELO)
    boids_cont = font.render(str(len(boids)), False, AZUL)

    screen.blit(boids1_cont, (10, 5))
    screen.blit(boids_cont, (1150, 5))


    pygame.display.flip()
    pygame.time.delay(10)
