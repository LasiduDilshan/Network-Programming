import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.8.160', 12345)

    client_socket.connect(server_address)
    with open('To send.txt', 'rb') as file:
        data = file.read(1000)
        while data:
            client_socket.sendall(data)
            data = file.read(1000)

    print("FIle sent successfully.")
    client_socket.close()

start_client()
