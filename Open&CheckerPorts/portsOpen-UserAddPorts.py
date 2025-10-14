import socket
import threading


def server(HOST: str,PORT: int):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen(1) # 1 - mean only one connection
        try:
            # Handle one connection
            communication_socket , clientIP = server.accept()
            print(f"New Connection from: {clientIP} to Port: {PORT}")
        except:
            print("\nShutting down server...")
        finally:
            server.close()
            print("Socket is close!")

hostname = socket.gethostname()
ADDRESS = socket.gethostbyname(hostname)
PORT_LIST = input("Which ports do you want me to open? (space-separated): ")
PORT_LIST = [int(port) for port in PORT_LIST.split()]
print(PORT_LIST)
threads = []

for PORT in PORT_LIST:
      t=threading.Thread(target=server,args=(ADDRESS,PORT))
      t.start()
      threads.append(t)

for t in threads:
     t.join()
