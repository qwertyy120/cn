import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(1)

print("Server is listening on port 8888...")
conn, addr = server_socket.accept()
print(f"Connected to client at {addr}")

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == 'exit':
        print("Client ended the chat.")
        break
    print(f"Client: {client_msg}")

    # Send response
    server_msg = input("You: ")
    conn.sendall(server_msg.encode())

    if server_msg.lower() == 'exit':
        print("Chat ended.")
        break

conn.close()