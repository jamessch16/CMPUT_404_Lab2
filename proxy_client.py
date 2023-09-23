import socket

BUFFER_SIZE = 4096

def get(host, port):
    # open socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # ipv4, tcp
        s.connect((host, port))

        # send GET
        request = b"GET / HTTP/1.1\n" + host.encode("utf-8") + b"\n\n"
        s.send(request)
        s.shutdown(socket.SHUT_WR) # note: the SHUT_WR parameter specifies that further sending (ie, writing) has been disabled. To disable recieveing, SHUT_RD (ie, reading), and SHUT_RDWR for both.
                                   # note: this sends empty string to reciever. does not specify the shutdown type. programs should handle the case where it was fully shutdown. this can also happen if internet cuts out.

        # recieve response
        recieved = s.recv(BUFFER_SIZE)
        result = b'' + recieved
        while len(recieved) > 0:
            recieved = s.recv(BUFFER_SIZE)
            result += recieved

        print(result)

if __name__ == "__main__":
    get("localhost", 8080) # address/port for echo_server
