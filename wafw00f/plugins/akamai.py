#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Akamai (Akamai Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'GHost')),
        self.matchContent(r'<TITLE>Access Denied'),
    ]
    if all(i for i in schemes):
        return True
    return False