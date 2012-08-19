#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from lib.settings import *
from lib.logging import log
import sys, json
import lib.basic as basic


def main():
    parameter = basic.getParameter(sys.argv)


    try:
        logFilePath = parameter['log']
        forceLoggingToFile = True
    except KeyError:
        logFilePath = 'sharelockhomes.log'
        forceLoggingToFile = False
    finally:
        try:
            logging = log(filePath=logFilePath, writeToFile=forceLoggingToFile)
        except IOError:
            logging = log(filePath='/tmp/sharelockhomes.log', writeToFile=forceLoggingToFile)


    try:
        configFilePath = parameter['config']
    except KeyError:
        configFilePath = 'sharelockhomes.conf'
    finally:
        configuration = basic.getConfigFromFile(configFilePath)
        if configuration == {}:
            configuration = DEFAULTCONFIG
            logging.write(LOGTAGS[1]+'Configfile "' + configFilePath + '" does not exists or is not a valid json file! Will use defaults.')


    if forceLoggingToFile == False:
        if configuration['logging'] == True:
            logging.writeToFile = True
            logging.activate()

    logging.write('ShareLockHomes v' + VERSION + ' starting up')

    basic.quit(True)
    return 0







if __name__ == '__main__':
    main()

