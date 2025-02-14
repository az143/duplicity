#!/bin/sh
[ -z "$SNAP" ] && {
  echo Missing env var SNAP.
  exit 1
}

# append the paths in our snap for our binaries to be used in case they did not exist already
[ "$DUPL_LAUNCHER" != "DEBUG1" ] && {
  PATH="${PATH:+$PATH:}/snap/bin:$SNAP/usr/sbin:$SNAP/usr/bin:$SNAP/sbin:$SNAP/bin:/snap/core20/current/usr/bin"
  export PATH
}

case "$DUPL_LAUNCHER" in
  "DEBUG"*)
    echo running \'$0\'
    echo PATH=\'$PATH\'
    echo PYTHONPATH=\'$PYTHONPATH\'
    echo python3=\>\'$(which python3)\'
    echo python3.8=\>\'$(which python3.8)\'
    echo gpg=\>\'$(which gpg)\'
    # run command if given
    "$@"
    exit $?
    ;;
esac

# enforce or packaged python with installed modules and readymade librsync
"$SNAP"/usr/bin/python3.8 "$SNAP"/bin/duplicity "$@"
