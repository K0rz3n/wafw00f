#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'baota (baota Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>宝塔网站防火墙'),
        self.matchContent(r'<li>您提交的内容包含危险的攻击请求'),
        self.matchContent(r'这是误报，请联系宝塔 <a href="http://www\.bt\.cn/bbs" target="_brank">'),
        
    ]
    if any(i for i in schemes):
        return True
    return False