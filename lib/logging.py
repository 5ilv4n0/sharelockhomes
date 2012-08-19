#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

import os, time

class log(object):
    def __init__(self, path='logfile.log', enabled=True):
        self.filePath = os.path.abspath(path)
        self.fileBuffer = open(self.filePath,'a')
        self.enabled = enabled
		
	def write(self, line):
		if self.enabled:
			dateTimeStamp = self.nowDateTimeStamp()
			logLine = self.makeLogLine(dateTimeStamp, line)
			self.fileBuffer.write(logLine)
			self.fileBuffer.flush()
		return self.enabled
				
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
		self.fileBuffer.close()
