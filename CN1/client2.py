import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

while True:
    message = input("You: ")
    client_socket.sendto(message.encode(), server_address)
    if message.lower() == 'bye':
        break
    data, _ = client_socket.recvfrom(1024)
    print("Server:", data.decode())

client_socket.close()