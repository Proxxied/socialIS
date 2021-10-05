#import socket module
from socket import *
serverSocket = socket (AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
serverPort = 6789 #assign port number
serverSocket.bind(('', serverPort)) #bind server address to port number
serverSocket.listen(1) #finds any incoming connections
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #establishes connection
    try:
        message = connectionSocket.recv(1024).decode() #receives request msg from client
        filename = message.split () [1]
        f = open(filename[1:], errors="ignore")
        outputdata = f.read() #Fill in start #Fill in end #returns the number of bytes from the file
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.x 200 OK\r\n\r\n'.encode()) #send a http header line
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.x 404 Not Found\r\n\r\n'.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close() #close client socket
        #Fill in end
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
