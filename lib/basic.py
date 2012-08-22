#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from log import LOGGER

import log
import settings
import json, sys, os, re


def printHelp():
    top = 'ShareLockHomes Version '+settings.VERSION+' Help'
    print 'ShareLockHomes Version',settings.VERSION,'Help'
    print '-'*len(top)
    print 'Parameters:'
    print '   --help'
    print '   --config <file>'
    print '   --log <file>'
    print '   --db <dir>'
    print '-'*len(top)


def createDirectories(*dirs):
    for path in dirs:
        LOGGER.write(log.LOGTAGS[0],'Try to create directory "' + path + '"')
        try:
            os.makedirs(path, 0664)
            LOGGER.write(log.LOGTAGS[0],'Directory "' + path + '" created.')
        except OSError as error:
            errorCode, errorMessage = getOSErrorMessage(error)
            logTagID = errorCodeToLogTagID(errorCode)
            LOGGER.write(log.LOGTAGS[logTagID],'Not able to create directory "' + path + '":',errorMessage+'!')


def getOSErrorMessage(error):
    errorRegex = re.match(r'\[.+ (.+)\] (.+):.+',str(error))
    return int(errorRegex.groups()[0]), errorRegex.groups()[1] 	


def errorCodeToLogTagID(errorCode):
    if errorCode == 17:
        logTagID = 0
    else:
        logTagID = 2
    return 	logTagID


def initiateShareLockHomes():
    configuration = initiateParameterAndConfig()
    return configuration


def initiateParameterAndConfig():
    parameters = getParameters()
    configFilePath = getParameter('config', 'sharelockhomes.conf')
    logFilePath = getParameter('log')
    if not logFilePath == False:
        LOGGER.activateFileMode(logFilePath)
    LOGGER.write(log.LOGTAGS[0],'Try to use config from file "' + configFilePath + '"')
    configuration = Config(configFilePath)
    logging = getConfigValue(configuration, 'logging')
    logFilePath = getConfigValue(configuration, 'logFilePath', 'sharelockhomes.log')
    if logging == True and LOGGER.writeToFile == False:
        LOGGER.activateFileMode(logFilePath)
    dbPathParameter = getParameter('db')
    dbPathConfig = getConfigValue(configuration, 'databasePath','db')
    dbPath = useParameterIfExistsElseUseConfig(dbPathParameter, dbPathConfig)
    createDirectories(dbPath)      
    return configuration 


def useParameterIfExistsElseUseConfig(parameter, config):
    if not parameter == False:
        return parameter
    else:
        return config


def getConfigValue(configuration, value, defaultValue=False):
    try:
        return configuration.get()[value]
    except KeyError:
        return defaultValue   


def getParameter(parameter, defaultValue=False):
    parameters = getParameters()
    try:
        return parameters[parameter]
    except KeyError:
        return defaultValue   


def getParameters():
    if '--help' in sys.argv:
        printHelp()
        sys.exit()
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


def waitForCtrlC():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        LOGGER.write(log.LOGTAGS[0],'ShareLockHomes','shutting down...')
        quit(False, logTag=0, message='Exiting by user.')


def isJsonFile(filePath):
    with open(filePath, 'r') as f:
        try:
            json.load(f)
            return True
        except ValueError:
            return False





class Config(object):
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
            jsonEncoded = json.dumps(self.configuration, sort_keys=True, indent=4)
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




