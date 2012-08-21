#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import os, time


LOGTAGS = {0: 'INFO:', 1: 'WARNING:', 2: 'ERROR:'}

class Log(object):
    def __init__(self, **keyWordArgs):
        try:
            self.filePath = keyWordArgs['filePath']
        except KeyError:
            self.filePath = 'log.log'
        try:
            self.writeToFile = keyWordArgs['writeToFile']
        except KeyError:
            self.writeToFile = False
        if self.writeToFile == True:
            self.activateFileMode(self.filePath)
            self.write(LOGTAGS[0],'Use "' + self.filePath + '" as logfile.')


    def write(self, *lineParts):
        line = " ".join(lineParts)
        dateTimeStamp = self.nowDateTimeStamp()
        logLine = self.makeLogLine(dateTimeStamp, line)
        if self.writeToFile == True:
            self.fileBuffer.write(logLine)
            self.fileBuffer.flush()
        print logLine.replace(os.linesep,'')
        return True

  
    def writeConsoleOnly(self, *lineParts):
        line = " ".join(lineParts)
        dateTimeStamp = self.nowDateTimeStamp()
        logLine = self.makeLogLine(dateTimeStamp, line)
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


    def activateFileMode(self, filePath):
        self.writeToFile = True		
        self.filePath = os.path.abspath(filePath)
        self.fileBuffer = self.openLogFile(filePath)


    def openLogFile(self, filePath):
        try:
            return open(filePath,'a')
        except IOError:
            self.writeConsoleOnly(LOGTAGS[1],'Permission denied for logfile "' + filePath + '". Use "/tmp/log.log".')
            return open('/tmp/log.log','a')
            
LOGGER = Log()
