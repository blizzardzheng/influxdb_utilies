#!/usr/bin/env python
#_*_ encoding: utf-8 _*_

from __future__ import division
import requests
import sys


url = 'http://localhost:8086/write?db=lighthouse'

num_lines = sum(1 for line in open('output', 'r'))

with open('output', 'r') as f:
    for i, line in enumerate(f):
        r = requests.post(url, data=line)
        sys.stdout.write("\r%d %d%%" % (i, i / num_lines * 100))
        sys.stdout.flush()
        if r.status_code is not 204:
            print i, r.status_code, r.reason

print
print 'done'
