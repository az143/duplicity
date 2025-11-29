#!/bin/bash

export PYTEST_ARGS="$@"

set -e

cd `dirname $0`/distro

docker compose up
echo "===== Summary ====="
docker compose logs 2>&1 | grep -E '= .* (failed|passed|skipped).* in .* =' | sort
