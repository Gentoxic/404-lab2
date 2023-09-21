import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" # IP, LOCAL HOST
PORT = 8080

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Initialize the socket
        s.bind((HOST,PORT)) # Bind to IP and PORT
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen() # listen for incoming connections
        conn, addr = s.accept() # Conn = socket referrring to the client, addr - address of the client (IP, PORT)
        handle_connection(conn, addr) # send it a response.


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) # wait for a request, and when you get it, you receive it
            if not data: # if I receive an empty byte string --> b''
                break
            print(data)
            conn.sendall(data) # send it back to the client

# start multithreaded server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


#start_server()
start_threaded_server()