import socket
import sys
  
TCP_IP = '192.168.0.12'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
except socket.error, (value,message):
    if s:
        s.close()
        print 'could not open socket: '+ message
        sys.exit(1)
print 'Connected'
s.send(MESSAGE)
print 'sending message', MESSAGE
data = s.recv(BUFFER_SIZE)
s.close()
print 'waiting for response..'
print "Response received data:", data
