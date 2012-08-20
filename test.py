#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import socket, ssl

def main():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock1 = ssl.wrap_socket(s1, cert_reqs=ssl.CERT_NONE)
    ssl_sock2 = ssl.wrap_socket(s2, cert_reqs=ssl.CERT_NONE)
    ssl_sock1.connect(('127.0.0.1', 10023))
    ssl_sock2.connect(('127.0.0.1', 10024))
    print repr(ssl_sock1.getpeername())
    print repr(ssl_sock2.getpeername())
    print ssl_sock1.cipher()
    print ssl_sock2.cipher()
    for i in range(1, 10):
        print i
        ssl_sock1.send('lala' + str(i) + chr(13))
        ssl_sock2.send('lala' + str(i) + chr(13))
    ssl_sock1.close()
    ssl_sock2.close()

if __name__ == '__main__':
    main()
