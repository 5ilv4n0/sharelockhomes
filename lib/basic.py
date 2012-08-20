#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

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
        logging = log.Log(filePath=logFilePath, writeToFile=True)
    except KeyError:
        logging = log.Log()      
    logging.write(log.LOGTAGS[0] + 'Try to use config from file "' + configFilePath + '"')
    configuration = config(configFilePath, log=logging)
    return logging, configuration 


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
        print 'SYNTAX ERROR'
        return {}
    for ID in xrange(len(options)):
        parameters[options[ID].replace('--','')] = arguments[ID]
    return parameters


def quit(noError=True, **keyWordArgs):
    try:
        logging = keyWordArgs['log']
    except KeyError:
        logging = False
    try: 
        logTagID = keyWordArgs['logTag']
    except KeyError:
        logTagID = 1
    try: 
        message = keyWordArgs['message']
    except KeyError:
        message = 'unknown error!'       
    
        
    if noError == False:
        if not logging == False:
            logging.write(log.LOGTAGS[logTagID] + message)
        sys.exit(1)
    if not log == False:
        logging.write(log.LOGTAGS[0] + 'Exiting without error')
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
        try:
            self.log = keyWordArgs['log']
        except KeyError:
            self.log = False
        self.filePath = filePath
        self.configuration = self.getConfigFromFile(filePath)
        if self.configuration == {}:
            self.configuration = settings.DEFAULTCONFIG
            self.write()
        if not self.log == False:
            if self.log.writeToFile == False:
                if self.isLoggingToFileEnabled(): 
                    logFilePath = self.getLogFilePath()
                    self.log.activateFileMode(logFilePath)


    def getConfigFromFile(self, filePath):
        if not os.path.isfile(filePath):
            if not self.log == False:
                self.log.write(log.LOGTAGS[1] + 'Configfile "' + filePath + '" does not exists! Will use default config.')
            return {}
        if not isJsonFile(filePath):
            if not self.log == False:
                self.log.write(log.LOGTAGS[1] + 'Configfile "' + filePath + '" is no valid json file! Will use default config.')
            return {}
        with open(filePath, 'r') as f:
            if not self.log == False:
                self.log.write(log.LOGTAGS[0] + 'Configfile "' + filePath + '" is valid.')
            return json.load(f)


    def write(self):
        with open(self.filePath, 'w') as f:
            jsonEncoded = json.dumps(self.configuration)
            f.write(jsonEncoded)
            f.flush()
            f.close()
            if not self.log == False:
                self.log.write(log.LOGTAGS[0] + 'Config written to "' + self.filePath + '"')           


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




