import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialise a socket (af-net -> p)
    s.connect((host,port)) # connect to google
    s.send(request) #request google homepage
    s.shutdown(socket.SHUT_WR) # I am done sending the request
    result = s.recv(BYTES_TO_READ) # continuuiously receiving the response
    while(len(result)>0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    s.close()

#get("www.google.ca", 80)
get("localhost", 8080)