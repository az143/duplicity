#!/usr/bin/env python3
"""
Manual helper to verify whether specific GnuPG keys require a passphrase.

What this script does
---------------------
- Changes to the project root and sets `GNUPGHOME` to use the test keyring in
  `testing/gnupg`.
- Calls `duplicity.util.key_needs_passphrase(gpgbin, key)` for a small set of
  known test keys with both `gpg` and `gpgsm` and reports results.
- Prints PASS/FAIL per key and exits with the number of failures as the status
  code (0 means all checks passed).

How to run
----------
- From the project root:
    - `python3 testing/manual/needspass.py`

Optional debugging
------------------
- To see the interaction with `gpg-agent` via `pexpect`, set `logfile=sys.stdout`
  where indicated in the code (search for the comment “set logfile=sys.stdout”).

Prerequisites
-------------
- `gpg`, `gpgsm`, and a functioning `gpg-agent` available in PATH.
- No additional arguments are needed; the script is self‑contained for the
  repository’s test keyring.

Notes
-----
- The expected outcomes for the embedded test keys are specified in
  `test_keys` below; modify or extend this list if you need to try other keys.
"""

import os
import sys

os.chdir(os.path.dirname(__file__) + "/../..")
os.environ["GNUPGHOME"] = "testing/gnupg"

from duplicity import log
from duplicity import util

test_keys = [
    ("gpgsm", "\\&165F2FB4F58D537404FE223A603878F54CD444E5", True),
    ("gpgsm", "\\&86E23738BB09B27C6C7E4F76C39DA0194586CF4B", True),
    ("gpg", "56538CCF", True),
    ("gpg", "B5FA894F", False),
    ("gpg", "9B736B2A", True),
]

log.setup()
log.setverbosity(log.DEBUG)

passed = failed = errored = 0

for gpgbin, key, needs_passphrase in test_keys:
    # set logfile=sys.stdout to see pexpect output
    res = util.key_needs_passphrase(gpgbin, key, logfile=None)
    if res is None:
        log.Debug(f"HARD FAIL: gpg-agent failed for {key}")
        errored += 1
    elif res == needs_passphrase:
        log.Debug(f"PASS: {key} needs passphrase={needs_passphrase} OK")
        passed += 1
    else:
        log.Debug(f"FAIL: {key} needs passphrase={needs_passphrase} got {res=}")
        failed += 1

    log.Debug("\n========================================\n")

log.Debug(f"{passed=}, {failed=}, {errored=}")

sys.exit(failed)
