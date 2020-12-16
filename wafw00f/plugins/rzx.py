#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RZX (RZX Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>Request Denied'),
        self.matchContent(r'RZX IT by'),
        self.matchContent(r'Web Page Blocked!'),
    ]
    if all(i for i in schemes):
        return True
    return False