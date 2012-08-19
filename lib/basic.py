#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import json, sys, os


def quit(logFile, noError=True):
    if noError == False:
        logFile.write('abort with errors!')
        sys.exit(1)
    sys.exit()



def isJsonFile(filePath):
    with open(filePath, 'r') as f:
        try:
            json.load(f)
            return True
        except ValueError:
            return False


def getParameter(argv):
    argv = argv[1:]
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


def getConfigFromFile(logFile, configFilePath):
    noErrors = True
    if not os.path.isfile(configFilePath):
        logFile.write('config "' + configFilePath + '" do not exists!')
        quit(logFile, False)
    with open(configFilePath, 'r') as f:
        if not isJsonFile(configFilePath):
            logFile.write('config "' + configFilePath + '" not valid!')
            quit(logFile, False)
        configuration = json.load(f)
        return configuration
