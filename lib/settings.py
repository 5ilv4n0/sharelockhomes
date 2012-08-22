#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

VERSION = '0.1a'
COPYRIGHT = '2012 Silvano Wegener & Daniel Henschel'

DEFAULTCONFIG = {
    'logging': False,
    'logFilePath': 'sharelockhomes.log',
    'databasePath': 'db',
    'server': {
        'cert': 'src/cert.pem',
        'key': 'src/key.pem',
        'listen': '0.0.0.0',
        'port': 10023
    },
    'client': {
        'cert': 'src/cert.pem',
        'key': 'src/key.pem',
        'listen': "0.0.0.0",
        'port': 10024
        }
}

