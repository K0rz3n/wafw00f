#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'shyundun (shanghaiyundun Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WAF/(.*?)')),
        self.matchContent(r'<div class="err-tips-en">Blocked by Cloud WAF'),
        self.matchStatus(461)
    ]
    if all(i for i in schemes):
        return True
    return False