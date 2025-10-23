import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is ready to receive messages.")

while True:
    data, addr = server_socket.recvfrom(1024)
    msg = data.decode()
    if msg.lower() == 'bye':
        print("Client ended the chat.")
        break
    print("Client:", msg)
    reply = input("You: ")
    server_socket.sendto(reply.encode(), addr)

server_socket.close()
