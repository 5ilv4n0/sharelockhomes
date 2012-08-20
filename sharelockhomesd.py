#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.Basic import Basic
from lib.Log import Log
from lib.Sock import SockServer, ServerHandler, ClientHandler
from lib.settings import *
import sys, json, threading


def main():
    logging = Log(filepath='sharelockhomes.log', writeToFile='False')
    logging.write('ShareLockHomes v' + VERSION + ' starting up')
    basic = Basic(sys.argv, logging)

    server = SockServer(ServerHandler, basic.configuration['server'], logging)
    cserver = SockServer(ClientHandler, basic.configuration['client'], logging)

    threads = {}
    threads['server'] = threading.Thread(target=server.serve_forever)
    threads['cserver'] = threading.Thread(target=cserver.serve_forever)

    threads['server'].daemon = True
    threads['cserver'].daemon = True

    threads['server'].start()
    threads['cserver'].start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        basic.quit()

    return 0






if __name__ == '__main__':
    main()

