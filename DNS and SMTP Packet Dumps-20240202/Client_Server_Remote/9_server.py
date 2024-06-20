import socket
import time

def current_milli_time():
    return round(time.time() * 1000)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    server_socket.bind(('192.168.8.119', 12345))  #insert the private ip of remote server
    server_socket.listen(1)

    print("Server is listening.........")

    conn, addr = server_socket.accept()
    print("Connection from: ", addr)

    with open("received_file.txt", "wb") as file:
        last_bw_time = current_milli_time()
        data_count = 0
        total_data = 0
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
            data_count = data_count + len(data) #1024
            total_data = total_data +len(data)
            if (current_milli_time() > (last_bw_time + 1000)):
                print("Speed ::", data_count/1000, "kB/S", "Total ::", total_data/1000, "kB")
                last_bw_time = current_milli_time()
                data_count = 0

    print("File received successfully.")
    time.sleep(10)
    conn.close()

start_server()
