#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import lib.settings as settings
import lib.basic as basic
import lib.log as log

import sys, json, threading
from lib.connection import SockServer, ServerHandler, ClientHandler






def main():
    logging, configuration = basic.initiateLogAndConfig()
    logging.write(log.LOGTAGS[0] + 'ShareLockHomes V' + settings.VERSION + ' starting up...')


    server = SockServer(ServerHandler, configuration.get()['server'], logging)
    cserver = SockServer(ClientHandler, configuration.get()['client'], logging)
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
        basic.quit(False, log=logging, logTag=0, message='Exiting by user.')
        
    return 0



if __name__ == '__main__':
    main()
    basic.quit(log=logging)







