#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.basic import Basic
from lib.settings import *
from lib.logging import log
import sys, json


def main():
    basic = Basic(sys.argv)
    print basic.configuration

    #if forceLoggingToFile == False:
    #    if configuration['logging'] == True:
    #        logging.writeToFile = True
    #        logging.activate()

    #logging.write('ShareLockHomes v' + VERSION + ' starting up')

    basic.quit(True)
    return 0







if __name__ == '__main__':
    main()

