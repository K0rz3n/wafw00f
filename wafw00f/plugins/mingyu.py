#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'mingyu (anheng Technologies)'


def is_waf(self):
    schemes = [
        self.matchStatus(400),
        self.matchContent(r'<title>Error 400 —— (.*?)'),
        self.matchContent(r'<strong>400'),
    ]
    if all(i for i in schemes):
        return True
    return False