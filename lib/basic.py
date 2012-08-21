#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from log import LOGGER

import log
import settings
import json, sys, os


def initiateLogAndConfig():
    parameters = getParameters()
    try:
        configFilePath = parameters['config']
    except KeyError:
        configFilePath = 'sharelockhomes.conf'
    try:
        logFilePath = parameters['log']
        LOGGER.activateFileMode(logFilePath)
    except KeyError:
        pass      
    LOGGER.write(log.LOGTAGS[0],'Try to use config from file "' + configFilePath + '"')
    configuration = config(configFilePath)
    return configuration 


def getParameters():
    argv = sys.argv[1:]
    options = []
    arguments = []
    parameters = {}
    for arg in argv:
        if arg[0] == '-':
            options.append(arg)
        else:
            arguments.append(arg)
        
    if len(options) != len(arguments):
        quit(noError=False, logTag=2, message='Syntaxerror in parameters!')
    for ID in xrange(len(options)):
        parameters[options[ID].replace('--','')] = arguments[ID]
    return parameters


def quit(noError=True, **keyWordArgs):
    try: 
        logTagID = keyWordArgs['logTag']
    except KeyError:
        logTagID = 2
    try: 
        message = keyWordArgs['message']
    except KeyError:
        message = 'unknown error!'       

    if noError == False:
        LOGGER.write(log.LOGTAGS[logTagID],message)
        sys.exit(1)
    LOGGER.write(log.LOGTAGS[0],'Exiting without error')
    sys.exit()


def isJsonFile(filePath):
    with open(filePath, 'r') as f:
        try:
            json.load(f)
            return True
        except ValueError:
            return False





class config(object):
    def __init__(self, filePath, **keyWordArgs):
        self.filePath = filePath
        self.configuration = self.getConfigFromFile(filePath)
        if self.configuration == {}:
            self.configuration = settings.DEFAULTCONFIG
            self.write()


    def getConfigFromFile(self, filePath):
        if not os.path.isfile(filePath):
            LOGGER.write(log.LOGTAGS[1],'Configfile "' + filePath + '" does not exists! Will use default config.')
            return {}
        if not isJsonFile(filePath):
            LOGGER.write(log.LOGTAGS[1],'Configfile "' + filePath + '" is no valid json file! Will use default config.')
            return {}
        with open(filePath, 'r') as f:
            LOGGER.write(log.LOGTAGS[0],'Configfile "' + filePath + '" is valid.')
            return json.load(f)


    def write(self):
        with open(self.filePath, 'w') as f:
            jsonEncoded = json.dumps(self.configuration)
            f.write(jsonEncoded)
            f.flush()
            f.close()
            LOGGER.write(log.LOGTAGS[0],'Default config is written to "' + self.filePath + '"')           


    def get(self):
        return self.configuration


    def set(self, configuration):
        self.configuration = configuration


    def isLoggingToFileEnabled(self):
        try:
            return self.configuration['logging']
        except KeyError:
            return False


    def getLogFilePath(self):
        try:
            return self.configuration['logFilePath']
        except KeyError:
            return 'log.log'




