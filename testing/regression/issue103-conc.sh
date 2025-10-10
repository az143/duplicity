#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

alias python3=python3.10

#export PYDEVD=True

rm -rf ~/.cache/duplicity/issue103-conc /tmp/first_drive /tmp/second_drive

duplicity/__main__.py \
    full \
    --name issue103-conc \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --concurrency 4 \
    `pwd` \
    multi:///`pwd`/testing/regression/issue103-conc.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue103-conc /tmp/first_drive /tmp/second_drive
sleep 2

duplicity/__main__.py \
    full \
    --name issue103-conc \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --concurrency 4 \
    `pwd` \
    multi:///`pwd`/testing/regression/issue103-conc.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue103-conc /tmp/first_drive /tmp/second_drive
sleep 2

duplicity/__main__.py \
    remove-older-than 2s \
    --name issue103-conc \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --force \
    --verbosity 9 \
    --concurrency 4 \
    multi:///`pwd`/testing/regression/issue103-conc.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue103-conc /tmp/first_drive /tmp/second_drive
sleep 2

duplicity/__main__.py \
    collection-status \
    --name issue103-conc \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --verbosity 9 \
    --concurrency 4 \
    multi:///`pwd`/testing/regression/issue103-conc.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue103-conc /tmp/first_drive /tmp/second_drive
