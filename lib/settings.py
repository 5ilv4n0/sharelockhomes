#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Silvano Wegener & Daniel Henschel

VERSION = '0.1'
COPYRIGHT = '2012 Silvano Wegener & Daniel Henschel'

LOGTAGS = {0: 'INFO: ', 1: 'WARNING: ', 2: 'ERROR: '}

DEFAULTCONFIG = {
    'logging': False,
    'server': {
        'cert': 'cert.pem',
        'key': 'key.pem',
        'listen': '0.0.0.0',
        'port': 10023
    }
}

