import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server_socket.bind(('localhost', 12346))
server_socket.listen(1)

print("Server is listening for connections...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'bye':
        print("Client ended the chat.")
        break
    print("Client:", msg)
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()