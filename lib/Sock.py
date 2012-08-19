#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import SocketServer, socket
from OpenSSL import SSL

class SockServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, RequestHandlerClass, configuration, logging):
        listenaddress = configuration['server']['listen']
        listenport    = configuration['server']['port']
        x509cert      = configuration['server']['cert']
        x509key       = configuration['server']['key']

        SocketServer.BaseServer.__init__(self, (listenaddress, listenport),
                                         RequestHandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.use_certificate_file(x509cert)
        ctx.use_privatekey_file(x509key)

        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
                                                        self.socket_type))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_bind()
        self.server_activate()

class ServerHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        while self.data:
            print '{} wrote: '.format(self.client_address[0]) + self.data
            self.data = self.request.recv(1024).strip()

    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)
