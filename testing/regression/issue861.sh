#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

alias python3=python3.10

#export PYDEVD=True

function run_full() {
    echo "########## $1 full run ##########"
    duplicity/__main__.py \
        full \
        --name issue861 \
        --file-prefix-manifest 'meta_' \
        --file-prefix-signature 'meta_' \
        --file-prefix-archive 'data_' \
        --no-encryption \
        --concurrency 4 \
        `pwd`/docs \
        multi:///`pwd`/testing/regression/issue861.json\?mode=mirror

    ls -lR ~/.cache/duplicity/issue861 /tmp/first_drive /tmp/second_drive
    sleep 2
}

rm -rf ~/.cache/duplicity/issue861 /tmp/first_drive /tmp/second_drive
run_full "1st"
run_full "2nd"


export PYDEVD=vscode
tar -C / -xvf /tmp/issue102.tar
echo "########## clean up ##########"
duplicity/__main__.py \
    remove-older-than 1s \
    --name issue861 \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --force \
    --verbosity 9 \
    multi:///`pwd`/testing/regression/issue861.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue861 /tmp/first_drive /tmp/second_drive
sleep 2

export PYDEVD=""

echo "########## collect status ##########"
duplicity/__main__.py \
    collection-status \
    --name issue861 \
    --file-prefix-manifest 'meta_' \
    --file-prefix-signature 'meta_' \
    --file-prefix-archive 'data_' \
    --no-encryption \
    --verbosity 9 \
    --concurrency 4 \
    multi:///`pwd`/testing/regression/issue861.json\?mode=mirror

ls -lR ~/.cache/duplicity/issue861 /tmp/first_drive /tmp/second_drive
