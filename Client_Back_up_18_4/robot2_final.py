import time
from Queue import Queue
import numpy as np
import cv2
import requests
import urllib2, urllib
import socket
import RPi.GPIO as GPIO
from time import sleep

#initialise the camera
cap = cv2.VideoCapture(0)
cap.set(0,320)

#define motor pins
Motor1A = 19
Motor1B = 21

Motor2A = 16
Motor2B = 18

Motor3A = 22
Motor3B = 23

Motor4A = 24
Motor4B = 26

#motor direction functions
def forward():
    print "Going forwards"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

 
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)


    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.LOW)

    GPIO.output(Motor4A,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.LOW)

    
def backwards():
    print "Going backwards"
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)

     
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)


    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.HIGH)

    GPIO.output(Motor4A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.HIGH)

def left():
    print "Turn Left"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

 
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)


    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.HIGH)

    GPIO.output(Motor4A,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.LOW)

def right():
    print "Turn right"
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)

     
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)


    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.LOW)

    GPIO.output(Motor4A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.HIGH)


def stop():
    print "Stop"
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)

    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.LOW)

    GPIO.output(Motor4A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.LOW)

def setup():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)

     
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)


    GPIO.setup(Motor3A,GPIO.OUT)
    GPIO.setup(Motor3B,GPIO.OUT)

    GPIO.setup(Motor4A,GPIO.OUT)
    GPIO.setup(Motor4B,GPIO.OUT)

#define sensor pins
sensor1 = 11

sensor2 = 12

sensor3 = 13

sensor4 = 14

#initialise the sensors

def setup_sensors():
    GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(sensor1,GPIO.IN) 
    GPIO.setup(sensor2,GPIO.IN) 
    GPIO.setup(sensor3,GPIO.IN)
    GPIO.setup(sensor4,GPIO.IN) 



#setting the server url
ip = '192.168.1.33'
url_capture = 'http://'+ip+'/xampp/FYP/upload_file1.php'

#initialising the socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.33', 8092))

#process for capturing and uploading images to server
def image_capture_upload_process():
    while 1:
        print "Main program running\n"

        #store the captured frame in frame variable
        ret, frame = cap.read()

        #display image in opencv window
        #note: doesnt work ...coz of some opencv error
        #cv2.imshow('frame',frame)

        
        cv2.imwrite("outimage1.jpg",frame)

        #upload image to server using python requests library and php handler
        files = {'file': open('outimage2.jpg', 'rb')}
        r = requests.post(url_capture, files=files)
        sleep(0.5)

        


#process for local motion processing
#basic obstacle avoidance algorithm
def motion_control_process(in_q):
    
    setup_sensors()  #initialise the sensors

    ls = GPIO.input(sensor1)
    rs = GPIO.input(sensor2)
   
    while 1:
        setup()  #initialise the motors
        stop()  
        print "Receiving the data in motion control process:"

        #receive the data send by msg_process
        data = in_q.get()
    
        print data

        if data == 1:
           stop()
           break;

        if(ls == 0 & rs == 0):
           forward()
           sleep(0.3)
           stop()
           sleep(0.5)
           
           print "Forward"

        elif(ls == 1 & rs == 1):
            backwards()
            sleep(0.3)
            stop(0.3)
            left(0.3)
            stop(0.5)
            print "Backward left"

        elif(ls == 1 & rs == 0):
            right()
            sleep(0.5)
            stop()
            sleep(0.5)
            print "Right"

        elif(ls == 0 & rs == 1):
            left()
            sleep(0.5)
            stop()
            sleep(0.5)
            print "Left"


# process for receiving messages from server
def msg_process(out_q):
    
    while 1:

        #receive 4 bytes from server socket
        msg = clientsocket.recv(4)

        #convert recieved message from string to int (typecasting)
        msg_int = int(msg)
        
        print "Response received from server"
        print "Number of circles detected:"
        print msg_int
        
        #send the received message to motion_control_process
        out_q.put(msg_int)
        
        
        #time.sleep(1)
        


from threading import Thread

q = Queue()
t1 = Thread(target=image_capture_upload_process,args=())
t1.start()

t2 = Thread(target=msg_process,args=(q,))
t2.start()

t3 = Thread(target=motion_control_process,args=(q,))
t3.start()
