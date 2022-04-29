#imports time, system, and pygame
import time
import sys
import pygame

#initiates pygame
pygame.init()

#sets up a display for pygame to use
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN);
pygame.display.set_caption("Caption?")

#reads the batsignal image from file "BatSignal.png"
BatSignal = pygame.image.load("BatSignal.png")

#loops for as only as the program runs
while True:

    #loops for each pygame event
    for event in pygame.event.get():
        #checks for quit event
        if(event.type == pygame.QUIT):
            #stops the program
            pygame.quit()
            sys.exit()

        #checks for keypressed event
        if(event.type == pygame.KEYDOWN):
            #checks if the escape key was pressed
            if(event.key == pygame.K_ESCAPE):
                #stops the program
                pygame.quit()
                sys.exit()

    #makes the background black
    screen.fill((0, 0, 0))

    #draws the batsignal
    screen.blit(BatSignal, (0, 0))

    #updates the display
    pygame.display.update()

    #waits to add delay for the next frame
    time.sleep(0.01)
