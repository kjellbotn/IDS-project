#imports time, system, and pygame
import time
import sys
import pygame

#initiates pygame
pygame.init()

#reads current desktop size
screenInfo = pygame.display.Info()

screenSize = (screenInfo.current_w, screenInfo.current_h)

#sets the screensize to the size of the first desktop
screen = pygame.display.set_mode(screenSize)

#creates a surface to draw the display data onto
DrawSurf = pygame.Surface((1920, 1080))

#adds a title for the window
pygame.display.set_caption("Caption?")

#enables fullscreen
pygame.display.toggle_fullscreen()

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
    DrawSurf.fill((0, 0, 0))

    #draws the batsignal
    DrawSurf.blit(BatSignal, (0, 0))

    screen.blit(pygame.transform.scale(DrawSurf, screenSize), (0, 0))

    #updates the display
    pygame.display.update()

    #waits to add delay for the next frame
    time.sleep(0.01)
