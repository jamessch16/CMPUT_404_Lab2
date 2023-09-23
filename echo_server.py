import socket
from threading import Thread

BUFFER_SIZE = 4096
HOST = "127.0.0.1" # localhost in ipv4
PORT = 8080 # an alternative HTTP port. we use this to listen for connections while we send on 80.

"""
Server to echo any requests that it recieves to www.google.com
"""
def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        request = b""

        # echo any data recieved back to the client until the socket is closed
        data = conn.recv(BUFFER_SIZE)
        while data:
            print(data)
            conn.sendall(data)
            data = conn.recv(BUFFER_SIZE)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # open socket with ipv4, tcp
        # set up socket
        s.bind((HOST, PORT)) # bind ip and port to socket

        # socket.SO_RESUEADDR is a flag that allows us to bind TODO
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        
        # wait for connection
        s.listen() # makes the socket a server socket
        conn, addr = s.accept() # waits for a connection and accepts it. conn = connected local socket, addr = return address
        handle_connection(conn, addr)

def start_threaded_server():
    pass

if __name__ == "__main__":
    start_server()
    #start_threaded_server()
