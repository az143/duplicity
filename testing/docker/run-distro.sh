#!/bin/bash

set -e

cd `dirname $0`/distro

docker compose up
docker compose logs -n1 | sort
