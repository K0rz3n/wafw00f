#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wangsu (wangsu Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WAF/(.*?)')),
        self.matchContent(r'<img src="https://blocksrc\.haplat\.net/waf_forbidden_file'),
        
    ]
    if all(i for i in schemes):
        return True
    return False