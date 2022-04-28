import time
import system
import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Caption?")

BatSignal = pygame.image.load("BatSignal.png")

while True:

    screen.fill((0, 0, 0))

    screen.blit(BatSignal, (0, 0))


    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            system.exit()

    time.sleep(0.01)
