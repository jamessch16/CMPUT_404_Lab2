import socket
from threading import Thread

BUFFER_SIZE = 4096
HOST = "127.0.0.1" # localhost in ipv4
PORT = 8080

"""
Server to echo any requests that it recieves to www.google.com
"""
def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        request = b""

        # read in data from the socket until closed
        data = conn.recv(BUFFER_SIZE)
        while data:
            print(data)
            request += data
            data = conn.recv(BUFFER_SIZE)

        # send data to google and return response through the client connection
        response = send_request("www.google.com", 80, request)
        print(response)
        conn.sendall(response)

def send_request(host, port, request):
    # open socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # ipv4, tcp
        s.connect((host, port))

        # send GET
        s.send(request)
        s.shutdown(socket.SHUT_WR)

        # recieve response
        data = s.recv(BUFFER_SIZE)
        result = b"" + data
        while len(data) > 0:
            data = s.recv(BUFFER_SIZE)
            result += data

        return result

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # open socket with ipv4, tcp
        # set up socket
        s.bind((HOST, PORT)) # bind ip and port to socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TODO EXPLAIN
        
        # wait for connection
        s.listen() # listen for connections
        conn, addr = s.accept()
        handle_connection(conn, addr)

# unthreaded server loop
#def start_server():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # open socket with ipv4, tcp
#        # set up socket
#        s.bind((HOST, PORT)) # bind ip and port to socket
#        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TODO EXPLAIN
#        
#        # wait for connection
#        s.listen() # listen for connections
#        conn, addr = s.accept()
#        handle_connection(conn, addr)

if __name__ == "__main__":
    start_server()
    #start_threaded_server()
