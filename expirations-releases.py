#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2016-2017 Matt Nordhoff <mnordhoff@mattnordhoff.com>
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
./expirations-releases.py firefox-expiration.csv firefox-releases.csv >firefox-expiration-release-dates.csv
./expirations-releases.py firefox-esr-expiration.csv firefox-esr-releases.csv >firefox-esr-expiration-release-dates.csv
./expirations-releases.py firefox-esr-expiration.csv firefox-esr38-releases.csv >firefox-esr38-expiration-release-dates.csv
./expirations-releases.py firefox-esr-expiration.csv firefox-esr45-releases.csv >firefox-esr45-expiration-release-dates.csv
./expirations-releases.py firefox-esr-expiration.csv firefox-esr52-releases.csv >firefox-esr52-expiration-release-dates.csv
./expirations-releases.py tor-browser-expiration.csv tor-browser-releases.csv >tor-browser-expiration-release-dates.csv
./expirations-releases.py tor-browser-expiration.csv tor-browser-alpha-releases.csv >tor-browser-alpha-expiration-release-dates.csv
./expirations-releases.py tor-browser-expiration.csv tor-browser-stable-releases.csv >tor-browser-stable-expiration-release-dates.csv
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
    c_expirations = csv.DictReader(fh_expirations)
    c_releases = csv.DictReader(fh_releases)
    c_out = csv.writer(sys.stdout, lineterminator=os.linesep)
    write_row = [
        'version', 'release_date', 'expiration_date', 'expiration_days',
        'previous_expiration_days', 'previous_release_days'
        ]
    if 'firefox_version' in c_releases.fieldnames:
        write_row.append('firefox_version')
    c_out.writerow(write_row)
    expirations = {}
    for row in c_expirations:
        version = row['version']
        expiration_s = row['expiration_s']
        expirations[version] = expiration_s
    previous_expiration_datetime = previous_release_datetime = None
    for row in c_releases:
        version = row['version']
        if 'firefox_version' in c_releases.fieldnames:
            firefox_version = row['firefox_version']
        release_date = row['date']
        expiration_datetime = datetime.datetime.utcfromtimestamp(float(expirations[version]))
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
        write_row = [
            version, release_date, expiration_date, expiration_window_days,
            expiration_previous_window_days, release_window_days
            ]
        if 'firefox_version' in c_releases.fieldnames:
            write_row.append(firefox_version)
        c_out.writerow(write_row)
        previous_expiration_datetime = expiration_datetime
        previous_release_datetime = release_datetime
    fh_expirations.close()
    fh_releases.close()

if __name__ == '__main__':
    main()
