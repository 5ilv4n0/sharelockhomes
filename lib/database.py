#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

from log import LOGGER
import log

import os


class Share(object):
    def __init__(self, filePath, **information):
        self.lastChange = None
        self.information = information
        self.filePath = os.path.abspath(filePath)
        self.fileSize = os.path.getsize(self.filePath)
        self.allowedStations = []
        information['filePath'] = self.filePath
        information['fileSize'] = self.fileSize
        information['allowedStations'] = self.allowedStations


    def allowStation(self, stationIdentifier):
        LOGGER.write(log.LOGTAGS[0],'Allow Station "'+ stationIdentifier +'"', 'to read "' + self.filePath + '"')
        if stationIdentifier in self.allowedStations: 
            LOGGER.write(log.LOGTAGS[1],'Station "'+ stationIdentifier +'"', 'already allowed.')
            self.lastChange = False
            return False
        self.allowedStations.append(stationIdentifier)
        self.updateInformation('allowedStations', self.allowedStations)
        self.lastChange = True
        return True


    def denyStation(self, stationIdentifier):
        LOGGER.write(log.LOGTAGS[0],'Deny Station "'+ stationIdentifier +'"', 'to read "' + self.filePath + '"')
        if not stationIdentifier in self.allowedStations:
            LOGGER.write(log.LOGTAGS[1],'Station "'+ stationIdentifier +'"', 'already denied.')
            self.lastChange = False
            return False
        del self.allowedStations[self.getStationPosition(stationIdentifier)]
        self.updateInformation('allowedStations', self.allowedStations)
        self.lastChange = True
        return True
        

    def getStationPosition(self, stationIdentifier):
        for ID, station in enumerate(self.allowedStations):
            if station == stationIdentifier:
                return ID
        return False


    def updateInformation(self, key, value):
        self.information[key] = value


    def wasSuccessful(self):
        return self.lastChange
