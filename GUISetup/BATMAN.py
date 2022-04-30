#imports time, system, and pygame
import time
import sys
import pygame

#imports board and the BME library
import board
from adafruit_bme280 import basic as BME280

#initiates pygame
pygame.init()

#sets up the I2C pins
i2c = board.I2C()

#defines the BME
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

#reads current desktop size
screenInfo = pygame.display.Info()

#stores the screen size for later
screenSize = (screenInfo.current_w, screenInfo.current_h)

#sets the screensize to the size of the first desktop
screen = pygame.display.set_mode(screenSize)

#creates a surface to draw the display data onto
DrawSurf = pygame.Surface((1920, 1080))

#generates a phont to write text with
font = pygame.font.SysFont("wasy10", 35);

#adds a title for the window
pygame.display.set_caption("Caption?")

#enables fullscreen
pygame.display.toggle_fullscreen()

#reads the batsignal image from file "BatSignal.png"
BatSignal = pygame.image.load("BatSignal.png")

#loops for as only as the program runs
while True:

    while mode == "Loading":
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

                elif(event.key == pygame.K_ENTER):

                    #tell the program to start reading data
                    mode = "Reading Data"

        #makes the background black
        DrawSurf.fill((0, 0, 0))

        #draws the batsignal
        DrawSurf.blit(BatSignal, (0, 0))

        #draws the buffered dispaly to the screen after resizing it
        screen.blit(pygame.transform.scale(DrawSurf, screenSize), (0, 0))

        #updates the display
        pygame.display.update()

        #waits to add delay for the next frame
        time.sleep(0.01)

    #loops the screen is displaying data
    while mode == "Reading Data":

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

        #clears the displaySurface
        DrawSurf.fill((0, 0, 0))

        #draws the test text
        DrawSurf.blit(font.render("Hello", True, (255, 255, 255)), (900, 400))

        #draws the buffered dispaly to the screen after resizing it
        screen.blit(pygame.transform.scale(DrawSurf, screenSize), (0, 0))

        #updates the display
        pygame.display.update()

        #waits to add delay for the next frame
        time.sleep(0.01)
