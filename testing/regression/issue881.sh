#! /bin/bash

set -e

cd `dirname $0`/../..

export PYTHONPATH=`pwd`

rm -rf ~/.cache/duplicity/issue881 /tmp/issue881/success
duplicity/__main__.py --name issue881 --no-comp --no-enc -v DEBUG full testing "multi://`pwd`/testing/regression/issue881.json?mode=mirror&onfail=continue"

ls -l /tmp/issue881/success
