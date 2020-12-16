#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'yxlink (yxlink Technologies)'


def is_waf(self):
    schemes = [
       
        self.matchContent(r'<TITLE>访问禁止'),
        self.matchContent(r'检测到可疑访问'),
    ]
    if all(i for i in schemes):
        return True
    return False