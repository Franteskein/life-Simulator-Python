import pygame
import random

# Define la estructura del agente
class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 100

    def mover(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.energy -= 1

# Configuración inicial
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
agents = [Agente(random.randint(0, width), random.randint(0, height)) for _ in range(10)]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualiza la posición de los agentes
    for agent in agents:
        agent.mover()

    # Dibuja los agentes en la pantalla
    screen.fill((255, 255, 255))
    for agent in agents:
        pygame.draw.circle(screen, (0, 0, 255), (agent.x, agent.y), 5)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
