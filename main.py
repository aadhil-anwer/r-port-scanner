import socket
import sys
from datetime import datetime 
#specify arguements
greeting_header="""
  _____        _____           _      _____                                 
 |  __ \      |  __ \         | |    / ____|                                
 | |__) |_____| |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  _  /______|  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | | \ \      | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
 |_|  \_\     |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                            
                                                                            
"""
if len(sys.argv) ==2:
    target = socket.gethostbyname(sys.argv[1]) # dns resolution
else:
    print("*" * 50)
    print("Invalid Arguements")
    print("python3 main.py <ip address>") 
    print("*" * 50) 

print(greeting_header)
print("Created by R0001")
print("A Useless Shitty Port Scanner")
print("Don't Use Unless You are deeply in love with me")
print("\n")

print("Scanning Target :"+target)
print("Start Time: "+str(datetime.now()))
  
try:
    for port in range(50,81):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is Open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Exciting Program......")
    print("Keyboard Interrupt")
    sys.exit()
except socket.gaierror:
    print("Hostname couldn't be resolved.")
    print("Exciting Program .....")
    sys.exit()
except socket.error:
    print("Couldn't Connect to server")
    print("Exciting Program .....")
    sys.exit()
 