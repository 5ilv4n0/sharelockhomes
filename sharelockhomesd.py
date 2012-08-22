#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.log import LOGGER

import lib.settings as settings
import lib.basic as basic
import lib.log as log
import lib.connection as connection

import sys, json, threading




configuration = basic.initiateShareLockHomes()
LOGGER.write(log.LOGTAGS[0],'ShareLockHomes V'+settings.VERSION,'starting up...')
#################################################################
server = connection.SockServer(connection.ServerHandler, configuration.get()['server'])
cserver = connection.SockServer(connection.ClientHandler, configuration.get()['client'])
threads = {}
threads['server'] = threading.Thread(target=server.serve_forever)
threads['cserver'] = threading.Thread(target=cserver.serve_forever)
threads['server'].daemon = True
threads['cserver'].daemon = True
threads['server'].start()
threads['cserver'].start()
################################################################# 
basic.waitForCtrlC()
basic.quit()








