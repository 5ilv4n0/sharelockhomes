#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.settings import *
from lib.logging import log
from lib.Sock import SockServer, ServerHandler
import sys, json
import lib.basic as basic






def main():
    logFile             = log('sharelockhomes.log', True)
    parameter           = basic.getParameter(sys.argv)
    configuration       = basic.getConfigFromFile(logFile, parameter['config'])
    logFile.enabled     = configuration['logging']
    logFile.write('ShareLockHomes v' + VERSION + ' starting up')

    server = SockServer(ServerHandler, configuration, logFile)
    server.serve_forever()


    basic.quit(logFile, True)
    return 0



if __name__ == '__main__':
    main()

