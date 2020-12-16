#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'TencentCloud (Tencent Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>501 Not Implemented'),
        self.matchStatus(501)

    ]
    if all(i for i in schemes):
        return True
    return False