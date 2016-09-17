#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2016 Matt Nordhoff <mnordhoff@mattnordhoff.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
./convert-us.py <firefox-expiration-us.csv >firefox-expiration.csv
./convert-us.py <firefox-esr-expiration-us.csv >firefox-esr-expiration.csv
./convert-us.py <tor-browser-expiration-us.csv >tor-browser-expiration.csv
"""

from __future__ import division

import csv
import datetime
import os
import sys

def main():
    c_in = csv.DictReader(sys.stdin)
    c_out = csv.writer(sys.stdout, lineterminator=os.linesep)
    c_out.writerow(['version', 'expiration_s', 'expiration_us', 'expiration_iso'])
    for row in c_in:
        version = row['version']
        expiration_us = row['expiration_us']
        expiration_s = int(expiration_us) / 10**6
        expiration_iso = datetime.datetime.utcfromtimestamp(expiration_s).isoformat() + 'Z'
        c_out.writerow([version, expiration_s, expiration_us, expiration_iso])

if __name__ == '__main__':
    main()
