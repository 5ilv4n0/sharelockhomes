#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import json, sys, os
from settings import *

class Basic(object):
    def __init__(self, argv, logging):
        self.configuration = {}
        self.parameters = {}
        self.logFilePath = ''
        self.logging = logging

        self.getParameters(argv)
        self.getConfig()

    def quit(self, noError=True):
        if noError == False:
            self.logging.write('Exiting with error')
            sys.exit(1)
        self.logging.write('Exiting without error')
        sys.exit()

    def isJsonFile(self, filePath):
        with open(filePath, 'r') as f:
            try:
                json.load(f)
                return True
            except ValueError:
                return False

    def getParameters(self, argv):
        argv = argv[1:]
        options = []
        arguments = []
        for arg in argv:
            if arg[0] == '-':
                options.append(arg)
            else:
                arguments.append(arg)
        if len(options) != len(arguments):
            print 'SYNTAX ERROR'
            return {}
        for ID in xrange(len(options)):
            self.parameters[options[ID].replace('--','')] = arguments[ID]

    def getConfigFromFile(self, path):
        if not os.path.isfile(path):
            return {}
        if not self.isJsonFile(path):
            return {}
        with open(path, 'r') as f:
            self.configuration = json.load(f)

    def getConfig(self):
        try:
            self.logFilePath = self.parameters['log']
        except KeyError:
            self.logFilePath = 'sharelockhomes.log'

        try:
            self.getConfigFromFile(self.parameters['config'])
        except KeyError:
            self.getConfigFromFile('sharelockhomes.conf')

        if self.configuration == {}:
            self.configuration = DEFAULTCONFIG
