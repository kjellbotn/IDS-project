import time
import RPi.GPIO as GPIO
LED = 5

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)

def flash (t):
  GPIO.output(LED, True)
  time(1)
  GPIO.output(LED, False)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
