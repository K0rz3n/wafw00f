#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Panyun (360 Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'panyun/(.*?)')),
        self.matchStatus(473)
        
    ]
    if all(i for i in schemes):
        return True
    return False