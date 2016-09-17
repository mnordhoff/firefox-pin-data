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
./tor-browser-expirations-releases.py firefox-esr-expiration.csv tor-browser-releases.csv >tor-browser-expiration-release-dates.csv
./tor-browser-expirations-releases.py firefox-esr-expiration.csv tor-browser-alpha-releases.csv >tor-browser-alpha-expiration-release-dates.csv
./tor-browser-expirations-releases.py firefox-esr-expiration.csv tor-browser-stable-releases.csv >tor-browser-stable-expiration-release-dates.csv
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
    c_out.writerow([
        'version', 'release_date', 'expiration_date', 'expiration_days',
        'previous_expiration_days', 'previous_release_days', 'firefox_version'
        ])
    expirations = {}
    for firefox_version, expiration_s, _, _ in c_expirations:
        expirations[firefox_version] = expiration_s
    previous_expiration_datetime = previous_release_datetime = None
    for version, firefox_version, release_date in iter_c_releases:
        # XXX 45.4.0esr hasn't been released yet and i haven't dug up data on it.
        if firefox_version == '45.4.0esr':
            continue
        expiration_datetime = datetime.datetime.utcfromtimestamp(float(expirations[firefox_version]))
        expiration_date = expiration_datetime.strftime('%Y-%m-%d')
        release_datetime = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        expiration_window_timedelta = expiration_datetime - release_datetime
        expiration_window_s = expiration_window_timedelta.total_seconds() / 86400
        expiration_window_days = '{:.2f}'.format(expiration_window_s)
        if previous_expiration_datetime is None:
            expiration_previous_window_days = release_window_days = 'none'
        else:
            expiration_previous_window_timedelta = previous_expiration_datetime - release_datetime
            expiration_previous_window_s = expiration_previous_window_timedelta.total_seconds() / 86400
            expiration_previous_window_days = '{:.2f}'.format(expiration_previous_window_s)
            release_window_timedelta = release_datetime - previous_release_datetime
            release_window_s = release_window_timedelta.total_seconds() / 86400
            release_window_days = '{:.2f}'.format(release_window_s)
        c_out.writerow([
            version, release_date, expiration_date, expiration_window_days,
            expiration_previous_window_days, release_window_days, firefox_version
            ])
        previous_expiration_datetime = expiration_datetime
        previous_release_datetime = release_datetime

if __name__ == '__main__':
    main()
