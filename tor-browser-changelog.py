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
./tor-browser-changelog.py <ChangeLog.txt >tor-browser-releases.csv
"""

import csv
import os
import sys

_months = {
    'Jan': '1',
    'January': '1',
    'Feb': '2',
    'February': '2',
    'Mar': '3',
    'March': '3',
    'Apr': '4',
    'April': '4',
    'May': '5',
    'Jun': '6',
    'June': '6',
    'Jul': '7',
    'July': '7',
    'Aug': '8',
    'August': '8',
    'Sep': '9',
    'September': '9',
    'Oct': '10',
    'October': '10',
    'Nov': '11',
    'November': '11',
    'Dec': '12',
    'December': '12',
}

def main():
    changelog = sys.stdin.readlines()
    changelog.reverse()
    c_out = csv.writer(sys.stdout, lineterminator=os.linesep)
    c_out.writerow(['version', 'firefox_version', 'date'])
    for line in changelog:
        if line.startswith('   * Update Firefox to '):
            firefox_version = line[len('   * Update Firefox to '):].rstrip('\r\n')
        elif line.startswith('Tor Browser '):
            split = line.split()
            version = split[2]
            if not version.startswith(('4', '5', '6')):
                continue
            if version.startswith('4.0'):
                continue
            version = version.replace('-alpha-', 'a')
            month = _months[split[4]]
            if len(month) == 1:
                month = '0' + month
            day = split[5]
            if len(day) == 1:
                day = '0' + day
            if version == '6.0.5':
                year = '2016'
            else:
                year = split[6]
            date = '%s-%s-%s' % (year, month, day)
            c_out.writerow([version, firefox_version, date])

if __name__ == '__main__':
    main()
