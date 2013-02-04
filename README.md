vsc-passwords
=============

vsc-passwords contains python tools for password management.

[![Build Status](https://jenkins1.ugent.be/job/VSC-passwords/badge/icon)](https://jenkins1.ugent.be/job/VSC-passwords/)

# Usage
This package contains a script to pull data from a keepass file into your keyring (linux, osx, windows)
It also pulls in the python-keyring package, so you can get passwords from the keyring
```python
import keyring
password = keyring.get_password(service, username)
```

# License
VSC-passwords is made available under the GNU Library General Public License (LGPL) version 2 or at your opinion any later version.

# Acknowledgements
VSC-passwords was created with support of [Ghent University](http://www.ugent.be/en),
the [Flemish Supercomputer Centre (VSC)](https://vscentrum.be/nl/en),
the [Hercules foundation and the Department of Economy](http://www.herculesstichting.be/in_English),
and [the Department of Economy, Science and Innovation (EWI)](http://www.ewi-vlaanderen.be/en).

