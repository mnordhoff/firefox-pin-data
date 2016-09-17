# Firefox and Tor Browser pin data

CSV files containing Firefox (stable and ESR stable) and Tor Browser (alpha and stable) release dates and static key pinning expiration dates. And two hacky Python programs for processing it.

Files:

* `firefox-esr-*`: Firefox ESR releases
* `firefox-*`: Firefox regular releases
* `tor-browser-alpha-*`: Tor Browser alpha releases, and a few stable releases
* `tor-browser-stable-*`: Tor Browser stable releases
* `tor-browser-*`: Tor browser alpha and stable releases in chronological order

* `*-expiration-release-dates.csv`: Most of the information combined; see below
* `*-expiration-us.csv`: Pin expiration timestamps, in microseconds since 1970-01-01T00:00:00.000000Z
* `*-expiration.csv`: Pin expiration second timestamps, microsecond timestamps, and ISO 8601 strings
* `*-releases.csv`: Release dates

* `*.py`: Hacky Python scripts. :-)

Columns:

1. `version`: Firefox or Tor Browser version
2. `release_date`: Firefox or Tor Browser release date
3. `expiration_date`: Static pin expiration date
4. `expiration_days`: Days from the release date until the expiration date
5. `previous_expiration_days`: Days from the current row's release date until the previous row's expiration date
6. `previous_release_days`: Days from the previous row's release date until the current row's release date
7. `firefox_version`: Tor Browser only; Firefox version it is based on

Firefox `45.4.0esr` and Tor Browser `6.5a3` have yet to be released and are subject to change. Firefox `45.4.0esr-6.0.5` refers to the revision of Firefox `45.4.0esr` used by Tor Browser `6.0.5`, which may differ from the final release.

The `.csv` files are, i believe, in the public domain by nature. The other files are under the MIT license.
