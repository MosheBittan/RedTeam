import socket

HOST = '192.168.1.2'
PORT = 9091

PORT_LIST = [80,443,25,389]

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(3) # optional: 3-second timeout

try:
    client.connect((HOST,PORT))
    print(f"port: {PORT}     open")
except (socket.timeout, ConnectionRefusedError, OSError):
    print(f"port: {PORT}     close")
finally:
    client.close()