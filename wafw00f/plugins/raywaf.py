#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'raywaf (shengbang Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('DrivedBy', 'WAF-Engine/(.*?)')),
        
    ]
    if any(i for i in schemes):
        return True
    return False