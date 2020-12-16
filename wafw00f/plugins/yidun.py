#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'yidun (yunyi Technologies)'


def is_waf(self):
    schemes = [

    	self.matchHeader(('X-Protected-By', 'YunYiSec')),
    	self.matchHeader(('Server', 'YiDun/(.*?)')),
        self.matchContent(r'<h1>An Error Was Encountered</h1>'),
        self.matchContent(r'<p>The URI you submitted has disallowed characters.</p>'),
    ]
    if all(i for i in schemes):
        return True
    return False