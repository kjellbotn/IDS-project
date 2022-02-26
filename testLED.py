import time
import RPi.GPIO as GPIO
LED = 5

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)

def flash (t):
  GPIO.output(LED, True)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
