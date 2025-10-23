import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8888)

print("Connected to UDP server. Type 'exit' to quit.")

while True:
    # Send message
    message = input("You: ")
    client_socket.sendto(message.encode(), server_address)

    if message.lower() == 'exit':
        print("Chat ended.")
        break

    # Receive response
    data, _ = client_socket.recvfrom(1024)
    reply = data.decode()
    print(f"Server: {reply}")

    if reply.lower() == 'exit':
        print("Server ended the chat.")
        break

client_socket.close()
