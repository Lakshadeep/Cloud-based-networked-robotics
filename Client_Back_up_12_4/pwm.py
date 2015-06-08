import RPi.GPIO as io
from time import sleep
io.setmode(io.BOARD)
in1_pin = 16
in2_pin = 18
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)


p = io.PWM(16,50)
p.start(50)
io.output(in2_pin,io.LOW)

sleep(2)
p.ChangeDutyCycle(20)
sleep(2)
p.ChangeFrequency(50)
sleep(2)
io.output(in1_pin,io.LOW)
io.output(in2_pin,io.LOW)
io.cleanup()
