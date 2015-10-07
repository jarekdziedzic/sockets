#! /usr/bin/env python

from socket import *

def create_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 1234))
    s.listen(1)
    conn, addr = s.accept()
    print 'Incoming connection'
    while 1:
        data = conn.recv(1024)
        if data == 'Goodbye':
            break
        print 'Received data: %r' % data

    conn.close()
    s.shutdown(2)
    s.close()
    print 'Server shutdown.'


if __name__ == '__main__':
    create_server()
