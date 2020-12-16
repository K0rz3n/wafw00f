#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'aliyun (alibaba Technologies)'


def is_waf(self):
    schemes = [
        
        self.matchContent(r'g\.alicdn\.com/sd/punish/waf_block\.html'),
        self.matchContent(r'您的访问被阻断'),
        self.matchContent(r'detected malicious traffic from your network'),
        self.matchContent(r'/waf\.123\.123'),
        self.matchContent(r'应用防火墙'),
        self.matchContent(r'errors\.aliyun\.com'),


    ]
    if any(i for i in schemes):
        return True
    return False