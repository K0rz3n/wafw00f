#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wangfangG01 (gongan Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'legendsec http proxy')),
        self.matchContent(r'<h1 class="text_404">403</h1>'),
        
    ]
    if all(i for i in schemes):
        return True
    return False