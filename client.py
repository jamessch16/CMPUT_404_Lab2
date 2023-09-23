import socket

BUFFER_SIZE = 4096

def get_request(host, port):
    # open socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # ipv4, tcp
        s.connect((host, port))

        # send GET
        request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"  # note: HTTP header is GET -> root -> protocol -> hostname on newline
        s.send(request)
        s.shutdown(socket.SHUT_WR) # note: the SHUT_WR parameter specifies that further sending (ie, writing) has been disabled. To disable recieveing, SHUT_RD (ie, reading), and SHUT_RDWR for both.
                                   # note: this sends empty string to reciever. does not specify the shutdown type. programs should handle the case where it was fully shutdown. this can also happen if internet cuts out.

        # recieve response
        result = s.recv(BUFFER_SIZE)
        while len(result) > 0:
            print(result)
            result = s.recv(BUFFER_SIZE)

if __name__ == "__main__":
    #get_request("www.google.com", 80) # for part 1 of assignment. note: for some reason this doesn't work with port 80. why?
    get_request("localhost", 8080) # address/port for echo_server
