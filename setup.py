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
"""
@author: Jens Timmerman (Ghent University)
vsc-passwords password tools setup.py
"""
from shared_setup import jt
from shared_setup import action_target

PACKAGE = {
    'name': 'vsc-passwords',
    'version': '0.1',
    'install_requires': ['vsc-base >= 0.99', 'keepassdb >= 0.1.0', 'keyring >= 1.1'],
    'author': [jt],
    'maintainer': [jt],
    'scripts': ['bin/add_keys_to_keyring.py'],

    'package_dir': {'': '.'},
    'provides': ['python-vsc-packages-passwords = 0.1'],
}

if __name__ == '__main__':
    action_target(PACKAGE)
