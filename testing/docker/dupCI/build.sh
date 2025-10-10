#!/bin/bash
#
# Copyright 2017 Nils Tekampe
# Copyright 2017 Kenneth Loafman
#
# This file is part of duplicity.
# This script sets up a test network for the tests of dupclicity
# This script takes the assumption that the containers for the testinfrastructure do deither run
# or they are removed. It is not intended to have stopped containers.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

set -e

cd `dirname "$0"`

# setup gnupg
cp -rp ../../gnupg ./
echo -e "%Assuan%\nsocket=/root/S.gpg-agent\n" > ./gnupg/S.gog-agent
echo -e "%Assuan%\nsocket=/root/S.gpg-agent.browser\n" > ./gnupg/S.gog-agent.browser
echo -e "%Assuan%\nsocket=/root/S.gpg-agent.extra\n" > ./gnupg/S.gog-agent.extra
echo -e "%Assuan%\nsocket=/root/S.gpg-agent.ssh\n" > ./gnupg/S.gog-agent.ssh

# setup requirements
cp -p ../../../requirements.txt ./
sed '1,/documentation libraries/!d' ../../../requirements.dev > requirements.dev

# build version specced by Dockerfile extenwion
for FILE in Dockerfile.py3*; do
    VERS="${FILE##*.}"
    docker build $@ --compress --tag=dupci/${VERS} -f Dockerfile.${VERS} ./
done

# cleanup gnupg and requirements
rm -r ./gnupg
rm ./requirements.*
