import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18

Motor2A = 19
Motor2B = 21
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
 
print "Turning motors on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)

 
sleep(2)
 
print "Stopping motors"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)
 
GPIO.cleanup()

