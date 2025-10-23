import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

print("Connected to server. Type 'exit' to quit.")

while True:
    # Send message to server
    client_msg = input("You: ")
    client_socket.sendall(client_msg.encode())

    if client_msg.lower() == 'exit':
        print("Chat ended.")
        break

    # Receive response
    server_msg = client_socket.recv(1024).decode()
    if server_msg.lower() == 'exit':
        print("Server ended the chat.")
        break
    print(f"Server: {server_msg}")

client_socket.close()