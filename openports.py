import socket

HOST = '192.168.1.2'
PORT_LIST = [9091,1500,999,8888]

for PORT in PORT_LIST:
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen(5)
        while True:
            communication_socket, address = server.accept()
            print(f"Connected to {address}")
            communication_socket.close()
            print(f"Connection with {address} ended!")
    except (KeyboardInterrupt,TimeoutError,ConnectionRefusedError):
        # Ctrl+C pressed — cleanup here
        print("\nReceived Ctrl+C, shutting down server...")
    finally:
        server.close()
        print("Server socket closed. Exiting.")

