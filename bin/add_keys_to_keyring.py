#!/usr/bin/python
##
# Copyright 2009-2013 Ghent University
#
# This file is part of vsc-passwords,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/vsc-passwords
#
# vsc-passwords is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# vsc-passwords is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with vsc-passwords. If not, see <http://www.gnu.org/licenses/>.
##
"""@author: Jens Timmerman

Adds keys from a specified keepass database to your keyring"""
import os
import getpass
import keyring

from keepassdb.db import LockingDatabase as Database
from vsc.utils import fancylogger
from vsc.utils.generaloption import ExtOptionParser

# add all keys to the keyring for which the comment field has this entry in it
ADD_IF_COMMENT = 'keyring'
DEFAULT_FILE = "../../ugenthpc/documents/keys.kdb"

# parse options
parser = ExtOptionParser(usage="testusage\n%s" % __doc__)
parser.add_option("-f", "--file", dest="filename",
                  help="use FILE as keepass database", metavar="FILE", default=DEFAULT_FILE)
(options, args) = parser.parse_args()

# set up logging
fancylogger.logToScreen()
log = fancylogger.getLogger()
fancylogger.setLogLevelInfo()

log.info("using file %s", os.path.abspath(options.filename))

db = Database(options.filename, password=getpass.getpass("Please enter keepass file password: "))

try:
    for group in db.groups:
        for entry in group.entries:
            if ADD_IF_COMMENT in entry.notes:
                log.info("adding %s", entry.title)
                keyring.set_password(entry.title, entry.username, entry.password)
finally:
    db.close()
log.info("done")
