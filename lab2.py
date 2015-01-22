import socket
import sys
#create an INET, STREAMing socket:
#this is the type of socket- socket.AF_INET
#this is for TCP packages?? - socket.SOCK_STREAM
try:
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM) 
except socket.error as msg:
    print('Failed to create socket!')
    print('Error code: ' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print(' Socket created successfully')

host = ''
port = 8080

try:
    s.bind((host, port))
except socket.error:
    msg = str(socket.error)
    print('Bind failed! Error code: ' + str(msg[0]) + ', message: ' + msg[1])
    sys.exit()
print('Socket bind complete.')
s.listen(10) #limitation of number of connection that can be in the backlog
print('Socket is now listening.')
conn, addr = s.accept()
print('Connected with '+ addr[0] + ':' + str(addr[1]))

data = conn.recv(1024)
#data2 = str(data)
#data2 = data2[2:len(data2)-5]
reply = "hello "+ str(data) 
conn.sendall(reply.encode("UTF8"))

conn.close()
s.close()

#try:
    #remote_ip= socket.gethostbyname(host)
#except socket.gaierror: #short of rget address int? error:
    #print('Host name could not be resolved')
    #sys.exit()
    
#print('IP address of ' + host + ' is ' +remote_ip)

##now connect to the web server on port 80
## - the normal http port
#s.connect((remote_ip, port))
#print('Socket connected to ' + host + ' on ip ' + remote_ip)

#message = 'GET / HTTP/1.1\r\n\r\n'
#try:
    #s.sendall(message.encode("UTF8"))
#except socket.error:
    #print('Send failed:')
    #sys.exit()
#print('Message send successfully')

##define buffer size in the power of 2. 
#reply = s.recv(4096)
#print (reply)
#s.close()