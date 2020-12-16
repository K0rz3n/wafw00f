#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Minimum (Minimum strategy)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Access Denied'),
        self.matchContent(r'Request Denied'),
        self.matchContent(r'访问禁止'),
        self.matchContent(r'检测到可疑访问'),
        self.matchStatus(403),

    ]
    if any(i for i in schemes):
        return True
    return False