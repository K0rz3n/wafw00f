#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'leichi (chaitin Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<!-- event_id:(.*?)-->'),
        
    ]
    if any(i for i in schemes):
        return True
    return False