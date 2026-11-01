import socket
import threading

def monitor():
    server = socket.socket()
    server.bind(("127.0.0.1",9999))
    server.listen()

    print("IDS Started")

    while True:
        conn , addr = server.accept()
        print("Connection detected")
        conn.close()

threading.Thread(target = monitor , daemon = True).start()

client = socket.socket()
client.connect(("127.0.0.1",9999))
print("Connection successful")
client.close()
