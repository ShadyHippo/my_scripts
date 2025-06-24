import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 26
GPIO.setup(PIN, GPIO.OUT)

print("Starting shutdown")
GPIO.output(PIN, GPIO.HIGH)

time.sleep(1)
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3")
time.sleep(1)
print("4")
time.sleep(1)
print("5")
time.sleep(1)
print("6")

GPIO.output(PIN, GPIO.LOW)
print("off")

GPIO.cleanup()

