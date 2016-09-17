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
./firefox-expirations-releases.py firefox-expiration.csv firefox-releases.csv >firefox-expiration-release-dates.csv
./firefox-expirations-releases.py firefox-esr-expiration.csv firefox-esr-releases.csv >firefox-esr-expiration-release-dates.csv
"""

from __future__ import division

import csv
import datetime
import itertools
import os
import sys

def main():
    fh_expirations = open(sys.argv[1], 'rb')
    fh_releases = open(sys.argv[2], 'rb')
    c_expirations = csv.reader(fh_expirations)
    c_releases = csv.reader(fh_releases)
    iter_c_expirations = iter(c_expirations)
    iter_c_releases = iter(c_releases)
    next(iter_c_expirations)
    next(iter_c_releases)
    c_out = csv.writer(sys.stdout, lineterminator=os.linesep)
    c_out.writerow(['version', 'release_date', 'expiration_date', 'expiration_days', 'previous_release_days'])
    previous_release_datetime = None
    for expiration, release in itertools.izip(iter_c_expirations, iter_c_releases):
        expiration_version, expiration_s, _, _ = expiration
        release_version, release_date = release
        if expiration_version != release_version:
            raise ValueError("%r != %r" % (expiration_version, release_version))
        expiration_datetime = datetime.datetime.utcfromtimestamp(float(expiration_s))
        expiration_date = expiration_datetime.strftime('%Y-%m-%d')
        release_datetime = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        expiration_window_timedelta = expiration_datetime - release_datetime
        expiration_window_s = expiration_window_timedelta.total_seconds() / 86400
        expiration_window_days = '{:.2f}'.format(expiration_window_s)
        if previous_release_datetime is None:
            release_window_days = 'none'
        else:
            release_window_timedelta = release_datetime - previous_release_datetime
            release_window_s = release_window_timedelta.total_seconds() / 86400
            release_window_days = '{:.2f}'.format(release_window_s)
        c_out.writerow([expiration_version, release_date, expiration_date, expiration_window_days, release_window_days])
        previous_release_datetime = release_datetime

if __name__ == '__main__':
    main()
