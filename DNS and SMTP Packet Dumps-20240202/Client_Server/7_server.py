import socket
import time

def current_milli_time():
    return round(time.time() * 1000)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    server_socket.bind(('192.168.8.160', 12345))
    server_socket.listen(1)

    print("Server is listening.........")

    conn, addr = server_socket.accept()
    print("Connection from: ", addr)

    with open("received_file.txt", "wb") as file:
        last_bw_time = current_milli_time()
        data_count = 0
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received successfully.")
    time.sleep(10)
    conn.close()

start_server()
