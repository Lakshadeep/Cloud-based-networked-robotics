import RPi.GPIO as GPIO
from time import sleep
 

 
Motor1A = 19
Motor1B = 21


Motor2A = 16
Motor2B = 18

Motor3A = 22
Motor3B = 23

Motor4A = 24
Motor4B = 26

num = 5


while 1:
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)

     
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)


    GPIO.setup(Motor3A,GPIO.OUT)
    GPIO.setup(Motor3B,GPIO.OUT)

    GPIO.setup(Motor4A,GPIO.OUT)
    GPIO.setup(Motor4B,GPIO.OUT)

    print num


    num = raw_input("Enter motor number")
    

    if num == '1':
        print "Going forwards"
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

 
    
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)


        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)

        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        

    if num == '2':
        print "Going backwards"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)

     
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)


        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.HIGH)

        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.HIGH)
        

    if num == '3':
        print "Turn Left"
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

 
    
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)


        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.HIGH)

        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        
        
    if num == '4':
        print "Turn right"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)

     
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)


        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)

        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.HIGH)
        

    if num == '5':
        print "Now stop"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)

        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.LOW)

        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.LOW)

    if num == '6':
        print "Quit"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)

        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.LOW)

        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.LOW)
        GPIO.cleanup()
        break
   
 
    #sleep(10)
    #GPIO.cleanup()
     
    
     
    
     
    

   
     
    


