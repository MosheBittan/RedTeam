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



r1=threading.Thread(target=server,args=("192.168.88.146",1000))
r1.start()
r1=threading.Thread(target=server,args=("192.168.88.146",1001))
r1.start()
r1=threading.Thread(target=server,args=("192.168.88.146",1002))
r1.start()
