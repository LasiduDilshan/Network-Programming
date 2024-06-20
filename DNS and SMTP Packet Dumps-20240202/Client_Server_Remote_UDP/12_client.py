import socket

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("20.189.120.250", 12345)  #Private ip of server
bufferSize = 1024

#Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Bind to address and ip
UDPServerSocket.sendto(bytesToSend, serverAddressPort)

with open('To send.pdf', 'rb') as file:
    data = file.read(1024)
    while data:
        UDPClientCocket.sendto(data, serverAddressPort)
        data = file.read(1024)

data = None
UDPClientSocket.sendto('b', serverAddressPort)

print("File sent successfully")
