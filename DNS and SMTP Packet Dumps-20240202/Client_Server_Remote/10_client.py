import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.8.119', 12345) ##Private ip of remote server

    client_socket.connect(server_address)
    with open('To send.pdf', 'rb') as file:
        data = file.read(1000)
        while data:
            client_socket.sendall(data)
            data = file.read(1000)

    print("FIle sent successfully.")
    client_socket.close()

if __name__ = "__main__":
    start_client()
