import socket

HOST = '192.168.1.2'
PORT_LIST = [9091,1500,999,3333]


for PORT in PORT_LIST:
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.settimeout(3) # optional: 3-second timeout
        client.connect((HOST,PORT))
        print(f"port: {PORT}\topen")
    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"port: {PORT}\tclose")
    finally:
        client.close()