#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ddun (ddun Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>D.*?_'),
        self.matchStatus(403)
    ]
    if all(i for i in schemes):
        return True
    return False