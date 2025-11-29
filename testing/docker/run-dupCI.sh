#!/bin/bash

export PYTEST_ARGS="$@"

set -e

cd `dirname $0`/dupCI

docker compose up
echo "===== Summary ====="
docker compose logs 2>&1 | grep -E '= .* (failed|passed|skipped).* in .* =' | sort
