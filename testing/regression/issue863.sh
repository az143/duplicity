#! /bin/bash

set -e

cd `dirname $0`/../..

export GNUPGHOME=testing/gnupg
export PYTHONPATH=`pwd`

rm -rf ~/.cache/duplicity/issue863 /tmp/issue863
duplicity/__main__.py --name issue863 --metadata-sync-mode partial --encrypt-key 839E6A2856538CCF full testing file:///tmp/issue863/

rm -rf ~/.cache/duplicity/issue863
duplicity/__main__.py --name issue863 --metadata-sync-mode partial --encrypt-key 839E6A2856538CCF full testing file:///tmp/issue863/

ls -l ~/.cache/duplicity/issue863 /tmp/issue863
