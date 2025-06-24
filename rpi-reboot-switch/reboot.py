import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 26
GPIO.setup(PIN, GPIO.OUT)

print("Starting reboot")
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


print("waiting 10 seconds for computer to be fully off")
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
time.sleep(1)
print("7")
time.sleep(1)
print("8")
time.sleep(1)
print("9")
time.sleep(1)
print("10 - done waiting")

print("Starting server again")
GPIO.output(PIN, GPIO.HIGH)

time.sleep(0.3)
GPIO.output(PIN, GPIO.LOW)

print("Turning on - script done")
GPIO.cleanup()

