import time
from Queue import Queue
import numpy as np
import cv2
import requests
import urllib2, urllib
import socket
import RPi.GPIO as GPIO
from time import sleep
 
#initialise the motors
GPIO.setmode(GPIO.BOARD)
Motor1A = 19
Motor1B = 21
Motor2A = 16
Motor2B = 18
Motor3A = 22
Motor3B = 23
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)


#initialise the camera
cap = cv2.VideoCapture(0)
cap.set(0,320)

#setting the server url
#ip = 'localhost'
#url_capture = 'http://'+ip+'/xampp/FYP/upload_file1.php'

#initialising the socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.0.101', 8093))

#process for capturing and uploading images to server
#def image_capture_upload_process():
#    while 1:
#        print "Main program running\n"
#
        #store the captured frame in frame variable
#        ret, frame = cap.read()
#
        #display image in opencv window
        #note: doesnt work ...coz of some opencv error
#        cv2.imshow('frame',frame)

        
#        cv2.imwrite("outimage.jpg",frame)

        #upload image to server using python requests library and php handler
#        files = {'file': open('outimage.jpg', 'rb')}
#        r = requests.post(url_capture, files=files)

        


#process for local motion processing
#basic obstacle avoidance algorithm
def motion_control_process(in_q):

    while 1:
        print "Receiving the data in motion control process:"

        #receive the data send by msg_process
        data = in_q.get()
    
        print data

        if data > 100:
        print "Going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW) 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)

    


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
