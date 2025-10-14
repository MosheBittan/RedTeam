import threading
import time
import socket


def portCheck(HOST,PORT):
    try:
        #First socket - Module , Second socket - Class , we read socket.AF_INET - socket (Module importat) than the file name .
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((HOST,PORT)) # Only if this connected then will over to next line - this mean port open , if not will raise exception and go to print Close port
        print(f"Address: {HOST}\tPORT: {PORT}\tOPEN")
    except ConnectionRefusedError:
        print(f"Address: {HOST}\tPORT: {PORT}\tCLOSE")
    finally:
        # finally always accure , this close the connection
        client.close()

#def socketCon(HOST,PORT):
hostname = socket.gethostname() 
ADDRESS = socket.gethostbyname(hostname)
#User will provide the ports number and space between them
PORT_LIST = input("Which ports do you want me to check? (space-separated): ")
PORT_LIST = [int(port) for port in PORT_LIST.split()]

threads = [] #create new threads list that will have pointer to them for check keep alive or status and more ...
for PORT in PORT_LIST:
    t=threading.Thread(target=portCheck,args=(ADDRESS,PORT),daemon=False)
    t.start()
    threads.append(t)


# later: coordinate shutdown / wait for completion
for t in threads:
    t.join()
