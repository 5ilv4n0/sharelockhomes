#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.Basic import Basic
from lib.Log import Log
from lib.settings import *
import sys, json


def main():
    logging = Log(filepath='sharelockhomes.log', writeToFile='False')
    logging.write('ShareLockHomes v' + VERSION + ' starting up')
    basic = Basic(sys.argv, logging)

    basic.quit(True)
    return 0







if __name__ == '__main__':
    main()

