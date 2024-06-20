import socket
import time

def current_milli_time():
    return round(time.time() * 1000)

localIP = "10.1.0.4"  #Private ip of server
local port = 12345
bufferSize = 1024

#Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

with open("received_file.txt", "wb") as file:
    last_bw_time = current_milli_time()
    data_count = 0
    total_data = 0
    transfer_start = 0
    
    while True:
        data = UDPServerSocket.recvfrom(bufferSize)
        if not data[0]:
            break
        if not transfer_start:
            transfer_start = current_milli_time()
        

        file.write(data[0])
        data_count = data_count + len(data[0]) #1024
        total_data = total_data +len(data[0])
        time_now = current_milli_time()
        if (time_now > (last_bw_time + 1000)):
            print("Speed ::", data_count/1000. "kB/S", "Total ::", total_data/1000, "kB")
            last_bw_time = current_milli_time()
            data_count = 0

print("File received successfully.")
