#!/bin/sh
[ -z "$SNAP" ] && {
  echo Missing env var SNAP.
  exit 1
}

[ -z "$DUPL_VENV" ] && {
  echo Missing env var DUPL_VENV.
  exit 1
}

SNAP_DUPL_VENV="${SNAP}/${DUPL_VENV}"

# append the paths in our snap for our binaries to be used in case they did not exist already
[ "$DUPL_LAUNCHER" != "DEBUG1" ] && {
  PATH="${PATH:+$PATH:}$SNAP/usr/bin:/snap/core24/current/usr/bin"
  PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}${SNAP_DUPL_VENV}/lib/python3.12/site-packages:$SNAP/usr/lib/python3/dist-packages"
}
export PATH PYTHONPATH

case "$DUPL_LAUNCHER" in
  "DEBUG"*)
    echo running \'$0\'
    echo PATH=\'$PATH\'
    echo PYTHONPATH=\'$PYTHONPATH\'
    echo DUPL_VENV=\'$DUPL_VENV\'
    echo "'ls -la ${SNAP_DUPL_VENV}/bin/python* $SNAP/usr/bin/python*' => '$(echo;ls -la ${SNAP_DUPL_VENV}/bin/python* $SNAP/usr/bin/python*)'"
    PYTHON="${SNAP_DUPL_VENV}"/bin/python3
    echo "'python --version' => '$("$PYTHON" --version)'"
    echo "'which gpg' => '$(which gpg)'"
    # run command if given
    "$@"
    exit $?
    ;;
esac

# enforce our packaged python with installed modules and readymade librsync module
"${SNAP_DUPL_VENV}"/bin/python3.12 "${SNAP_DUPL_VENV}"/bin/duplicity "$@"
