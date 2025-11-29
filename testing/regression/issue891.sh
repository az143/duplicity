#! /bin/bash

# set -e

cd `dirname $0`/../..

export GNUPGHOME=testing/gnupg
export PYTHONPATH=`pwd`
export OPTS="--name issue891 --vol=1 --no-enc --num-ret=3 --backend-ret=1"


# cleanup
rm -rf ~/.cache/duplicity/issue891
[ -e /tmp/issue891 ] && chmod ugo+r /tmp/issue891
[ -e /tmp/issue891 ] && rm -rf /tmp/issue891

# make target unreadable
mkdir -p /tmp/issue891
chmod ugo-r /tmp/issue891

echo -e "\nFull backup\n"
duplicity/__main__.py full ${OPTS} --no-check-remote testing file:///tmp/issue891

sleep 1

echo -e "\nInc backup\n"
duplicity/__main__.py inc ${OPTS} --no-check-remote testing file:///tmp/issue891

# make target readable
chmod ugo+r /tmp/issue891

echo -e "\nVerify backup\n"
duplicity/__main__.py verify ${OPTS} file:///tmp/issue891 testing

# get results
echo -e "\nResults\n"
ls -l ~/.cache/duplicity/issue891 /tmp/issue891

# cleanup
rm -rf ~/.cache/duplicity/issue891 /tmp/issue891
