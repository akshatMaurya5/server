import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '0.0.0.0'  # Listen on all available network interfaces
server_port = 8080  # You can use any available port

server_socket.bind((server_host, server_port))
server_socket.listen(1)

print(f"Listening on {server_host}:{server_port}...")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    print(f"Received: {data.decode('utf-8')}")

client_socket.close()
server_socket.close()
