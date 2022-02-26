import time
import RPi.GPIO as GPIO
LED-r = 5
LED-g = 22

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED-r, GPIO.OUT)
GPIO.setup (LED-g, GPIO.OUT)


def flash (t):
  GPIO.output(LED-r, True)
  GPIO.output (LED-g, False)
  time.sleep(1)
  GPIO.output(LED-r, False)
  GPIO.output(LED-g, True)
  time.sleep(1)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
