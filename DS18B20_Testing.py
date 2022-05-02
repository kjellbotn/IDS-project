import os
import glob
import time

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

def readTemp()
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

while True:
    print(readTemp())
