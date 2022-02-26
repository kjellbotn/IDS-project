import time
import RPi.GPIO as GPIO
LEDr = 5
LEDg = 22
BUTTON = 20

GPIO.setmode (GPIO.BCM) #makes pin numbers accurate
GPIO.setup (LEDr, GPIO.OUT)
GPIO.setup (LEDg, GPIO.OUT) #identifies as output
GPIO.setup(BUTTON, GPIO.IN) # knows to read input from button
ON = False

def flash (t):
  GPIO.output(LEDr, True)
  GPIO.output (LEDg, False)
  time.sleep(1)
  GPIO.output (LEDr, False)
  GPIO.output (LEDg, False)
  time.sleep(0.5)
  GPIO.output(LEDr, True)
  GPIO.output (LEDg, False)
  time.sleep(1)
  GPIO.output(LEDr, False)
  GPIO.output(LEDg, True)
  time.sleep(1)
  GPIO.output(LEDr, False)
  GPIO.output(LEDg, False)
  time.sleep(0.5)
  GPIO.output(LEDr, False)
  GPIO.output(LEDg, True)
  time.sleep(1)

if GPIO.input(BUTTON) == False:
  GPIO.output (LEDg, False)
  GPIO.output (LEDr, False)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
