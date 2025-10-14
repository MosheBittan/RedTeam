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
PORT_LIST = [80,1000,1001,1002]
threads = []

for PORT in PORT_LIST:
      t=threading.Thread(target=server,args=(ADDRESS,PORT))
      t.start()
      threads.append(t)

for t in threads:
     t.join()
