#imports time, system, and pygame
import time
import sys
import pygame

#imports os and global for DS18B20
import os
import glob

#imports board and the BME library
import board
from adafruit_bme280 import basic as BME280

#initiates pygame
pygame.init()

#sets up thermometer as w1 device
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#finds file for reading data from sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#read raw file data
def readRaw():
    #opens file
    f = open(device_file, 'r')
    #reads file
    lines = f.readlines()
    #closes file
    f.close()

    #returns read lines
    return(lines)

def readTemp():
    #reads raw temp data
    lines = readRaw()
    #loops until reading works
    while lines[0].strip()[-3:] != 'YES':
        #waits and reads again
        time.sleep(0.2)
        lines = readRaw()
    #finds the first occurence of t=
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        #reads the temperature
        temp_string = lines[1][equals_pos+2:]
        #converts to degrees C from string
        temp_c = float(temp_string) / 1000.0
        return(temp_c)

    #returns nonsense on failiure
    return(-100000)

#sets up the I2C pins
i2c = board.I2C()

#defines the BME
bme280 = BME280.Adafruit_BME280_I2C(i2c)

#reads current desktop size
screenInfo = pygame.display.Info()

#stores the screen size for later
screenSize = (screenInfo.current_w, screenInfo.current_h)

#sets the screensize to the size of the first desktop
screen = pygame.display.set_mode(screenSize)

#creates a surface to draw the display data onto
DrawSurf = pygame.Surface((1920, 1080))

#generates a phont to write text with
#best p052
#font = pygame.font.SysFont("omni10", 35);
font = pygame.font.Font("Qdbettercomicsans-jEEeG.ttf", 70)

#adds a title for the window
pygame.display.set_caption("Caption?")

#enables fullscreen
pygame.display.toggle_fullscreen()

#reads the batsignal image from file "BatSignal.png"
BatSignal = pygame.image.load("BatSignal.png")

#a variable to store the current operating mode
mode = "Loading"

counter = 0

#loops for as only as the program runs
while True:

    while mode == "Loading":
        if counter == 40:
            mode = "Reading Data"

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

                elif(event.key == pygame.K_RETURN):

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

        counter += 1

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

        #reads data from sensors and changes it to a string
        temp = "BME Temperature: " + str(bme280.temperature)
        press = "BME Pressure: " + str(bme280.pressure)
        humid = "BME Humidity: " + str(bme280.humidity)
        DSTemp = "DS18B20 Temperature: " + str(readTemp())

        #writes the current temperature display
        DrawSurf.blit(font.render(temp, True, (255, 255, 255)), (50, 50))

        #writes the current pressure display
        DrawSurf.blit(font.render(press, True, (255, 255, 255)), (50, 150))

        #writes the current humidity display
        DrawSurf.blit(font.render(humid, True, (255, 255, 255)), (50, 250))

        DrawSurf.blit(font.render(DSTemp, True, (255, 255, 255)), (50, 350))

        #draws the buffered dispaly to the screen after resizing it
        screen.blit(pygame.transform.scale(DrawSurf, screenSize), (0, 0))

        #updates the display
        pygame.display.update()

        #waits to add delay for the next frame
        time.sleep(0.01)
