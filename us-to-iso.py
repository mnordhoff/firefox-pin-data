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

import csv
import datetime
import os
import sys

def main():
    cin = csv.reader(sys.stdin)
    cout = csv.writer(sys.stdout, lineterminator=os.linesep)
    cout.writerow(['version', 'expiration_us', 'expiration_iso'])
    it = iter(cin)
    it.next()
    for version, expiration_us in it:
        expiration_s = int(expiration_us) / 10**6
        expiration_iso = datetime.datetime.fromtimestamp(expiration_s).isoformat() + 'Z'
        cout.writerow([version, expiration_us, expiration_iso])

if __name__ == '__main__':
    main()
