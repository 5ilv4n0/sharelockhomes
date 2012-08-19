#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import os, time

class log(object):
    def __init__(self, **keyWordArgs):
        try:
            self.filePath = keyWordArgs['filePath']
        except KeyError:
            self.filePath = 'log.log'
        try:
            self.writeToFile = keyWordArgs['writeToFile']
        except KeyError:
            self.writeToFile = False
        self.filePath = os.path.abspath(self.filePath)
        if self.writeToFile == True:
            self.fileBuffer = open(self.filePath,'a')


    def write(self, line):
        dateTimeStamp = self.nowDateTimeStamp()
        logLine = self.makeLogLine(dateTimeStamp, line)
        if self.writeToFile:
            self.fileBuffer.write(logLine)
            self.fileBuffer.flush()
        print logLine.replace(os.linesep,'')
        return True


    def nowDateTimeStamp(self):
        dateTimeStamp = time.strftime("[%d.%m.%Y - %H:%M:%S]", time.localtime())
        return dateTimeStamp


    def makeLogLine(self, dateTimeStamp, line):
        logLine = []
        logLine.append(dateTimeStamp)
        logLine.append('->')
        logLine.append(line)
        logLine.append(os.linesep)
        return ' '.join(logLine)


    def __del__(self):
        if self.writeToFile == True:
            self.fileBuffer.close()
