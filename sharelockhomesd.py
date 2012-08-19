#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.logging import log

# junk - muss in die config
logging = True







def main():
    logFile = log('sharelockhomes.log', logging)


    del logFile
    return 0

if __name__ == '__main__':
    main()

