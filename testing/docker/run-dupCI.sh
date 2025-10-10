#!/bin/bash

set -e

cd `dirname $0`/dupCI

docker compose up
docker compose logs -n1 | sort
