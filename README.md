# Firefox and Tor Browser pin data

CSV files containing Firefox (stable and ESR stable) and Tor Browser (alpha and stable) release dates and static key
pinning expiration dates. And some hacky Python programs for processing it.

For context, please read [Ryan Duff's][6] post [Postmortem of the Firefox (and Tor) Certificate Pinning Vulnerability Rabbit Hole][7].

## Files

* `firefox-esr38-*`: Firefox ESR 38 releases
* `firefox-esr45-*`: Firefox ESR 45 releases
* `firefox-esr52-*`: Firefox ESR 52 releases
* `firefox-esr-*`: Most Firefox ESR releases in chronological order
* `firefox-*`: Firefox regular releases
* `tor-browser-alpha-*`: Tor Browser alpha releases, and a few stable releases
* `tor-browser-stable-*`: Tor Browser stable releases
* `tor-browser-*`: All Tor browser alpha and stable releases in chronological order

* `*-expiration-release-dates.csv`: Most of the information combined; see below
* `*-expiration-us.csv`: Pin expiration timestamps, in microseconds since 1970-01-01T00:00:00.000000Z
* `*-expiration.csv`: Pin expiration second timestamps, microsecond timestamps, and ISO 8601 strings
* `*-releases.csv`: Release dates

* `*.py`: Hacky Python scripts. :-)

## Columns

1. `version`: Firefox or Tor Browser version
2. `release_date`: Firefox or Tor Browser release date
3. `expiration_date`: Static pin expiration date
4. `expiration_days`: Days from the release date until the expiration date
5. `previous_expiration_days`: Days from the current row's release date until the previous row's expiration date
6. `previous_release_days`: Days from the previous row's release date until the current row's release date
7. `firefox_version`: Tor Browser only; Firefox version it is based on

## Limitations

Firefox 33's release date is given as [2014-10-13][4] or [2014-10-14][5] in different sources. 2014-10-13 is used here.

Firefox [38.0.6][1] and [40.0.1][2] sort of exist, but have no official release dates, and are excluded from this data.
Their expiration timestamps were identical to the preceding releases.
I suspect that 38.0.6 was released immediately after 38.0.5, and 40.0.1 was released immediately before 40.0.2.

When releases (usually from different series) are made simultaneously, the `previous_expiration_days` and `previous_release_days` fields can be nonsensical.

There were several Tor Browser 4.0.x series point releases after 4.5a1, but they didn't support pinning and are excluded.

## Sources

* https://gitweb.torproject.org/tor-browser.git/
* https://gitweb.torproject.org/builders/tor-browser-bundle.git/tree/Bundle-Data/Docs/ChangeLog.txt
* https://gitweb.torproject.org/builders/tor-browser-bundle.git/tree/Bundle-Data/Docs/ChangeLog.txt?h=maint-6.0
* https://gitweb.torproject.org/builders/tor-browser-bundle.git/tree/Bundle-Data/Docs/ChangeLog.txt?h=maint-6.5

* https://hg.mozilla.org/releases/mozilla-esr38/
* https://hg.mozilla.org/releases/mozilla-esr45/
* https://hg.mozilla.org/releases/mozilla-esr52/
* https://hg.mozilla.org/releases/mozilla-release/

* https://wiki.mozilla.org/Releases/Old/2014
* https://wiki.mozilla.org/Releases/Old/2015

* https://www.mozilla.org/en-US/firefox/releases/

## License

Licensed under the MIT license; see [`LICENSE.txt`][8]. Nonetheless, i believe the `.csv` files are in the public domain by nature.

## Contact

Matt Nordhoff <mnordhoff@gmail.com> ([@mnordhoff][3])

[1]: https://wiki.mozilla.org/Releases/Firefox_38.0.6/BuildNotes
[2]: https://wiki.mozilla.org/Releases/Firefox_40.0.1/BuildNotes
[3]: https://twitter.com/mnordhoff
[4]: https://www.mozilla.org/en-US/firefox/33.0/releasenotes/
[5]: https://wiki.mozilla.org/Releases/Old/2014
[6]: https://twitter.com/flyryan
[7]: https://medium.com/@flyryan/postmortem-of-the-firefox-and-tor-certificate-pinning-vulnerability-rabbit-hole-bd507c1403b4
[8]: LICENSE.txt
