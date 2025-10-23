import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12346))
print("Connected to the server.")

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'bye':
        break
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()