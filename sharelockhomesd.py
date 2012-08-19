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
    logFile = log(filePath='sharelockhomes.log', writeToFile=True)
    parameter = basic.getParameter(sys.argv)

    try:
        configFilePath = parameter['config']
    except KeyError:
        configFilePath = 'sharelockhomes.conf'
    finally:
        configuration = basic.getConfigFromFile(logFile, configFilePath)

    logFile.writeToFile = configuration['logging']
    logFile.write('ShareLockHomes v' + VERSION + ' starting up')

    server = SockServer(ServerHandler, configuration, logFile)
    server.serve_forever()



    basic.quit(logFile, True)
    return 0



if __name__ == '__main__':
    main()

