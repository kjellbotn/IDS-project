import time
import RPi.GPIO as GPIO
LEDr = 5
LEDg = 22
BUTTON = 20

GPIO.setmode (GPIO.BCM)
GPIO.setup (LEDr, GPIO.OUT)
GPIO.setup (LEDg, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
ON = False
display.setup(GPIO, LEDr, LEDg, ON)

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

if BUTTON = ON:
  GPIO.output (LEDg, False)
  GPIO.output (LEDr, False)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
