import socket

HOST = '192.168.1.2'
PORT = 9093

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)


try:
    while True:
        communication_socket, address = server.accept()
        print(f"Connected to {address}")
        message = communication_socket.recv(1024).decode('utf-8')
        print(f"Message from client is : {message}")
        communication_socket.send(f"Got your messag! Thank you!".encode('utf-8'))
        communication_socket.close()
        print(f"Connection with {address} ended!")

except (KeyboardInterrupt,TimeoutError,ConnectionRefusedError):
    # Ctrl+C pressed — cleanup here
    print("\nReceived Ctrl+C, shutting down server...")
finally:
    server.close()
    print("Server socket closed. Exiting.")

