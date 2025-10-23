import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8888))

print("UDP Server is ready to chat... (type 'exit' to quit)")

while True:
    # Receive message
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Client: {message}")

    if message.lower() == 'exit':
        print("Client ended the chat.")
        break

    # Send response
    reply = input("You: ")
    server_socket.sendto(reply.encode(), client_address)

    if reply.lower() == 'exit':
        print("Chat ended.")
        break

server_socket.close()
