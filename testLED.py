import time
import RPi.GPIO as GPIO
LEDr = 5
LEDg = 22

GPIO.setmode (GPIO.BCM)
GPIO.setup (LEDr, GPIO.OUT)
GPIO.setup (LEDg, GPIO.OUT)


def flash (t):
  GPIO.output(LEDr, True)
  GPIO.output (LEDg, False)
  time.sleep(1)
  GPIO.output(LEDr, True)
  GPIO.output (LEDg, False)
  time.sleep(1)
  GPIO.output(LEDr, False)
  GPIO.output(LEDg, True)
  time.sleep(1)
  GPIO.output(LEDr, False)
  GPIO.output(LEDg, True)
  time.sleep(1)

try:
  while True:
    flash(1)
   
finally:
  GPIO.cleanup()
