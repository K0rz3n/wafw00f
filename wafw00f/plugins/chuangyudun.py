#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'chuangyudun (zhidaochuangyu Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<span class="r-tip01"><%= error_403 %>'),
        self.matchContent(r"'hacker';"),
        self.matchContent(r'<center>client: (.*?), server: (.*?), time: (.*?)</center>'),
  
    ]
    if all(i for i in schemes):
        return True
    return False