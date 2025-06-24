import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 26
GPIO.setup(PIN, GPIO.OUT)

print("Starting server")
GPIO.output(PIN, GPIO.HIGH)

time.sleep(0.3)
GPIO.output(PIN, GPIO.LOW)

print("Turning on - script done")
GPIO.cleanup()

