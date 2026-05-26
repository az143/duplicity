
(Unreleased) / 2026-05-12
=========================



rel.3.0.8.dev5 / 2026-05-12
===========================

 * 3997156c:chg: Update README-RELEASE.md.
 * 0f5430db:fix: Fix so GNUPGHOME is not changed in production.
 * 53cc9659:fix: lower boto warning log level, rephrase.
 * 88bfc75e:chg: Misc cleanups for developers
 * 4b0bb8d5:chg: Update 'release pip version' in README-RELEASE.md.

rel.3.0.8.dev4 / 2026-03-31
===========================

 * c17b03bc:fix: try/except block masking real S3UploadFailedError
 * db127ce5:new: Add --full-if-n-inc flag for count-based full backup.
 * dc977419:fix: Simplify swig module definition.
 * 0de30e69:chg: Adjust to newer sphinx.
 * c1883117:fix: Add templates for bug and feature requests.
 * 39150d34:fix: delete unused Path.patch_with_attribs.
 * 1a7c6790:fix: Remove support for Python 2.
 * 564dd593:fix: fix flag name --gpg-agent -> --use-agent.
 * 866680d0:chg: Multiple changes for 2026 are planned
 * 29e00b55:fix: Fix incompatibility with Python 3.14.
 * 50faabfc:chg: Partial fix for #924.
 * 00ae7687:fix: webdav, always send warmup OPTIONS request, prevent loop
 * 37841a0e:fix: Handle local version identifiers in b2backend

rel.3.0.8.dev3 / 2026-01-14
===========================

 * 3475dd05:fix: Unnecessary passphrase prompt with --encrypt-key --no-check-remote.
 * b8508f6d:chg: Remove slow marker from tests.

rel.3.0.8.dev2 / 2026-01-14
===========================


rel.3.0.7 / 2025-12-31
======================

 * ad175c22:fix: replace custom deltree with built-in shutil.rmtree.
 * 101be7fd:fix: delete duplicate code in DirDelta.
 * c0d3e72d:fix: webdavs with "--concurrency 1" failed because of missing auth header
 * a08f8bef:fix: disable s3 checksum workaround, warn only...
 * f7055a7a:fix: --log-timestamp no longer working.
 * ac163d5e:fix: Combined fix to related issues 912 and 914

rel.3.0.6.3 / 2025-12-05
========================

 * dd45a92d:chg: Update check_tags to use current branch.
 * 5bbb5813:fix: Change log level from Info to Notice in get_passphrase().
 * a9c4fbad:chg: Add key_needs_passphrase(key).
 * abaf8485:chg: Better error message from get_remote_file().
 * b083fca8:fix: 'duplicity --no-check-remote inc' prints spurious warning "found missing difftar(s) in backup sets"
 * 9400fc37:chg: Add check_tags minor fix to setversion.
 * 29227571:fix: delete unused diffdir.DirSig, diffdir.SigTarBlockIter, librsync.SigFile.
 * 29205145:fix: Delete unused IndexedTuple.
 * b0653566:fix: Delete unused Patch, patch_diff_tarfile, PathPatcher.
 * bd2742f6:fix: Delete unused Patch_from_iter.
 * 41ffec77:chg: Merge branch 'unusedbvr' into dev
 * 540f2c04:chg: Fix .gitlab-ci.yml
 * 9324947e:fix: delete unused BadVolumeException.

rel.3.0.6.2 / 2025-11-20
========================

 * 9933c1b3:chg: Fix merge conflict resolution error.
 * dc35ab40:chg: Merge origin/issue901 into issue901
 * 3a5d56b4:chg: Changes from Thomas's review. See MR 318.
 * d378b438:fix: Remove test not running under Docker.
 * 08a4cf17:fix: Don't check for missing in first CollectionStatus().set_values().
 * 018726cd:fix: Fix "full" not working. Add more tests.
 * 8c138f3b:fix: Fix "Upgrade to 3.0.6 on Archlinux gives gcry_kdf_derive failed" (#901)
 * 493643c3:fix: Remove test not running under Docker.
 * 9a36384d:fix: Don't check for missing in first CollectionStatus().set_values().
 * c8172aef:fix: ssh_pexpect_backend: fix TypeError
 * af76fd33:fix: fix compilation with gcc 15
 * 9f522b23:fix: --files-from fails when backing up root
 * e82df376:fix: Fix "full" not working. Add more tests.
 * b192f814:fix: Crash with b2backend when b2sk isn't available, rather than proper error
 * 55d0aa18:fix: Parsing the gpg version failed when using Sequoia Chameleon
 * 575234ef:fix: Fix "Upgrade to 3.0.6 on Archlinux gives gcry_kdf_derive failed" (#901)

rel.3.0.6.1 / 2025-11-13
========================

 * a08b2409:chg: Revert "chg:pkg: Cleanup the build system."

rel.3.0.6.1.dev1 / 2025-11-07
=============================

 * c489e2a6:chg: Changes to .gitchangelog.rc
 * ae5a2873:fix: Regression in pexpect+sftp backend
 * 222ae9d2:fix: unpin httplib2 but add pysocks needed for proxy support...
 * 54deadc4:fix: pin httplib2 for HTTP(S)_PROXY env var support

rel.3.0.6 / 2025-11-02
======================

 * 7338dd6f:fix: gdrive dies with 503 during init
 * 3547dc29:chg: Cleanup the build system.
 * a05d2241:chg: Fix .gitchangelog.rc
 * 4ece4812:chg: Fix wheels publish.

rel.3.0.6.dev12 / 2025-10-25
============================

 * 32098d01:chg: Misc build tools upgrades.
 * da0427d6:chg: Add error message to raw assert statements.
 * 46030f89:fix: 'duplicity incremental' attempts to fetch remote manifest which is not needed for the current backup

rel.3.0.6.dev11 / 2025-10-19
============================

 * 79dab78a:chg: Use python -m build --sdist
 * 7c449f84:fix: if using authentication, send warmup OPTIONS request
 * d6cc4dfe:chg: Add py314 to wheels build.
 * ad7c0012:fix: 'duplicity incremental' attempts to fetch remote manifest which is not needed for the current backup
 * 4f49923d:fix: Fix removal of signature from latest backup
 * 2c559941:chg: Fix chdir() in tools/setversion.
 * 7d0dc6d9:chg: Move SetVersionCommand to tools/setversion.
 * 3c680390:chg: Merge branch dev314 into dev
 * e8b68709:chg: Don't check versions under pytest.
 * 3efb263b:chg: Fix/add TODO's for argparse311.
 * e405b0c4:fix: Fix check for optimization.
 * fcff7026:fix: Black to run on py314.
 * f0c16c50:fix: Fix check for optimization.
 * a78d2bc6:chg: Only run on py39 thru py314.
 * 63164267:chg: Updates to wheels build.
 * c6c1f9d6:fix: collection-status with a specific file fails with TypeError
 * d57ccd2f:fix: duplicity verify fails with KeyError.
 * f6c16405:fix: Restore a file to directory fails and empties target directory - related to #111
 * 62c7b167:chg: Upload manylinux wheels to PyPi
 * 8e1163fb:chg: boto3 1.36+ breaks Duplicity...but there is a workaround
 * 2133ea13:fix: Make swiftbackend imports global.
 * 23e87cff:chr: remove 'are_errors_fatal' mechanism, no longer needed.

rel.3.0.6.dev10 / 2025-10-01
============================

 * cb0e5c94:chg: Fix chdir() in tools/setversion.
 * 755f3f6f:chg: Move SetVersionCommand to tools/setversion.
 * deceec02:chg: Set black>=24.8.0
 * 81e9e410:chg: Don't check versions under pytest.
 * 002669c5:chg: Fix/add TODO's for argparse311.
 * 34ff6b3a:fix: Black to run on py314.
 * 1f79ec0a:chg: Only run on py39 thru py314.

rel.3.0.6.dev9 / 2025-09-25
===========================

 * 567a10a9:fix: Fix check for optimization.
 * ba547f21:chg: Updates to wheels build.

rel.3.0.6.dev8 / 2025-09-14
===========================

 * 1c716f55:fix: collection-status with a specific file fails with TypeError
 * b9775a0f:fix: duplicity verify fails with KeyError.
 * 77a30010:fix: Restore a file to directory fails and empties target directory - related to #111

rel.3.0.6.dev7 / 2025-08-02
===========================

 * 9bff3a21:chg: Upload manylinux wheels to PyPi
 * 97839467:chg: boto3 1.36+ breaks Duplicity...but there is a workaround

rel.3.0.6.dev6 / 2025-07-24
===========================

 * 88c8d3d5:fix: Make swiftbackend imports global.
 * 63e263a3:chg: remove 'are_errors_fatal' mechanism, no longer needed.
 * 503659d1:fix: multi backend: if we looped around, and any passed, break out.
 * af2cfef0:fix: make @retry report fatals as exceptions, not log.FatalError.
 * a1316025:fix: on uncaught BackendException, make the exit code backend_error (50).

rel.3.0.6.dev5 / 2025-07-05
===========================

 * 8901a21a:fix: Revert "use pyproject plugin for ppa"

rel.3.0.6.dev4 / 2025-07-05
===========================

 * 4dc57cc0:fix: use pyproject plugin for ppa
 * 3bc1bb97:fix: fix TotalDestinationSizeChange with concurrency.
 * b95a67eb:fix: pexpect+sftp: support absolute path in URL.

rel.3.0.6.dev3 / 2025-06-25
===========================


rel.3.0.5.1 / 2025-06-25
========================

 * 2cc62173:chg: Fixes for LP builds. See #877.
 * faf55675:fix: Revert "Fix build-system.requires and requirements.txt"

rel.3.0.5 / 2025-06-19
======================

 * 569d5f6f:chg: Changes to support Ubuntu 20.04.
 * 3683aa4d:fix: Fix build-system.requires and requirements.txt
 * eecf5a0c:fix: Fix handling of .p7m filename suffix during sync.
 * 9002a280:fix: Cache negative getpwnam/getgrnam lookups.
 * 1f773b02:chg: Add ENODEV to list of "robust" ignored exceptions
 * 4fd83cb1:fix: Fix gpgsm version check.
 * 841aad6b:chg: Delete unused CollectionsStatus.action variable.
 * a261d017:chg: Fix tools/makesnap. CLI changes.
 * 606e9eec:fix: Incompatible with par2cmdline v1.0.0
 * da47450c:fix: Allow the full range of time formats as arguments to --full-if-older-than
 * a9136c82:chg: Delete unused BackupSet.action variable.
 * 8dc698a3:chg: Support gpg binary 'gpgsm'.
 * 9aacccde:chg: Accept GPG user id formats other than hex.
 * cc915d0e:chg: add env var BACKEND_PASSWORD, deprecate FTP_PASSWORD
 * 14fbc90b:chg: Restore backends. Set setuptools<78.0.0
 * 5a637fd1:chg: Move import in function to __init__().
 * 918a21e4:chg: PyPA struck again. 'positional' does not build now.
 * e85c3bb6:fix: Fix problems with password request and metadata sync
 * ca8971b9:fix: snapcraft.io didn't like us to symlink core24's python...
 * 9cef5b19:chg: simplify snap by not packaging python but using core24's python instead...
 * b24b4706:fix: "OverflowError: bytes object is too large to make repr" see issue 862
 * a81847f0:chg: Fix issue103.sh and add issue103-conc.sh.
 * 0de67d13:fix: Prevent webdav log password at info log level...
 * c27a082a:chg: Improve contact points

rel.3.0.4.1 / 2025-02-26
========================

 * 2a0dac20:new: Introduce core24 snaps now in even more flavor *errr* archs...
 * db1d5626:fix: Par2 files for vol1.difftar not being created when --concurrency is set
 * 2bb2baa8:chg: Delete unneeded tools.
 * 490876a8:fix: Fix typo in previous.
 * 7c97c6eb:fix: Suppress deprecation error for core20 snap users.

rel.3.0.4 / 2025-02-08
======================

 * 88c24acc:fix: fix snap PATH handling...
 * 37f67a24:fix: SNAPCRAFT_BUILD_FOR unbound error when building snap on Ubuntu24
 * 2caea280:fix: allow for python versions 3.12+ e.g. 3.12.8
 * 905de6d5:new: Support for Microsoft Azure "Cold" blob storage tier.
 * 8eaa200b:fix: INFO and DEBUG messages when verbosity is warning
 * 98e7113b:chg: Allow to build with py3.13.x

rel.3.0.3.2 / 2024-11-25
========================

 * 466de45b:fix: Concurrency without setting verbosity throws exception.
 * 140b09dc:fix: argument --max-blocksize: invalid round512 value
 * ffdfa3bc:chg: Remove 'test' mentions from setup.py.
 * 3e6125cb:chg: Merge main into dev.
 * 714dc277:fix: Fix handling of zero length files for older librsync versions.
 * 1f750b01:chg: Fix so amd64 snaps build with tahoe support.

rel.3.0.3.1 / 2024-11-19
========================

 * 6d72127d:chg: Fix .gitchangelog.rc for 4 digit version.
 * 8d2161f5:fix: Fix handling of zero length files for older librsync versions.
 * ced398c0:chg: Fix so amd64 snaps build with tahoe support.

rel.3.0.3 / 2024-11-17
======================

 * 6223ae89:chg: Move config from code to pyproject.toml.
 * 26561757:chg: Fix docs for --max-blocksize.
 * 0b9312f7:chg: Upgrade black to 24.10.0 for py313.
 * 951f742e:chg: Allow Python 3.13 to install.
 * 4d5d4160:chg: High memory usage when creating duplicity backup of a single very large file
 * 81c2f8d0:chg: Fix problem with reading ".../progress" file after aborted.
 * 19d2b517:chg: Revert gdocsbackend.py. Remove TODO's
 * 1890f129:chg: Fix requirements for upcoming atom release.
 * 0133e2b3:chg: Turn off atom for py313.
 * aa9f3cb0:chg: Temp removal of atom requirement.
 * d3b450a2:fix: Add setuptools to requirements.txt.
 * 3f94bf1f:fix: Verbosity setting is broken with concurrency.
 * ac8acff5:chg: Only log if backend import failed.

rel.3.0.2 / 2024-08-09
======================

 * 42653410:chg: Fix collection-status print.

rel.3.0.1 / 2024-08-05
======================

 * 778483cf:chg: Merge dev into main.
 * 9bbc00e1:chg: Remove version limits on urllib3.
 * 8b94b6d7:chg: add some debug output to help pinpoint B2 backend import issues
 * 7027aa89:chg: Fixes #832, urllib3 error under python3.12.
 * f89d24a8:fix: Rework logging to be compatible with Python's logging
 * 5748a731:chg: Fix typo in setuptools section and migrate to new structure.
 * 940b4642:fix: S3 glacier storage class and --concurrency #831.
 * e7a6797e:fix: Unblock multiprocessing deadlock, ensure local disk usage not exceed n+1 volumes, switch to "spawn".
 * 1084c2ac:fix: Add file-size query support to rclonebackend
 * e435874a:fix: Allow empty manifest list. #827
 * fa9d13da:fix: Make --ignore-errors actually ignore (and recover from) errors
 * 7084a77e:fix: SSLCertVerificationError despite --ssl-no-check-certificate
 * 8bb35c81:chg: Use functools.lru_cache with limit, not unlimited.
 * 78a6ce65:fix: Instead of raise call command_line_error() directly.
 * e0df7a6a:fix: Empty exclude string results in unfriendly traceback.
 * b72a0b4b:chg: Set dev branch to 3.0.1.dev.

rel.3.0.0 / 2024-05-29
======================

 * 83f7fb68:fix: Volume missing if --asynchronous-upload and put fails
 * f4abf149:chg: Collected fixes to setup process.
 * ce3eb13c:chg: CommandLineError: argument --gpg-options: expected one argument.
 * 15d94a58:chg: Set dev branch to 2.2.5.dev.
 * dc7181cb:fix: don't raise KeyError if OSError.errno is unrecognized
 * 13f57320:chg: Skip tests on Launchpad.

rel.2.2.4 / 2024-05-20
======================

 * 68709a30:chg: Bump to version 2.2.4.
 * cddd7fea:chg: Move install-requires back to setup.py.

rel.2.2.4rc3 / 2024-05-19
=========================

 * 66b202aa:chg: Use pip-compile to build requirements.txt.

rel.2.2.4rc2 / 2024-05-18
=========================

 * b7b632c6:chg: Adjust since twine does not do wildcards.
 * 66f8190f:chg: Revert "chg:pkg: Add missing fasteners install dependency"
 * 0b67b55c:chg: Add requirements.dev to tests.
 * 371b0e02:chg: Split requirements.txt into .txt and .dev.
 * ce3baa9a:chg: Add missing fasteners install dependency
 * de66c40d:fix: onedrive: fix "unauthorized" upload error by not passing auth
 * c2c805fe:chg: Fix typo in ignore new pylint warning.
 * cc2bb790:chg: Ignore new pylint warning E0606 (possibly-used-before-assignment).

rel.2.2.4rc1 / 2024-05-15
=========================

 * 54cfce26:chg: Fix typo in ignore new pylint warning.
 * 0e0b83f3:chg: Ignore new pylint warning E0606 (possibly-used-before-assignment).
 * 867fab71:chg: Upgrade setup process and instructions (2nd try)
 * 8654a111:fix: Don't drop args when restarting with execve
 * 21b1e809:chg: reformating, typos
 * 92b9512f:chg: Add deprecation warning for `--async`
 * 2074cf3d:fix: Really fix invalid option error
 * 9e1c920c:fix: Fix invalid option error.
 * 1061aeae:fix: move missleading warning to debug level #813
 * 416d8eb2:fix: duplicity 2.2.3: --use-agent can be wrongly turned off
 * 5b943495:fix: Adjust #810 fix for py38.
 * df6304d3:fix: Pass "usedforsecurity=False" to md5() and sha1().
 * 512119b8:chg: Set packaging and black version requirements.
 * d4ec7723:chg: Adjust debian/control for focal builds.
 * be8a8cce:chg: Adjust debian/control for focal builds.
 * 4f47ee88:chg: Adjust debian/control for focal builds.

rel.2.2.3 / 2024-03-20
======================

 * 36ba5b52:chg: Remove setuptools_scm and usages.
 * 7dfdd763:chg: pip install duplicity fails with "AssertionError: es_PR" (or other language)
 * 2bf13416:fix: add fail open condition, for backends with no support
 * b0ef8900:chg: Launchpad PPAs not built correctly for 2.2.[0,1], PyPI pips for 2.2.[0,1,2]
 * 0c104f6a:chg: Change ngettext to _ and fix wording.
 * 48e2859e:chg: move validate to backend
 * e7b3b407:fix: Change path logging from Info to Debug.
 * 751eab2c:fix: Whoops! Remove parens in fix of #803.
 * cb7c674a:fix: Exception using --exclude-older-than.
 * 69feccb1:chg: Run only one pipeline on merge request
 * 8832fefc:chg: Merge issue799 into dev.
 * f3316bef:chg: Warn on symmetric encrypt with --use-agent.
 * cb8ad568:chg: Warn on symmetric encrypt with --use-agent.
 * 256d2a63:chg: Remove last of bin/duplicity.
 * 5722fee6:chg: Merge main into dev.
 * a653e131:chg: Merge main into dev.

rel.2.2.2 / 2024-02-03
======================

 * 104321c1:chg: Merge dev into main.
 * fdb8e9f3:chg: Ask google_auth_oauthlib not to open browser during authentication flow
 * 4c1216b1:fix: Clean up debian/rules.
 * 4636e043:fix: Add duplicity console script.
 * 081ed48b:chg: update `python_requires` to allow py3.12

rel.2.2.1 / 2024-01-29
======================


rel.2.2.0 / 2024-01-27
======================

 * 220b03f0:fix: Invalid option error using `--[gpg|par2|rsync|ssh]-options '...'
 * bee077d9:chg: Remove support for old mock
 * 0fb419ae:chg: Allow pipelines to run if not merge request.
 * 63f883c6:chg: Version as 2.2.0
 * 1155b6cc:chg: Upgrade current build and test systems

rel.2.1.5 / 2023-12-28
======================

 * 31abc1bf:chg: Fix debian/rules for versioned.
 * 1f172eea:chg: Version as 2.1.5.
 * bcd44a79:fix: Swap implied and removed action checks
 * 9f35b0e3:fix: Error on dry-run with verify.
 * 2f15ab89:fix: Fix imports in boxbackend.py.
 * 83dda9b6:chg: Remove "backup" and "replicate" dead code.
 * c444d0f0:chg: Deprecate PyDrive backend. Replaced with GDrive backend.
 * 8c8a6a3b:chg: setuptools_scm not needed at runtime.
 * 33ab2b62:fix: multibackend not working with remove-all-but-n-full in stripe mode.
 * edfbc1e3:chg: Fix swift uploads to default to 5GB segment size
 * 3b0b6a62:fix: Fix collection-status with file-changed argument
 * 1bc7e798:chg: Add venv* to .gitignore.
 * ca3f43dd:chg: Some formatting fixes.
 * c6fa2392:chg: Fix check of versions in setup.py.
 * 488c99e9:chg: Limit range of versions in setup.py.

rel.2.1.4 / 2023-10-20
======================

 * 8f36249f:fix: Print command line error on empty commandline.
 * 48b36777:fix: Print help on empty commandline.
 * d2bdb824:fix: --full-if-older-than being ignored?
 * 46113ad9:chg: --asynchronous-upload is not parsed correctly

rel.2.1.3 / 2023-10-08
======================

 * 460b81ca:fix: Intermixed argument lists cause problems
 * 4e0339fd:fix: exclude-other-filesystems seems to be ignored since duplicity 2
 * 577251f3:fix: Change backup to inc after CLI processing
 * 99233fba:fix: Fix typos in cli_data.py and release-prep.
 * ee32e57f:fix: --version showing 'duplicity_logging' not 'duplicity'
 * 6d83f048:chg: Fix typo in cli_data.py
 * e65454df:fix: --full-if-older-than being ignored?

rel.2.1.2 / 2023-09-27
======================

 * 982ee445:chg: fix archive name in release-prep.
 * a7671c06:chg: Ignore commit error in release-prep.
 * 6395ea31:fix: More argparse refinements, especially wrt. removed/changed options ...
 * 72456c16:fix: Fix mega v1 backend. Fixes #762.
 * 37e33fde:fix: Refix format of paramiko host authenticity message.
 * 6830a1a6:fix: Fix format of authenticity message.
 * e7ad4de0:fix: Add -f to lftp mkdir to ignore existing dirs.
 * d96c1017:fix: Whoops, paramiko uses MD5 not SHA256.
 * 8bd74ee8:fix: Adjust paramiko host key format to hex.
 * b5b0182d:fix: Adjust debian/control and requirements.txt.
 * 6f355912:fix: Restore s3_use_server_side_encryption.
 * fb2ecc6a:chg: Merge remote-tracking branch 'origin/main'
 * 4b374ab3:fix: issue #759 "--asynchronous-upload is not parsed correctly"
 * 76f83602:fix: Implement _retry_cleanup for ssh_paramiko
 * 7d5d6bdb:fix: Adjust azure import handling. Fixes #756.
 * 2920e882:chg: Change message in check_target_url.

rel.2.1.1 / 2023-09-02
======================

 * fc754962:fix: Pexpect backend fix
 * dd8688ef:chg: Make action command missing error message more helpful.
 * 5ae52180:chg: Allow duplicity --help and -h. Fixes #749.
 * ea8c9625:chg: Do not wrap body of git commit.
 * 211c6999:chg: Skip some tests on Launchpad.

rel.2.1.0 / 2023-08-26
======================

 * 0f4fc775:chg: Merge remote-tracking branch 'origin/main'
 * ef56ea06:fix: Implement implied commands via pre parsing. Fixes #733.
 * db2926ef:new: Skip inc backup if nothing has changed.
 * 66a40ebd:new: log a warning when using dangerous --asynchronous-upload option
 * 91068da2:fix: Replace util.fsdecode with os.fsdecode. Fixes #748.
 * a15104dc:fix: Try import of setuptools_scm. Fixes #746.
 * 33668f95:new: Keep stats in files. Fixes #722.

rel.2.0.2 / 2023-08-15
======================

 * d147528a:fix: Fixes to tools/release-prep.
 * 1a2a4af3:fix: Adjust to new azure module structure. Fixes #731.
 * 8085295e:fix: Handle --encrypt-sign-key. Fixes #736.
 * 06a4994f:fix: Fix PEP8 error.
 * 1399cce3:fix: Fix *-options commands. Fixes #732.
 * b042cb8c:fix: enable selection options for verify. Fixes #734.

rel.2.0.1 / 2023-08-08
======================

 * 76145e34:fix: Adjust regex for 2.0.0x.
 * fc8da777:fix: Restore pre-parser. Fixes #727.
 * 295e641b:fix: Add missing import to cli_util.py. Fixes #730.
 * 97fd0957:fix: Add missing import to b2backend.py. Fixes #729.

rel.2.0.0 / 2023-08-07
======================

 * 5cb97560:fix: Adjust version to build under LP.
 * 598352ba:fix: Adjust to build under LP Mantic.

rel.2.0.0x / 2023-08-07
=======================

 * 7b62e3b9:chg: Merge branch 'duplicity-py3' into main-py3
 * cc52f91d:fix: S3 backend issues. Fixes #31
 * 690aa36b:fix: Fix Exception Type for verbosity level
 * 56d585d8:chg: Improve --verbosity help.
 * afbeb408:chg: Remove implied command support for now.
 * 05d93270:chg: Remove --s3-european-buckets used by boto.
 * 6b1294f0:chg: Fix short filenames use in new s3 files.

rel.2.0.0rc2 / 2023-07-24
=========================

 * cacd9c32:chg: Fix format strings in idrivedbackend.py.
 * d662f92c:chg: Add additional CLI checks.
 * 72f18fda:chg: Fix format strings in idrivedbackend.py.
 * f344bd0b:chg: Fix format string in statistics.py.
 * 07413838:chg: Remove kerberos from snap builds.
 * 388eaccb:chg: Changes to allow building snaps.

rel.2.0.0rc1 / 2023-07-17
=========================

 * dfd542f2:chg: Fix implied command handling.

rel.2.0.0rc0 / 2023-07-10
=========================

 * a6e15afe:fix: Finish conversions to f-strings.
 * 538d6b34:fix: Convert to f-strings via 'flynt -tc -tj'.
 * b76d7e87:fix: With py2 gone remove unicode string adornments.
 * 466e7327:fix: Fix implied command when target is empty.

rel.2.0.0b2 / 2023-07-02
========================

 * 87555c39:chg: Fix syntax error in .gitlab-ci.yml.
 * 5a667546:chg: Fix website to only run with WEBSITE_TRIGGER_TOKEN.
 * 01190635:chg: Resolve some minor merge issues.
 * 75ff0d51:chg: Merge in duplicity-py3.
 * be6396c7:fix: Fix #710. Missing Content-Type header on webdav.
 * acae9132:chg: Whoops, used f-string to fix #716. Fixed.
 * 20167bf1:chg: Fix #716. Print filename on read error.
 * 0e844e6a:chg: Fix #709. Add docs on passphrase encryption used.
 * 2f0ce69f:fix: S3 filename encoding
 * 20986903:fix: Fix #712 "if cache lost. `*.sigtar.gpg` files not accessible"
 * f75e0f11:chg: Fixes for handling snaps again.
 * add59ff7:fix: handle read-only remote parent folder better in gio backend
 * b57a7d85:chg: Force cryptography<3.4 for py2 support.
 * 2437da04:chg: Fix tools release-prep & makechangelog.
 * 3ef92b09:chg: Fix tools/release-prep.
 * 6bed4876:fix: Use cryptography == 3.4.8.
 * 5aca6d29:new: Xorriso backend for optical media
 * de39e34c:fix: Warn rather than fail on op-not-supported restore errors
 * 2d83b920:fix: Fixes #701 - unable to resume full backup to B2.
 * 220a5c6f:chg: Fix spelling errors.
 * 6cb82cf5:fix: Fixes #698 - backups without GPG decryption key.
 * 5dc39789:fix: Fixes #698 - backups without GPG decryption key.
 * 01359578:chg: Cleanup. Add 'unsquashfs -l' test from @ede.
 * 6e3af59b:fix: Fixes #686 - PCA backend does not unseal volumes.
 * 1d5ff95b:fix: Revert to medieval string formatting.
 * dfcc1611:fix: Revert to medieval string formatting.
 * 6ad573bb:fix: Revert to medieval string formatting.
 * 308b4053:fix: Revert to medieval string formatting.
 * 3e8dd7d6:fix: Remove dependency scanner.
 * 1db7652c:fix: Fix PEP8 and todo issues.
 * 395553ee:fix: Misc fixes to testing/build environ.
 * dcd29f0c:fix: Encoding errors when logging. Fixes #693.
 * cf2e2093:fix: Onedrive may hang indefinitely. Fixes #695.
 * 305aa82d:chg: Update Makefile 'make clean' list.
 * cd6d2b96:chg: fix run website ci call after pushes/releases
 * 4af6f3ea: fix typo
 * d823ae7e: try to fix
 * f9a155cc:new: Onedrive for Business Support
 * 1811956b:chg: Update version for Launchpad.
 * 545fda03:chg: Update duplicity.pot.
 * e011b550:fix: Fix to work with b2sdk 1.19.0
 * ddacbf93:fix: Fix #692. Redundant --encrypt option added in gpg.py.
 * 72a373af:fix: Regression on issue #147, change password for incremental.
 * 00ef3807: Merge remote-tracking branch 'origin/main'
 * e11ccfc1:fix: Crash if a socket is listed with --files-from. Fixes #689.
 * 9acfb505: add detailed step-by-step instructions
 * 17a7c1d0:chg: More changes to get release process working.
 * 0a3617a5: Merge remote-tracking branch 'origin/main'
 * d7b9a522:chg: Fix for setuptools changes. Add testing data files to mix.
 * c082b722:chg: Update duplicity.pot.
 * 0d7b7422:fix: Fix for issue #683.
 * a4820c80:chg: Remove gpg_error_codes.py / update duplicity.pot.
 * 767322fc:chg: Fix name in .gitlab-ci.yml.
 * fda4ad84:chg: Go back to standard tests, no master image.
 * 9dfe8f8e:chg: Go back to standard tests, no master image.
 * 9153c5f8:chg: Go back to standard tests, no master image.
 * df06df9e:chg: Go back to standard tests, no master image.
 * 244100a1:chg: Go back to standard tests, no master image.
 * e81f8d96:chg: Go back to standard tests, no master image.
 * 198e2e42:chg: Add testing for Python 3.11.
 * bc158f7d:new: Add rsync style --files-from=FILE. Fixes #151.
 * f692aa03:chg: Update deprecation messages. Cleanup.
 * 76f92788:chg: Reformat / cleanup Makefile.
 * 102271fc:chg: Fixup help entries in Makefile.
 * e5feb6a1:chg: Remove targets xlate-*. Add target pot.
 * 55163f1e:chg: Change Crowdin commit message.
 * dc432294:fix: Azure Blob Storage backend fails to resume. Fixes #149.
 * 456e04d8:fix: Went to aggressive on cleanup().
 * 3de878f3:chg: Update po/duplicity.pot.
 * 9a8fc346:chg: Cleanup and make sure setup cleans po dir.
 * 9c508e46:chg: fix version, oversight in previious commit
 * 2c487cbe:chg: fix snap build for non-amd64 archs
 * f9a9d894:chg: Add filter mode to log line. #138
 * 91b237cb:chg: Fix emacs mode line.
 * a1034c89:fix: Fix about 20 pep8 issues.
 * b46fc2fc:new: Add literal include/excludes. Fixes #138.
 * 1ecdce37:fix: More fixes to po/update-po.
 * 98420557:fix: Fix po/update-pot to leave po/LINGUAS in po.
 * c93a1e2a:fix: Nuke LP translations.
 * b49f1360:fix: Revert changes to gpg_failed().
 * 6647ee7c:chg: Various cleanups to code and tests.
 * 6b0782b4: Merge remote-tracking branch 'origin/main'
 * 35531fe4:chg: Accept all .po files for LINGUAS gen.
 * a7e097d0:chg: Build control files for update-pot.
 * 99ce4986: Update Crowdin configuration file
 * ded1dcb2:chg: Accept all .po files for update-pot.
 * 3af2de3d:chg: Build control files for update-pot.
 * 93e961a7: Update Crowdin configuration file
 * 05f45f6b: Update Crowdin configuration file
 * 5d8e9dcd: Update Crowdin configuration file
 * a357124c:chg: Add tags to commit message.

rel.2.0.0b1 / 2023-06-30
========================

 * d4d6168d:chg: Some basic PEP8 and code cleanup.
 * ba42f56c:chg: Set socket default timeout in CLI.
 * 3fc175d8:chg: Fixes for deprecated/changed options.

rel.2.0.0b0 / 2023-06-24
========================

 * afbb2678:chg: Fix #24. Allow users to tune copy block size.

rel.2.0.0a2 / 2023-06-14
========================

 * 44c1b412:chg: Remove pathvalidate from use. Fixes #27.

rel.2.0.0a1 / 2023-06-14
========================

 * 3618b22f:chg: More CLI improvements.
 * 00aff999:chg: Add implied backup/restore back.
 * 7f9b9a50:chg: CLI improvements and cleanup.
 * b051c882:chg: Minor cleanup, rm dead code.
 * de560074:chg: "--ignore-errors" gets proper handling in CLI.
 * bcfcd4c6:fix: Fix #22, “--no-compression” doesn't have effect.
 * 44840c52:fix: Fix .gitlab-ci.yml file syntax error.

rel.2.0.0a0 / 2023-06-01
========================

 * 6d5476da:chg: Fix initial version.
 * b674f437:chg: Give up. Let setup mangle as it will.
 * daf39cfc:chg: Use semver tags, let setup mangle.
 * 3c4cba8e:chg: Make PEP 440 compatible, not semver yet.
 * ff495158:chg: Changes to allow alpha, beta, rc prerelease.
 * e8f4aece:chg: remove 'rdiffdir'. Not used.
 * 55d9eabf:chg: add 'make sdist' to Makefile.
 * 972635fb:chg: update .gitignore.
 * 4b6b9dfb:chg: setuptools_scm.get_version now uses 'fallback_version'.
 * 7f1e0db3:chg: Remove old s3_boto_backend.py.
 * 3e044081:chg: Remove spaces in version specs.
 * 11d66fd4:fix: Add a missing super() call in path.py.
 * 5ab38c8e:fix: add a missing method to some super calls
 * c68e3464:chg: Cleanup py2 cruft and more.
 * 9f4c9de3:chg: Cleanup py2 cruft and more.
 * 6bafc799:chg: Uncomment log.test_command_line_error
 * 364ae5a7:chg: raise CommandLineError on deprecated/changed options.
 * f5e8f9b6:chg: Whoops, don't move import_backends.
 * 15941e8f:chg: Fix code, tests, and do cleanup.
 * afc55b2d:chg: Requirements and code cleanup.
 * bba33ad3:chg: Whoops, fix code style.
 * b98c5666:chg: Add error/ignored msg for deprecated options.
 * a9da48dd:chg: Some cli cleanup for subcommands.
 * adeb19e9:chg: Normalize error handling in cli_util.py.
 * 6a8a7667:chg: Some small command line fixes.
 * 5b8fd3be:chg: Clean out the last py2 cruft, I hope.
 * 500e21a6:chg: Change optparse to argparse. Checkpoint.
 * b8a62734:chg: Change optparse to argparse. Checkpoint.
 * b510a8df:chg: Change optparse to argparse. Checkpoint.
 * 47fbd14f:chg: Change optparse to argparse. Checkpoint.
 * f8813d2f:chg: Change optparse to argparse. Checkpoint.
 * 2d599c54:chg: Change optparse to argparse. Checkpoint.
 * d3319384:chg: Some py2 to py3 cleanup.
 * 90c08ab5:chg: Change optparse to argparse. Checkpoint.
 * 78a9e6df:chg: Change optparse to argparse. Checkpoint.
 * fb591b32:chg: Change optparse to argparse. Checkpoint.
 * d6d22b90:chg: Change optparse to argparse. Checkpoint.
 * 0eb768c1:chg: Change optparse to argparse. Checkpoint.
 * 19375606:chg: Change optparse to argparse. Checkpoint.
 * 6cbd32fd:chg: Change optparse to argparse. Checkpoint.
 * 76e0256b: Merge remote-tracking branch 'alpha/duplicity-py3' into duplicity-py3
 * 8323396d:chg: Change optparse to argparse. Checkpoint.
 * 938ea10c:chg: Change optparse to argparse. Checkpoint.
 * 5484182d:chg: Change optparse to argparse. Checkpoint.
 * 964c0ba7:chg: Change optparse to argparse. Checkpoint.
 * 85747071:chg: Change optparse to argparse. Checkpoint.
 * ba4d2e81: Merge remote-tracking branch 'alpha/duplicity-py3' into duplicity-py3
 * b3048a59: Merge remote-tracking branch 'alpha/duplicity-py3' into duplicity-py3
 * f74c4d15:chg: Change optparse to argparse. Checkpoint.
 * 580fa4f0:chg: Change optparse to argparse. Checkpoint.
 * cd8d3634:chg: Fix version and required python version.
 * 4a5b003a:chg: Fix version and required python version.
 * 72cbcf97:chg: More refactoring and cleanup after merge.
 * 09d2420c:chg: More refactoring and cleanup after merge.
 * 221fb7c5: Merge branch 'main' into branch 'duplicity-py3'
 * bb3b1fbd: Merge branch 'main' into branch 'duplicity-py3'
 * 9406ce28:chg: Change optparse to argparse. Checkpoint.
 * ff165dfb:chg: Change optparse to argparse. Checkpoint.
 * f75fc5fd:chg: Change optparse to argparse. Checkpoint.
 * 046d199a:chg: Change optparse to argparse. Checkpoint.
 * d3667b20:chg: Change optparse to argparse. Checkpoint.
 * 8fdd91ef:chg: Change optparse to argparse. Checkpoint.
 * fc656ee8:chg: Change optparse to argparse. Checkpoint.
 * 1c1a7cb9:chg: Change optparse to argparse. Checkpoint.
 * 6e565d52:chg: Change optparse to argparse. Checkpoint.
 * b99a2ff5:chg: Change optparse to argparse. Checkpoint.
 * 66a59050:chg: Change optparse to argparse. Checkpoint.
 * c539c191:chg: Change optparse to argparse. Checkpoint.
 * a50a5dac:chg: Change optparse to argparse. Checkpoint.
 * e057a3bd:chg: Change optparse to argparse. Checkpoint.
 * 3694b0c8:chg: Change optparse to argparse. Checkpoint.
 * fbc6e6fe:chg: Change optparse to argparse. Checkpoint.
 * e2b7166a:chg: Change optparse to argparse. Checkpoint.
 * e82e9bd9:chg: Change optparse to argparse. Checkpoint.
 * d4d5c3a2:chg: Change optparse to argparse. Checkpoint.
 * eae14f0a:chg: Change optparse to argparse. Checkpoint.
 * a2edcc90:chg: Change optparse to argparse. Checkpoint.
 * 1e220982:chg: Change optparse to argparse. Checkpoint.
 * e9527bec:chg: Change optparse to argparse. Checkpoint.
 * e93ae31e:chg: Change optparse to argparse. Checkpoint.
 * 54e47489:chg: Change optparse to argparse. Checkpoint.
 * 903b068f:chg: Change optparse to argparse. Checkpoint.
 * 732d8686:chg: Fix version and required python version.
 * c9088f07:chg: Fix version and required python version.
 * a9ab58bf:chg: Fix version and required python version.
 * d1f76dd5:chg: Fix version and required python version.
 * 09c24bb3:chg: More refactoring and cleanup after merge.
 * 3ad81e3e:chg: More refactoring and cleanup after merge.
 * b0099a70: Merge branch 'main' into branch 'duplicity-py3'
 * d5ecdee0: Merge branch 'main' into branch 'duplicity-py3'
 * 429afccf:chg: Change optparse to argparse. Checkpoint.
 * d687f5eb:chg: Change optparse to argparse. Checkpoint.
 * 614d5514:chg: Change optparse to argparse. Checkpoint.
 * 89823744:chg: Change optparse to argparse. Checkpoint.
 * 5c44870e:chg: Change optparse to argparse. Checkpoint.
 * cfbd76f0:chg: Change optparse to argparse. Checkpoint.
 * ecfa798c:chg: Change optparse to argparse. Checkpoint.
 * 9143a167:chg: Change optparse to argparse. Checkpoint.
 * fc4e36d1:chg: Change optparse to argparse. Checkpoint.
 * 52455bb8:chg: Change optparse to argparse. Checkpoint.
 * e2ea30b5:chg: Add Note on --time-separator in manpage.
 * 0bd83d2f:chg: Add Note on --time-separator in manpage.
 * 18961f1f:chg: Remove refs to --old/short-filenames. Fix CI.
 * 31066fd2:chg: Remove refs to --old/short-filenames. Fix CI.
 * 2f179d2f:chg: Remove deprecated --short-filenames code.
 * ce583090:chg: Remove deprecated --short-filenames code.
 * 453e015d:chg: Remove deprecated --old-filenames code.
 * 8b1884d1:chg: Remove deprecated --old-filenames code.
 * 0f18af4b:chg: Remove deprecated --gio code.
 * efc014b3:chg: Remove deprecated --gio code.
 * ef467bca:chg: Remove globbing deprecated code.
 * 7b863a77:chg: Remove globbing deprecated code.
 * 03701327:chg: Remove stdin deprecated code.
 * 4f1a2d0c:chg: Remove stdin deprecated code.
 * bdc1b4dc:chg: Remove incomplete replicate command.
 * 606fb53e:chg: Remove incomplete replicate command.
 * 7a7e2ac2: Merge branch main into branch duplicity-py3.
 * 30e28ba6: Merge branch main into branch duplicity-py3.
 * 5520f128:chg: Remove LINGUAS. Replace with globbing.
 * b632218d:chg: Remove LINGUAS. Replace with globbing.
 * ccdb8eb1:fix: Nuke LP translations.
 * 3bdc90be:fix: Nuke LP translations.
 * 272f578d:chg: More cleanup from inspections.
 * 847bf6f8:chg: More cleanup from inspections.
 * 90a26a3e: Merge branch cleanup into branch duplicity-py3.
 * 95d81eb8: Merge branch cleanup into branch duplicity-py3.
 * c5af0330:chg: util.fsdecode ==> os.fsdecode.
 * 45defd3a:chg: util.fsdecode ==> os.fsdecode.
 * a74d2daa: Merge main into duplicity-py3.
 * 8a38a6b9: Merge main into duplicity-py3.
 * d268c567: Merge remote-tracking branch 'origin/duplicity-py3' into duplicity-py3
 * d3f2ad93: Merge remote-tracking branch 'origin/duplicity-py3' into duplicity-py3
 * 9acf9135: Merge main into branch duplicity-py3.
 * bce7130a: Merge main into branch duplicity-py3.
 * 3ac62bd1:chg: Update README-SNAP.md to show options.
 * 2327b8c7:chg: Add instructions for building snaps.
 * 5f20c2c7:fix: Replace pydrive with pydrive2. Fixes #62
 * 0c378739:chg: add missing license metadata
 * 010a6e92:chg: More docker cleanup.
 * faf32c60:chg: trigger website rebuild on pushes/tags
 * 9803f2fd:chg: More docker cleanup.
 * e68c5761:chg: More docker cleanup.
 * fd1d0405:chg: Optimize build of duplicity_test image.
 * e01343d2:fix: Add missing ':''.
 * 60c89698:fix: Add missing ':''.
 * 2ab58710:fix: Remove requirement for kerberos.
 * 44e808b5:fix: Remove requirement for kerberos.
 * 71bd8b8d:fix: Remove most 'pylint: disable=import-error'.
 * c913cd32:fix: Remove most 'pylint: disable=import-error'.
 * 7aa52d12:fix: Fix more py3 problems.
 * 4a56c821:fix: Fix more py3 problems.
 * 356ff324:fix: Recurse glob to include duplicity/backends.
 * 39e9f319:fix: Recurse glob to include duplicity/backends.
 * f9ea4e4a:fix: Remove extra print statement.
 * f9862a5e:fix: Remove extra print statement.
 * e7383e70:fix: Add back test_unadorned... Cleanup.
 * bb1323f0:fix: Add back test_unadorned... Cleanup.
 * d4550426:fix: Merge current issue125 branch.
 * 56bcd371:fix: Merge current issue125 branch.
 * 10d4ddcc:fix: Fix indentation cause by adorning.
 * 5ade0634:fix: Fix indentation cause by adorning.
 * 4c8af238:fix: Adorn python strings to make merges easier.
 * efe1447b:fix: Adorn python strings to make merges easier.
 * c96becfa:fix: Remove extra newline in print.
 * 1478f77b:fix: Remove extra newline in print.
 * b59d0a2f:fix: Add list_python_files to tools.
 * 0de565d1:fix: Add list_python_files to tools.
 * 2e18cf9c:fix: Move find/fix un/adorned to tools.
 * a3b8d92f:fix: Move find/fix un/adorned to tools.
 * 10ddc907:fix: Unadorn bin/duplicity and bin/rdiffdir.
 * b72e458f:fix: Unadorn bin/duplicity and bin/rdiffdir.
 * ec887b7f:fix: Recover and add find/fix un/adorned strings.
 * b1d8626b:fix: Recover and add find/fix un/adorned strings.
 * 56aaab81:fix: Fix PEP8 issue.
 * e2622406:fix: Fix PEP8 issue.
 * 56c9140d:fix: Optimize imports.
 * eb5b761c:fix: Optimize imports.
 * c623c7a8:fix: GDrive backend: Add environment args for configuring oauth flow
 * 7cb65f39:fix: Optimize imports.
 * a5735e55:fix: Optimize imports.
 * a44deeae:fix: Use os modules fsencode/fsdecode not ours.
 * a297ac8a:fix: Use os modules fsencode/fsdecode not ours.
 * 21969275:fix: GDrive backend: For Google OAuth, switch to loopback flow
 * 74195614:fix: Fix case where gpg return code is None.
 * 00518250:fix: Fix case where gpg return code is None.
 * bfd2e3a9:fix: Reduce number of GPG file descriptors, add GPG translatable errors
 * 69c39dd2:fix: Remove redundant code.
 * d32feceb:fix: Remove redundant code.
 * e6472be6:fix: Print stderr on gpg fail plus error code and string.
 * 6215144c:fix: Print stderr on gpg fail plus error code and string.
 * 7404e887:fix: Fix handling of gpg_error_codes.
 * b69dfc4f:fix: Fix handling of gpg_error_codes.
 * 7852da97:fix: Add _() for translations of msgs in gpg_error_codes.py
 * 30dbed9c:fix: Add _() for translations of msgs in gpg_error_codes.py
 * fa4d9471:fix: Add stderr_fp back in. Too much noise otherwise.
 * 3031885d:fix: Add stderr_fp back in. Too much noise otherwise.
 * ff55ddb1:fix: Remove stderr_fp and use process return code to report errors.
 * 2fd3a986:fix: Remove stderr_fp and use process return code to report errors.
 * ba583b12:fix: Remove status_fd if no sign_key in gpg.py.
 * 47a9064f:fix: Remove status_fd if no sign_key in gpg.py.
 * 6704e0e0:fix: Cleanup, remove test_2to3.
 * 1afc9de2:fix: Cleanup, remove test_2to3.
 * 2d9236ab:fix: Cleanup, remove all uses of logger_fd.
 * 0c6aea66:fix: Cleanup, remove all uses of logger_fd.
 * 56c7cdfe:fix: Add back status_fd for signature verification.
 * 235f15a9:fix: Add back status_fd for signature verification.
 * 52be14ea: Merge branch 'main' into issue125
 * d64adc2c: Merge branch 'main' into issue125
 * 2940a2ce:fix: Remove unused GPG file handles.
 * 10236bc5:fix: Remove unused GPG file handles.
 * 61de7dee:fix: Remove support for Python 2.7. Second pass.
 * c3c43552:fix: Remove support for Python 2.7. Second pass.
 * 219c2ae4:fix: Remove support for Python 2.7. First pass.
 * 5505fb51:fix: Remove support for Python 2.7. First pass.
 * 026b2e3f: Merge remote-tracking branch 'alpha/main'
 * 115583c4: Merge remote-tracking branch 'origin/main'
 * d118a710: Merge remote-tracking branch 'alpha/main'
 * 76aba8e3:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * 1078d8aa:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * 0390d3e2:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * 4a5ff171:fix: Remove sign-build step. Does not work.
 * 979b2099:fix: Add back overzealous removal of 'import re'.
 * 2420ea5f: Merge remote-tracking branch 'origin/main'
 * c0751cbc: Merge branch 'main' of gitlab.com:AlphaPrime/duplicity
 * 749ae666: Merge remote-tracking branch 'origin/main'
 * 06c358bf:fix: webdav listing failed on responses with namespace 'ns0'
 * 1f9673f4:chg: Add limits to chardet and urlllib to keep requests quiet.
 * 907afd21:chg: Add limits to chardet and urlllib to keep requests quiet.
 * ff0d6476:chg: Action and Audience must be lowercased.
 * ca500d73: Merge branch 'main' of gitlab.com:duplicity/duplicity
 * ed327934:chg: New os_options for SWIFT backend.
 * cfd2f6d9: Merge branch 'main' of gitlab.com:duplicity/duplicity
 * da42202b:fix: Fix build of apsw/sqlite3 bundle. Don't store apsw in repo.
 * 1da483d1:chg: Change from master to main branch naming.
 * b8f453cc:chg: Better defaults for S3 mac procs and chunk sizing
 * 916426ad:chg: --s3_multipart_max_procs applies to BOTO3 backend also
 * 743bb4e9:fix: Make sure that FileChunkIO#name is a string, not a bytes-like object.
 * 89d3fd9e:fix: Fix possible memory leaks. Fixes #128. Fixes #129.
 * 192afb1b:chg: Fix modeline, change utf8 to utf-8 to make emacs happy.
 * bb535323:chg: Replace pexpect.run with subprocess_popen in par2backend.
 * 034e5ff4:fix: Additional fixes/checks for pexpect version. Fixes #125.
 * b0eaa1a0:fix: Fixes #125. Add use_poll=True to pexpect.run in par2backend.
 * e88f66ce:fix: Fix issue #78 - Retry on SHA1 mismatch.
 * 9058e4b7:chg: Add py310 to list of versions supported.
 * 4f3a5a54:chg: Fix script pushsnap to handle errors.
 * 108d164e:chg: Add returncode to BackendException for rclonebackend.
 * 5941aa54:chg: snap use core20 coreutils if none in PATH env var
 * 6d0a413f:chg: Need to install python3 for pages.
 * 081a54de: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * c6fbce08:chg: Don't push to savannah any more.
 * 7f645f3b:chg: Fix version for builds.
 * 0dd5b6be:fix: Install requirements.dev.
 * 551367f5:chg: Fix PEP8 issue.
 * 7410fb68:fix: Fix LP bug #1970124 - obscure error message.
 * 2b68f57c:new: Add --webdav-headers to webdavbackend. Fixes #94
 * 714bc930:chg: Remove build on merge request and unused variables.
 * 0bef4918: pkg:fix: make extra sure correct python binary is used
 * 2eeb7daf:chg: Cosmetic changes only.
 * 34ca7b1c:chg: Make pages manual deploy.
 * baa81312: Merge remote-tracking branch 'origin/clean-dist'
 * 19571d56:chg: Changelog removed, remove needs.
 * 5c56a64e:chg: Only build pip and snap, don't push.
 * 986e8a50:new: Add tests for Python 3.10.
 * bfac95d1:chg: Remove deploy jobs needing secret keys.
 * bc607694:chg: Fix misspelled stage name.
 * 40338f74:chg: fix deps format.
 * b0fedcb2:chg: fix deps format.
 * 6445045d:chg: Add requirements.dev to tox.ini.
 * 6ac85669:chg: Include pydevd in requirements.txt.
 * 7650bbed:chg: Go back to ubuntudesktop/gnome-3-38-2004.
 * 530a4ef3:chg: Add tools dir to changes list in deploy-template.
 * 353554ca:chg: Try snap with utuntu:20.04. Fix artifacts loc.
 * 831b40ae:chg: Some debugging statements.
 * 37e21461:chg: Some debugging statements.
 * cf1e462c:chg: Set up the SSH key and the known_hosts file.
 * 6e448f37:chg: Set up config for git.
 * f6fd051a:chg: Clone repo so setuptools-scm works properly.
 * 5393c5cb:chg: Move setuptools* to .dev. Nuke report.xml artifact.
 * 23a17ccc:chg: Add some more requirements.
 * fe89bbc3:chg: Install git and intltool for changelog.
 * f4de6727:chg: Add changes: to deploy-template.
 * f2201806:chg: Fix syntax.
 * 832eadd0:chg: Minimize CI/CD overhead.
 * 57663915:chg: Split requirements into .txt and .dev.
 * c91d1d09:chg: Standardize startup sequence.
 * ede4182c:chg: Do not supply user/password to twine, just access token.
 * cb221158:chg: Do not supply user/password to twine, just access token.
 * 939c091a:new: Make sdist only provide necessary items for build.
 * c6df8dc0:chg: Add default never to .test-template.
 * 35591b04:chg: Change PYPI_ACCESS_TOKEN back to variable and just echo it.
 * 790dc9a2:chg: Just cp PYPI_ACCESS_TOKEN to ~/.pypirc
 * a5f4945f:chg: Fix usage of PYPI_ACCESS_TOKEN.
 * 754b394d:chg: fix conflicts
 * 1d051ef3:chg: Set to run deploy only after a push event.
 * 3138d6b2: Optimize CI/CD to only run when needed
 * 431dc6a4:chg: Whoops, can't run deploy on source branch to merge.
 * 71218263:chg: Use rules in templates. Always run on merge requests.
 * ebb07305:chg: Always run pipeline on merge request event.
 * f294f985:chg: Make sure we run all during merge requests.
 * 09005b01:chg: Add deploy-template to only run when source changes.
 * e65a38f7:chg: Fix to only run tests if source code changes.
 * 4981dd34:chg: If no changes, exit 0 to allow pip and snap builds.
 * 51bb3930:chg: Set up pypi access token for uploading.
 * cb044377:new: Add changelog to deploy stage to build CHANGELOG.md.
 * fb55c0a8:chg: keep pip build artifacts for 30 days as pipeline artifacts
 * 0836658d: Merge remote-tracking branch 'origin/rclone_options'
 * b559eec5: Merge branch 'duplicity-core20' of git@gitlab.com:duplicity/duplicity.git into duplicity-core20
 * 7db7ab97:chg: Skip tests, not ci, so we can build snaps, pips, pages, etc.
 * 6874dc58:chg: Allow non-Docker environs to sign snaps.
 * f2960b85:chg: Allow GitLab CI to upload snaps to the store.
 * c0cea90c:chg: Update or add copyright and some cosmetic changes.
 * 821a58b1:new: enable CI snapcraft amd64 builds with docker
 * 50656438:chg: Remove install of snapcraft, snap, snapd.
 * 34dd70c8:chg: Add grpcio-tools to top to get latest version.
 * 4a3eb632:chg: Remove conflicting build env variable. Nuke evil tabs.
 * c8a2a837:chg: Allow duplicity-core20 to run deploy steps, for now.
 * 16452f93:chg: Install snapcraft snap snapd.
 * 1898a751:fix: Nuke a couple of false pylint errors, use inline disable.
 * b829ccb3:fix: Nuke a couple of false pylint errors, fix spelling.
 * 961eb9c8:chg: Allow pip and snap builds from branches for now.
 * a726b909:chg: Add build_snap and build_pip back.
 * add0ff01:fix: Nuke a couple of false pylint errors.
 * 799119d4: Merge remote-tracking branch 'origin/master' into duplicity-core20
 * 5cee78db:chg: More tests for tools/testsnap
 * 469c6350:chg: More snapcraft.yaml fixups.
 * 7f968c57:new: fix other archs, expose rdiffdir
 * e1eb4939:fix: minor formatting fix
 * 4e7f65b7:fix: fixup some minor formatting issues
 * 6a93d5e6:new: demote boto backend to legacy ...
 * 6aa7b664:new: promote boto3 backend to default s3:// backend ...
 * ef6ef52e:chg: Add further checks to testing for backup and multi-lib.
 * 3e7496a3:chg: Remove SNAPCRAFT_PYTHON_INTERPRETER per edso, no change on U20.
 * e4a4e81a:chg: Try to force Python 3.8 only.
 * 1b97fcdf:chg: More detailed error message.
 * 2693f97b: Merge branch 'duplicity-core20' into 'master'
 * 8765916c: upgrade to base core20
 * b4a5feb1:chg: Divide makesnap into makesnap, testsnap, and pushsnap.
 * ac1120ee: Merge branch 'website_links' into 'master'
 * 85a76122:chg: Revert to core18. core20 is still unusable.
 * e41e833c: switch website to gitlab.io, promote duplicity.us
 * 6154cbc3: fix website link
 * df6eed72:fix: Add --no-files-changed option. Fixes issue #110.
 * 87ee7e1c:chg: Changes to run on Focal with core20.
 * bc5ca889:chg: Use multiple -m options on commit to split comment.
 * 016b6c08:chg: Remove build-pip and build-snap. Build locally for now.
 * 5a43d899:chg: Remove build-pip and build-snap. Build locally for now.
 * 8956a854:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * fc6403e6:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 8789e202:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * e8bd420f:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * db61970c:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 6e11a000:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * c8618a9e: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 03a6deee:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 6c9cfbc6:chg: Remove sudo.
 * c20c6e08:chg: core20 usess py38, not py36.
 * 718892fa: Revert "chg:dev:core20 usess py38, not py36."
 * c074a356:chg: core20 usess py38, not py36.
 * 21137218:chg: Attempt core20 again.
 * 4e0ff6d8:chg: Fix syntax.
 * a7403e3b:chg: Remove unneeded Dockerfiles. Rename.
 * a35d934d:chg: Try remote snap build.
 * ff271933:chg: Remove unneeded Dockerfiles. Rename.
 * f995c276:chg: Cosmetic fixes.
 * 77301e26:chg: Try forcing snaps to use python3.6 in 18.04.
 * 313af8b4:chg: Add check for correct platform.
 * 5e92e7e6:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 689aa4cc:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * f1f23055:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 1ca58b56:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * d1e07c7f:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * f371f526:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * e259663f:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 585960cd:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * bf97f527:chg: Add warning for replicate command. See issue #98.
 * df21af40: Merge branch 'filecoin-backend' into 'master'
 * 9fc13528: Slate Backend
 * dd7a283d:fix: Fix use of sorted() builtin (does not sort in place).
 * 209c8e57:chg: Minor tweaks.
 * 86c77df7:chg: Add wheels to .gitignore.
 * 25f8c66d:chg: Cosmetic changes.
 * aca274a5:chg: Add collection-status at end of test.
 * 0ba16e10:fix: Revert snapcraft.yaml to build on core18. core20 was flakey.
 * b8d279df:fix: Fix #107 - TypeError in restart_position_iterator.
 * 579a5c18:fix: Need to pass kwargs to BaseIdentitu.
 * 5ee6c55d:fix: Fix __init__ in hubic.py. Fixes #106.
 * 6bd386d8:fix: Try building snap on core20.
 * 8b82f36d:fix: Try building snap on core20.
 * 28b3d2e7:fix: Somehow missed boto when doing #102. Now supported.
 * 6c0ba35a:new: Add --use-glacier-ir option for instant retrieval. Fixes #102.
 * 6b34bec6:new: Add manual test for issue 100.
 * 3317c415:chg: Remove gpg socket files during clean.
 * e958f6e0:new: Add option --show-changes-in-set <index> to collection-status.
 * d199103e:chg: Back off to default image.
 * 917cd67f:chg: Try adding apt-get upgrade.
 * 7575bfca:chg: Add .test-template to allow skipping qual and tests.
 * e786c59c:chg: Try build with apt-get update
 * eadd63c0:chg: Try building snap on 20.04.
 * 255e0567: Merge branch 'mr-origin-75'
 * 29d4f373:fix: Fix logic of skipIf test.
 * a7c71f69:chg: More changes to xlate-* for LP translations.
 * 4fc596be: Skip tests for ppc64le also
 * dd5fa9e6:chg: Add targets to manually import/export translations.
 * f29c7222:chg: Update duplicity.pot for LP translation.
 * e176b42d:chg: Ignore 'LP translations' commits.
 * 2875517f: chg:pks:Revert commit of LP translations.
 * 1f36775b: Revert "chg:pkg:Import LP translations."
 * f9bc1a8d:chg: Import LP translations.
 * c0189127:fix: Fix data_files AUTHORS to CONTRIBUTING.md.
 * 7f8041a7:chg: Revert "Put out first 'post' release to fix pypi issue".
 * d607e3c8:chg: Put out first 'post' release to fix pypi issue.
 * 82a40349:chg: Rename AUTHORS to CONTRIBUTING.md.
 * a794cfab:chg: Rename dist dir to tools to avoid collision with setuptools.
 * 9151301a:new: Add release-prep.sh for release preparation.
 * 365065a8:new: Add py310 to envlist to test against python 3.10.
 * a19b1e69:chg: When buiilding for amd64 build snap locally, else remote.
 * b526f096:fix: Fix #93 - dupliicity wants private encryption key.
 * cbcd917c:fix: PAR2 backend failes to create par2 file with spaces in name.
 * dcfe6f94:fix: Fix bug 930151 - Restore symlink changes target attributes (2)
 * e94205bc:fix: Fix LP bug 930151 - Restore a symlink changes target attributes
 * e1d5ace3:fix: Fix #89 part 2 - handle small input files where par2 fails.
 * ddde782c:fix: Fix PEP8 issue.
 * 24025ab1:fix: Fix #90 - rclone backend fails with spaces in pathnames.
 * 8c9d8452:fix: Fix #89 - Add PAR2 number volumes option.
 * 971c2b74:fix: Fix #88 - Add PAR2 creation failure error message.
 * db85a25d:fix: Fix bug #87, Restore fails and stops on corrupted backup volume
 * 4b2d674a:fix: Fix bug #86, PAR2 backend fails on restore, with patch supplied.
 * 9a987b6c:fix: Fixed Catch-22 in pyrax_identity.hubic. Debian bug #996577
 * 5095042b:chg: Fix command line warning messages.
 * 1a9799e1:chg: Fix clean command to include module doc .rst files.
 * 463f5409:chg: Forgot to add myst-parser. Comment out tests for now.
 * 9ee80f62: new:Add update of API docs to deploy step.
 * b8e6f930: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 9496cc2a: Merge branch 'issue73' into 'master'
 * 704d8d3e: resolve os option key naming mismatch
 * 9c384b5a: Merge branch 'master' into 'master'
 * c4036981: Set up gdrive client credentials scope correctly
 * 44773860: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * b4023bda: Merge branch 'y0va-master-patch-75623' into 'master'
 * cea955d1: Merge branch 'issue85' into 'master'
 * f2e0c743: upgrade docker test environment
 * 771c6a03: don't query for filesize.
 * dc313f28: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 19ef7d7a: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 443402c7: Merge branch 'mr4' into 'master'
 * 3855f247: Fix TypeError.
 * 8febe9f8:chg: Whoops, left out import sys.
 * 707be9f7:chg: Skip test to allow py27 and py35 to pass.
 * f119356c:fix: Fix issue #81 - Assertion fail when par2 prefix forgotten.
 * 96fa77f8:chg: Some tweaks to run cleaner.
 * 7d950886:fix: Fix issue #79 - Multibackend degradation.
 * 641a0e25:fix: Add verbose exception on progress file failure.
 * b0693761: Merge branch 'mr3' into 'master'
 * 898f28c1: Merge branch 'mr2' into 'master'
 * 273d03ba: Merge branch 'mr1' into 'master'
 * ac139078: SSHPExpectBackend: Implement _delete_list method.
 * 870d57b9: MultiBackend: Don't log username and password.
 * 5bd14df9: Fix NameError.
 * 05d260ea:chg: Fix typo in test selection.
 * 063eba9e: Merge branch 'onedrive-token-take2' into 'master'
 * 25caace6: onedrive: Support using an external client id / refresh token
 * 092eb039: Merge branch 'fix-tmdir' into 'master'
 * bc224403: Merge branch 'date' into 'master'
 * bbc2000f: fix functional tests when _runtestdir is not /tmp
 * 902e61d2: Allow to override manpage date with SOURCE_DATE_EPOCH
 * debe89ce: Merge branch 'origin/merge-requests/61'
 * 030f9325:chg: Remove redundant call to pre_process_download_batch.
 * 8748c50c:chg: Fix mismatch between pre_process_download[_batch] calls.
 * 908f5ef8: Remove backup file.
 * a2a5f304: Don't skip CI
 * 9dba3ad8: Improved management of volumes unsealing for PCA backend For PCA backend, unseal all volumes at once when restoring them instead of unsealing once at a time. Use pre_process_download method already available in dup_main. Need to implement it on BackendWrapper and Multibackend as well.
 * 908b1e64: Merge branch 'master' into 'master'
 * 3ecfea83: Add support for new b2sdk V2 API
 * 60d38e07:chg: build_ext now builds inplace for development ease.
 * c5ab5a4e:chg: Remove lockfile to avoid user confusion.
 * efbad2da:fix: Release lockfile only once.
 * 5d208eb3:fix: Release lockfile only once.
 * 2f8231a7: Merge branch 'master' into 'master'
 * 116058bc:chg: Fix Support DynamicLargeObjects inside swift backend
 * d32eb304: Merge branch 'issue#68' into 'master'
 * 79e25a50: have duplicity retry validate_block so object storage can report correct size
 * d7d7cba8:chg: Fix makechangelog to output actual problems.
 * fad60dcc: Merge branch 'master' into 'master'
 * e292689e: Replace b2sdk private API references in b2backend with public API
 * f034e44a:chg: Add dependency scanning.
 * c259f6e2:chg: Make sure changelog is only change to commit.
 * 4d3ebf60:chg: Fix indentation.
 * 4ec4c48c:fix: Support -o{Global,User}KnownHostsFile in --ssh-options
 * 25a20fcd:fix: Add pydrive2 to requirements.txt.
 * 7ea0d094:chg: Add support for --s3-multipart-chunk-size, default 25MB
 * 8970812e:chg: Add interruptable:true as default.
 * 1e5081ea:chg: Fix snapcraft commands.
 * 7c86b3b9:chg: Fix snaplogin file use.
 * abb9b54a:chg: Add deployment for pip and snap builds.
 * 26b7e740:chg: Add build_pip job.
 * a0e5a950: Merge branch 'master' into 'master'
 * 4e3c9351: Update b2 backend to use *public* b2sdk API.
 * 19ea323d:chg: Fix PEP8 issue.
 * 2c5bc14d: Merge branch 'bullfrogalj/duplicity-master'
 * 9e7eab53: b2sdk 1.8.0 refactored minimum_part_size to recommended_part_size (the value used stays the same)
 * 3d2aac6b:chg: More cleanup for snap builds.
 * a1c9b14a:chg: Move arch selection to dist/makesnap.
 * 20a9c2f4:chg: Try snap build on all architectures.
 * d0891579:chg: Build for i386, amd64, armhf.
 * beb27cb4:chg: Move to remote build of armfh and amd64.
 * a55844e7:chg: Attempt remote build of armfh
 * 76c4c0b7:fix: Fix error message on gdrivebackend.
 * b5bc7830:chg: More cleanup on requirements.
 * 19fb1dc4:chg: megatools no longer supports py35.
 * 07e4d334:chg: Get more stuff from pypi than repo. Some cleanup.
 * 86d38b33:chg: Fix spaces before inline comments.
 * 413bbe19:chg: Enable access-member-before-definition in pylintrc.
 * e822b9b1:chg: Fix indentation.
 * 8604bb22:fix: Fix issue #57 SSH backends - IndexError: list index out of range
 * 37873f1d:chg: Module gdata still does not work on py3.
 * 33f0d8da:chg: Tweak requirements for gdrivebackend. Cosmetic changes.
 * 99ee0a4b: Merge branch 'PR-backend-gdrive-mydrive' into 'master'
 * d55c144b: added Google MyDrive support updated man pages and --help text
 * db8a5891:chg: Display merge comments. Better formatting.
 * f2daebc7: Merge branch 'develop' into 'master'
 * d5c4729d: Fix "Giving up after 5 attempts. timeout: The read operation timed out"
 * 01f82d41: Merge branch 'master' into 'master'
 * 9f30c714:chg: Clean up readability. Minor changes.
 * 66621bc0:fix: gdata module passes on py27 only.
 * 61d4b216:fix: Restore pylintrc, add requirement
 * 500085d8:fix: Fix unadorned string in restored pylint test.
 * 77232591:fix: Restored pylint test. Fixed one issue found.
 * e78b76e4:fix: More py27 packages bit the dust.
 * 39764414: Merge branch 'fix-uexec-returns-None' into 'master'
 * 8e4b6ab2: fix util.uexc: do not return None
 * bd50ad46:fix: util.uexec() will return u'' if no err msg in e.args.
 * a66fb4e6:fix: util.uexec() should check for e==None on entry.
 * 9d509ef0:fix: Mark skip those not usable on py27. Fix version.
 * b2ed6214:fix: Uncomment backends. Mark skip those not usable on py27.
 * bd44147f: Merge branch 'boxbackend' into 'master'
 * 17170746: Implement Box backend
 * 966c975b: Merge branch 'megav3' into 'master'
 * c2ba2382: Implement megav3 backend to to cater for change in MEGACmd
 * e9f77854:fix: Lock in some module versions to last supporting py27.
 * 67a6f749: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * 6e61a411:fix: Allow py27 to fail CI. Restrict mock pkg to 3.05.
 * 63d0f89c: Merge branch 'use-new-azure-python-packages' into 'master'
 * 3ab947e5: fix documentation for azure backend
 * 5f3bfd51: Merge branch 'master' into 'master'
 * e60946ca: Fix typo
 * b6bae49c: Merge branch 'master' into 'master'
 * f3f97832: Add IDrive backend
 * 12a249aa: Merge branch 'master' into 'master'
 * 7eb0fe2a: Progress bar improvements
 * aa582696: fix;usr:Fixes bug #1652953 - seek(0) on /dev/stdin crashes
 * a394508e:fix: Fix bug #1547458 - more consistent passphrase prompt
 * 41dc6448:fix: Fixes bug #1454136 - SX backend issues
 * f1aad37b:fix: Fixes bug 1918981 - option to skip trash on delete on mediafire
 * b897faa2:fix: Fix bug 1919017 - MultiBackend reports failure on file deletion
 * dcf6ba1d: Don't sync when removing old backups
 * 05a577e0:new: Merge branch 'google-drive-v3' into 'master'
 * acbd2410: Add a new Google Drive backend (gdrive:)
 * 44fc3cf6:fix: Recomment, py2 does not support all backends.
 * 66dd52a2:fix: Add azure-storage module requirement. Uncomment all.
 * c7e1399d:chg: Cosmetic chnges.
 * ac6bd1f0: Merge branch 'azurev12' into 'master'
 * f876383b: Replaced original azure implementation
 * 3aaa717d: Revert "fix:pkg:Remove requirement for python3-pytest-runner. Not used."
 * 2f18eeed:fix: Remove requirement for python3-pytest-runner. Not used.
 * 3573a22a: Fixed code smells
 * 016c2934: Azure v12 support
 * f0a0d1b0:fix: Install older version of pip before py35 deprecation.
 * 6a69debc:fix: Add py27 and py35 back to CI.
 * 17a5d1a0:fix: Fix setup.py to handle Python 2 properly.
 * 0be5a984:chg: Make testing/manual/bug1893481 into a tarball, not directory.
 * 2d838c88: Merge branch 'feature/list-required-volumes-on-restore-dry-run' into 'master'
 * 2bb8cf83: List required volumes when called with 'restore --dry-run'
 * d37933d4:chg: Add Makefile and update docs.
 * 23733225: Merge branch 'swrmr-master-patch-23969' into 'master'
 * 4807c22b: Fix sorting of BackupSets by avoiding direct comparison
 * 89b5688f: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * de9abc5e:fix: Fixes #41 - par2+rsync (non-ssh) fails
 * 7ba07966: Merge branch 'master' into 'master'
 * 3f6c5b8c: Update mailing list link
 * ff449237: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * d52d7b6f: Fixes #16 - Move from boto to boto3.
 * ae71032d: py27 EOL 01/2020, py35 EOL 01/2021, remove tests.
 * 6f18c8e2: Move py27 tests to ub16 and py35 tests to ub18.
 * f75daac5: Fixes #16 - Move from boto to boto3.
 * 95a6be9d: py27 EOL 01/2020, py35 EOL 01/2021, remove tests.
 * baab2a1c: Remove 2to3 from ub16 builds.
 * 8ddbf23b: Move py35 back to ub16, try 2.
 * 182e791f: Move py35 back to ub16.
 * 5fc9ddbf: Move py27 tests to ub16 and py35 tests to ub18.
 * cdc4d4c3: Fixes #33, remove quotes from identity filename option.
 * fff00f02: Fix to correctly build _librsync.so.
 * 83d38b0c: Fix to add --inplace option to build_ext.
 * 770bac31: Rename pylintrc to .pylintrc
 * 8e53a0df: Merge branch 'fix-prefix-affinity-registration' into 'master'
 * 37876f98: Move testfiles dir to a temp location.
 * 20bd733e: Merge remote-tracking branch 'alpha/testfiles'
 * 83336e8c: Skip unicode tests that fail on non-Linux systems like macOS.
 * db044ed8: Multibackend: fix indentation error that was preventing from registering more than one affinity prefix per backend
 * e3636e9a: Merge branch 'onedrive-token' into 'master'
 * d0b18532: onedrive: Support using an external client id / refresh token
 * 45c79c78: Update .gitlab-ci.yml to need code test to pass.
 * d422cc51: Update .gitlab-ci.yml to need code test to pass.
 * e071d6a7: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * d180ec07: Fix issue #29 Backend b2 backblaze fails with nameprefix restrictions.
 * dbf0b052: Fix issue #26 Backend b2 backblaze fails with nameprefix restrictions
 * 906468eb: Fix unadorned strings.
 * 42bf3803: Merge branch 'Rufflewind-master-patch-11811' into 'master'
 * 0f059fa0: Remove basepython in code and coverage tests.
 * cef47882: Add report.xml.
 * 7e435992: Bulk replace testfiles with /tmp/testfiles
 * 0bbbf05a: Add report.xml.
 * c006de87: Remove basepython in code and coverage tests.
 * 8dfdc6b6: Report errors if B2 backend does exist but otherwise fails to import
 * dc706f1c: Fix pep8 warning.
 * 799a3216: Added option --log-timestamp to prepend timestamp to log entry.
 * e7e1eab4: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 1ec95ce2: Improve patch for Python 3.10.
 * 66fc925f: Merge branch 'master' into 'master'
 * 6b346bc0: Improve.
 * 7ad41d7f: Conditionalize for Python version.
 * 6e7e7af5: Patch for Python 3.10.
 * 65d14c7e: Fixup ignore_regexps for optional text.
 * 8dfc1e12: Fix issue #26 (again) - duplicity does not clean up par2 files.
 * c77f6bc6: Fix issue #26 - duplicity does not clean up par2 files.
 * bfb6d083: Fix issue #25 - Multibackend not deleting files.
 * 062ad8c9: Adjust setup.py for changelog changes.
 * c1313c1d: Delete previous manual changelogs.
 * a993d8b2: Tools to make a CHANGELOG.md from git commits.
 * 99def906: Merge branch 'exc-if-present-robust' into 'master'
 * 17ac136e: Make exclude-if-present more robust
 * 69386fbd: Merge branch 'no-umask' into 'master'
 * a22c6564: Drop default umask of 0077
 * cdbcfa4f: Comment out RsyncBackendTest, again.
 * 30a15ab1: Fix some unadorned strings.
 * 3a41817e: Fixed RsyncBackendTeest with proper URL.
 * 9fa8f971: Merge branch 'Yump-issue-23' into 'master'
 * e0f7e8cf: Fix issue #23
 * cc9ec317: rclonebackend now logs at the same logging level as duplicity.
 * d5a79f18: Allow sign-build to fail on walk away. Need passwordless option.
 * 2e21208e: Merge branch 'fix-rename' into 'master'
 * 550b7502: Fix --rename typo
 * dd00339d: Move back to VM build, not remote. Too many issues with remote.
 * 54d64fac: Merge branch 'escape-quote' into 'master'
 * e615b928: Escape single quotes in machine-readable log messages
 * 56bac677: Uncomment review-tools for snap.
 * cfaaad83: Whoops, missing wildcard '*'.
 * 2140f16f: Changes to allow remote build of snap on LP.
 * b19e64b7: Changes to allow remote build of snap on LP.
 * 20e639b2: Add a pylint disable-import-error flag.
 * 9793a301: Change urllib2 to urllib.request in parse_digest_challenge().
 * 41f87bfc: Fix Python 3.9 test in .gitlab-ci.yaml.
 * 15f80fc3: Fix Python 3.9 test in .gitlab-ci.yaml.
 * 6255ed93: Add Python 3.9 to .gitlab-ci.yaml.
 * 4746e800: Add Python 3.9 to the test suite. It tests sucessfuly.
 * e698d684: Fix bug #1893481 again for Python2. Missed include.
 * b928ca17: Fix bug #1893481 Error when logging improperly encoded filenames
 * 574bcc05: Merged in s3-unfreeze-all
 * a56be51d: Merge branch 's3-unfreeze-all' into 'master'
 * a85322b3: Add boto3 to list of requirements.
 * 79adde32: Remove ancient CVS Id macro
 * 9870db37: Merged in OutlawPlz:paramiko-progress
 * f7a4ef01: Merge branch 'paramiko-progress' into 'master'
 * 6cbdccc3: Fixes paramiko backend progress bar
 * eb8f7264: Merged in lazy init for Boto3 network connections
 * 1f2ce0b3: Merge branch 'feature/lazy_init_boto3' into 'master'
 * bc5c913d: Initial crack at lazy init for Boto3
 * c3354c12: Merge branch 'hostname' into 'master'
 * 1b0ff4ce: Record the hostname, not the fqdn, in manifest files
 * a42483d0: Merge branch 'listdir-contains' into 'master'
 * 4f676fb9: Avoid calling stat when checking for exclude-if-present files
 * 506cddb7: Fix build control files after markdown conversion.
 * 183ff724: Recover some changes lost after using web-ide.
 * cc1fd428: Paperwork
 * 07cf2b34: Merge branch 's3-boto3-region-and-endpoint' into 'master'
 * dd5e856f: Wait for Glacier batch unfreeze to finish
 * af419f9e: Update README-REPO.md
 * 8afcf29a: Make code view consistent.
 * 82c08c4b: Update setup.py
 * 55cfa4d3: Update README.md
 * 11016d3a: Set default values for s3_region_name and s3_endpoint_url
 * f4e971a0: Allow setting s3 region and endpoint
 * 52ecdd92: Paperwork.
 * c2f82bee: Revert "Merge branch 's3-boto3-region-and-endpoint' into 'master'"
 * a53b616d: Adorn string as unicode
 * 2cac6beb: Utilize ThreadPoolExecutor for S3 glacier unfreeze
 * 4302d773: Refine codestyle according to PEP-8
 * 8a4a702b: Adorn strings as unicode
 * aa07947e: Always paperwork.
 * 6dac477c: Merge branch 's3-boto3-region-and-endpoint' into 'master'
 * cdfbaf8c: Merge branch 'pydrive-notfound' into 'master'
 * aa7b6b0e: Merge branch 'pydriveshared' into 'master'
 * d66ed51a: Allow setting s3 region and endpoint
 * 23870755: Fixed indentation
 * 27b1e7f2: Added shared drive support to existing `pydrive` backend instead of a new backend
 * 781ead61: Fix missing FileNotUploadedError in pydrive backend
 * 49869b8e: Fix caps on X-Python-Version.
 * a711a339: Fix issue #10 - ppa:duplicity-*-git fails to install on Focal Fossa
 * 46e5ac5d: PydriveShared backend is identical to Pydrive backend, except that it works on shared drives rather than personal drives
 * fd255831: Include the query when parsing the backend URL string, so users can use it to pass supplementary info to the backend
 * 05945d4c: S3 unfreeze all files at once
 * 35981973: Merge branch 'patch-2' into 'master'
 * c606eb80: Merge branch 'patch-1' into 'master'
 * b1b4a6ad: Remove python-cloudfiles from suggestions
 * 26a7fb9f: Update azure requirement
 * fa46ff27: Fix bug #1211481 with merge from Raffaele Di Campli
 * 0373b25c: Merge branch 'master' into 'master'
 * 617978ef: Added `--do-not-restore-ownership` option
 * f1694eef: Fix bug #1887689 with patch from Matthew Barry
 * 8e079a4f: Merge branch 'fix-glacier-check' into 'master'
 * 57687fc1: Fix check for s3 glacier/deep
 * b6a86335: Change from push to upload.
 * ff30ca4d: Add specific version for six.
 * 68db69d1: Set deprecation version to 0.9.0 for short filenames.
 * 5df9b7d1: Fixes for issue #7, par2backend produces badly encoded filenames.
 * 938963a1: Added a couple of fsdecode calls for issue #7.
 * 8c4d93bc: Generalize exception for failed get_version() on LaunchPad.
 * 563fe704: Ignore *.so files.
 * 361c3ff6: Update docs
 * a020bbca: Catch up on paperwork.
 * 1b4667f0: Merge branch 'mikix/rename-fix' into 'master'
 * 582f6bca: Fix --rename encoding
 * 9f4f052f: Merge remote-tracking branch 'team/fix-py27-testing'
 * 7daf3313: Skip tests failing on py27 under 18.04 (timing error).
 * fba34cfe: Fix code style issue.
 * 28c8664b: Add PATHS_FROM_ECLIPSE_TO_PYTHON to environ whan starting pydevd.
 * e48632b3: Add *.pyc to .gitignore.
 * 6feb23a4: Replace compilec.py with 'setup.py build_ext', del compilec.py.
 * f2d0c90c: Merge branch 'master' into 'master'
 * 5bba3ba9: Support PyDrive2 library in the pydrive backend
 * ad2a7eff: Fix unadorned string.
 * 075fe94c: Fix usage of TOXPYTHON and overrides/bin shebangs.
 * 887f3a99: Use default 'before_script' for py27.
 * 1fb21a93: Don't collect coverage unless needed.
 * 7dd2f80f: Merge branch 'Tidy_up_gitlab_CI_doc' into 'master'
 * dfecbe21: Tidy .gitlab-ci.yml, fix py3.5 test, add py2.7 test (allowed to fail)
 * c4f40124: Merge branch 'fix-py27-CI'
 * 5d4b3a08: Test code instead of py27 since py27 is tested elsewhere.
 * 95e88faf: Fix RdiffdirTest to use TOXPYTHON as well.
 * 83d4cb4c: Set TOXPYTHON before tests.
 * 1ea20cba: Put TOXPYTHON in passed environment.
 * de479cc5: More fixes for bug #1877885 - Catch quota overflow on Mega upload.
 * 19a5d340: More fixes for bug #1877885 - Catch quota overflow on Mega upload.
 * 146af891: Undo: Try forcing python version to match tox testing version.
 * 7781f1c3: Always upgrade pip.
 * 08e52b6b: Try forcing python version to match tox testing version.
 * bb3aa986: Uncomment all tests.
 * 77323dd2: Test just py27 for now.
 * 3bbdcba9: Replace bzr with git.
 * f3db17d2: Don't load repo version of future, let pip do it.
 * 5820d5db: Hmmm, Gitlab yaml does not like continuation lines. Fix it.
 * aba5e2b2: Fix typo.
 * d7bb2682: Update to use pip as module and add py35 test.
 * 2fe68d81: Add py35 to CI tests.
 * bd072de8: More changes to support Xenial.
 * e0a37bc1: Fix typo.
 * 27bf6ac2: Fix duplicity to run under Python 3.5.
 * 0861c46d: Fix duplicity to run under Python 3.5.
 * 0d751d68: Merge branch 'add_gitlab_testing' into 'master'
 * bacd104b: Update .gitlab-ci.yml to update pip before installing other pip packages (to try to fix more-itertools issue: https://github.com/pytest-dev/pytest/issues/4770 )
 * 1ab8047c: Don't include .git dir when building docker images.
 * 761d8efd: Merge branch 'update_pip_before_install' into 'master'
 * 2c8f4e2f: Upgrade pip before installing requirements with it. Fixes more-itertools error as newer versions of pip identify that the latest more-itertools are incompatible with python 2.
 * 25886504: Patched in a megav2backend.py to update to MEGAcmd tools.
 * 31f40e5d: Change log.Warning to log.Warn. Whoops!
 * d3469cb8: Fixed bug #1875937 - validate_encryption_settings() fails w/S3 glacier
 * 6ad82bd5: Restore commented our backend requirements.
 * 6645afb0: Fixes for rclonebackend from Francesco Magno (original author)
 * 0e2a16fc: Version man pages during setup.py install.
 * 900e3a30: More fixes for Launchpad build limitations.
 * 756d3d87: More fixes for Launchpad build limitations.
 * 57f78ea5: Move setuptools_scm to setup_requires.
 * e32f95c4: Back off requirements for fallback_version in setup.py.
 * d5f2c6ee: Add some requirements for LP build.
 * 647e0ac5: Make sure we get six from pip to support dropbox.
 * f346b832: Provide fallback_version for Launchpad builder.
 * daf74b95: Remove python3-setuptools-scm from setup.py.
 * 3929cd27: Add python3-setuptools-scm to debian/control.
 * 934445cc: Try variation with hyphen seperator.
 * 7f14dad9: Try python3_setuptools_scm (apt repo name). Probably too old.
 * b7f2f866: Add setuptools_scm to install_requires.
 * b4e4fe67: Fixed release date
 * e8c18b85: Fixed bug #1876446 - WebDAV backend creates only tiny or 0 Byte files
 * dccd21ee: Fix to run with --dist-dir command
 * 59c3b344: Fixed bug #1876778 - byte/str issues in megabackend.py
 * bc395a15: Fix to use 'setup.py develop' instead of sdist
 * 623c4406: Fix to run with --dist-dir command
 * 40d8ce10: Fixed bug #1875529 - Support hiding instead of deletin on B2
 * 98a044f5: Uncomment upload and sign.
 * 9014f6bc: Reworked versioning to be git tag based.
 * b38da029: Migrate bzr to git
 * b312d8b1: Fixed bug #1872332 - NameError in ssh_paramiko_backend.py
 * 38b258b3: Fix spelling error.
 * 7de78feb: Fixed bug #1869921 - B2 backup resume fails for TypeError
 * 2c8355f2: Merged in lp:~kenneth-loafman/duplicity/duplicity-pylint - Enable additional pylint warnings. Make 1st pass at correction. unused-argument, unused-wildcard-import, redefined-builtin, bad-indentation, mixed-indentation, unreachable - Renamed globals to config to fix conflict with __builtin__.glogals() - Resolved conflict between duplicity.config and testing.manual.config - Normalized emacs mode line to have encoding:utf8 on all *.py files
 * a2f3c290: Fixed bug #1868414 - timeout parameter not passed to BlobService for Azure backend
 * bf49c52d: More changes for pylint. * Resolved conflict between duplicity.config and testing.manual.config * Normalized emacs mode line to have encoding:utf8 on all *.py files
 * 59b412ca: More changes for pylint. * Remove copy.com refs.
 * 4f5c34b5: More changes for pylint.
 * 3a5830b7: More changes for pylint.
 * 738c4bff: Enable additional pylint warnings. Make 1st pass at correction. - unused-argument, unused-wildcard-import, redefined-builtin, bad-indentation, mixed-indentation
 * 791ad27a: Launchpad automatic translations update.
 * 824dd783: Fixed bug #1867742 - TypeError: fsdecode() takes 1 positional argument but 2 were given with PCA backend
 * f90a6612: Launchpad automatic translations update.
 * e61e2f63: Fixed bug #1867529 - UnicodeDecodeError: 'ascii' codec can't decode byte 0x85 in position 0: ordinal not in range(128) with PCA
 * 9cc23a72: Launchpad automatic translations update.
 * 72c6870b: Fixed bug #1867468 - UnboundLocalError (local variable 'ch_err' referenced before assignment) in ssh_paramiko_backend.py
 * 4ca18004: Launchpad automatic translations update.
 * 6929f79d: Fixed bug #1867444 - UnicodeDecodeError: 'ascii' codec can't decode byte 0x85 in position 0: ordinal not in range(128) using PCA backend
 * ad6c8a45: Fixed bug #1867435 - TypeError: must be str, not bytes using PCA backend
 * b864fe2e: Move pylint config from test_code to pylintrc.
 * ed4f2bdc: Launchpad automatic translations update.
 * b57e2e41: Launchpad automatic translations update.
 * 96169b96: Cleaned up some setup issues where the man pages and snapcraft.yaml were not getting versioned.
 * 30dcad4a: Launchpad automatic translations update.
 * c169736e: Fixed bug #1769267 - [enhancement] please consider using rclone as backend.
 * c8bf327c: Fixed bug #1755955 - best order is unclear, of exclude-if-present and exclude-device-files - Removed warning and will now allow these two to be in any order. If encountered outside of the first two slots, duplicity will silently move them to be in the first two slots. Within those two slots the order does not matter.
 * 8d4800c0: Launchpad automatic translations update.
 * 27ad08a8: Fixed a couple of file history bugs: #1044715 Provide a file history feature + removed neutering done between series - #1526557 --file-changed does not work + fixed str/bytes issue finding filename
 * c629b02a: Fixed bug #1865648 - module 'multiprocessing.dummy' has no attribute 'cpu_count'. - replaced with module psutil for cpu_count() only - appears Arch Linux does not support multiprocessing
 * d22a26d4: Launchpad automatic translations update.
 * 5d9a0cd9: Launchpad automatic translations update.
 * c26c5032: Launchpad automatic translations update.
 * a80c6e2f: Mod to get focal build on LP working.
 * 1ce51e04: Mod to get focal build on LP working.
 * e1bc2044: Mod to get focal build on LP working.
 * 90e7fb96: Launchpad automatic translations update.
 * 8b2bd992: Merged in translation updates
 * bb551878: Fixed to work around par2 0.8.1 core dump on short name - https://github.com/Parchive/par2cmdline/issues/145
 * dda0c28e: Launchpad automatic translations update.
 * 26a9710a: Fixed bug #1857818 - startswith first arg must be bytes - use util.fsdecode on filename
 * 8b90ec5a: Launchpad automatic translations update.
 * 93304826: Fixed bug #1863018 - mediafire backend fails on py3 - Fixed handling of bytes filename in url.
 * 84b57ed4: Launchpad automatic translations update.
 * 9b958add: Add rclone requirement to snapcraft.yaml
 * 43ab38fd: Fixed bug #1236248 - --extra-clean clobbers old backups - Removed --extra-clean, code, and docs
 * 608819fb: Launchpad automatic translations update.
 * 6c260884: Fixed bug #1862672 - test_log does not respect TMPDIR - Patch supplied by Jan Tojnar.
 * 98cbfcfd: Fixed bug #1860405 - Auth mechanism not supported - Added python3-boto3 requirement to snapcraft.yaml
 * 4e0bf28c: Launchpad automatic translations update.
 * dadb6151: more readthedocs munges
 * a58a7965: don't format the po files for readthedocs
 * 2be90075: add readthedocs.yaml config file, try 3
 * 8427ec7c: add readthedocs.yaml config file, try 2
 * 19d19c4f: add readthedocs.yaml config file
 * 7c795a9f: remove intltool for readthedocs builder
 * 0a9e02ca: add python-gettext for readthedocs builder
 * e295e751: add gettext/intltool for readthedocs builder
 * 945dcbfd: add gettext for readthedocs builder
 * d3dca815: add intltool for readthedocs builder
 * 149831be: add intltools for readthedocs builder
 * e7d949ea: add intltools for readthedocs builder
 * d280f1aa: Point readthedocs.io to this repo.
 * 3acf1052: Renamed botobackend.py to s3_boto_backend.py
 * b2209b51: Renamed botobackend.py to s3_boto_backend.py
 * 0569b52f: Launchpad automatic translations update.
 * 12099038: missing comma
 * e0f88015: Merged from parent to bring in changes
 * 2b2ff2a3: Launchpad automatic translations update.
 * a4e06ed0: some code cleanup and play with docs
 * dd6ab768: Uncomment snapcraft sign-build. Seems it's fixed now.
 * ea8dd5ec: fix argument order on review-tools.
 * 2c7ef46a: Reworked setup.py to build a pip-compatible distribution tarball of duplicity. * Added dist/makepip for convenience.
 * 7776b4ec: Launchpad automatic translations update.
 * c179a408: Adjust Dockerfiles to new requirements.
 * 8294d2e8: Fix bug #1861287 - Removing old backup chains fails using pexpect+sftp
 * a2b9c3f6: Adjust Dockerfiles to new requirements.
 * d7db23cc: Launchpad automatic translations update.
 * 6ae3eb8f: Enhance setup.py/cfg to allow install by pip
 * 084677d8: Enhance setup.py/cfg to allow install by pip
 * 812165dc: Enhance setup.py/cfg to allow install by pip
 * 51f1649d: Launchpad automatic translations update.
 * 5bae0e3c: Gave up fighting the fascist version control munging on snapcraft.io. Duplicity now has the form 0.8.10.1558, where the last number is the bzr revno. Can't do something nice like having a dev/fin indicator like 0.8.10dev1558 for dev versions and a fin for release or final.
 * 78055144: Renamed MulitGzipFile to GzipFile to avoid future problems with upstream author of mgzip fixing the Mulit -> Multi typo
 * b1e58587: Launchpad automatic translations update.
 * ef01d4d3: Launchpad automatic translations update.
 * 655bd113: Fixed bug #1858207 missing targets in multibackend - Made it possible to return default value instead of taking a fatal exception on an operation by operation approach. The only use case now is for multibackend to be able to list all targets and report back on the ones that don't work.
 * 744d3c1b: Launchpad automatic translations update.
 * 5177bd54: Fixed bug #1858204 - ENODEV should be added to list of recognized error stringa
 * 5fec94a2: Launchpad automatic translations update.
 * da516788: Comment out test_compare, again.
 * 3adc7fd6: Launchpad automatic translations update.
 * b5c61993: Clean up deprecation errors in Python 3.8
 * a321dd2d: Clean up some TODO tasks in testing code.
 * 0c9c05f5: Launchpad automatic translations update.
 * 0c811e42: Fixed bug #1859877 - syntax warning on python 3.8
 * d6eff2a4: Move to single-sourceing the package version - Rework setup.py, dist/makedist, dist/makesnap, etc., to get version from duplicity/__init__.py - Drop dist/relfiles. It was problematic.
 * cdbed4bb: Launchpad automatic translations update.
 * af9d6055: Fixed bug #1859304 with patch from Arduous - Backup and restore do not work on SCP backend
 * 19bfc7e5: Launchpad automatic translations update.
 * da5b9b53: Revert last change to duplicity.__init__.py.
 * 4302e56b: Py27 supports unicode returns for translations - remove install that does not incude unicode - Removed some unneeded includes of gettext
 * 00703b2b: Launchpad automatic translations update.
 * 7c48ace8: Fixed bug #1858713 - paramiko socket.timeout - chan.recv() can return bytes or str based on the phase of the moon. Make allowances.
 * 04f66cb8: Switched to python3 for snaps.
 * 916f1e4d: Launchpad automatic translations update.
 * d381e5a2: Fix unadorned string.
 * 5af048a2: Launchpad automatic translations update.
 * 0ced7482: Launchpad automatic translations update.
 * b4ee7f0b: Change of plans. Skip test if rclone not present.
 * 30670f59: Add rclone to setup testing requirements.
 * 9b56e4cf: Revert to testing after build.
 * 33001039: Fixed bug #1855736 again - Duplicity fails to start - remove decode from unicode string
 * f668e74f: Fixed bug #1858295 - Unicode error in source filename - decode arg if it comes in as bytes
 * 89670919: Add snapcraft login to makesnap
 * f195e223: Launchpad automatic translations update.
 * c631e4ed: Launchpad automatic translations update.
 * 21faa128: Fix bug #1858153 with patch from az - mega backend: fails to create directory
 * 3d3a1aba: Fix bug #1857734 - TypeError in ssh_paramiko_backend - conn.recv() can return bytes or string, make string
 * ac16aed3: Fix bytes/string differences in subprocess_popen() - Now returns unicode string not bytes, like python2
 * f4eaa700: Adding missed mgzip import and adjusting untouched unit tests
 * 14a48105: Adding multi-core support by using mgzip instead of gzip
 * 4b7b33a9: Launchpad automatic translations update.
 * 672610a1: Convert all shebangs to python3 for bug #1855736
 * d465bbd7: Launchpad automatic translations update.
 * 8f2d3bf9: Fixed bug #1857554 name 'file' is not defined - file() calls replaced by open() in 3 places.
 * 57098b3a: Original rclonebackend.py from Francesco Magno for Python 2.7
 * 3a075133: Launchpad automatic translations update.
 * f6e3266d: Merged in lp:~ed.so/duplicity/boto.fixup - fix manpage indention - clarify difference between boto backends - add boto+s3:// for future use when boto3+s3:// will become default s3 backend
 * 8fde90ee: Renamed testing/infrastructure to testing/docker
 * 6afbacac: fix manpage indention clarify difference between boto backends add boto+s3:// for future use when boto3+s3:// will become default s3 backend
 * ece38f9d: Launchpad automatic translations update.
 * f9470053: Fixed a mess I made. setup.py was shebanged to Py3, duplicity was shebanged to Py2. This meant that duplicity ran as Py2 but could not find its modules because they were under Py3. AArgh!
 * d6886763: Launchpad automatic translations update.
 * ade3b8ee: Fixed bug #1855736 - duplicity fails to start - Made imports absolute in dup_main.py
 * 0373e2c9: Fixed bug #1856447 with hint from Enno L - Replaced with formatted string
 * c4fd0b93: Launchpad automatic translations update.
 * 2c25749c: Launchpad automatic translations update.
 * 5cd4a977: Fixed bug #1855736 with help from Michael Terry - Decode Popen output to utf8
 * ede53e71: Launchpad automatic translations update.
 * 3af8b54e: Fixed bug #1855636 with patch from Filip Slunecko - Wrong buf type returned on error. Make bytes.
 * 1ff62298: Launchpad automatic translations update.
 * eb9dfaef: Merged in translation updates
 * 7f5a31e5: Merged in translation updates
 * 60c61d33: Launchpad automatic translations update.
 * aa3a25a9: Removed abandoned ref in README * Comment out signing in makesnap
 * f7b5a572: Fixed bug #1854554 with help from Tommy Nguyen - Fixed a typo made during Python 3 conversion.
 * e520b1a6: Launchpad automatic translations update.
 * b791126e: Fixed bug #1855379 with patch from Daniel González Gasull - Issue warning on temporary connection loss. * Fixed misc coding style errors.
 * 2135e0be: Launchpad automatic translations update.
 * 1160274d: Disabling autotest for LP build. I have run tests on all Ubuntu releases since 18.04, so the code works. To run tests manually, run tox from the main directory. Maybe LP build will work again soon.
 * 85e2c33c: Merged in lp:~carlalex/duplicity/duplicity - Fixes bug #1840044: Migrate boto backend to boto3 - New module uses boto3+s3:// as schema.
 * 13b9f117: Launchpad automatic translations update.
 * af56a95d: Update to manpage
 * 62504f4a: Convert debian build to Python 3.
 * 679ac29f: Replace python with python3 in shebang.
 * 164d0ae3: Convert debian build to Python 3.
 * 607083bf: BUGFIX: list should retun byte strings, not unicode strings
 * 70b8e1a2: Updating comments
 * c7e71a4b: select boto3/s3 backend via url scheme rather than by CLI option. Doc changes to support this.
 * 5e3cb587: renaming boto3 backend file
 * 514eee53: merging from parent
 * 10c7402d: Adding support for AWS Glacier Deep Archive. Fixing some typos.
 * 4ad0467f: Manpage updates. Cleaning up the comments to reflect my current plans. Some minor clean-ups.
 * 09339a2c: updating comments
 * 8c1223fb: SSE options comitted. AES tested, KMS not tested
 * 6b40a28d: handling storage class on backup
 * 08e18318: handling storage class on backup
 * bc575522: minor clean-ups
 * 49fbb177: rename boto3 backend py file
 * bb9806a6: removing 'todo' comment for multi support. Defaults in Boto3 chunk the upload and attempt to use multiple threads. See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig
 * 1be1119c: format fix
 * 0c3ecbd6: Fixing status reporting. Cleanup.
 * 7a069a49: better exception handling. Return -1 for unknwon objects in _query.
 * 02ec9e7e: updating comment
 * 7ff5db9e: Making note of a bug
 * 1eeffae2: removing unused imports
 * 22fcdd9c: Launchpad automatic translations update.
 * 45519bde: implementing _query for boto3
 * 3bbc88e6: minor clean-up.
 * 032504d4: Some initial work on a boto3 back end.
 * 5d5e88b6: Fixed bug #1853809 - Tests failing with Python 3.8 / Deprecation warnings - Fixed the deprecation warnings with patch from Sebastien Bacher - Fixed test_globmatch to handle python 3.8 same as 3.7 - Fixed tox.ini to include python 3.8 in future tests
 * f1d0e3ec: Launchpad automatic translations update.
 * 63d141b3: Fixed bug #1853655 - duplicity crashes with --exclude-older-than - The exclusion setup checked for valid string only. Made the code comprehend datetime (int) as well.
 * f2f04d23: Launchpad automatic translations update.
 * 3ee5aaec: Just some cosmetic changes.
 * d66cef2a: Launchpad automatic translations update.
 * af1411f1: Fixed bug #1851668 with help from Wolfgang Rohdewald - Applied patches to handle translations.
 * 2685df16: Launchpad automatic translations update.
 * 94bd9a68: Fixed bug #1852876 '_io.BufferedReader' object has no attribute 'uc_name' - Fixed a couple of instances where str() was used in place of util.uexc() - The file was opened with builtins, so use name, not uc_name
 * 3dbeb2d8: Added build signing to dist/makesnap.
 * 38019ad6: Launchpad automatic translations update.
 * d4b0bd9c: Fixed bug #1852848 with patch from Tomas Krizek - B2 moved the API from "b2" package into a separate "b2sdk" package. Using the old "b2" package is now deprecated. See link: https://github.com/Backblaze/B2_Command_Line_Tool/blob/master/b2/_sdk_deprecation.py - b2backend.py currently depends on both "b2" and "b2sdk", but use of "b2" is enforced and "b2sdk" isn't used at all. - The attached patch uses "b2sdk" as the primary dependency. If the new "b2sdk" module isn't available, it falls back to using the old "b2" in order to keep backward compatibility with older installations.
 * a7fe9700: Launchpad automatic translations update.
 * 10576e1a: Launchpad automatic translations update.
 * d01b5f5f: Fixed bug #1851727 - InvalidBackendURL for multi backend - Encode to utf8 only on Python2, otherwise leave as unicode
 * 64a1661f: Merged in lp:~mterry/duplicity/resume-encrypt-no-pass - This branch arose from a Debian patch that has been disabling the encryption validation of volume1 during restarts for years. - Debian has been preserving the ability to back up with just an encrypt key and no password (i.e. to have no secrets on the backup machine).
 * 06a377f1: Merged in lp:~mterry/duplicity/pydrive-cache-fix - The pydrive backend had another of the ongoing bytes/string issues. :) - This time, it was saving a bytes filename in its internal cache after each volume upload. Then when asked for a list of files later, it would add the byte-filenames from its cache to the results. And we'd end up thinking there were two of the same filename on the backend, which would cause a crash at the end of an otherwise successful backup, because the collections code would assert on the filenames being unique.
 * f4431444: Launchpad automatic translations update.
 * ab04c2f6: Fix resuming without a passphrase when using just an encryption key
 * 07889245: Fix bytes/string issue in pydrive backend upload
 * 80b9aff3: Fixed bug #1851167 with help from Aspen Barnes - Had Popen() to return strings not bytes
 * e8e2763c: Added dist/makesnap to make spaps automagically.
 * 9199198c: Launchpad automatic translations update.
 * 3b667194: Fixed bug #1850990 with suggestion from Jon Wilson - --s3-use-glacier and --no-encryption cause slow backups
 * 567ca69a: Fix header in CHANGELOG
 * 20c8439e: Added b2sdk to snapcraft.yaml * Fixed bug #1850440 - Can't mix strings and bytes.
 * 3eaa679f: Launchpad automatic translations update.
 * ccab17d6: Merged in translation updates
 * b0c3b382: Launchpad automatic translations update.
 * 993213a0: Updated snapcraft.yaml to remove python-lockfile and fix spelling.
 * 95abb82d: Updated snapcraft.yaml to remove rdiffdir and add libaft1 to stage.
 * 47590db2: Updated snapcraft.yaml to include rdiffdir and did some reformatting.
 * 70868ce4: Launchpad automatic translations update.
 * cac41849: Updated snapcraft.yaml to include rdiffdir and did some reformatting.
 * d5252ce4: Launchpad automatic translations update.
 * 082bb15f: Removed file() call in swiftbackend. It's been deprecated since py2.
 * 2e6e3748: Launchpad automatic translations update.
 * 164a48ae: Revisited bug #1848783 - par2+webdav raises TypeError on Python 3 - Fixed so bytes filenames were compared as unicode in re.match()
 * 97892d62: Launchpad automatic translations update.
 * b9b8fb8f: Removed a couple of disables from pylint code test. - E1103 - Maybe has no member - E0712 - Catching an exception which doesn't inherit from BaseException
 * f84ddb7a: Added additional fsdecode's to uses of local_path.name and source_path.name in b2backend's _get() and _put. See bug #1847885 for more details.
 * b1e2283c: Fixed bug #1849661 with patch from Graham Cobb - The problem is that b2backend uses 'quote_plus' on the destination URL without specifying the 'safe' argument as '/'. Note that 'quote' defaults 'safe' to '/', but 'quote_plus' does not!
 * 9972101f: Launchpad automatic translations update.
 * 05f347bd: Fixed bug #1848166 - Swift backend fails on string concat - added util.fsdecode() where needed
 * 0aacccd6: Launchpad automatic translations update.
 * 5977711f: Fixed bug #1848783 with patch from Jacob Middag - Don't use b'' strings in re.*
 * 2c3c233a: Fixed bug #1848783 with patch from Jacob Middag - Don't use b'' strings in re.*
 * 2cc6dcf9: Launchpad automatic translations update.
 * 9a3f11a0: Fixed bug #1626061 with patch from Michael Apozyan - While doing multipart upload to s3 we need to report the total size of uploaded data, and not the size of each part individually. So we need to keep track of all parts uploaded so far and sum it up on the fly.
 * 882da026: Launchpad automatic translations update.
 * 4aecac8a: Removed revision 1480 until patch is validated.
 * 49222a44: Launchpad automatic translations update.
 * 92a7792f: Fixed bug #1626061 with patch from Michael Apozyan - While doing multipart upload to s3 we need to report the total size of uploaded data, and not the size of each part individually. So we need to keep track of all parts uploaded so far and sum it up on the fly.
 * fabb5e49: Fixed bug #1848203 with patch from Michael Apozyan - convert to integer division
 * 10202c4b: Fix unadorned string.
 * 4bff69af: Fix unadorned string.
 * 7f5d9ad5: Launchpad automatic translations update.
 * e0db40e8: Updated b2 backend to work with both v0 and v1 of b2sdk * Fixed bug #1847885 - B2 fails on string concatenation. - use util.fsdecode() to get a string not bytes. - Partially fixed in bug #1843995, this applies same fix to remaining instances of the problem
 * 9ff5cab4: In version 1 of the B2sdk, the list_file_names method is removed from the B2Bucket class.
 * 88b9694b: complete fix for string concatenation in b2 backend
 * 5b32ad48: Launchpad automatic translations update.
 * 265f9b05: Fixed Resouce warnings when using paramiko. It turns out that duplicity's ssh_paramiko_backend.py was not handling warning suppression and ended up clearing all warnings, including those that default to off.
 * cff9513e: Fixed Resouce warnings when using paramiko. It turns out that duplicity's ssh_paramiko_backend.py was not handling warning suppression and ended up clearing all warnings, including those that default to off.
 * 4fd7e13a: Launchpad automatic translations update.
 * 8142080f: Removed a setting in tox.ini that causes coverage to be activated during testing duplicity.
 * f26da48d: Launchpad automatic translations update.
 * ea837434: Launchpad automatic translations update.
 * 3cbdcaf2: Fixed bug #1846678 - --exclude-device-files and -other-filesystems crashes - assuming all options had arguments was fixed.
 * cd4a41a0: Fixed bug #1844950 - ssh-pexpect backend syntax error - put the global before the import.
 * 0c688ce7: Fixed bug #1846167 - webdavbackend.py: expected bytes-like object, not str - base64 now returns bytes where it used to be strings, so just decode().
 * d39bb267: Fixed bug reported on maillist - Python error in Webdav backend. See: https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00026.html
 * 52a4e36d: Fix bug #1844750 - RsyncBackend fails if used with multi-backend. - used patch provided by KDM to fix.
 * 55cb37cb: Fix bug #1843995 - B2 fails on string concatenation. - use util.fsdecode() to get a string not bytes.
 * 74a46964: Launchpad automatic translations update.
 * 719fa0ff: Clean up some pylint warnings.
 * b647ca5c: Add testenv:coverage and took it out of defaults. Some cleanup.
 * 67e74918: Launchpad automatic translations update.
 * 7f7bb75c: Fix MacOS tempfile selection to avoid /tmp and /var/tmp. See thread: https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00000.html
 * 97a24b19: Launchpad automatic translations update.
 * 5df55e89: Sort of fix bugs #1836887 and #1836888 by skipping the tests under question when running on ppc64el machines.
 * 9cb8c3c8: Launchpad automatic translations update.
 * a4addd79: Launchpad automatic translations update.
 * 9549dd55: Added more python future includes to support using python3 code mixed with python2.
 * ce5a86b0: Fix exc.args handling. Sometimes it's (message, int), other times its (int, message). We look for the message and use that for the exception report.
 * 165153e5: Adjust exclusion list for rsync into duplicity_test.
 * 93be690d: Set to allow pydevd usage during tox testing.
 * 6fb4ce23: Launchpad automatic translations update.
 * 50e4c7be: Don't add extra newline when building dist/relfiles.txt.
 * ecc4ed31: Changed dist/makedist to fall back to dist/relfiles.txt in case bzr or git is not available to get files list. Tox sdist needs setup.py which needs dist/makedist. * Updatated LINGUAS file to add four new translations.
 * 81f5c0ae: Launchpad automatic translations update.
 * 0fa41cb9: Launchpad automatic translations update.
 * aeb19bab: Made some changes to the Docker infrastructure: All scripts run from any directory, assuming directory structure remains the same. - Changed from Docker's COPY internal command which is slow to using external rsync which is faster and allows excludes. - Removed a couple of unused files.
 * b8a9251d: Run compilec.py for code tests, it needs the import.
 * 9d23e289: Launchpad automatic translations update.
 * 52b07ac4: Merged in lp:~aaron-whitehouse/duplicity/08-docker-local-import - Convert the Docker infrastructure to pull the local branch into duplicity_test. This allows testing the local branch with the known-good Docker environment, even if it has not yet been committed to trunk. - As a consequence, remove the -r option to build-duplicity_test.sh. This functionality can be achieved by branching that revision before running the script.
 * fba1daa8: Simplify README-TESTING and change this to recommend using the Docker images to test local branches in a known-good environment.
 * 61f5075e: Convert Dockerfile-19.10 to new approach (using local folder instead of remote repo) * run-tests passes on 19.10 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED: py36: InterpreterNotFound: python3.6; py37: commands succeeded; report: commands succeeded)
 * ae230ea2: Convert Dockerfile-19.04 to new approach (using local folder instead of remote repo) * run-tests passes on 19.04 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED: py36: InterpreterNotFound: python3.6; py37: commands succeeded; report: commands succeeded)
 * 10ec6bf4: Edit Dockerfile-18.10 to use the local folder. * Tests all pass on 18.10 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test_unicode_filelist; TestUnicode.test_unicode_paths_asterisks; TestUnicode.test_unicode_paths_non_globbing; TestUnicode.test_unicode_paths_square_brackets)
 * eabf46d4: Use local folder instead of bzr revision, so remove the revision arguments in the setup script. * Modify Dockerfile and Dockerfile-18.04 to copy the local folder rather than the remote repository. * Tests all pass on 18.04 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test_unicode_filelist; TestUnicode.test_unicode_paths_asterisks; TestUnicode.test_unicode_paths_non_globbing; TestUnicode.test_unicode_paths_square_brackets)
 * 868e62c9: Merge with trunk
 * e1045b46: Launchpad automatic translations update.
 * d8de8c56: Fix .bzrignore
 * 34d3b5f9: Launchpad automatic translations update.
 * 891d34f6: Merged in lp:~kaffeekiffer/duplicity/azure-filename - Encode Azure back-end paths
 * bd4ccabb: Merged in lp:~aaron-whitehouse/duplicity/08-README-TESTING - Change README-TESTING to be correct for running individual tests now that we have moved to Tox/Pytest.
 * 9562e9c3: Encode Azure backend file names
 * 6d669015: Fix debian/rules file
 * 669ce449: Fix setup.py shebang
 * 41b30829: Fix debian/rules file
 * b6743b76: Fix debian/rules file
 * e725164b: Fix debian/rules file
 * 9c872909: Fix debian/control file
 * 4af01c18: Fix debian/control file
 * dad0c63b: Fix debian/control file
 * a3f1d544: Fix debian/control file
 * 4cb7ca43: Launchpad automatic translations update.
 * b7a27ad3: Fix debian/control file
 * aa387b44: Fix debian/control file
 * dea42195: Fix debian/control file
 * 8725ca01: Fix debian/control file
 * 00e59fd5: Fix debian/control file
 * 1dbc9a7a: Fix debian/control file
 * dfe8803b: Ran futurize selectively filter-by-filter to find the ones that work.
 * f3b1f584: Fixed build on Launchpad for 0.8.x, so now there is a new PPA at https://launchpad.net/~duplicity-team/+archive/ubuntu/daily-dev-trunk
 * 9dd955f4: Fix debian/control file
 * ae8a5318: Fix debian/control file
 * 9762a72a: Merged in lp:~aaron-whitehouse/duplicity/08-snap-python2 - Add packaging code for Snapcraft/Snap packages
 * 4a96e695: Add snap package creation files * Modify dist/makedist to version the snapcraft.yaml
 * 0767bce9: Remove a mess I made.
 * 29a0d1fb: Fixed bug #1839886 with hint from denick - Duplicity crashes when using --file-prefix * Removed socket.settimeout from backend.py. It was already set in commandline.py. * Removed pycryptopp from README requirements
 * 701b5a27: Launchpad automatic translations update.
 * e7b0a1f5: Fixed bug #1839728 with info from Avleen Vig - b2 backend requires additional import
 * 85f53c01: Launchpad automatic translations update.
 * 6e22e1b8: Launchpad automatic translations update.
 * a1b72c75: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py * Fixed division differences with futurize
 * b3ad29ca: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py * Fixed division differences with futurize
 * 42061d8f: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py
 * 3f6b9819: More changes to provide Python test coverage: Now covers functional tests spawning duplicity - Does not cover bin/duplicity for some reason
 * cb4ca276: Fixed bugs #1838427 and #1838702 with a fix suggested by Stephen Miller. The fix was to supply tarfile with a unicode grpid, not bytes.
 * 659573a4: Launchpad automatic translations update.
 * 85eac110: Some changes to provide Python test coverage: Coverage runs with every test cycle - Does not cover functional tests that spawn duplicity itself. Next pass. - After a run use 'coverage report html' to see an overview list and links to drill down. It shows up in htmlcov/index.html.
 * 51893a19: Fix dist/makedist to run on python2/3
 * 4af852c6: Fix dist/makedist to run on python3
 * 84890aa5: Fix dist/makedist to run on python3
 * f0e9f3f1: One last change for bug #1829416 from charlie4096
 * a017fd78: Merged in po-updates. * Fixed bug #1829416 with help from charlie4096 - onedrive: Can’t convert ‘bytes’ object to str implicitly
 * 64ece375: Enhanced build_duplicity_test.sh - Use -h to get help and defaults - Takes arguments for distro, revno, help - Distros supported are 18.04, 18.10, 19.04, 19.10 - Revnos are passed to bzr -r option
 * 3487456a: Fix so Docker image duplicity_test will update and pull new bzr revisions if changed since last build.
 * 13f4e348: Remove speedup in testing backup. The math was correct, but it's failing on Docker and Launchpad testing.
 * cb53a81f: Fix language classifiers in setup.py
 * 7d2fab89: Removed python-gettext from setup.py. Whoops!
 * a020404e: Move pytest-runner setup requirement to a test requirement
 * 5de10b39: Merged in lp:~stragerneds/duplicity/duplicity - Cache results of filename parsing for speedup
 * d8e710dd: Merged in lp:~limburgher/duplicity/dropbox - Fixes bug #1836611 dropbox mixing bytes and strings
 * eab278fd: Fixed bug #1836829 progress.py: old_div not defined - also fixed old_div in _boto_multi.py
 * 11df6f2d: Fixed bug #1836829 progress.py: old_div not defined - also fixed old_div in _boto_multi.py
 * d2512351: Remove python-gettext from requirements.txt. Normal Python installation includes gettext. * Mod README to include Python 3.6 and 3.7
 * 8de013d5: Correct types for os.join in Dropbox backend.
 * 1f4c71de: Launchpad automatic translations update.
 * f2518d66: Merged in po-updates.
 * a32dd60f: Comment out HSIBackendTest since shim is not up-to-date.
 * 161cf6ac: Install python3.6 and 3.7 explicitly in Dockerfile. Tox and Docker now support testing Python 2,7, 3.6, and 3.7.
 * 54b38b9b: Launchpad automatic translations update.
 * fae48318: Launchpad automatic translations update.
 * 5ef79b3e: Make sure test filenames are bytes not unicode. * Fix test_glob_to_regex to work on Python 3.7
 * 0896a250: Going back to original. No portable way to ignore warning.
 * 2d57667d: Another unadorned string.
 * 64627284: Cleanup some trailing spaces/lines in Docker files.
 * 738bc950: Fix so we start duplicity with the base python we run under.
 * f6447695: Adjust POTFILES.in for compilec.py move.
 * 867dadf6: Ensure _librsync.so is regenned before toc testing.
 * 0c21c20f: Add encoding to logging.FileHandler call to make log file utf8
 * 7e27f4a7: Fix warning in _librsync.c module.
 * b459768f: Optimize loading backup chains; reduce file_naming.parse calls
 * bdaf3d19: Fix some issues found by test_code.py (try 2)
 * 266e6a83: Fix some issues found by test_code.py.
 * 8cd38578: Fix reversed port assignments (FTP & SSH) in docker-compose.yml.
 * b6a634e1: Convert the docker duplicity_test image to pull the local branch into the container, rather than lp:duplicity. This allows the use of the duplicity Docker testing containers to test local changes in a known-good environment before they are merged into trunk. The equivalent of the old behaviour can be achieved by starting with a clean branch from lp:duplicity. * Expand Docker context to parent branch folder and use -f in the docker build command to point to the Dockerfile. * Simplify build-duplicity_test.sh now that the whole folder is copied (individual files no longer need to be copied)
 * f8db0aa9: Fix reimport problem where "from future.builtins" was being treated the differently than "from builtins". They are both the same, so converted to shorter form "from builtins" and removed duplicates.
 * 7f83e334: Merged in lp:~mterry/duplicity/s3fsdecode - Fix s3 backups by encoding remote filenames
 * 6a7a1499: Merged in lp:~aaron-whitehouse/duplicity/08-dockerfixes - Update duplicity_test Dockerfile: Use 18.04 instead of 16.04 * Use Ubuntu 18.04 version of pip * Add Python3 and 2to3 as a dependencies * Set docker locale as UTF-8
 * ee08ae88: Merged lp:~mterry/duplicity/boto-import - A couple functions in the boto backend were using the boto module without importing it first.
 * e07b429e: Normalize shebang to just python, no version number * Fix so most testing/*.py files have the future suggested lines - from __future__ import print_function from future import standard_library standard_library.install_aliases()
 * 64d71775: Fix s3 backups by encoding remote filenames
 * c2819f57: Merge with trunk
 * da3cf0e6: Add 2to3 as a dependency to dockerfile
 * 37387bea: Add tzdata back in as a dependency and set DEBIAN_FRONTEND=noninteractive so no tzdata prompt
 * d46e4bae: Set docker container locale to prevent UTF-8 errors
 * 95d074cf: Change dockerfile to use 18.04 instead of 16.04 and other fixes.
 * d3916839: Fix s3 backups by importing the boto module
 * f4b69317: Launchpad automatic translations update.
 * a0d9f96d: Fixed failing test in testing/unit/test_globmatch.py - Someone is messing with regex. Fix same. - See https://bugs.python.org/issue29995 for details
 * 79981055: Fixed bug #1833559 0.8 test fails with 'duplicity not found' errors - Fixed assumption that duplicity/rdiffdir were in $PATH
 * 60251204: Fixed bug #1833573 0.8.00 does not work on Python 2 - Fixed shebang to use /usr/bin/python instead of python2
 * 3eaf74ce: Launchpad automatic translations update.
 * 110c5332: Fix some test_code errors that slipped by.
 * 95ca6247: Merged in lp:~kaffeekiffer/duplicity/azure-python3-fix - Use util.fsencode to encode file string
 * 8b7b7e81: Fixed bug #1831178 sequence item 0: expected str instance, int found - Simply converted int to str when making list
 * 22337823: Fix some import conflicts with the "past" module - Rename collections.py to dup_collections.py - Remove all "from future.utils import old_div" - Replace old_div() with "//" (in py27 for a while). - All tests run for py3, unit tests run for py3. The new import fail is "from future import standard_library"
 * c75520e9: Fix Azure backend for python 3
 * 97830b83: Spaces to tabs for makefile.
 * 76a6e901: Change to python3 for build
 * d9b170a3: Merged in lp:~mterry/duplicity/uexc-string - The return type of util.uexc should always be a string.
 * 05943596: Have uexc to always return a string
 * 934aad0d: Launchpad automatic translations update.
 * 81439742: Add requirements for python-gettext
 * abddc91c: Merged in lp:~mterry/duplicity/gio-pydrive-fsdecode - Fix gio and pydrive backends to use fsdecode
 * 56d0c818: Fix gio and pydrive backends to use fsdecode
 * 0eafcbe1: Merged in lp:~stragerneds/duplicity/duplicity - improve test backup speed - insure all test output is read
 * b439ff29: Launchpad automatic translations update.
 * 9482562b: Fix TestGlobToRegex.test_glob_to_regex for py3.6 and above - see https://bugs.python.org/issue29995 for details
 * e46eb344: Launchpad automatic translations update.
 * 3d3fe25a: Remove unnecessary sleeping after running backups in tests
 * fadea9e3: Minimize time spent sleeping between backups
 * f530dd76: Ensure all duplicity output is captured in tests
 * a9a34425: Some more work on unadorned strings - Fixed test_unadorned_string_literals to list all strings found - Added bin/duplicity and bin/rdiffdir to list of files tested - All unadorned strings have now been adorned
 * cde7b7b9: Launchpad automatic translations update.
 * ec945ce4: Fixed bug #1828662 with patch from Bas Hulsken - string.split() had been deprecated in 2, removed in 3.7
 * 41bac6d6: Merged in lp:~mgorse/duplicity/0.8-series - Python 3 fixes to imapbackend.py - Fix bug 1828869: refresh CollectionsStatus after sync
 * 7beafc6b: Fix some unadorned strings.
 * 56ade83a: Fix some unadorned strings.
 * bc38fa13: Fix to allow >=2.7 or >=3.5
 * 98f181ef: Fix to always compile _librsync before testing.
 * fd130945: setup.py: allow python 2.7 again
 * 6829ac38: Bug #1828869: update CollectionsStatus after sync
 * bc62bffb: imap: python 3 fixes
 * 7ba0b41c: sync: handle parsed filenames without start/end times
 * ba40023f: More PEP 479 fixes
 * 7c68abdd: Manual merge of lp:~yajo/duplicity/duplicity - Support partial metadata sync. - Fixes bug #1823858 by letting the user to choose partial syncing. Only the metadata for the target chain will be downloaded. If older (or newer) chains are encrypted with a different passphrase, the user will be able to restore to a given time by supplying only the passphrase for the chain selected by the `--restore-time` option when using this new option. - A side effect is that using this flag reduces dramatically the sync time when moving files from one to another location, in cases where big amounts of chains are found.
 * 8e0bb1b3: Change to Python >= 3.5
 * 784b87ed: Merged in lp:~brandon753-ba/duplicity/aws-glacier - Adds support for for a command line option to store data on AWS S3 Glacier.
 * bd65c5c3: Fix bug #1811114 with revised onedrivebackend.py from David Martin - Adapt to new Microsoft Graph API
 * 8f0030bf: Removed last mention of copy.com from man page with help from edso.
 * 997e4eaf: Merged in lp:~aaron-whitehouse/duplicity/08-style-fixes - Fix pylint style issues (over-indented text, whitespace on blank lines etc) - Removed "pylint: disable=bad-string-format-type" comment, which was throwing an error and does not seem to be needed.
 * d9ddf161: Merged in lp:~aaron-whitehouse/duplicity/08-uexc-fix - Fix for Bug #1770929 with associated test cases (thanks to Pete Zaitcev (zaitcev) in Bug #1797928 for the head start).
 * 8d6664d3: Merged in lp:~mgorse/duplicity/0.8-series - More python 3 fixes
 * 8f8369cd: Added documentation on how to use the new AWS S3 Glacier option.
 * 9e52eeff: Fix pylint style issues (over-indented text, whitespace on blank lines etc) * Removed "pylint: disable=bad-string-format-type" comment, which was throwing an error and does not seem to be needed.
 * 82b49937: Accomodate unicode input for uexc and add test for this.
 * f087516f: Convert deprecated .message to args[0]
 * 6166fe0d: Add test case for lp:1770929 * Added fix (though using deprecated .message syntax)
 * 45dac6ff: Change README-TESTING to be correct for running individual tests now that we have moved to Pytest.
 * 7c902b20: Fixed a typo in prior commit
 * ef326de3: Added support for AWS glacier storage class
 * 76896c0d: Attempt to port sx backend to python 3
 * b7337f22: rsync: py3 fixes
 * cc77e0bf: ncftp: py3 fixes
 * 4ed97fe1: test_selection.py: fix an invalid escape sequence on py3
 * 28f4a4e8: Fix sync_archive on python 3
 * 5f3ef2d0: ssh_pexpect: py3 fixes
 * f7a18010: Pull from main branch
 * d541342c: Launchpad automatic translations update.
 * f09663ca: Fixed bug #1817375 with hint from mgorse - Added 'global pexpect' at end of imports
 * 7bd2233f: Merged in lp:~mterry/duplicity/pydrive-root - Just a tiny fix to clean up the temporary file we create to find the root ID. It's a little surprising for the user if they wind up with this file called "i_am_in_root" that they don't know where it came from. Almost sounds like they were hacked.
 * e95da3df: Merged in lp:~mgorse/duplicity/0.8-series - More changes for unicode and py3 support
 * 28d4a425: pydrive: delete temporary root file
 * 4c8051d0: Launchpad automatic translations update.
 * 709a3bee: __unicode__ -> __str__
 * 01960302: Fix a regex substitution on python 3
 * 51a8c742: Return temporary filenames as bytes
 * cfdf24d7: Modify some generators to return when finished
 * 6c2a5084: Fix lftp breakage introduced by the python 3 changes
 * ba4bce04: Bug #1813214 was marked fixed in 0.7.13. There were still a couple of copy.com references remaining in the docs and web. Got those nuked, finally.
 * 3c3c63a8: Merged in lp:~vam9/duplicity/0.8-series-s3-kms-support - Added s3 kms server side encryption support with kms-grants support.
 * 13430f7f: Merged in lp:~okrasz/duplicity/duplicity - Add --azure-blob-tier that specifies storage tier (Hot,Cool,Archive) used for uploaded files.
 * 36f8ea7d: Putting option in man in alphabetical order + description improvement.
 * dd96df13: Adds setting to specify Azure Blob standard storage tier.
 * 5bdfbcc4: Fixed bug #1803896 with patch from slawekbunka - Add __enter__ and __exit__ to B2ProgressListener
 * 083006e2: Launchpad automatic translations update.
 * 10c117c9: Merged in lp:~mgorse/duplicity/0.8-series - First pass at a python 3 port.
 * 47c51ee4: tox: Target py3, rather than py36
 * ac55ddad: Fix some punctuation.
 * 92ce7610: Launchpad automatic translations update.
 * fd8a0c60: Fixed bug #1798206 and bug #1798504 * Made paramiko a global with import during __init__ so it would not be loaded unless needed.
 * 9df440ef: Merged in lp:~mcuelenaere/duplicity/duplicity - Make sure we don't load files completely into memory when transferring them from/to the remote WebDAV endpoint.
 * a956029d: _librsyncmodule.c: Use s in format parameters again under python 2
 * ca3f6ab5: Fix comment from last commit
 * bda236b1: compilec.py: work around conflict with collections.py vs. built-in collections module
 * b51cd393: First pass at a python 3 port
 * 875c8738: tox: pass LC_CTYPE
 * 1212e466: Change WebDAV backend to not read/write files into memory, but stream them from/to disk to/from the remote endpoint
 * 6bb552cd: Launchpad automatic translations update.
 * bd48c470: Fixed but #1797797 with patch from Bas Hulsken - use bytes instead of unicode for '/' in filenames
 * ba7204e1: Merged in lp:~mgorse/duplicity/0.8-series - Run futurize --stage1, and adjust so that tests still pass.
 * 00b48bd2: Launchpad automatic translations update.
 * fa0b478f: Run futurize --stage1 on rdiffdir
 * f2b23a96: Run futurize --stage1 on bin/duplicity
 * a0ebce15: Run futurize --stage1, and adjust so that tests still pass.
 * 0785121d: Merged in lp:~mgorse/duplicity/0.8-series - Adorn some remaining strings
 * bfaab509: Adorn some remaining strings
 * 45425a4c: Launchpad automatic translations update.
 * 90bc58b6: Merged in lp:~qsantos/duplicity/fix-unmatched-rule-error - There are actually two commits: the first fixes a very minor detail in the README regarding the Python version that should be used; the second fixes the way exceptions are handled when an incorrect rule is specified, and display the nice error message rather than an obscure stack trace.
 * 423b5024: Fix error message on unmatched glob rules
 * b3f1c3c7: Fix required Python version in README
 * 4e737e33: Launchpad automatic translations update.
 * 5aa8f24f: Fixed bug #1795227 global name Dropbox is not defined - Applied patch from Pedro Gimeno to restore globals
 * bcc017cd: Merged in lp:~mgorse/duplicity/0.8-series - Adorn more strings in duplicity/*.py
 * 4032a94c: Annotate more strings in duplicity/*.py
 * 51946b3a: Added s3 kms server side encryption support with kms-grants support.
 * 6924ede6: Launchpad automatic translations update.
 * 66780970: Merged in lp:~mgorse/duplicity/0.8-series - Adorn some duplicity/*.py strings. I've avoided submitting anything that I think might require significant discussion; I think that reviewing will be easier this way. Mostly annotated strings as unicode, except for librsync.py.
 * ed328524: Adorn strings in some duplicity/*.py files. Several files are still tbd.
 * bdb765d6: Unicode fixes
 * 2bd92912: Make files executable.
 * ec0c1bfd: Launchpad automatic translations update.
 * 844d82bd: Mark adorned all but one of testing/unit.
 * da0bfc17: Launchpad automatic translations update.
 * a4ce06b8: Released some things without proper paperwork: Adorned strings in testing/, testing/functional/, and testing/unit * Added AUTHORS file listing all copyright claimants in headers
 * e9ee3a99: Launchpad automatic translations update.
 * 09d1ef84: Missed a couple. Simple sort.
 * 1af0adf6: Add AUTHORS file.
 * 61e9cea5: Checkpoint: Fixing unadorned strings for testing/unit/*.
 * f0504074: Launchpad automatic translations update.
 * bab4d04f: Launchpad automatic translations update.
 * 23f74eca: Fixed unadorned strings for testing/functional/*.
 * d53e4754: Fixed unadorned strings for testing/*.
 * 9511554c: Reverted back to rev 1317 and reimplemented revs 1319 to 1322
 * 93872236: Reverted back to rev 1317 and reimplemented revs 1319 to 1322
 * cdc60b11: Whoops, my bad! Released before fully testing. Reverting to rev 1317 and proceeding from there with unadorned string conversion.
 * 38e9584e: Move docs/conf.py to ignored. Sphinx rewrites it.
 * 2e92030d: Launchpad automatic translations update.
 * 0dffa871: Fix a misspelling
 * 99835a30: Fix 2to3 error found with newer 2to3 module.
 * b15e2f74: Nuke remnants of copycom and acdcli backends * Regen docs
 * bfdc1f33: Fixed unadorned strings to unicode in duplicity/*/* - Some fixup due to shifting indenataion not matching PEP8. - Substituted for non-ascii char in jottlibbackend.py comment.
 * 2228530a: Fixed unadorned strings to unicode in duplicity/backends/* - Some fixup due to shifting indenataion not matching PEP8.
 * 957833d5: Fixed unadorned strings to unicode in duplicity/backends/* - Some fixup due to shifting indenataion not matching PEP8.
 * b78f448a: Launchpad automatic translations update.
 * 28813e6f: Added function to fix unadorned strings (testing/fix_unadorned_strings.py) - Fixes by inserting 'u' before token string - Solves 99.9% of the use cases we have - Fix unadorned strings to unicode in bin/duplicity and bin/rdiffdir - Add import for __future__.print_function to find_unadorned_strings.py
 * 06b11a47: Fix unadorned strings to unicode.
 * 238942df: Add gpg sockets to ignore list.
 * 8a03ad70: Add fix_unadorned_strings.py to ignore list.
 * a74d19c4: Add function to fix unadorned strings by inserting 'u' before. Solves 99.9% of the use cases we have.
 * 70a2f933: Add import for __future__.print_function
 * cf73e52c: Launchpad automatic translations update.
 * 5a7b6ba3: Merged in lp:~aaron-whitehouse/duplicity/08-adorn-strings - Adorning string literals (normally to make these unicode), in support of a transition to Python 3. See https://blueprints.launchpad.net/duplicity/+spec/adorn-string-literals - Adorn string in duplicity/globmatch.py. - Adorn strings in testing/unit/test_globmatch.py - Adorn strings in selection.py - Adorn strings in functional/test_selection.py and unit/test_selection.py - Remove ignores for these files in test_code.py
 * f5059f2a: Adorn globs in functional/test_selection.py and unit/test_selection.py * Remove ignores for these files in test_code.py
 * 5eee717e: Remove selection.py exception from test_code.py
 * 2cb9f5ea: Adorn globs in selection.py
 * e7e2ab14: Merge with trunk
 * d9ca13f8: Launchpad automatic translations update.
 * e376c54b: Launchpad automatic translations update.
 * bd2b1530: Fixed bug #1780617 Test fail when GnuPG >= 2.2.8 - Relevant change in GnuPG 2.2.8: https://dev.gnupg.org/T3981 - Added '--ignore-mdc-error' to all gpg calls made.
 * 599a1ada: Launchpad automatic translations update.
 * 6d96af59: Merged in lp:~excitablesnowball/duplicity/s3-onezone-ia - Add option --s3-use-onezone-ia S3 One Zone Infrequent Access Storage
 * fac137b1: Add support for S3 One Zone - Infrequent Access storage class.
 * 8d7f2724: Adorn strings in testing/unit/test_globmatch.py
 * 4d46e84f: Adorn string literals in duplicity/globmatch.py.
 * 77e70a83: Launchpad automatic translations update.
 * ef1547d7: Merged in lp:~aaron-whitehouse/duplicity/08-unadorned-strings - Added new script to find unadorned strings (testing/find_unadorned_strings.py python_file) which prints all unadorned strings in a .py file. - Added a new test to test_code.py that checks across all files for unadorned strings and gives an error if any are found (most files are in an ignore list at this stage, but this will allow us to incrementally remove the exceptions as we adorn the strings in each file). - Adorn string literals in test_code.py with u/b
 * 2ebb1072: Merged in lp:~aaron-whitehouse/duplicity/08-pycodestyle - Tox changes to accommodate new pycodestyle version warnings. Ignored W504 for now and marked as a TODO. Marked W503 as a permanent ignore, as it is prefered to the (mutually exclusive) W504 under PEP8. - Marked various regex strings as raw strings to avoid the new W605 "invalid escape sequence".
 * 7dd613a1: Added new script to find unadorned strings (testing/find_unadorned_strings.py python_file) which prints all unadorned strings in a .py file. * Added a new test to test_code.py that checks across all files for unadorned strings and gives an error if any are found (most files are in an ignore list at this stage, but this will allow us to incrementally remove the exceptions as we adorn the strings in each file).
 * 1e64cdee: Adorn string literals in test_code.py with u/b * Add test for unadorned string literals (currently only single file)
 * 12649b7e: Tox changes to accommodate new pycodestyle version warnings. Ignored W504 for now and marked as a TODO. Marked W503 as a permanent ignore, as it is prefered to the (mutually exclusive) W504 under PEP8. * Marked various regex strings as raw strings to avoid the new W605 "invalid escape sequence".
 * d4aacfa5: Fixed bug #x1717935 with suggestion from strainu - Use urllib.quote_plus() to properly quote pathnames passed via URL
 * 3ad79af2: Fixed bug #1768954 with patch from Max Hallden - Add AZURE_ENDPOINT_SUFFIX environ variable to allow setting to non-U.S. servers
 * 6fe72d50: Merged in lp:~dawgfoto/duplicity/fixup1252 * only check decryptable remote manifests - fixup of revision 1252 which introduces a non-fatal error message (see #1729796) - for backups the GPG private key and/or it's password are typically not available - also avoid interactive password queries through e.g. gpg agent
 * 3a9932d4: only check decryptable remote manifests - fixup of revision 1252 which introduces a non-fatal error message (see #1729796) - for backups the GPG private key and/or it's password are typically not available - also avoid interactive password queries through e.g. gpg agent
 * c1c17c2a: check last manifest only with prev. backup
 * b1db604d: Launchpad automatic translations update.
 * 367f1334: Launchpad automatic translations update.
 * 7279d50c: Launchpad automatic translations update.
 * 4e51a2a3: Launchpad automatic translations update.
 * 34950330: Launchpad automatic translations update.
 * a1850691: Mass update of po files from launchpad translations.
 * 5f463949: Merged in lp:~dawgfoto/duplicity/fixup1251 - Avoid redundant replication of already present backup sets. - Fixed by adding back BackupSet.__eq__ which was accidentally(?) removed in 1251.
 * ad8c5a1d: Avoid redundant replication of already present backup sets - Add back BackupSet.__eq__ which was accidentally removed in 1251
 * 1698df42: Reduce dependencies on backend libraries - Moved backend imports into backend class __init__ method - Surrounded imports with try/except to allow better errors - Put all library dependencies in requirements.txt
 * 16c411ca: Merged in lp:~aaron-whitehouse/duplicity/08-ufn-to-fsdecode - Change util.fsdecode to use "replace" instead of "ignore" (matching behaviour of util.ufn) - Replace all uses of ufn with fsdecode - Make backend.tobytes use util.fsencode rather than reimplementing
 * a87414af: Make backend.tobytes use util.fsencode rather than reimplementing
 * 86b6258d: Merge with trunk
 * 9ace158a: Change util.fsdecode to use "replace" instead of "ignore" (matching behaviour of util.ufn) * Replace all uses of ufn with fsdecode
 * e56a707b: Fixes so pylint 1.8.1 does not complain about missing conditional imports. - Fix dpbxbackend so that imports require instantiation of the class. - Added pylint: disable=import-error to a couple of conditional imports
 * 98be0f65: Update docs.
 * eccd197c: Merged in lp:~aaron-whitehouse/duplicity/08-ufn-to-uc_name - Replace util.ufn(path.name) with path.uc_name throughout.
 * 1d6e0511: Merge with trunk.
 * 57230453: Replace util.ufn(path.name) with path.uc_name throughout.
 * 97b9c6c9: More pytest changes - Use requirements.txt for dependencies - Run unit tests first, then functional - Some general cleanup
 * b4bb3654: More pytest changes - Use requirements.txt for dependencies - Run unit tests first, then functional - Some general cleanup
 * 783b72fd: Converted to use pytest instead of unittest (setup.py test is now discouraged) - We use @pytest.mark.nocapture to mark the tests (gpg) that require no capture of file streams (currently 10 tests). - The rest of the tests are run normally
 * b1882672: Remove precise-lpbuild. EOL as of April 28, 1917.
 * cf47e310: Remove unused import.
 * 7523d612: First cut converting to pytest. - 'setup.py test' now uses pytest. We still use tox for correct virtualenv setup. All seem to be current best practices since 'setup.py test' use is discouraged. - Global --capture=no option to allow gpg tests to complete successfully. Future should only turn off capture to the gpg tests themselves. Creates a still messy output.
 * 9f11e31a: Merged in lp:~aaron-whitehouse/duplicity/08-unicode - Many strings have been changed to unicode for better handling of international characters and to make the transition to Python 3 significantly easier, primarily on the 'local' side of duplicity (selection, commandline arguments etc) rather than any backends etc.
 * 62e297e7: Various code tidy-ups pre submitting for merge. None should change behaviour.
 * 91916e54: Change fsdecode to use globals.fsencoding * Add 'ANSI_X3.4-1968' to the list of fsencodings that globals.fsencode treats as probably UTF-8
 * b1603245: Merge in lp:~mterry/duplicity/unicode-future
 * 8d9d0c39: Sync with trunk.
 * fd55349a: Merge with trunk * Add back in testing/testfiles.tar.gz (accidentally made unversioned in previous commit when doing manual merge of archives) * PEP8 error (from trunk)
 * 1cf52762: Fix PEP8 issues.
 * 61c38e0e: Merged in lp:~crosser/duplicity/fix-small-file-upload - Fixed small file upload changes made in Dropbox SDK v7.1
 * a91474c8: Merge with trunk (including manual merge of testfiles.tar.gz to add select-unicode to the version without the non-UTF8 file)
 * 8f2240c2: dpbxbackend: fix small files upload (API change)
 * b3584716: Specify debian dependency too
 * 62b1ce5e: Specify future requirement
 * a3b05cae: Merged in lp:~crosser/duplicity/dpbx-fix-file-listing - Fixed bug #1639664 "Dropbox support needs to be updated for Dropbox SDK v7.1"
 * bdd76822: Merged in lp:~crosser/duplicity/fix-oauth-flow - Fixed bug #1638236 "BackendException with oauth2client 4.0.0"
 * e4e65932: dpbxbackend: check for specific API error for missing folder
 * a33c50ff: The "new" Dropbox OAuth API return objects rather than tuples. Adjust auth flow to that.
 * 5453c89d: The "new" Dropbox API for directory listing raises an exception when the directory is empty (and duplicity directory will be empty on the first run). We actually want and empty list of files if the list of files is emtpy. So catch the ListFolderError and continue.
 * a632d28e: More fixes for Unicode handling - Default to 'utf-8' if sys.getfilesystemencoding() returns 'ascii' or None - Fixed bug #1386373 with suggestion from Eugene Morozov
 * ca58c22f: Fixed bug #1733057 AttributeError: 'GPGError' object has no attribute 'decode' - Replaced call to util.ufn() with call to util.uexc(). Stupid typo!
 * 0c1fa988: Fix attribution for patch of 1448094 to Wolfgang Rohdewald.
 * 22699028: Merge with trunk (and fix PEP error in backends/pydrivebackend.py)
 * 31ffda2a: Remove non-UTF8 filename from testfiles.tar.gz.
 * 086f84c5: Fixed bug #1730902 GPG Error Handling - use util.ufn() not str() to handle encoding
 * 7e4a37a1: Fixed bug #1723890 with patch from Killian Lackhove - Fixes error handling in pydrivebackend.py
 * 08f6949d: Fixed bug #1720159 - Cannot allocate memory with large manifest file since 0.7.03 - filelist is not read if --file-changed option in collection-status not present - This will keep memory usage lower in non collection-status operations
 * f79aaf31: Fix PEP8 issues in b2backend.py.
 * da6955d2: Fixed bug #1724144 "--gpg-options unused with some commands" - Add --gpg-options to get version run command
 * 86924571: Fixed bug #1448094 with patch from Tomáš Zvala - Don't log incremental deletes for chains that have no incrementals
 * 1ecb27d1: Fixed bug #1654756 with new b2backend.py module from Vincent Rouille - Faster (big files are uploaded in chunks) - Added upload progress reporting support
 * 98a9ba7c: Remove conditional pexpect in testing/functional/__init__.py -- while the commented-out text is the nicer approach in versions after pexpect 4.0, we need to support earlier versions at this stage and a single code path is simpler.
 * 8468dbb8: Patched in lp:~mterry/duplicity/rename-dep - Make rename command a dependency for LP build
 * 75852da1: Merge with trunk
 * f34d8004: Fixed bug #1714663 "Volume signed by XXXXXXXXXXXXXXXX, not XXXXXXXX" - Normalized comparison length to min length of compared keys before comparison - Avoids comparing mix of short, long, or fingerprint size keys.
 * 0244a0e8: Merge with trunk.
 * 387eb406: Fix PEP8 issues.
 * 4e05ed79: Fixed bug #1715650 with patch from Mattheww S - Fix to make duplicity attempt a get first, then create, a container in order to support container ACLs.
 * 75f779e3: More fixes to backend.py plus some cleanup.
 * e6fb27a2: Fix backend.py to allow string, list, and tuple types to support megabackend.py.
 * aa2d25d9: Merged in lp:~mterry/duplicity/more-decode-issues - Here's some fixes for another couple UnicodeDecodeErrors. - The duplicity/dup_time.py fixes when a user passes a utf8 date string (or a string with bogus utf8 characters, but they have to really try to do that). This is bug 1334436. - The bin/duplicity change from str(e) to util.uexc(e) fixes bug 1324188. - The rest of the changes (util.exception_traceback and bin/duplicity changes to use it) are to make the printing of exceptions prettier. Without this, if you see a French exception, you see "accept\xe9es" instead of "acceptées". - You can test all of these changes in one simple line: $ LANGUAGE=fr duplicity remove-older-than $'accept\xffées'
 * c0351375: Fix some unicode decode errors around exceptions
 * 68662bb7: Fixed bug introduced in new megabackend.py where process_commandline() takes a string not a list. Now it takes both. * Updated web page for new megabackend requirements.
 * 4313c6eb: Fixed bug #1638033 Remove leading slash on --file-to-restore - code already used rstrip('/') so change to just strip('/')
 * 22f9c373: 2017-08-31 Kenneth Loafman <kenneth@loafman.com>
 * 860581fc: # Fixed bug #1394386 with new module megabackend.py from Tomas Vondra - uses megatools from https://megatools.megous.com/ instead of mega.py library which has been deprecated - fixed copyright and PEP8 issues - replaced subprocess.call() with self.subprocess_popen() to standardize
 * c16acf93: # Fixed bug #1394386 with new module megabackend.py from Tomas Vondra - uses megatools from https://megatools.megous.com/ instead of mega.py library which has been deprecated - fixed copyright and PEP8 issues
 * 5b1483ff: Merged in lp:~mterry/duplicity/gpg-tag-versions - Support gpg versions numbers that have tags on them. - This can happen if you build gpg from git trunk (e.g. 2.1.15-beta20). Or if you run against the freedesktop flatpak runtime (e.g. 2.1.14-unknown).
 * f6573679: Fix errors where log.Warn was invoked with log.warn in webdavbackend.py
 * 943c4571: Support gpg versions with -tag suffixes
 * de28ab97: Merged in lp:~mterry/duplicity/gio_child_for_display_name - gio: be slightly more correct and get child GFiles based on display name
 * 45f82fcc: Fixed PEP8 errors in bin/duplicity
 * ffb851b3: Fixed bug #1709047 with suggestion from Gary Hasson * fixed so default was to use original filename
 * b6fee2ad: gio: be slightly more correct and get child GFiles based on display name
 * 70fb3a6d: Merged in lp:~mterry/duplicity/giobackend-display-name - giobackend: handle a wider variety of gio backends by making less assumptions; in particular, this fixes the google-drive: backend
 * 1a8ebd3c: giobackend: handle a wider variety of gio backends by making less assumptions; in particular, this fixes the google-drive: backend
 * e70d1275: Merge from trunk (with pylint fixes).
 * 96614394: Fixed encrypted remote manifest handling to merely put out a non-fatal error message and continue if the private key is not available.
 * 96f13485: Fixed slowness in 'collection-status' by basing the status on the remote system only. The local cache is treated as empty.
 * 2d37ea73: Merge from trunk
 * f5b8e76a: Fix text of last change.
 * 54ee4f38: Patched in lp:~dawgfoto/duplicity/skip_sync_collection_status - collection-status should not sync metadata - up-to-date local metadata is not needed as collection-status is generated from remote file list - syncing metadata might require to download several GBs
 * fd5f4f8a: collection-status should not sync metadata - up-to-date local metadata is not needed as collection-status is generated from remote file list - syncing metadata might require to download several GBs
 * c7052a74: Fixed PEP8 and 2to3 issues.
 * 60aa6ef6: Merged in lp:~xlucas/duplicity/pca-backend - Add support for OVH Public Cloud Archive backend.
 * 3f001439: Merged in lp:~xlucas/duplicity/multibackend-prefix-affinity - Support prefix affinity in multibackend.
 * 3d32cf96: Merge with trunk, turning string literals in the new testing/functional/test_replicate.py into unicode.
 * 02378290: Merged in lp:~dawgfoto/duplicity/replicate - Add integration test for newly added replicate command. - Also see https://code.launchpad.net/~dawgfoto/duplicity/replicate/+merge/322836.
 * a627de1f: add integration test for newly added replicate command
 * d3681607: Fixed problem in dist/makedist when building on Mac where AppleDouble files were being created in the tarball. See: https://superuser.com/questions/61185/why-do-i-get-files-like-foo-in-my-tarball-on-os-x
 * e0ce2a69: Fixed problem in dist/makedist when building on Mac where AppleDouble files were being created in the tarball. See: https://superuser.com/questions/61185/why-do-i-get-files-like-foo-in-my-tarball-on-os-x
 * c80cc195: Add support for OVH Public Cloud Archive backend.
 * ab246ece: Remove util.bytes_to_uc (as either .decode or fsdecode is preferable). * Move unicode conversion for select options from selection.py to commandline.py.
 * 09f69b1c: Replace util.py functions to and from unicode with direct calls to .encode and .decode, as it did not save much code, means the "strict"/"ignore"/"replace" decision can be made per call. Also helps narrow down on why sys.getfilesystemencoding() is not working as expected in some places.
 * 9dcb238c: Merge remaining file from trunk. Tests pass.
 * ebc7efb6: Merged in lp:~duplicity-team/duplicity/po-updates
 * bec1efe6: Merge all but bin/duplicity/ (which breaks testing.functional.test_final.FinalTest.test_asym_with_hidden_recipient_cycle )
 * 4dfa7abd: Merged in lp:~xlucas/duplicity/swift-multibackend-bug - Fix a bug when swift backend is used in a multibackend configuration.
 * d4f4e305: Merged in lp:~xlucas/duplicity/swift-multibackend-bug - Fix a bug when swift backend is used in a multibackend configuration.
 * 290b3478: Copy.com is gone so remove copycombackend.py.
 * 8d681de8: Copy.com is gone so remove copycombackend.py.
 * 54120606: Fixed bug #1265765 with patches from Matthias Larisch and Edgar Soldin - SSH Paramiko backend now uses BufferedFile implementation to enable collecting the entire list of files on the backend.
 * f7821cee: Fixed bug #1265765 with patches from Matthias Larisch and Edgar Soldin - SSH Paramiko backend now uses BufferedFile implementation to enable collecting the entire list of files on the backend.
 * cd47dcb7: Support prefix affinity in multibackend.
 * 00b69529: Merge with trunk. All tests pass.
 * 097dadcb: Added capability to mount user workspace for testing local code.
 * 48594012: Added variable substitution to docker-compose.yml - .env file contains first 24 bits of subnet addr * Added teardown.sh as completion of setup.sh
 * 78e13007: Merged in lp:~aaron-whitehouse/duplicity/08-fix-man-verify - Fix description of --verify and --compare-data in the man page. Now clarifies that verify compares the restored files to hashes stored at backup date, while --compare-data compares restored files to files in target_path.
 * c0a9ca31: Fix bin/duplicity.1 entries for --verify and --compare-data
 * 22a77fcf: Merged in lp:~dernils/duplicity/docker-compose - Test Infrastructure now utilizing docker-compose
 * f4dd72ea: test infrastructure now using docker-compose
 * 80ce2994: Fix bug #1672540 with patch from Benoit Nadeau - Rename would fail to move par files when moving across filesystems. - Patch uses shutil.move() to do the rename instead.
 * 8d227266: Fix bug #1672540 with patch from Benoit Nadeau - Rename would fail to move par files when moving across filesystems. - Patch uses shutil.move() to do the rename instead.
 * 7baf638b: Some changes ported 0.7 to/from 0.8 to keep up-to-date.
 * 04dfffc3: Some changes ported 0.7 to/from 0.8 to keep up-to-date.
 * ed251965: Revisited bug #670891 with patch from Edgar Soldin - Forced librsync.PatchedFile() to extract file object from TemporaryFile() object when on Windows or Cygwin systems. This allows us to avoid the problem of tmpfile() use which creates temp files in the wrong place. - See discussion at https://bugs.launchpad.net/duplicity/+bug/670891
 * cfc35d04: Revisited bug #670891 with patch from Edgar Soldin - Forced librsync.PatchedFile() to extract file object from TemporaryFile() object when on Windows or Cygwin systems. This allows us to avoid the problem of tmpfile() use which creates temp files in the wrong place. - See discussion at https://bugs.launchpad.net/duplicity/+bug/670891
 * 9cc6b42c: Fix spurious warning message, return value not needed.
 * c91ec511: Merge with trunk.
 * 525c8390: Checkpoint - docker testbed mostly running - lots of format changes in setup.sh - made sure to kill off network and restart - simplified container naming and killall process - most tests run now with tox, 5 fail
 * 2cf407dd: Go back to original requirements file.
 * 8c255024: May have finally fixed bug #1556553, "Too many open files...". - Applied patch from Howard Kaye, question #631423. The fix is to dup the file descriptor, and then close the file in the deallocator routine in the glue code. Duping the file lets the C code and the Python code each close the file when they are done with it. - Invalidated and removed the fix put in for bug #1320832. - Caveat: long incremental chains will still eat up a large number of file descriptors. It's a very risky practice, so I'm not inclined to fix it.
 * eb4d9540: May have finally fixed bug #1556553, "Too many open files...". - Applied patch from Howard Kaye, question #631423. The fix is to dup the file descriptor, and then close the file in the deallocator routine in the glue code. Duping the file lets the C code and the Python code each close the file when they are done with it. - Invalidated and removed the fix put in for bug #1320832. - Caveat: long incremental chains will still eat up a large number of file descriptors. It's a very risky practice, so I'm not inclined to fix it.
 * 490a6508: Fix spelling and rearrange some.
 * b59b9a8a: Added lpbuild-trusty to replace lpbuild-precise pre Aaron Whitehouse's comment that there was a bug in pexpect < 3.4 that affects us.
 * cd4e9f18: Merged in lp:~dernils/duplicity/Dockerfile - Now have subnet name and IP of the subnet for testing as a variable.
 * 2b1e0b3c: minor changes to setup.sh
 * e2be29bd: minor fix to setup.sh
 * 3519dbd9: Merged in lp:~dernils/duplicity/Dockerfile - Added another backend to the docker test infrastructure, updated the setup for testing and updated the documentation.
 * e9534b26: Merged in lp:~xlucas/duplicity/swift-storage-policies - This brings support for Swift storage policies: when using a Swift backend, you can specify the policy containers should be operating on. - This is similar to AWS Cloud Storage classes (ia, rrs, glacier and so on).
 * cb8ebf11: added more test infrastructure
 * b6859a15: Merge in trunk.
 * b3701fb5: Support for Swift storage policies
 * 0df43bbd: Merged in lp:~aaron-whitehouse/duplicity/tox_pylint_fixes - Changes needed to run-tests without pylint E0401(import-error) errors
 * 59828f2e: Changes needed to run-tests without pylint E0401(import-error) errors
 * f87913fa: Merge in changes from trunk. * Tests all pass except pylint test (import-error that also happens for me on trunk, so will fix there).
 * 656efd1b: Remove unnecessary unicode conversion on commandline.py filelist append. * Tests all pass (and in previous commit).
 * 1fd9aed3: move stdin_test.sh to manual dir
 * d1613d61: remove run-tests-ve - not needed * move stdin_test.sh to manual dir
 * b9b70a29: Fix comments on ignored pylint messages.
 * f7bf6293: Remove precise-lpbuild test since precise is EOL.
 * f2584ad8: precise is EOL so drop testing for it.
 * c1ae120d: Use unicode version of pexpect.spawn for version >= 4.0, but bytes version below this.
 * b2851dec: Adjust control for LP build process, fasteners not lockfile.
 * 4598b3fd: Adjust control for LP build process, fasteners not lockfile.
 * e010d6e6: Fixed bug #1320641 and others regarding lockfile - swap from lockfile to fasteners module - use an fcntl() style lock for process lock of duplicity cache - lockfile will now clear if duplicity is killed or crashes
 * 74590df5: Fixed bug #1320641 and others regarding lockfile - swap from lockfile to fasteners module - use an fcntl() style lock for process lock of duplicity cache - lockfile will now clear if duplicity is killed or crashes
 * deeb4d8b: Fixed bug #1689632 with patch from Howard Kaye - On MacOS, the tempfile.TemporaryFile call erroneously raises an IOError exception saying that too many files are open. This causes restores to fail randomly, after thousands of files have been restored.
 * 2780015c: Fixed bug #1689632 with patch from Howard Kaye - On MacOS, the tempfile.TemporaryFile call erroneously raises an IOError exception saying that too many files are open. This causes restores to fail randomly, after thousands of files have been restored.
 * 1162114b: Fixed bug #1320832 with suggestion from Oskar Wycislak - Use chunks instead of reading it all in swiftbackend
 * b59345b4: Moved some things around in testing/infrastructure to clean up
 * 235459d2: Moved Dockerfile for duplicitytest into testinfrastructure/duplicity_test
 * 01277ec1: Merged in lp:~dernils/duplicity/DockerfileConvenience - Add a few files that are the beginning of further infrastructure based on docker. It contains a Dockerfile for a simple ftp server (used for backend testing) and a setup script that can be used to set up the complete test environment.
 * 723ad8d5: added furhter files for test infrastructure
 * f1d96196: Fixed bug #1320832 with suggestion from Oskar Wycislak - Use chunks instead of reading it all in swiftbackend
 * 7df9e8cc: Merge with trunk. All py27 tests pass, lpbuildd-precise still fails.
 * 07e360a8: Merged in lp:~dernils/duplicity/DockerfileConvenience - Added a few tools to the Dockerfile that make life easier
 * daeabff2: added ftp client to Dockerfile
 * e6880ff0: Updated Dockerfile
 * 594bcd7d: Make all tests pass on py27 tox environment. * lpbuildd-precise tests still fail because the outdated pexpect (2.4) has issues with unicode (pexpect.spawn does not support unicode and spawnu.readline fails).
 * e90318df: bzr does not honor perms so fix the perms at the start of the testing and avoid annoying error regarding testing/gnupg having too lenient perms
 * 3522c97d: Replace incoming non-ASCII chars in commandline.py
 * 3437fb8a: Merged in lp:~marix/duplicity/add-azure-arguments - Using the Azure backend to store large amounts of data we found that performance is sub-optimal. The changes on this branch add command line parameters to fine-tune some parameters of the Azure storage library, allowing to push write performance towards Azure above 1 Gb/s for large back-ups. If a user does not provide the parameters the defaults of the Azure storage library will continue to be used.
 * 5359b7c7: Merged in lp:~marix/duplicity/add-azure-arguments - Using the Azure backend to store large amounts of data we found that performance is sub-optimal. The changes on this branch add command line parameters to fine-tune some parameters of the Azure storage library, allowing to push write performance towards Azure above 1 Gb/s for large back-ups. If a user does not provide the parameters the defaults of the Azure storage library will continue to be used.
 * 6377e1ff: Merged in lp:~dawgfoto/duplicity/replicate - Add replicate command to replicate a backup (or backup sets older than a given time) to another backend, leveraging duplicity's backend and compression/encryption infrastructure. * Fixed some incoming PyLint and PEP-8 errors.
 * 6e943b06: unit/test_globmatch.py, unit/test_selection.py, functional/test_selection.py tests all pass. * Assume UTF-8 encoding for filelists (which also allows ASCII encoding). * Use new io module for selection filelist access. * Create new path.uc_name that is a unicode version of the path, which is then used throughout the selection code for path name matching etc. * Move selection.py to using unicode strings and uc_name versions of paths. * Made functional/__init__.py use unicode arguments to run duplicity for tests. * Use new io module in functional/test_selection.py. * Remove @unittest.expectedFailure from test_unicode_paths_square_brackets, which no longer fails. * Make unit/test_selection.py ParseTest support unicode and add test_unicode_paths_non_globbing unit test version of functional test.
 * 9af109cc: We need tzdata (timezone data).
 * 2098d906: Add command line arguments to fine-tune the Azure backend
 * 4129e373: You need tox to run tox. Doh!
 * 358d2c29: Add libffi-dev back. My bad.
 * 44965f96: Merged in lp:~dernils/duplicity/Dockerfile - separated requirements into requirements for duplicity (in requirements.txt) and for testing (in tox.ini)
 * af5bb630: fixed tox.ini
 * caff5d5d: separated pip requirements into duplicity and testing
 * bac60835: separated pip requirements into duplicity and testing
 * 53c92216: Remove dependencies we did not need
 * 5725ba76: Add test user and swap to non-priviledged.
 * b3605abf: Move branch duplicity up the food chain.
 * b4377a99: Simplify Dockerfile per https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ - Add a .dockerignore file - Uncomment some debug prints - quick fix for bug #1680682 and gnupg v1, add missing comma
 * 68f36e2a: Quick fix for bug #1680682 and gnupg v1, add missing comma.
 * 9f39f13b: Quick fix for bug #1680682 and gnupg v1, add missing comma.
 * 19f5affc: A little reorg, just keeping pip things together.
 * fa899ca3: More changes for testing: keep gpg1 version for future testing - some changes for debugging functional tests - add gpg-agent.conf with allow-loopback-pinentry
 * e8ea14f3: Merged in lp:~dernils/duplicity/Dockerfile Fixed variable name change in commandline.py
 * adf1d902: Edited Dockerfile
 * c2d8dda2: Whoops, deleted too much. Add rdiff again.
 * 5f54551e: Move pep8 and pylint to requirements.
 * 71e9fee7: Add rdiff install and newline at end of file.
 * 51d3ad00: delete tempfiles as soon as possible
 * 8626523e: Merged in lp:~dernils/duplicity/documentation - Minor changes to README-REPO, README-TESTING - Also redo the changes to requirements.txt and Dockerfile
 * aa03a5e1: Edited requirements.txt, minor changes to README-REPO and README-TESTING
 * 106658c4: Merged in lp:~dernils/duplicity/testing - Fixed minor stuff in requirements.txt. - Added a Dockerfile for testing. - Minor changes to README files. - Added README-TESTING with some information on testing.
 * cea007fd: Added README-TESTING, removed hmtlcov folder
 * b0505932: 2017-04-20 Kenneth Loafman <kenneth@loafman.com>
 * 2bd70213: edited requirements.txt
 * be375da8: Cleaned test cases
 * 2ea4dd69: Added Dockerfile
 * 0c2ac25d: updated requirements.txt
 * 69da35d0: updated requirements.txt
 * 3dd821ce: updated requirements.txt
 * 9c9f6e3e: Fixed bug #1684312 with suggestion from Wade Rossman - Use shutil.copyfile instead of os.system('cp ...') - Should reduce overhead of os.system() memory usage.
 * a2e8c122: Fixed bug #1680682 with patch supplied from Dave Allan - Only specify --pinentry-mode=loopback when --use-agent is not specified * Fixed man page that had 'cancel' instead of 'loopback' for pinentry mode
 * b0beb2ef: add replicate command - useful to replicate/archive backups to another backend - allows to partially replicate only older backup sets - checks existing backup sets on target to avoid redundant copies
 * b0c3643f: working on dpbx backend tests§
 * d26bf1e6: Add some commented-out debug print and move under error condition.
 * a7a1f16e: working on the READMEs
 * f8784203: worked on the requirements and README
 * baf1354e: Added some experiences to the README
 * 6ee9ac1d: Launchpad automatic translations update.
 * e6cfa3d0: Make test_selection.py use unicode string literals and still pass. * funtional/test_selection.py still fails.
 * 48e5c1d5: Make path.py only accept unicode. * Make all string literals in test_selection.py unicode. * Create path.uc_name as an alternative to path.name, allowing existing code to continue using bytes during transition. * Make file writes in test_selection.py use io.open. * Tests do not yet pass.
 * 0f1ed507: Make globmatch.py deal with either unicode or string globs. * Make path.uc_name for unicode name of path (vs path.name for bytes). * Functional select test failures.
 * 9a676187: test_globmatch.py now passing with unicode globs/paths * test_square_bracket_options_unicode now passing
 * 4c641be5: glob_to_regex converted to unicode, globmatch.py not yet passing tests
 * b3b8b66b: Merge in changes to trunk.
 * c6375adf: Added future imports to globmatch.py and added future to tox.ini deps.
 * 2189f8de: Added (failing) unicode test.
 * 49518c39: Add tests for square brackets.
 * d0ff26d4: Add test for unicode paths with asterisks in globs.
 * 9cf851c9: Added files with unicode names to testfiles and added TestUnicode.test_unicode_paths_non_globbing, which tests --include and --exclude works as expected with these files.
 * d9f7d0c7: Fixed bug #1668750 - Don't mask backend errors - added exception prints to module import errors
 * 47045bad: Fixed bug #1668750 - Don't mask backend errors - added exception prints to module import errors
 * e9613419: Fixed bug #1671852 - Code regression caused by revision 1108 - change util.uexc() back to bare uexc()
 * 454062de: Fixed bug #1671852 - Code regression caused by revision 1108 - change util.uexc() back to bare uexc()
 * 1220ed2f: Skip pylint on dpbxbackend.py for now.
 * d64ef21e: Refresh docs
 * 0fd50cb7: Merged in p:~aaron-whitehouse/duplicity/pep8_E402_fixes - Fixed PEP8 errors: E402 module level import not at top of file
 * c48ff6f4: Fixed PEP8 errors: E402 module level import not at top of file
 * 97fa82bd: Merged in lp:~benoit.bertholon/duplicity/duplicity - Use the globals.archive_dir variable to store only a string in the case of a path, uses globals.archive_dir_path
 * d3c2e106: uses the globals.archive_dir variable to store only a string in the case of a path, uses globals.archive_dir_path
 * 8c5d8e2f: Fixed bug #1367675 - IMAP Backend does not work with Yahoo server - added the split() as needed in 'nums=list[0].strip().split(" ")' - the other fixes mentioned in the bug report comments were already done
 * f10ff5df: Fixed bug #1367675 - IMAP Backend does not work with Yahoo server - added the split() as needed in 'nums=list[0].strip().split(" ")' - the other fixes mentioned in the bug report comments were already done
 * 08d7421f: Fixed variable name change in last merge which broke a bunch of tests - Changed archive_dir_root back to archive_dir
 * 9a72a06b: Merged in lp:~benoit.bertholon/duplicity/duplicity - Fixes bug #1666194 - ProcessCommandLine function called twice fail and arglist argument not used
 * 22fbd14d: Merged in lp:~aaron-whitehouse/duplicity/pep8_test_fixes - Fix PEP-8 testing by moving to using pycodestyle library. - Temporarily add ignores to allow these tests to pass. - Fix E305 PEP8 errors: expected 2 blank lines after class or function definition, found 1.
 * 4e65b733: Fix minor pep8 issue - line too long.
 * 9b423f99: Merged in lp:~marix/duplicity/azure-storage-sas - This branch adds support for Shared Access Signature to the Azure backend which allows to run Duplicity with a minimal set of permissions.
 * 8f291ae4: Merged in lp:~marix/duplicity/azure-storage-0.30.0-plus - This makes the Azure backend compatible with version 0.30.0 and up of the underlying azure-storage package.
 * 187bb611: Change the global name archive_dir to archive_dir_root add the arglist to the optparser
 * f0d3e5b6: Fix E305 PEP8 errors: expected 2 blank lines after class or function definition, found 1 * Remove E305 from pycodestyle ignores
 * c3e332db: Fix PEP-8 testing by moving to using pycodestyle library. * Temporarily add ignores to allow these tests to pass.
 * 442b45a5: Fix backup creation using azure-storage > 0.30.0
 * 08542cd4: Add support for Shared Access Signatures to the Azure backend.
 * 01c64aca: Make the Azure backend compatible with azure-storage 0.30.0 and up
 * 6612682c: Merged in lp:~aaron-whitehouse/duplicity/08-python-futurize-stage-1 - Made many of the safer changes for improved Python 3 support (python-future's futurize -stage1) without functional change to the code (and leaving the isinstance(s, types.StringType) tests unchanged). - Created Python 2/3 compatible tests for int and long. - Update setup.py to show only Python 2.7 support.
 * 7eba8beb: Update setup.py to show only Python 2.7 support.
 * 528dc103: Merge changes from trunk
 * 8cd38948: Some fixes to gpg.py to handle gpg1 & gpg2 & gpg2.1 commandline issues - --gpg-agent is optional on gpg1, but on gpg2 it is used automatically - --pinentry-mode is not a valid opt until gpg2.1, so condition on that
 * 1d04ea20: Fixed bug #1603704 with patch supplied by Maciej Bliziński - Crash with UnicodeEncodeError
 * 3022ffca: Fixed bug #1603704 with patch supplied by Maciej Bliziński - Crash with UnicodeEncodeError
 * 704b330c: Fixed the documentation of --use-agent in the man page
 * bd1f1ab1: merged revision 1270 from lp:duplicity/0.7-series
 * 2bc38e61: Fixed bug #1657916 with patch supplied by Daniel Harvey - B2 provider cannot handle two backups in the same bucket
 * 035c18b1: Fixed bug #1657916 with patch supplied by Daniel Harvey - B2 provider cannot handle two backups in the same bucket
 * ad6c9b9d: Merged in lp:~aaron-whitehouse/duplicity/08-refactor-unit-test-globmatch - Rename path_matches_glob_fn to select_fn_from_glob, as this more accurately reflects the return value. - Significantly refactored unit/test_globmatch.py to make this cleaner and clearer.
 * 6af41973: Add detail about import exceptions in onedrivebackend.py
 * 64f506a5: Add detail about import exceptions in onedrivebackend.py
 * 6564bdc4: Rename path_matches_glob_fn to select_fn_from_glob, as this more accurately reflects the return value. * Significantly refactored unit/test_globmatch.py to make this cleaner and clearer.
 * 993da29c: Merged in lp:~aaron-whitehouse/duplicity/08-merge-glob-parsers - Use a single code path for glob strings whether or not these contain special characters/wildcards (glob_get_normal_sf) and remove glob_get_filename_sf and glob_get_tuple_sf. - Remove run-tests-ve as this was identical to run-tests.
 * f880267c: Remove time from run-tests, in case this causes any issues (e.g. cross platform support).
 * ad13ff50: Add more scan tests.
 * 0b73f320: Removed unused non-globbing code (_glob_get_filename_sf and _glob_get_tuple_sf). * Made run-tests time test runs. * Removed run-tests-ve, which was identical to run-tests.
 * 0ccafc58: Move to using single (globing, glob_get_normal_sf) function for glob strings with and without globbing characters. No performance impact.
 * 056f1ff9: Make globs of "/" work with globbing code. * Make globs of "/" match everything.
 * 5710b947: Made _glob_get_filename_sf and _glob_get_tuple_sf internal functions to ensure no unit tests depend on them directly.
 * 789a193a: Merged in lp:~matthew-t-bentley/duplicity/duplicity - Sets a user agent. Backblaze asked for this in case there are errors that originate from the Duplicity B2 backend - Only retrieves a new upload URL when the current one expires, to bring it in line with their best practices for integrations: https://www.backblaze.com/b2/docs/integration_checklist.html
 * 77fa84ac: Merged in lp:~matthew-t-bentley/duplicity/duplicity - Sets a user agent. Backblaze asked for this in case there are errors that originate from the Duplicity B2 backend - Only retrieves a new upload URL when the current one expires, to bring it in line with their best practices for integrations: https://www.backblaze.com/b2/docs/integration_checklist.html
 * 7156ecd8: Only get a new upload URL when needed. Add a user agent
 * a1f9311a: Fixed bug #1658283 "Duplicity 0.7.11 broken with GnuPG 2.0" - Made gpg version check more robust than just major version - Now use --pinentry-mode=loopback on gpg 2.1 and greater - Removed check for non-Linux systems, a false problem
 * 98ee94b3: Fix pep8 issue.
 * 38ab4032: Fixed bug #1655268 "--gpg-binary option not working" - If gpg binary is specified rebuild gpg profile using new binary location
 * 510173fb: Fixed bug #1655268 "--gpg-binary option not working" - If gpg binary is specified rebuild gpg profile using new binary location
 * 2694f2c6: Futurize -stage1 all files, leaving the isinstance(s, types.StringType) tests unchanged. * Reverted earlier changes to types.StringType test in test files. * Created python 2/3 compatible tests for int and long.
 * 2f8617ea: Futurize -stage1 on py files in testing for improved python 2/3 support.
 * 184935f6: Merged in lp:~aaron-whitehouse/duplicity/0-8-merge_selection_tests - Merge in TestExcludeIfPresent from 0.7-series, which tests the behaviour of duplicity's --exclude-if-present option. - Move and rename TestTrailingSlash2 test (was duplicate name) as in 0.7-series. - Fix PEP error on adbackend.py. - Add jottalib as a tox dep to fix pylint error. - Remove unnecessary skipUnless Linux as per 0.7-series.
 * 122f1825: Fixed bug #1654220 with patch supplied by Kenneth Newwood - Duplicity fails on MacOS because GPG version parsing fails
 * 357f354a: Fixed bug #1654220 with patch supplied by Kenneth Newwood - Duplicity fails on MacOS because GPG version parsing fails
 * 7b55a7b1: Fixed bug #1623342 with patch supplied by Daniel Jakots - Failing test on OpenBSD because tar/gtar not found
 * 9d85aea3: Fixed bug #1623342 with patch supplied by Daniel Jakots - Failing test on OpenBSD because tar/gtar not found
 * 01d62f1c: Fix PEP error on adbackend.py. * Add jottalib as a tox dep to fix pylint error.
 * 952f2c28: Merge in TestExcludeIfPresent from 0.7-series, which tests the behaviour of duplicity's --exclude-if-present option
 * ed0a3595: Move and rename TestTrailingSlash2 test.
 * bcb66bdc: Merged in lp:~breunigs/duplicity/amazondrive3 - As reported on the mailinglist, if a space is entered while duplicity asks for the URL, it fails. Since all important spaces are URL encoded anyway, this should be fine even if there are spaces in the URL at all. I also patched it in the onedrive backend, because it must have similar issues.
 * a53b74cd: Merged in lp:~breunigs/duplicity/amazondrive3 - As reported on the mailinglist, if a space is entered while duplicity asks for the URL, it fails. Since all important spaces are URL encoded anyway, this should be fine even if there are spaces in the URL at all. I also patched it in the onedrive backend, because it must have similar issues.
 * 6a7d995d: Fix Bug #1642813 with patch from Ravi - If stat() returns None, don't attempt to set perms.
 * 1a73793e: Fix Bug #1642813 with patch from Ravi - If stat() returns None, don't attempt to set perms.
 * 43ec996b: Whoops, make a couple of changes to match series-7.
 * 3d805297: Whoops, fix bad patch * Add gpg2 dir to .bzrignore
 * b30ec5d7: Fix some issues with testing on MacOS * Fix problem with gpg2 in yakety and zesty
 * 6199e2d9: Fix problem with gpg2 in yakety and zesty
 * 5dd38216: Some fixes for MAC where gpg2 does not implement --pinentry-mode.
 * 026002f1: Skip locked folders tests if not on Linux platform.
 * dbabe01f: Merged in lp:~aaron-whitehouse/duplicity/Bug_1624725_files_within_folder_slash - Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters). This preserves the behaviour that an expression ending in "/" only matches a folder, but now the contents of any matching folder is included.
 * 81541c43: Merged in lp:~aaron-whitehouse/duplicity/Bug_1624725_files_within_folder_slash - Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters). This preserves the behaviour that an expression ending in "/" only matches a folder, but now the contents of any matching folder is included.
 * 2a533ded: Temp fix for tempfile.TemporaryFile failures.
 * 50892459: Fix encryption tests by specifying long key instead of short.
 * 3e710cae: Merged in lp:~horgh/duplicity/copy-symlink-targets-721599 - Add --copy-links to copy symlink contents, not just the link itself.
 * 49f3c2a8: Merged in lp:~horgh/duplicity/copy-symlink-targets-721599 - Add --copy-links to copy symlink contents, not just the link itself.
 * 4b889fd7: Improve description of new argument in man page
 * e8b0331b: Add new argument to duplicity manpage
 * a96db6f8: Add flag to copy target of symlinks rather than the link
 * fab20cc2: Merged in lp:~ed.so/duplicity/manpage.fixes - Fix html output via rman on the website
 * 2876ee53: Merged in lp:~ed.so/duplicity/manpage.fixes - Fix html output via rman on the website
 * 316bbc35: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 577b9acc: Revert to rev 1246.
 * 74d682d5: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 12753df3: Revert to rev 1246.
 * 1a8af10b: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 4b889f0c: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * a124b69a: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * bad3ea5e: Fix bug using 40-char sign keys, from Richard McGraw on mail list - Remove truncation of argument and adjust comments
 * 47b770bb: Fix bug using 40-char sign keys, from Richard McGraw on mail list - Remove truncation of argument and adjust comments
 * 82684b95: fix html output via rman
 * 37a32eb3: Merge in changes from trunk.
 * 9bd1ed0a: Added tests to ensure behaviour is as expected for expressions containing globs, as these traverse a different code path.
 * 578d6e4b: minor fix in manpage
 * a59f6da0: Added --backend-retry-delay to the manpage
 * 8d059743: Fixed bug #1642098 - does not create PAR2 archives when '--par2-options' is used - Missing space between par2-options plus default options
 * d5e6e80e: Fixed bug #1642098 - does not create PAR2 archives when '--par2-options' is used - Missing space between par2-options plus default options
 * 00c88278: added new command line option --backend-retry-delay
 * 33e38b45: added some robustness to dpbxbackend.py
 * 6bdf0471: Merged in lp:~breunigs/duplicity/amazondrive2 - Fixed variable renaming issue
 * e03be549: Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters)
 * 5060ccf0: fixed missing rename in Amazon Drive backend
 * 0bbda91e: Merged in lp:~breunigs/duplicity/amazondrive - Provide a native backend for AmazonDrive
 * 004fba71: Merged in lp:~havard/duplicity/jottacloudbackend - Adds support for a new backend, jottacloud.com, using the scheme `jottacloud:/<folder>`. - Reverse-engineered library, `jottalib`: http://github.com/havardgulldahl/jottalib - Here's how you set up jottalib https://github.com/havardgulldahl/jottalib/wiki
 * f0c62c2e: Fixed bug #1621194 with code from Tornhoof - Do backup to google drive working without a service account
 * 6315def0: Fixed bug #1621194 with code from Tornhoof - Do backup to google drive working without a service account
 * 538b5a98: rename to just "AD" to avoid any possible trademark issues
 * a43489fc: Merged in lp:~mwilck/duplicity/duplicity - GPG: enable truly non-interactive operation with gpg2 - This patch fixes the IMO unexpected behavior that, when using GnuPG2, a pass phrase dialog always pops up for saving backups. This is particularly annoying when trying to do unattended / fully automatic backups.
 * 9120a6ff: Merged in lp:~mwilck/duplicity/duplicity - GPG: enable truly non-interactive operation with gpg2 - This patch fixes the IMO unexpected behavior that, when using GnuPG2, a pass phrase dialog always pops up for saving backups. This is particularly annoying when trying to do unattended / fully automatic backups.
 * 2cd531ec: document peculiarities of AmazonDrive
 * 3eba5a9c: add and document native AmazonDrive backend
 * 4329060f: Added inline comment to globmatch.py explaining glob matching. * Removed trailing / from Path() unittests, as paths used in duplicity do not normally have these, even if they are folders. * Added unit test to show files within a matched folder are included without a trailing slash. * Fixed return value of test_slash_star_scans_folder unittest from include to scan.
 * ac458a25: Add unittests and code comments to explain glob processing/regex behaviour.
 * 5b4707da: GPG: enable truly non-interactive operation with gpg2
 * 0292f113: Add more tests for trailing slash behaviour.
 * 2ff9e842: Added (failing) test to show behaviour in Bug #1624725
 * 60c1a0a8: Fixed bug #1623342 with patch from Daniel Jakots - failing test on OpenBSD because tar/gtar not found
 * a83ce11a: Fixed bug #1623342 with patch from Daniel Jakots - failing test on OpenBSD because tar/gtar not found
 * 2fd70bf8: Merged in lp:~aaron-whitehouse/duplicity/bug_1620085_exclude-if-present-locked-folder - Fixes Bug #1620085: --exclude-if-present gives OSError looking for tag in locked folders
 * ac9acb35: remove uses_netloc directive
 * c92c3319: JottaCloudBackend: Don't return bytestrings in _list()
 * dac1bba8: Adding JottaCloud backend
 * 28cad7a9: Fixed bug #1620085: OSError when using --exclude-if-present with a locked directory in backup path. * Added tests for errors on locked files.
 * d5e8606d: Add functional tests for --exclude-if-present.
 * c67d2b43: Move and rename second TestTrailingSlash block to TestTrailingSlash2.
 * 93701ebe: Add requirements.txt - Remove module mocks in conf.py
 * e804d223: OK, finally grokked how to mock out _librsync, but it did mean having to change librsync.py with a conditional. Would have preferred a cleaner solution. - Fixed the remaining warnings in READTHEDOCS build, including the removal of a couple of files that were extraneous.
 * 2c0f3a2d: Try autodoc_mock_imports...
 * 53356134: Try autodoc_mock_imports...
 * b94fc651: Try autodoc_mock_imports...
 * 7b03ee0d: Try fully qualified module name, again.
 * 3832583b: Remove fully qualified name.
 * 8a598759: Resolve recursion in Mock.
 * b3986e26: Try fully qualified and not qualified module names.
 * f43f7fe2: Try without _librsync.
 * daf82414: Try fully qualified module name.
 * a6d3025b: Try with virtualenv.
 * c69c6d91: Try again...
 * 82b6825a: Mock sucks, big time!
 * e62798a4: Mock sucks, big time!
 * 9cea066b: Mock sucks!
 * 5a186b87: Try MagicMock.
 * 97292f0f: Try MagicMock.
 * 98664f91: Fix build on RTD.
 * e40e8468: Fix build on RTD.
 * 397eea8b: Fix build on RTD.
 * 5b8c3623: Fix build on RTD.
 * 309d763e: Fix build on RTD.
 * 34127775: Remove _build dir from git. Fix some names, authors.
 * 66a4fe37: Merged in lp:~mstoll-de/duplicity/duplicity - Backblaze announced a new domain for the b2 api
 * 326711dc: Merged in lp:~mstoll-de/duplicity/duplicity - Backblaze announced a new domain for the b2 api
 * db5655e4: Fixed bugs #815510 and #1615480 - Changed default --volsize to 200MB
 * fd1af0e6: Fixed bugs #815510 and #1615480 - Changed default --volsize to 200MB
 * a336add4: First pass at some Sphinx docs for moving to readthedocs.org
 * f691e1a1: Merged in lp:~fenisilius/duplicity/acd_init_mkdir - Allow duplicity to create remote folder
 * 82a45497: Merged in lp:~fenisilius/duplicity/acd_init_mkdir - Allow duplicity to create remote folder
 * e079f6a5: Fixed bug #1612472 with patch from David Cuthbert - Restore from S3 fails with --with-prefix-archive if prefix includes '/' * Merged in lp:~arashad.ahamad/duplicity/duplicity_latest - Changes for connecting to IBM Bluemix ObjectStorage. See man page.
 * 93daedee: Merged in lp:~arashad.ahamad/duplicity/duplicity_latest - Changes for connecting to IBM Bluemix ObjectStorage. See man page.
 * e936ed38: Fixed bug #1612472 with patch from David Cuthbert - Restore from S3 fails with --with-prefix-archive if prefix includes '/'
 * bc492c89: Added documentation for connecting to IBM Bluemix ObjectStorage
 * 9da8af5d: Added support to connect IBM Bluemix ObjectStorage
 * 905918d8: Restore testing/gnupg/gpg.conf and testing/gnupg/README.
 * 90525e9e: Whoops, committed too much!
 * 6913b458: Fixed conflict in merge from Martin Wilck and applied - https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301492 - merge fixes setsid usage in functional testing.
 * a80d0e45: Fixed conflict in merge from Martin Wilck and applied - https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301492 - merge fixes setsid usage in functional testing.
 * e85bf350: Remove -w from setsid in functional tests.
 * c39c171e: Merged in lp:~mwilck/duplicity/duplicity - Speedup of path_matches_glob() by about 8x. See https://code.launchpad.net/~mwilck/duplicity/duplicity/+merge/301268 for more details.
 * 96d3bcef: Merged in lp:~mwilck/duplicity/0.7-series - Speedup of path_matches_glob() by about 8x. See https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301332 for more details.
 * c25b225d: Fix unit test failures for {Old,Short}FilenamesFinalTest
 * d7e1490b: Fix failures of unit tests with --hidden-encrypt-key
 * 8d70d8ac: selection.py: use closure for matching paths with glob expressions
 * 68a027cb: selection.py: glob_get_normal_sf: use closure path_matches_glob_fn
 * 35eaca4a: globmatch: path_matches_glob_fn: return closure for path match
 * b1ec1931: Merged in lp:~aaron-whitehouse/duplicity/07-fix_deja_dup_error_on_locked_files - Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (e.g. deja dup; Bug #1605939).
 * 17720b42: Merged in lp:~aaron-whitehouse/duplicity/07-fix_deja_dup_error_on_locked_files - Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (e.g. deja dup; Bug #1605939).
 * c3f7b9e5: Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (deja dup).
 * 9b00b6bb: Fixed bug #1600692 with patch from Wolfgang Rohdewald - Allow symlink to have optional trailing slash during verify.
 * 1d62b316: Fixed bug #1600692 with patch from Wolfgang Rohdewald - Allow symlink to have optional trailing slash during verify.
 * b472fc99: Merged in lp:~aaron-whitehouse/duplicity/remove-python26 - Remove Python 2.6 support references and tests.
 * 11ed8050: Fix date in CHANGELOG. Release date was 2016-07-02, not 01.
 * 7b24b4ab: Fix date in CHANGELOG. Release date was 2016-07-02, not 01.
 * b9fe9cb6: Remove import of unittest2 for Python <2.7, now that Python 2.7 is the minimum version.
 * fcdda3b6: Remove Python 2.6 settings from tox.ini
 * 84c6896d: Merge with trunk.
 * 6f9ff93f: Changes from 0.7.08
 * 0f983576: Merged in lp:~aaron-whitehouse/duplicity/PEP8_W503_fixes - Fix PEP8 W503 errors (line break before binary operator) and enable the PEP8 test for this in test_code.CodeTest. * Merged in lp:~aaron-whitehouse/duplicity/PEP8_line_length - Set line length error length to 120 (matching tox.ini) for PEP8 and fixed E501(line too long) errors. * Merged in lp:~duplicity-team/duplicity/po-updates
 * c0228e28: Properly remove line too long errors (E501) from PEP8 ignores.
 * 93c40c87: Fixed lines longer than 120 chars.
 * 37bca7ab: Set line length error length to 120 (matching tox.ini) and fixed PEP8 E501(line too long) errors.
 * a7c644b1: Fix PEP8 W503, line break before binary operator.
 * f65381b2: Remove Python 2.6 support from the test suite and references to it from README and README-REPO.
 * d832ee6b: Merge 0.7-series changes to README-REPO.
 * eefccc4a: Merge 0.7 series changes to README
 * 65be0081: Merge 0.7 series changes to tox.ini
 * b6534962: Fixed bug #1594780 with patches from B. Reitsma - Use re.finditer() to speed processing
 * 4e363902: Merged in lp:~aaron-whitehouse/duplicity/fix_stat_errors - Only give an error about not being able to access possibly locked file if that file is supposed to be included or scanned (i.e. not excluded). Fixes Bug #1089131
 * acccc48d: Fixed README-REPO to no longer mention 0.6-series
 * db457c11: Only give an error about not being able to access possibly locked file if that file is supposed to be included or scanned (i.e. not excluded).
 * 8ce8d24e: Fixed bug #822697 ssh-options not passed in rsync over ssh - Added globals.ssh_options to rsync command line * Increased default volume size to 200M, was 25M
 * 54696c83: Merged in lp:~aaron-whitehouse/duplicity/fix_pep8 - Fix PEP8 error in onedrivebackend.py (space before bracket)
 * 60957c05: Fix PEP8 error in onedrivebackend.py (space before bracket).
 * 18f32bae: Fix pep8 issues from last two patch sets.
 * 6e2d9adb: Merged in lp:~mstoll-de/duplicity/b2-reauth - Fixes bug #1588503 b2: large uploads fail due to expired auth token
 * 7f1dfc84: Fixed bug #1589038 with patches from Malte Schröder - Added ignore_case option to selection functions
 * fd6d4021: b2 reauth: use other log level
 * dce5d95b: Handle expired auth token
 * 8af78267: Fixed bug #1586992 with patches from Dmitry Nezhevenko - Patch adds _delete_list to Par2Backend. And _delete_list fallbacks to _delete calls if wrapped backend has no _delete_list.
 * 11acea79: Fixed bug #1586934 with patches from Dmitry Nezhevenko - fixes error handling in wrapper
 * 0ef87160: Fixed bug #1573957 with patches from Dmitry Nezhevenko - upload last chunk with files_upload_session_finish to avoid extra request - upload small files using non-chunked api
 * 19a0d4ed: Merged in lp:~ghoz/duplicity/swift-prefix - adds the abiliy to use path in the swift backend, in order to have multiple backups to the same container neatly organized.
 * 5557f82f: Adds prefix support to swift backend
 * ecd3b406: Merged in lp:~noizyland/duplicity/fix_azurebackend_typo - Fix typo in error handling code
 * 8bc62f85: Fix typo in error handling code.
 * 680383ca: Add missing build-dep apparently now not installed by default with python2 in xenial+
 * a245be3d: Fixed bug #1570293 - removed flush() after write. - revert to previous version
 * d3e45a2e: Fixed bug #1571134 and #1558155 - used patch from https://bugs.debian.org/820725 but made changes to allow the user to continue using the old version
 * 9a4ec02d: Remove unused (default) argument.
 * f09975d6: Fixed bug #1569523 - bug introduced in improper fix of bug #1568677 - gotta love those inconsistent APIs
 * 3cb28a95: Blasted JIT imports got me again!
 * 74acd2bb: Fixed bug #1568677 - bug introduced by incomplete fix of bug 1296793 - simplified setting of bucket locations
 * cbde060a: Fixed bug 1568677 with suggestions from Florian Kruse - bug introduced by incomplete fix of bug 1296793
 * 725d6571: Merged in lp:~duplicity-team/duplicity/po-updates
 * df4ad4e0: Launchpad automatic translations update.
 * 2263ee98: Fix bug reported on the mailing list from Mark Grandi (assertion error while backing up). In file_naming.parse() the filename was being lower cased prior to parsing. If you had used a prefix with mixed case, we were writing the file properly, but could not find it in the backend.
 * ebe7340c: Merged in lp:~aaron-whitehouse/duplicity/split_glob_matching_from_select - Move glob matching code out of selection.py's Select function and into globmatch.py.
 * e8e8bd7b: Re-added import of re, as re.compile still used in selection.py.
 * af0b1a1f: Move complexity of matching paths to globs into globmatch.py path_matches_glob, rather than in selection.py Select.
 * d1bbf7e6: Merged in lp:~aaron-whitehouse/duplicity/improve_present_get_sf_man_page - Improve man page entry for --exclude-if-present
 * 3cf53b10: Move ignorecase handling out of re.compile to use .lower() instead.
 * b3a6e6a8: Remove glob_get_prefix_res from selection.py, now that it has moved to globmatch.py.
 * 86c9b85f: Move content of glob_get_prefix_res to globmatch.py glob_get_prefix_regexs.
 * a3c9b9cc: Improve man page entry for --exclude-if-present
 * 183bfa7f: Fixed globmatch tests. Tests pass.
 * 833ec732: Resync with trunk.
 * b61f6bbc: Move glob_to_re to globmatch.py. Moved associated tests into test_globmatch.py.
 * aa674cf5: Applied patch from Dmitry Nezhevenko to upgrade dropbox backend: update to SDK v2 - use chunked upload
 * 2c6cfbae: More fixes to dist/makedist to make it more OS agnostic. * Merged in lp:~ed.so/duplicity/webdav.lftp.ssl-overhaul duplicity.1, commandline.py, globals.py - added --ssl-cacert-path parameter backend.py - make sure url path component is properly url decoded, in case it contains special chars (eg. @ or space) lftpbackend.py - quote _all_ cmd line params - added missing lftp+ftpes protocol - fix empty list result when chdir failed silently - added ssl_cacert_path support webdavbackend.py - add ssl default context support for python 2.7.9+ (using system certs eg. in /etc/ssl/certs) - added ssl_cacert_path support for python 2.7.9+ - gettext wrapped all log messages - minor refinements
 * 0f52e522: path may be unset
 * b9466340: duplicity.1, commandline.py, globals.py - added --ssl-cacert-path parameter backend.py - make sure url path component is properly url decoded, in case it contains special chars (eg. @ or space) lftpbackend.py - quote _all_ cmd line params - added missing lftp+ftpes protocol - fix empty list result when chdir failed silently - added ssl_cacert_path support webdavbackend.py - add ssl default context support for python 2.7.9+ (using system certs eg. in /etc/ssl/certs) - added ssl_cacert_path support for python 2.7.9+ - gettext wrapped all log messages - minor refinements
 * 96e5cc95: Reverted changes made in rev 1164 w.r.t. getting the source from VCS rather than local directory. Fixes bug #1548080.
 * 4ac187e0: Move the logic of the glob_to_re method into the glob_to_regex function in globmatch.py.
 * aecc571d: Launchpad automatic translations update.
 * 9db90f91: Merged in lp:~rye/duplicity/mediafire - Backend for https://www.mediafire.com - Requires https://pypi.python.org/pypi/mediafire/ installed.
 * 78dc8b12: Backed out changes made by patching for bug #1541314. These patches should not have been applied to the 0.7 series.
 * cbf1dabc: Added acdclibackend.py from Stefan Breunig and Malay Shah - renamed from amazoncloudbackend to stress use of acd_cli * Fixed some 2to3 and Pep8 issues that had crept in
 * 9d06b1a4: Merged in lp:~harningt/duplicity/multibackend-mirror - This changeset addresses multibackend handling to permit a mirroring option in addition to its "stripe" mode to make it a redundancy tool vs space-expansion tool. To do this without changing the configuration too much, I used the query string that would generally go unused for files to specify behavior that applies to all items inside the configuration file.
 * 99285559: Fixed bug 1474994 Multi backend should offer mirror option - added query parameter option to multi-backend - added mode parameter to alter how the backend list is operated on (mirror/stripe) - added onfail parameter to alter how backend failure is handled - updated man-page with documentation
 * 7731ded6: Checkpoint, merge latest.
 * ea04f388: Use built-in username/password support in backends.py.
 * ede2fbd9: Remove custom logging, add usage info.
 * 46db9ccd: Merge changes from trunk.
 * 2c755731: Fixed a patching error in ssh_pexpect_backend.py * Merged in lp:~fpytloun/duplicity/webdav-gssapi-fix - Make kerberos optional for webdav backend
 * c24e6cac: Make kerberos optional for webdav backend
 * bf1c2907: Launchpad automatic translations update.
 * 9f890500: Applied patch from kay-diam to fix error handling in ssh pexpect, fixes bug #1541314
 * 2ffa1ebc: Fix bug #1540279 - mistake in --help
 * 6dcbcdb6: Clean up pep8 issues.
 * 3d402f45: Launchpad automatic translations update.
 * fa84e9a6: Fix for bug #1538333 - assert filecount == len(self.files_changed) - added flush after every write for all FileobjHooked files which should prevent some errors when duplicity is forcibly closed.
 * 68931583: Add more pylint ignore warnings tags * Adjust so test_restart.py can run on Mac as well
 * 6ab6e2b0: Merged in lp:~fpytloun/duplicity/webdav-gssapi - support GSSAPI authentication in webdav backend
 * 64fca867: Support GSSAPI authentication in webdav backend
 * 3ae39b68: Launchpad automatic translations update.
 * 7103d66c: Checkpoint,merge in current changes.
 * 4c7dfb08: Fix submitter name in changelogs. - Change comment to be correct.
 * 5f45e963: Fixed bug #1492301 with patch from askretov (manually refresh oauth).
 * d44338fa: Fixed bug #1379575 with patch from Tim Ruffling (shorten webdav response).
 * 10a51c43: Fixed bug #1375019 with patch from Eric Bavier (home to tmp).
 * 72b42e9f: Fixed bug #1369243 by adjusting messages to be more readable.
 * 1c0686fc: Fixed bug #1260666 universally by splitting the filelist for delete before passing to backend.
 * ac0c7b4e: Pep8 corrections for recently released code.
 * 3d086b81: Merged in lp:~mifchip/duplicity/duplicity - fix bug #1313964, absolute path doesn't work for FTP
 * a873fe5e: Bug #1313964 fix. lstrip('/') removed all the slashes, it was an issue.
 * 593735de: Fixed bug #1296793 - Failed to create bucket - use S3Connection.lookup() to check bucket exists - skips Boto's Exception processing for this check - dupe of bug #1507109 and bug #1537185
 * 736b56b7: Checkpoint,merge in current changes.
 * 337fba33: Create folder recursively
 * fcc102d7: Use upload session context manager
 * a81cf0ab: Applied changes from ralle-ubuntu to fix bug 1072130. - duplicity does not support ftpes://
 * d15299f9: Allow importing module, but fail on init
 * c884f4b8: MediaFire Backend - initial version
 * a22c4673: Undo changes to test_restart.py. GNU tar is needed. * Fix minor pep8 nit in collections.py
 * 1113f5e7: Applied patch from abeverly to fix bug #1475890 - allow port to be specified along with hostname on S3 - adjusted help text and man page to reflect the change
 * 569d08d5: Launchpad automatic translations update.
 * 428a07ca: Applied patch from shaochun to fix bug #1531154, - --file-changed failed when file contains spaces
 * 56f43e60: Fix stupid issue with functional test path for duplicity
 * e10686b9: Make test_restart compatible with both GNUtar and BSDtar
 * 0ad884c5: Partial fix for bug #1529606 - shell code injection in lftpbackend - still need to fix the other backends that spawn shell commands
 * 1376f352: Random stuff: supply correct path for pydevd under Mac - fix some tests to run under Mac as well
 * db6a875c: Checkpoint: remove RPM stuff from makedist - have makedist pull directly from VCS, not local dir - update po translation directory and build process - clean up some odd error messages - move Pep8 ignores to tox.ini
 * d61e2677: Checkpoint: remove RPM stuff from makedist - have makedist pull directly from VCS, not local dir - update po translation directory and build process - clean up some odd error messages - move Pep8 ignores to tox.ini
 * d4134176: 2to3 cleanup.
 * ed7ada43: Pep8 cleanup.
 * f75c9183: Fix date.
 * d0ec4cbb: Merged in lp:~matthew-t-bentley/duplicity/b2 - A couple fixes allowing multiple backups to be hosted in different folders in the same bucket as well as some logging for -v9.
 * 6dac2d84: Make sure listed files are exactly in the requested path Thanks to Andreas Knab <knabar@gmail.com> for the pull request
 * 722109ee: Set fake (otherwise unused) hostname for prettier password prompt Thanks to Andreas Knab <knabar@gmail.com> for the patch
 * 37066626: Add debugging for b2backend
 * f0f70edf: Merged in lp:~matthew-t-bentley/duplicity/b2 - Allow multiple backups in the same bucket. - Fixes #1523498.
 * 2b48a03c: Allow multiple backups in the same bucket
 * 4d962564: Merged in lp:~matthew-t-bentley/duplicity/b2 - Fix import and error typos.
 * 6626f37d: Merge and re-add missing error
 * 53a2339f: Fix missing import and typos
 * b131bfb9: Merge from upstream
 * 97b583cb: Merged in lp:~matthew-t-bentley/duplicity/b2 - Adds a backed for BackBlaze's (currently beta) B2 backup service. - This adds backends/b2backend.py, modifies log.py to add an error code and modifies commandline.py to add the b2:// example to the help text. * Fix perms on duplicity/backends/multibackend.py
 * ca29adf5: Undo changes to po files
 * 3ded609c: Remove unnecessary requirements section in manpage
 * bf2d980f: Merged in lp:~noizyland/duplicity/azurebackend-fixes - Support new version of Azure Storage SDK - Refactor _list method to support containers with >5000 blobs
 * 6404c837: Documentation
 * 4ff5881f: Merge from master
 * 28db5aa8: Add help text for b2
 * 3210ff56: Add basic error handling
 * 0c1d5afa: Support new version of Azure Storage SDK * Refactor _list method to support containers with >5000 blobs
 * 3bb85b70: Make sure which() returns absolute pathname.
 * dc70e733: Remove some print statements.
 * 4942b944: Fix bug #1520691 - Shell Code Injection in hsi backend - Replace use of os.popen3() with subprocess equivalent. - Added code to expand relative program path to full path. - Fix hisbackend where it expected a list not a string.
 * f446cd39: Add BackBlaze B2 backend. Still needs some work (error handling, etc)
 * 917bf22b: Fix missing self.
 * f5deaecb: Fix bug #1520691 - Shell Code Injection in hsi backend - Replace use of os.popen3() with subprocess equivalent.
 * d2891195: Merged in lp:~feraudet/duplicity/fix - Fix missing SWIFT_ENDPOINT_TYPE env var, bug 1519694.
 * ab0a5520: Fix #1519694
 * 66365ff4: Merged in lp:~michal-s/duplicity/duplicity - Fix azurebackend storage class import
 * 9d6316cf: debugged storage class import
 * 5263c933: Fixed bug #1511308 - Cannot restore no-encryption, no-compression backup - Corrected code to include plain file in write_multivolume() - Added PlainWriteFile() to gpg.py
 * ae5f2adf: Merged in lp:~ed.so/duplicity/tempfile.tempdir - make sure packages using python's tempfile create temp files in duplicity's temp dir
 * 0a61503a: make sure packages using python's tempfile create temp files in duplicity's temp dir
 * 9fd02664: Reversed previous changes to lockfile. Now it will take any version extant in the LP build repository. (PyPi is not avail in LP build).
 * dafcfc91: Reversed previous changes to lockfile. Now it will take any version extant in the LP build repository. (PyPi is not avail in LP build).
 * 82f2fadb: Try adding spaces.
 * c64ed6eb: Try lockfile>=0.11.0 (use full version number).
 * ef1204fe: Revert last change.
 * 980a9992: Try lockfile==0.11.0 instead of lockfile>=0.9
 * 998f0466: Merged in lp:~michal-s/duplicity/duplicity - WindowsAzureMissingResourceError and WindowsAzureConflictError changed due to SDK changes.
 * 7d1931fa: WindowsAzureMissingResourceError and WindowsAzureConflictError classes changed due to SDK changes
 * 5d0e5382: Cleanup issues around Launchpad build, mainly lockfile >= 0.9.
 * 1a399846: Merged in lp:~ed.so/duplicity/setup.shebang - Having the python interpreter searched in the PATH is much more flexible than the /usr/bin/python inserted into our scripts shebang by setuptools. This patch prevents that. don't touch my shebang! :)
 * f05b98bb: Modded tox.ini to use the latest lockfile.
 * 73b9c33a: also check python version number upper bound. we run on 2.6 and 2.7 currently
 * a1c9dc9d: Applied patch from Alexander Zangerl to update to changes in lockfile API 0.9 and later. Updated README to notify users.
 * 67d594cb: don't touch my shebang
 * 3e852241: Add __pycache__.
 * 9bf06ca4: Upgrade to newest version of pep8 and pylint. Add three ignores to test_pep8 and one to test_pylint to get the rest to pass. They are all valid in our case.
 * 3c821820: Fix header date.
 * 77904e32: The ptyprocess module no longer supports Python 2.6, so fix tox.ini to use an older version. Make explicit environs for all tests.
 * 8fd42175: Merged in lp:~mnjul/duplicity/s3-infreq-access - This adds support for AWS S3's newly announced Infrequent Access storage class and is intended to implement Blueprint: https://blueprints.launchpad.net/duplicity/+spec/aws-s3-std-ia-class . - A new command line option, --s3-use-ia, is added, and boto backend will automatically use the correct storage class value depending on whether --s3-use-rrs and --s3-use-ia is set. Command line parser will prompt error if both --s3-use-ia and --s3-use-rrs are used together, as they conflict with each other. - The manpage has been updated giving a short explanation on the new option. Its wording derives from Amazon's official announcement: https://aws.amazon.com/about-aws/whats-new/2015/09/announcing-new-\ amazon-s3-storage-class-and-lower-glacier-prices/
 * 027941c7: Add support for AWS S3 Standard - Infrequent Access storage class
 * 3da379e9: Merge changes from trunk.
 * 8d31748d: Merged in lp:~bmerry/duplicity/pydrive-id-cache - This fixes the issue a number of users (including myself) have been having with duplicity creating files with duplicate filenames on Google Drive. It keeps a runtime cache of filename to object ID mappings, so that once it has uploaded an object it won't be fooled by weakly consistent directory listings.
 * da48bd05: Fix up broken merge
 * 9349f45d: Merge in master
 * bf391089: Add more logging info
 * 8db85af9: Fix bug #1494228 CygWin: TypeError: basis_file must be a (true) file - The problem that caused the change to tempfile.TemporaryFile was due to the fact that os.tmpfile always creates its file in the system temp directory, not in the directory specified. The fix applied was to use os.tmpfile in cygwin/windows and tempfile.TemporaryFile in all the rest. This means that cygwin is now broken with respect to temp file placement of this one file (deleted automatically on close).
 * fd3456f7: Fix bug #1493573. Correct option typo in man page.
 * e6162f4e: Updated man pages to reflect more contributors.
 * 875a9a29: Sync with v0.7.
 * 48e9b68b: Merged in lp:~germar/duplicity/par2removefix - After reorganisation in revision 981 and the fix for bug #1406173 the par2backend does not remove .par2 files anymore when removing duplicity-*.gpg files. - This banch adds an unfiltered_list() method which is used in delete() and delete_list()
 * ada5f5c9: par2 backend remove par2 files
 * 81d38e17: Merged in lp:~w.baranowski/duplicity/selection_debug - This little patch logs debug messages concerning path selection process, and so allows users to debug their include/exclude configuration.
 * 6f7f14a9: Added debug msgs to the routine checking path selection
 * cf14d3d6: Refactored the selection.Select.Select method; fewer exit points now
 * 642c2c8c: Fixed Bug 1438170 duplicity crashes on resume when using gpg-agent with patch from Artur Bodera (abodera). Applied the same patch to incremental resumes as well.
 * 2ee3fec8: Launchpad automatic translations update.
 * 07655506: Merged in lp:~aaron-whitehouse/duplicity/disable_code_tests_for_lpbuildd - Set RUN_CODE_TESTS to 0 for lpbuildd tox profile, reflecting its value on the Launchpad build server (and therefore skipping PEP8, 2to3 and pylint). More accurately reflects the system we are mimicking and saves approximately 1 minute per test run.
 * ca314f1e: Rename tox profile for Launchpad's Precise build server to "lpbuildd-precise" for clarity (and to make it clear it should be removed once Precise is no longer supported).
 * 47dd2d23: Set RUN_CODE_TESTS to 0 for lpbuildd tox profile, reflecting its value on the Launchpad build server (and therefore skipping PEP8, 2to3 and pylint). More accurately reflects the system we are mimicking and saves approximately 1 minute per test run.
 * 1dc5f82f: Merged in lp:~aaron-whitehouse/duplicity/launchpad_tox_profile - Add tox testing profile that mimics the packages installed on the Launchpad build server, to reduce the likelihood of tests passing our test suite, but failing on the build server (e.g. because of the out-of-date mock version).
 * fb8eae7b: Fixed Bug 1476019 S3 storage bucket not being automatically created with patch from abeverley
 * 261ba3b5: Fixed Bug 1476019 S3 storage bucket not being automatically created with patch from abeverley
 * d26793e7: Add further instructions in README-REPO on how to test against one environment.
 * b7d323ec: Add lpbuilldd as an additional tox profile, replicating the setup of the launchpad build server.
 * 59a9032a: Merged in lp:~aaron-whitehouse/duplicity/fix_patch_error - Change use of mock.patch in unit tests to accommodate the obsolete version of python-mock on the build server.
 * 15aac370: Change use of mock.patch to accommodate the obsolete version of python-mock on the build server (and avoid the following error: TypeError: patch() got an unexpected keyword argument 'return_value' )
 * d4931324: Merged in lp:~aaron-whitehouse/duplicity/fix_2to3_issues - Fixed 2to3 issues. Updated README-REPO with more test information. Updated pylint and test_diff2 descriptions to make it clear these require packages to be installed on the sytem to pass. All tests pass on Python 2.6 and Python 2.7 as at this revision.
 * 4f7b7985: Merged in lp:~dag-stenstad/duplicity/swift_authversion_3_support - Added support for Openstack Identity v3 in the Swift backend.
 * 0dbbd223: Fixed 2to3 issues. Updated README-REPO with more test information. Updated pylint and test_diff2 descriptions to make it clear these require packages to be installed on the system to pass. All tests pass on Python 2.6 and Python 2.7 as at this revision.
 * 75efd658: Added support for Identity v3.
 * bd359a3c: Merged in lp:~aaron-whitehouse/duplicity/improve_tox_and_python2-6_testing - Testing improvements, particularly in relation to testing against Python version 2.6: tox.ini fixed so that it is possible to run individual tests against both Python 2.6 and 2.7; * updated test_code.py to use unittest2 for Python versions < 2.7 (instead of failing); * ./run-tests now correctly runs all tests against both Python 2.6 and 2.7; and * improved testing directions in README-REPO.
 * ed9a2d94: Merged back to trunk.
 * f1895791: Delete redundant second sys import in test_code.py.
 * f756b041: Fixed tox.ini to correctly run individual tests. Updated test_code.py to use unittest2 for Python versions < 2.7 (instead of failing). Improved testing directions in README-REPO.
 * 91471a01: Merged in lp:~aaron-whitehouse/duplicity/trailing_slash_match_dirs - Made globs with trailing slashes only match directories, not files, fixing Bug #1479545.
 * a2169f9d: Made globs with trailing slashes only match directories, not files, fixing Bug #1479545.
 * 31441334: Added functional unittests to exhibit current behaviour of trailing slashes in globs. See Bug #1479545.
 * 141361c0: Merged in lp:~aaron-whitehouse/duplicity/reenable_tests - Re-enable unit.test_selection tests that had been temporarily commented out.
 * 4c49785c: Re-enable tests that had been temporarily commented out.
 * 6003f4a8: Merged in lp:~aaron-whitehouse/duplicity/bug_884371 - Fixed Bug #884371 - Stopped an exclude glob trumping an earlier scan glob, but also ensured that an exclude glob is not trumped by a later include. This fix is important, as without it files that are specified to be included are not being backed up as expected. - Fixed Bug #932482 - a trailing slash at the end of globs no longer prevents them working as expected.
 * e73e5e5b: Add test_glob_re unit test back in.
 * dbedeb41: Remove unnecessary use of mock.patch in unit.test_selection.py.
 * 0ddd13bb: Remove special casing for final glob in glob list as no longer necessary.
 * 8cd88d39: Fixed Bug #932482 by checking for a trailing slash in each glob and removing it if present. Enabled tests checking this behaviour. PEP8 fixes along the way.
 * e292c843: Stopped an exclude glob trumping an earlier scan glob, but also ensured that an exclude glob is not trumped by a later include. Fixed Bug #884371. Activated the (expectedFailure) tests that were failing because of this bug.
 * 992906bb: Additional tests to exhibit current exclude/scan interaction and implement two functional tests as unit tests.
 * b1f42932: Added unit tests for negative square brackets ([!a,b,c] and [!1-4]).
 * 18caccd1: Added test cases (unit and functional) to test the current behaviour of selection.py.
 * 5d0b1231: Fixed bug 1471348 Multi back-end doesn't work with hubiC (again) - hubiC should reach up to duplicity.backend.__init__
 * 772d03a7: Fixed bug 1471348 Multi back-end doesn't work with hubiC - added init of appropriate superclass in both cases.
 * d2c3d755: Merged in lp:~aaron-whitehouse/duplicity/reactivate_progress_test - Re-enable the test of the --progress option (test_exclude_filelist_progress_option), which was marked as an expected failure. The issue causing this test to fail was fixed in revision 1095 and the test now passes.
 * 6edcd9c7: Merged in lp:~aaron-whitehouse/duplicity/fix_POTFILES.in_and_run-tests - Fixed two filename references in po/POTFILES.in, a mistake which crept in in rev 1093 and caused testing/run-tests to fail with "IndexError: list index out of range".
 * 89c33882: Fixed two filename references in po/POTFILES.in, a mistake which crept in in rev 1093 and caused testing/run-tests to fail with "IndexError: list index out of range".
 * b09199ba: Re-enable the test of the --progress option (test_exclude_filelist_progress_option), which was marked as an expected failure. The issue causing this test to fail was fixed in revision 1095 and the test now passes.
 * 704a2492: Merged in lp:~ed.so/duplicity/gpg.binary - new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * ae20199a: Merged in lp:~ed.so/duplicity/gpg.binary - new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * 3589c56d: new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * be733da8: Fixed bug 1466582 - reduce unnecessary syscall with --exclude-if-present - with patch from Kuang-che Wu to make sure resulting path is a directory.
 * 0b62ad25: Fixed bug 1466582 - reduce unnecessary syscall with --exclude-if-present - with patch from Kuang-che Wu to make sure resulting path is a directory.
 * 2e1ba52e: Fix missing argument in _error_code
 * 73dc60eb: Fixed bug 1466160 - pydrive backend is slow to remove old backup set - with patch from Kuang-che Wu to implement _delete_list().
 * f013057c: Fixed bug 1466160 - pydrive backend is slow to remove old backup set - with patch from Kuang-che Wu to implement _delete_list().
 * 97754400: Fixed bug 1452263 - par2 option not working on small processors - with patch from Kuang-che Wu to ignore default 30 second timeout.
 * aef40012: Fixed bug 1465335 - pydrive still use files in trash can - with patch from Kuang-che Wu to ignore trashed files.
 * 06d4eb37: Add an ID cache to the PyDrive backend.
 * 41c1e621: Fixed bug 791794 - description of --gpg-options is misleading, Simply needed to add the '--' before the options as in "--opt1 --opt2=parm".
 * ddda51ae: Fix a couple of PEP8 glitches.
 * 3d977000: Merged in lp:~raymii/duplicity/fix-swiftbackend-max-10000-files-in-list - Swiftclient by default returns at max 10000 files. By adding full_listing=True we make sure all objects are returned. Ref: https://lists.nongnu.org/archive/html/duplicity-talk/2015-05/msg00060.html and http://docs.openstack.org/developer/python-swiftclient/swiftclient.html#swiftclient.client.get_container
 * e749d50c: Merged in lp:~ed.so/duplicity/gdocs.pydrive - make pydrive new gdocs default backend - keep gdata backend as gdata+gdocs://
 * 33320f00: Add full_listing=True so that swiftclient returns more than 10000 objects. Default is False.
 * b1fbbfab: manpage - some reordering, update "A NOTE ON SSH BACKENDS" to the new prefix+ changes
 * 9269d030: make pydrive new gdocs default backend keep gdata backend as gdata+gdocs://
 * e5743342: Merged in lp:~bmerry/duplicity/pydrive-regular - This implements the proposal made by somebody else (http://lists.gnu.org/archive/html/duplicity-talk/2015-02/msg00037.html) to allow the pydrive backend to work with a normal drive account instead of a service account. It seems to be working for me: I was able to migrate seamlessly from the gdocs backend. It's set up so that a service account can still be used, depending on which environment variable is set. The man page is updated to describe how to use the new functionality.
 * 725b971b: Support using PyDrive with a regular Google account, instead of a service account.
 * 6b4cbf12: Merged in lp:~noizyland/duplicity/fix-progress - Fixes bug 1264744. selection.filelist_globbing_get_sfs leaves the filelist file object's position at the end of the file. When the --progress option is used the filelists need to be read twice. On the second read nothing is read from the file because file has already been read and the position is EOF. This patch calls seek(0) on the filelist to reset the position to BOF so that subsequent read() calls will return data. * Added pylint ignore error in webdavbackend.py.
 * ec0ae7f7: Perform seek(0) on filelist before read().
 * 41013145: Reset filelist position to beginning of file after calling read(). This allows file to be read again.
 * 86f88f64: Merge in lp:~sjakthol/duplicity/onedrive-error-message - Add proper error message for OneDrive backend when python-requests or python-requests-oauthlib is not installed (bug 1453355).
 * bed9d791: Add proper error messages for OneDrive backend when python-requests or python-requests-oauthlib is not installed (bug 1453355).
 * 39e73c64: Added ability to get single file status from collection-status with patch from jitao (bug 1044715), like so: $ duplicity collection-status --file-changed c1 file://./foo
 * 6fc98969: Launchpad automatic translations update.
 * c874f806: Launchpad automatic translations update.
 * cead6f00: Enable --ignore-errors flag in rdiffdir
 * 01ece1ff: Fixed bug 1448249 and bug 1449151 thanks to David Coppit. - When patching, close base file before renaming
 * 9be05c5b: Fixed bug 1444404 with patch from Samu Nuutamo - rdiffdir patch crashes if a regular file is changed to a non-regular file (symlink, fifo, ...)
 * fa4501c7: Merge in lp:~cemsbr/duplicity/duplicity - Fix bug 1432229 in Copy.com backend: Reply header has no content-type for JSON detection. Now, we also check whether the content starts with '{'.
 * b9a6fe2b: Fix bug 1432229 in Copy.com backend - Reply header has no content-type for JSON detection. Now, we also check whether the content starts with '{'.
 * 6113dc3f: Launchpad automatic translations update.
 * 691a388e: Launchpad automatic translations update.
 * 581619a7: Move requirements section lower in manpage.
 * d403efd6: Merge in lp:~stynor/duplicity/multi-backend - A new backend that allows use of more than one backend stores (e.g. to combine the available space from more than one cloud provider to make a larger store available to duplicity).
 * 5c737e5d: logging cleanup
 * 6eafd93c: typo - missing quote
 * 6e29444a: add doc
 * 911a2d98: add doc
 * 3efab9f1: adjust delete to make unit tests pass
 * 7ef7f76a: document json format
 * 77dff5b6: improved logs; dont allow low level retry to kick in
 * c63caf26: initial working code - tested with gdocs and file backends
 * 2ed13bc9: Fix bug 1437789 with patch from pdf - par2backend.py incorrect syntax in get()
 * cbcabb49: Fix bug 1434702 with help from Robin Nehls - incorrect response BackendException while downloading signatures file.
 * 90a0ca7b: Fix bug 1432999 with hint from Antoine Afalo.
 * 14d637ed: Merged in lp:~aaron-whitehouse/duplicity/filelist_combine - Merged globbing and non-globbing filelists to use the same code path and all accept globbing characters. Added deprecation warning to the --exclude-globbing-filelist and include-globbing-filelist options in commandline.py and hid them from help output. Updated the manual (and unit tests) accordingly. - Note that this does trigger a change in behaviour for duplicity. Previously, include patterns in include-filelist did not match files in a directory that was included, so /usr/local in an include file would not have matched /usr/local/doc. Now, this folder would be included, as would occur if --include or the old --include-globbing-filelist was used. Additional lines will therefore need to be added to filelists to unambiguously exclude unwanted subfolders, if this is intended. - Mark --include-filelist-stdin and --exclude-fielist-stdin for deprecation and hide from --help output.
 * d57b77e7: Updated duplicity.pot
 * 3f04b186: Merge in changes to rebase against dev.
 * df9d8587: Changed tests to test filelist, rather than globbing filelist, except for one functional globbing test of each type to ensure this continues to work until it is deliberately removed. Changed naming of tests etc accordingly.
 * b9806ad2: Removed unnecessary tests (post merging of non-globbing and globbing filelists) and created a globbing version of the one test that was only written for non-globbing filelists.
 * 48287b6f: Updated manual to remove references to globbing filelists and stdin filelists and make consequential changes to the description of include-filelist and exclude-filelist behaviour.
 * aebae1c7: Merge in lp:~duplicity-team/duplicity/po-updates
 * 5d216790: remove extraneous string format arg in previous scp fix.
 * d1864d6a: Fix for --pydevd debug environment and location under Eclipse. * Fix for bug where scp was actually working as scp and not working with rsync.net because of using extraneous test command in restricted shell. Was trying "test -d 'foo' || mkdir -p 'foo'", now only "mkdir -p foo".
 * 0129a806: Note Bug #1423367 was fixed in the previous commit.
 * 7b14c6ad: Mark --include-filelist-stdin and --exclude-fielist-stdin for deprecation and hide from --help output. Add additional tests in stdin_test.sh to test --include-filelist-stdin and that /dev/stdin is an adequate replacement.
 * 71cc37b8: Added bash script (stdin_test.sh) showing that filelists from stdin were working as expected despite the changes.
 * 43f9b747: Really fix bug 1416344 based on comment #5 by Roman Tereshonkov
 * da7c6f85: Fix _librsyncmodule.c compilation, bug 1416344, thanks to Kari Hautio.
 * 6aba6be4: Fix spelling error in manpage, bug 1419314.
 * 10d28763: Added deprecation warning to the --exclude-globbing-filelist and include-globbing-filelist options in commandline.py and hid them from help output. Commented out functions relating to non-globbing filelists. Commented out unit tests related to non-globbing filelists.
 * ae5e5086: Made non-globbing filelists use the globbing code path (ie made all filelists globbing), as per: http://lists.nongnu.org/archive/html/duplicity-talk/2015-01/msg00011.html Fixed Bug #1408411 in the process, as this issue was limited to the non-globbing code path.
 * 072ce385: Coalesce CHANGELOG
 * 30819fe9: Misc fixes for the following PEP8 issues: E401 - see http://pep8.readthedocs.org
 * 611f373e: Misc fixes for the following PEP8 issues: E231, E241, E251, E261, E262, E271, E272, E301, E302, E303, E502, E701, E702, E703, E711, E721, W291, W292, W293, W391 - see http://pep8.readthedocs.org
 * d6bcb224: Misc fixes for the following PEP8 issues: E231, E241, E251, E261, E262, E271, E272 - see http://pep8.readthedocs.org
 * 85446d0e: Misc fixes for the following PEP8 issues: E231, E241 - see http://pep8.readthedocs.org
 * e4d4b799: Misc fixes for the following PEP8 issues: E231, E241 - see http://pep8.readthedocs.org * Fixes for 2to3 issues
 * 0caf808f: Merged in lp:~aaron-whitehouse/duplicity/bug_932482_trailing_slashes_and_wildcards_error - Added functional and unit tests to show Bug #932482 - that selection does not work correctly when excludes (in a filelist or in a commandline option) contain both a single or double asterisk and a trailing slash.
 * 46057d22: Added functional and unit tests to show Bug #932482 - that selection does not work correctly when excludes (in a filelist or in a commandline option) contain both a single or double asterisk and a trailing slash.
 * 8d81fe77: Merged in lp:~aaron-whitehouse/duplicity/bug_884371_asterisks_in_includes - Added tests to unit/test_selection.py and funtional/test_selection.py to show the behaviour reported in Bug #884371, i.e. that selection is incorrect when there is a * or ** on an include line of a filelist or commandline --include.
 * 78b27da5: Added credit to Elifarley Cruz for one of the test cases.
 * f1130d1c: Added functional tests to functional/test_selection.py to show Bug #884371 (* and ** not working as expected) applies to commandline --include.
 * 3eedae1f: Added tests to unit/test_selection.py and funtional/test_selection.py to show the behaviour reported in Bug #884371, i.e. that selection is incorrect when there is a * or ** on an include line.
 * a14a55e5: Merged in lp:~angusgr/duplicity/exclude-older-than - Add "--exclude-older-than" commandline option, that allows you to only back up files with a modification date newer than a particular threshold. * Additional pep8 cleanup.
 * 8a2c4cc0: Ongoing pep8 corrections.
 * 4afbda13: Add option --exclude-older-than to only include recently modified files.
 * 67e7082f: Applied patch from Adam Reichold to fix bug # 1413792
 * aef50709: Fixed bug # 1414418 - Aligned commandline.py options and help display contents. - Aligned commandline.py options and manpage contents. * Changed --s3_multipart_max_timeout to --s3-multipart-max-timeout to be consistent with commandline option naming conventions.
 * f4e240cd: Launchpad automatic translations update.
 * 9ca6025d: Misc fixes for the following PEP8 issues: 201, 202, 203 - see http://pep8.readthedocs.org
 * d314c16a: Misc fixes for the following PEP8 issues: E127, E128 - see http://pep8.readthedocs.org
 * 92f81918: Misc fixes for the following PEP8 issues: E111, E121, E122, E124, E125, E126 - see http://pep8.readthedocs.org
 * 24ee18c8: Remove 'gs' and 's3+http' from uses_netloc[]. Fixes Bug 1411803.
 * 26f3de3b: Merged in lp:~duplicity-team/duplicity/po-updates
 * a99abfe0: Fixed variable typo in commandline.py that was causing build fails.
 * f56a246a: Fixed some tabs/spaces problems that were causing install failures.
 * 1e456813: Merged in lp:~user3942934/duplicity/pydrive - Currently duplicity uses gdocs backend for Google Drive backups. gdocs uses deprecated API and don't allow backups for managed Google accounts. (see https://bugs.launchpad.net/duplicity/+bug/1315684) - Added pydrive backend that solves both of those problems. Published also on https://github.com/westerngateguard/duplicity-pydrive-backend.
 * 7c181e2e: Merged in lp:~noizyland/duplicity/fix_azurebackend_container_names - Azure Backend examples have underscores in the container names. These are not valid Azure container names. The underscores have been replaced with hypens and a note about valid container names added to the man page. - Also corrects a problem where Azure Exceptions were returing unicode strings that were not being handled correctly.
 * 0d6e5fa0: Changed passing keyfile via query in URL to passing the key by environment variable. Fixed manpage accordingly. Restored Azure info in manpage that was somehow mistakenly deleted.
 * 2b016aec: removed underscores from example Azure container names - added Azure container name rules to man page - handle unicode messages correctly in Azure Exceptions
 * 21f0e7c1: Launchpad automatic translations update.
 * 40aa8c29: Merged in lp:~aaron-whitehouse/duplicity/progress_option_error - Added test_exclude_globbing_filelist_progress_option into functional/test_selection.py, which shows the error reported in Bug #1264744 - that the --exclude-globbing-filelist does not backup the correct files if the --progress option is used. Test is marked as an expected failure so as not to cause the test suite to fail.
 * 1e964e8b: Added test_exclude_globbing_filelist_progress_option into functional/test_selection.py, which shows the error reported in Bug #1264744 - that the --exclude-globbing-filelist does not backup the correct files if the --progress option is used. Test is marked as an expected failure so as not to cause the test suite to fail.
 * 2da16df8: fixed URI parsing
 * 777197e8: Merged in lp:~vincegt/duplicity/swift_regionname - Fixes bug #1376628 - Add mapping of SWIFT_REGIONNAME to select region inside SWIFT when a provider proposes more than one region.
 * 4c0cc984: Fixed some recently added 2to3 and pep8 issues.
 * e5584018: Add SWIFT_REGIONNAME parameter to select SWIFT REGION. See bug #1376628
 * 5fe93de6: added pydrive backend aimed to replace the deprecated gdocs backend
 * 3bcbb360: Merged in lp:~noizyland/duplicity/azurebackend - Add backend for Azure Blob Storage Service
 * 507d3c34: Merged in lp:~9-sa/duplicity/FixBug1408289 - Fix bug #1408289 - Wrong attribute name prevented raise of client exception, working now
 * 08035e77: Launchpad automatic translations update.
 * e5a08a5e: modified: duplicity/backends/azurebackend.py
 * 5c75fe2d: modified: duplicity/backends/azurebackend.py
 * 2053aad7: modified: bin/duplicity.1 duplicity/commandline.py
 * 6c37fe4f: Fix Bug #1408289
 * b674fecd: added: duplicity/backends/azurebackend.py
 * 24f92e54: Merged in lp:~hooloovoo/duplicity/process_filelists_for_spaces_etc - Process filelists to remove imperfections such as blank lines, comments and leading/trailing whitespace. Also correctly processes quoted folders containing spaces in their names. Extensive unit and functional tests to test these changes (and selection more generally). - The branch does add an additional folder to testfiles.tar.gz called select2. This included a folder with a trailing space, to test the quote test. The subfolders also have clearer names than in the "select" folder (eg "1sub2sub3") which makes it easier to keep track of issues in tests.
 * 1d6d2cb1: Merged in lp:~hooloovoo/duplicity/filelist_select_bug_1408411 - Adds functional test cases that fail because of Bug #1408411 (commented out), to assist in fixing that bug.
 * 9028a95f: Merged in lp:~stapelberg+ubuntu/duplicity/add-onedrive-backend - Add a Microsoft OneDrive backend
 * a1c6bea8: selection.py modified to pre-process lines for both globbing and non-globbing filelists to: remove leading and trailing whitespace; process quoted filenames correctly; remove blank lines; and ignore full-line comments. Added tests to unit/test_selection.py and functional/test_selection.py to cover these. Added a new folder select2 to the testfiles.tar.gz for the new functional tests (clearer names and a folder with trailing whitespace).
 * 700de23c: Added functional test cases to show the issue reported in Bug #1408411 (Filelist (non-globbing) should include a folder if it contains higher priority included files - https://bugs.launchpad.net/duplicity/+bug/1408411).
 * e1ca2579: Add a backend for Microsoft OneDrive
 * bf861f86: Fixed bug 1278529 by applying patch supplied in report - Use get_bucket() rather than lookup() on S3 to get proper error msg.
 * cf71f0aa: Misc fixes for the following PEP8 issues: E211, E221, E222, E225, E226, E228 - see http://pep8.readthedocs.org
 * 8ba5d034: Fixed bug 1406173 by applying patch supplied in report - Ignore .par2 files in remote file list * Removed redundant shell test testing/verify_test.sh
 * 080fcd11: Merged in lp:~hooloovoo/duplicity/add-else-to-badupload-try-except - Badupload test previously did not have an else in the try-except. The test passed if the except was triggered, but would also pass if the test did not trigger an error at all.
 * c37b0225: Merged in lp:~hooloovoo/duplicity/add-additional-verify-tests-for-corrupted-archives - Add tests to test_verify.py to test that verify fails if the archive file is corrupted. Changed file objects to use the with keyword to ensure that the file is properly closed. - Small edit to find statement in verify_test.sh to make it work as expected (enclose string in quotes).
 * f389a777: Add comments to the verify_test.sh script matching up the tests in there to the tests implemented in test_verify.py. All the tests in the shell script have now been implemented, so the shell script should perhaps be deleted.
 * ce7ede01: Add tests to test_verify.py to test that verify fails if the archive file is corrupted. Changed file objects to use the with keyword to ensure that the file is properly closed. Small edit to find statement in verify_test.sh to make it work as expected (enclose string in quotes).
 * 032ef264: Add else to try-except in badupload functional test, to catch where the test passes successfully instead of throwing an error (as it should).
 * 50c83e39: Merge in lp:~hooloovoo/duplicity/test-verify-improvements - Fix up test_verify, which was a bit of a mess: Simplify test_verify.py to just do a simple backup and verify on a single file in each test. - Modify tests to correctly use --compare-data option. - Add tests for when the source files have atime/mtime manipulated. * Fix duplicity verify to ignore the file system when globals.compare_data is False. This means that verify only validates the viability of the backup itself unless --compare-data is specified. * Reenable test_verify_changed_source_file test
 * c7b92449: Simplify test_verify.py to just do a simple backup and verify on a single file in each test. Modify tests to correctly use --compare-data option and to add tests for verify when the source files have the atime/mtime manipulated.
 * 08facffc: Make ssh an unsupported backend scheme * Temporarily disable RsyncBackendTest and test_verify_changed_source_file
 * f5fe71dd: Merge in lp:~ed.so/duplicity/move_netloc - move netloc usage definitions into respective backends - fix "[Question #259173]: rsync backend fails" https://answers.launchpad.net/duplicity/+question/259173
 * 1a4c9df6: Tests to validate that duplicity does not check filesystem source during verify unless --compare-data is specified
 * b78d7620: move netloc usage definitions into respective backends
 * 19b14d05: Added in tests including compare_data
 * e67597df: Added test_verify_changed_source_file test to flag up the issue mentioned in Bug #1354880
 * 141e0910: Merge in lp:~andol/duplicity/signkeyformat - Allow --sign-key to use short format, long format alt. full fingerprint.
 * 6afcb4b4: Source formatted, using PyDev, all source files to fix some easily fixed PEP8 issues. Use ignore space when comparing against previous versions.
 * f87f52f2: Merged in lp:~ed.so/duplicity/paramiko.identyfile - fix identity file parsing of --ssh-options for paramiko - manpage fixes
 * 90762e74: Launchpad automatic translations update.
 * 0e9dfe24: fix identity file parsing of --ssh-options for paramiko manpage fixes
 * 44633fbb: Modded .bzrignore to ignore *.egg test dependencies, normalized, sorted.
 * 811e3971: Manually merged in lp:~m4ktub/duplicity/0.6-reliability - Per fix proposed in Bug #1395341.
 * 94fe24c7: Fix changelogs comments.
 * 5a90dd80: Fixed bug 1255453 with changes by Gaudenz Steinlin, report backend import results, both normal and failed, at INFO log level.
 * 939f79da: Fixed bug 1236248 with changes by az, manpage warning about --extra-clean.
 * 1846fd88: Fixed bug 1385599 with changes by Yannick Molin. SSL settings are now conditioned on protocol ftp or ftps.
 * e68aefb8: Merged in lp:~adrien-delhorme/duplicity/hubic - Add Hubic support through pyrax and a custom pyrax_identity module.
 * ad368e2b: In webdavbackend.py: Fixed bug 1396106 with change by Tim Ruffing, mispelled member. - Added missing 'self.' before member in error message.
 * b776ec40: Merge lp:duplicity onto lp:~adrien-delhorme/duplicity/hubic
 * 11974c82: Update man page
 * 0db29890: Update man page Add hubic identity module
 * cb429578: Undid move of testing/test_code.py. Instead I fixed it so that it would not run during PPA build. It now needs the setting RUN_CODE_TESTS=1 in the environment which is supplied in the tox.ini file.
 * c8387d7f: Moved testing/test_code.py to testing/manual/code_test.py so PPA builds would succeed. Should be moved back later.
 * fa7dc5fb: Remove valid_extension() check from file_naming.py. It was causing failed tests for short filenames. Thanks edso.
 * bcfde46b: Launchpad automatic translations update.
 * a86ea3c6: Partial fix for PPA build failures, new backend name.
 * c0005eca: Merged in lp:~ed.so/duplicity/fix.dpbx.import - fix dpbx import error import lazily
 * 91744457: fix dpbx import error import lazily
 * 5349715d: Fix for failing PPA builds. FTP backend has variable class names.
 * 586f6ffb: Fix files list.
 * 84d8ff77: Merged in lp:~hooloovoo/duplicity/fix-typo-in-test-description - Fixed spelling mistake/typo in a description of a test.
 * a309c850: Merged in lp:~mterry/duplicity/missing-unicode-escape - Convert restore_dir to unicode before printing.
 * 844300e3: Merged in lp:~ed.so/duplicity/lftp.ncftp.and.prefixes - retire --ssh-backend, --use-scp parameters - introduce scheme prefixes for alternative backend selection e.g. ncftp+ftp://, see manpage - scp is now selected via scheme e.g. scp:// - added lftp fish, webdav(s), sftp support
 * a4626165: Launchpad automatic translations update.
 * 7b41238d: Launchpad automatic translations update.
 * 03aca7b0: Escape filename before printing in unicode
 * 7246e8fb: Launchpad automatic translations update.
 * 04a9fd80: Add Hubic backend
 * 62874fff: Fix typo ('hidding' to 'hiding')
 * d0cfd401: Support older versions of dpkg-parsechangelog
 * f407e8c1: add https cert verification switches
 * 49b48082: more manpage fixes/reformatting retire parameters --ssh-backend, --use-scp, functionality is achieved via scheme:// setting now add lftp webdav support add lftp fish support fix assertionerror when using par2+ backend
 * 2307cd24: Some small testing fixes to work on older copies of mock and pylint
 * 7e130e01: manpage: document ftp changes/minor enhancements
 * 482a8df9: allow ftp backend selection via prefix
 * 0f401da9: rename lftp/ncftp backends
 * e21c8804: restore ncftp backend
 * cb4a2070: Allow --sign-key to use short format, long format alt. full fingerprint.
 * 94150cce: Minor tweaks to debian/control to fix building on older versions of Ubuntu
 * f439d1cc: Merged in lp:~mterry/duplicity/debian-dir - Add a debian/ directory to make it easier to manage the PPAs for duplicity.
 * 1395e10f: Fix Edgar's name
 * bc081ec9: Merged in lp:~mterry/duplicity/code-nits - Fix some pylint/pep8 nits that prevented the test_code.py test from passing.
 * 76799e8e: Add debian packaging
 * 56010337: Avoid super() on old-style class
 * 2490765c: Fix pylint/pep8 nits so that tests pass
 * c7ef4fc9: Launchpad automatic translations update.
 * e739f1cb: Launchpad automatic translations update.
 * 1686422a: Adjust unit tests to expect single FTP backend
 * 36f1ae7b: Merged in lp:~moritzm/duplicity/duplicity - Use lftp for both FTP and FTPS
 * 819105ed: Minor accounting fix.
 * 1ff25aa1: Merged in lp:~johnleach/duplicity/1315437-swift-container-create - Check to see if the swift container exists before trying to create it, in case we don't have permissions to create containers. Fixes #1315437
 * ebb6bf63: Clean up imports.
 * 15643259: Launchpad automatic translations update.
 * 42365f6f: Merged in lp:~ed.so/duplicity/0.7-dpbx.importfix - fix this showstopper with the dropbox backend "NameError: global name 'rest' is not defined"
 * ced3a8e8: Launchpad automatic translations update.
 * 46b65cd8: Merged in lp:~jflaker/duplicity/BugFix1325215 - The reference to "--progress_rate" in the man page as a parameter is incorrect. Should be "--progress-rate".
 * 4a5d2346: Merged in lp:~hooloovoo/duplicity/updated-README-REPO - Changes to README-REPO to reflect the restructuring of the directories.
 * f0ec50af: use lftp for both FTP and FTPS
 * bbad2cdf: Launchpad automatic translations update.
 * 9f1dd251: Fixed bug 1375304 with patch supplied by Aleksandar Ivanovic
 * fec21cc3: Change the branch for stable. lp:duplicity/stable doesn't exist and so I've changed this to lp:~duplicity-team/duplicity/0.6-releases as this is the only non-Windows, non-dev branch.
 * e64a10cf: Corrected the extra dot in the stable branch line at step 1.
 * d82de7b5: Updated README-REPO to reflect restructuring of directories. See https://answers.launchpad.net/duplicity/+question/252898
 * d0eee66b: Launchpad automatic translations update.
 * 8539df34: Merged in lp:~jeffreydavidrogers/duplicity/duplicity - This change fixes two small typos in the duplicity man page.
 * 9a9bd6ea: Merged in lp:~ed.so/duplicity/manpage.verify - clarify verify's functionality as wished for by a user surprised with a big bandwidth bill from rackspace.
 * 37e5e2b3: Added sxbacked.py, Skylable backend. Waiting on man page updates.
 * b3a9f5e4: Fix two small typos in duplicity man page
 * c951dfcc: clarify verify's functionality as wished for by a user surprised with a big bandwidth bill from rackspace.
 * b5b8ebc2: Launchpad automatic translations update.
 * b2c9cab7: Fixed bug 1327550: OverflowError: signed integer is greater than maximum - Major and minor device numbers are supposed to be one byte each. Someone has crafted a special system image using OpenVZ where the major and minor device numbers are much larger (ploop devices). We treat them as (0,0).
 * f96cdedb: Merged in lp:~antmak/duplicity/0.7-par2-fix - Useful fix for verbatim par2cmdline options (like "-t" in par2-tbb version)
 * 6c6a7414: Restore accidental deletion.
 * cae2954b: Merged in lp:~mterry/duplicity/webdav-fixes - This branch fixes two issues I saw when testing the webdav backend: 1) Errors like the following: "Attempt 1 failed. BackendException: File /tmp/duplicity-LQ1a0i-tempdir/mktemp-u2aiyX-2 not found locally after get from backend". These were caused by the _get() method not calling setdata() on the local path object, so the rest of the code thought it didn't exist. - 2) Some odd issues from stale responses/data. We have a couple places in webdavbackend.py where we close the connection before making a request because of this problem. But I've changed it to do it every time, more reliably, by putting a _close() call inside the request() method. - With this, the webdav backend seems fine to me.
 * 2f443255: Merged in lp:~ed.so/duplicity/webdav200fix-0.7 - webdav backend fix "BackendException: Bad status code 200 reason OK. " when restarting an interrupted backup and overwriting partially uploaded volumes.
 * 93effcc8: Merged in lp:~3v1n0/duplicity/copy.com-backend - I've added a backend for Copy.com cloud storage, this supports all the required operations and works as it should from my tests. - You can use it by calling duplicity with something like: copy://account@email.com:your-password@copy.com/duplicity - The only thing I've concerns with is the optimized support for _delete_list which can't be enabled here because the test_delete_list tries also to delete a not-existing files, and it requires the backend not to raise an exception in that case (is this somewhat wanted or could we do the same as for _delete or _query?)
 * f6db6644: Fix setdata() not being called a better way
 * 6b506216: README: add copy.com requirements
 * 716f6d08: Add copy.com to man file
 * fedceb26: CopyComBackend: import non-main modules only when needed
 * bb89013d: CopyComBackend: remove unneded upload checks
 * 038fa9db: CopyComBackend: implement _query method
 * 342a9bc3: CopyComBackend: disable the _delete_list support, it won't work if a file doesn't exist
 * 1035f80d: CopyComBackend: add ability to delete list of files
 * f147180d: Backends: Add Copy.com support, implement basic operations
 * 5146aa02: Use writefileobj instead of direct write, for less code and so that we call setdata()
 * 263cc6d4: More reliably reset webdav connection
 * 3f263cff: webdav backend fix "BackendException: Bad status code 200 reason OK. " when restarting an interrupted backup and overwriting partially uploaded volumes.
 * c6b41d02: Added user defined verbatim options for par2
 * 706ce8e8: Update shebang line to python2 instead of python to avoid confusion.
 * 4a8d6267: Merged in lp:~mterry/duplicity/py2.6.0 - Support python 2.6.0. - Without this branch, we only support python >= 2.6.5 because that's when python's urlparse.py module became its more modern incarnation. (I won't get into the wisdom of them making such a change in the middle of the 2.6 lifecycle.) - Also, the version of lockfile that I have (0.8) doesn't work with python 2.6.0 or 2.6.1 due to their implementation of threading.current_thread().ident returning None unexpectedly. So this branch tells lockfile not to worry about adding the current thread's identifier to the lock filename (we don't need a separate lock per thread, since our locking is per process). - I've tested with 2.6.0 and 2.7.6 (both extremes of our current support).
 * dda927b5: Support py2.6.0
 * 334ab63f: Clean up indentation mismatches.
 * 4df9c06a: Launchpad automatic translations update.
 * 09489ba3: Misc format fixes.
 * a92828d9: Launchpad automatic translations update.
 * 234747e4: Applied expat fix from edso. See answer #12 in https://answers.launchpad.net/duplicity/+question/248020 * Forward-ported from r980 in 0.6-series
 * a84e6b13: First cut of 0.7.00 Changelog.
 * 7202204e: Launchpad automatic translations update.
 * 7637d9ef: Fix running ./testing/manual/backendtest to be able to find config.py and fix the tests in testing/manual/ to not be picked up by ./setup.py test
 * bf123154: Launchpad automatic translations update.
 * 47b09b9e: Merged in lp:~mterry/duplicity/encode-exceptions - Because exceptions often contain file paths, they have the same problem with Python 2.x's implicit decoding using the 'ascii' encoding that we've experienced before. So I added a new util.uexc() method that uses the util.ufn() method to convert an exception to a unicode string and used it around the place. - Bugs fixed: 1289288, 1311176, 1313966
 * 6eb013b8: Launchpad automatic translations update.
 * 69ec5019: Convert exceptions to unicode
 * a9d5329b: Merged in lp:~mterry/duplicity/backend-unification - Reorganize and simplify backend code. Specifically: Formalize the expected API between backends and duplicity. See the new file duplicity/backends/README for the instructions I've given authors. - Add some tests for our backend wrapper class as well as some tests for individual backends. For several backends that have some commands do all the heavy lifting (hsi, tahoe, ftp), I've added fake little mock commands so that we can test them locally. This doesn't truly test our integration with those commands, but at least lets us test the backend glue code. - Removed a lot of duplicate and unused code which backends were using (or not using). This branch drops 700 lines of code (~20%) in duplicity/backends! - Simplified expectations of backends. Our wrapper code now does all the retrying, and all the exception handling. Backends can 'fire and forget' trusting our wrappers to give the user a reasonable error message. Obviously, backends can also add more details and make nicer error messages. But they don't *have* to. - Separate out the backend classes from our wrapper class. Now there is no possibility of namespace collision. All our API methods use one underscore. Anything else (zero or two underscores) are for the backend class's use. - Added the concept of a 'backend prefix' which is used by par2 and gio backends to provide generic support for "schema+" in urls -- like par2+ or gio+. I've since marked the '--gio' flag as deprecated, in favor of 'gio+'. Now you can even nest such backends like par2+gio+file://blah/blah. - The switch to control which cloudfiles backend had a typo. I fixed this, but I'm not sure I should have? If we haven't had complaints, maybe we can just drop the old backend. - I manually tested all the backends we have (except hsi and tahoe -- but those are simple wrappers around commands and I did test those via mocks per above). I also added a bunch more manual backend tests to ./testing/manual/backendtest.py, which can now be run like the above to test all the files you have configured in config.py or you can pass it a URL which it will use for testing (useful for backend authors).
 * 069b0c5e: further fixes
 * 4b69b748: Launchpad automatic translations update.
 * b3c2ffe5: Merge from trunk
 * fc3a7d56: Minor fixes
 * c10bf10d: Merged in lp:~mterry/duplicity/py3-map-filter - In py3, map and filter return iterable objects, not lists. So in each case we use them, I've either imported the future version or switched to a list comprehension if we really wanted a list.
 * a26de1ef: Launchpad automatic translations update.
 * 94944335: Fix map usage for py3 readiness
 * 0c62651f: Fix filter usage for py3 readiness
 * d949051d: Fixed bug #1312328 WebDAV backend can't understand 200 OK response to DELETE - Allow both 200 and 204 as valid response to delete
 * 95498e17: Add ftp backend test
 * 04844590: Drop popen_subprocess_persist in favor of just the basic version; add ftps backend test
 * b0b9c49b: And test hsi backend too
 * 88da7047: Add fake tahoe executable, so we can test the tahoe backend
 * a4e9b7e6: Add support for backend prefixes, allow rsync backend to use local paths, and add some more tests
 * 5db5c650: Add some backend tests, clean up par2backend, and general fixes
 * 3c5d5064: Checkpoint
 * 391eabea: Launchpad automatic translations update.
 * 0bee78c9: # Merged in lp:~mterry/duplicity/more-test-reorg - Here's another test reorganization / modernization branch. It does the following things: Drop duplicity/misc.py. It is confusing to have both misc.py and util.py, and most of the code in misc.py was no longer used. I moved the one function that was still used into util.py. - Consolidated the various ways to run tests into just one. I made tox runs go through ./setup.py test, rather than nosetests. And I made the ./testing/run-tests scripts just call tox. Now we no longer need nosetests as a test dependency (although you can still use it if you want). - Added two more code quality automated tests: a pep8 one and a pylint one. I disabled almost all checks in each program that gave a warning. These tests just establish a baseline for future improvement. - Moved the test helper code into TestCase subclasses that all tests can use. And used more code sharing and setUp/tearDown cleverness to remove duplicated code. - Reorganized the tests in ./testing/tests into ./testing/functional and ./testing/unit -- for whether they drive duplicity as a subprocess or whether they import and test code directly. Each dir can have specialized TestCase subclasses now. - Renamed the files in ./testing/unit to more clearly indicate which file in ./duplicity they are unit testing. - Added some helper methods for tests to set environment and globals.* parameters more safely (i.e. without affecting other tests) by automatically cleaning up any such changes during test tearDown. - Removed test_unicode.py, since it is kind of dumb. It used to be more useful, but now with py2.6, we are just testing that one line of code in it is actually there.
 * 71b0033e: Add overrides dir
 * 7fe76cc6: more minor fixes
 * 2924362d: Move rootfiles.tar.gz into manual directory
 * a078e99d: Add initial pep8 and pylint tests
 * fcdc74e2: Minor fixes
 * 054b1fc9: Make run-tests scripts go through tox, this makes all our standard test-running modes ultimately go through ./setup test
 * 296953c7: Drop little-used misc.py
 * 373ee8b3: More reorg of testing/
 * e20d687a: Launchpad automatic translations update.
 * 974334a7: Merged in lp:~mterry/duplicity/encode-for-print - Encode translated strings before passing them to 'print'. - The print command can only apparently handle bytes. So when we pass it unicode, it freaks out. There were only four instances I saw where we used print, so I figured it was easiest to just convert them to use the log framework too. - That way all user-visible strings go through that framework and are subject to the same encoding rules.
 * 7852a537: Merged in lp:~mterry/duplicity/drop-static - Drop static.py. - This is some of the oldest code in duplicity! A bzr blame says it is unmodified (except for whitespace / comment changes) since revision 1. - But it's not needed anymore. Not really even since we updated to python2.4, which introduced the @staticmethod decorator. So this branch drops it and its test file.
 * b0c4959a: Merged in lp:~mterry/duplicity/2.6isms - Here's a whole stack of minor syntax modernizations that will become necessary in python3. They all work in python2.6. - I've added a new test to keep us honest and prevent backsliding on these modernizations. It runs 2to3 and will fail the test if 2to3 finds anything that needs fixing (with a specific set of exceptions carved out). - This branch has most of the easy 2to3 fixes, the ones with obvious and safe syntax changes. - We could just let 2to3 do them for us, but ideally we use 2to3 as little as possible, since it doesn't always know how to solve a given problem. I will propose a branch later that actually does use 2to3 to generate python3 versions of duplicity if they are requested. But this is a first step to clean up the code base.
 * c6e19f42: Drop static.py
 * 46cce40f: Launchpad automatic translations update.
 * a49901ae: Fix subprocess usage to work in py2.6 and fix a missing unicode
 * 09cc0b33: Solve has_key 2to3 fix
 * 2540b04d: Move imports fix to the 'don't care' section
 * 2952abf2: Solve import 2to3 fix
 * d595c4da: Solve numliterals 2to3 fix
 * 717580a1: Solve long 2to3 fix
 * a01a3648: Move urllib fix to the 'don't care' section
 * 1741ac8e: Solve basestring 2to3 fix
 * 06891cb1: Move long and raw_input fixes to the 'don't care' section
 * c0cccaa6: Solve reduce 2to3 fix
 * 5d010b76: Solve raise 2to3 fix
 * b8293ba3: Mark callable and future fixes as things we explicitly don't care about
 * 685fb9fa: Solve apply 2to3 fix
 * f9da9421: Solve idioms 2to3 fix
 * b8aaaa1f: Solve ws_comma 2to3 fix
 * dc8c8f9b: Solve renames 2to3 fix
 * fccc860b: Solve except 2to3 fix
 * 8b54538f: Add test_python3.py to test readiness of source code to run under python3 directly
 * 640aecb5: Merged in lp:~mterry/duplicity/drop-pexpect - Drop our local copy of pexpect in favor of a system version. - It's only used by the pexpect ssh backend (and if you're opting into that, you probably can expect that you will need pexpect) and the tests. - I've done a quick smoketest (backed up and restored using --ssh-backend=pexpect) and it seemed to work fine with a modern version of pexpect.
 * 3e071ea8: Merged in lp:~mterry/duplicity/fix-drop-u1 - Looks like when the drop-u1 branch got merged, its conflict got resolved badly. Here is the right version of backend.py to use (and also drops u1backend.py from POTFILES).
 * 550f01c3: fix typo
 * 069063ca: Drop local copy of pexpect -- only used by one of our ssh backends and our tests
 * 9fd193e7: Fix drop-u1 merge
 * 5c354027: Merged in lp:~mterry/duplicity/drop-u1 - Ubuntu One is closing shop. So no need to support a u1 backend anymore.
 * 2597eb3f: Merged in lp:~mterry/duplicity/require-2.6 - Require at least Python 2.6. - Our code base already requires 2.6, because 2.6-isms have crept in. Usually because we or a contributor didn't think to test with 2.4. And frankly, I'm not even sure how to test with 2.4 on a modern system.
 * 39da53fd: Merged in lp:~mterry/duplicity/modern-testing - Enable/use more modern testing tools like nosetests and tox as well as more common setup.py hooks like test and sdist. - Specifically: move setup.py to toplevel where most tools and users expect it * Move and adjust test files to work when running "nosetests" in toplevel directory. Specifically, do a lot more of the test setup in tests/__init__.py rather than the run-tests scripts * Add small tox.ini file for using tox, which is a wrapper for using virtualenv. Only enable for py26 and py27 right now, since modern setuptools dropped support for <2.6 (and tox 1.7 recently dropped <2.6) * Add setup.py hooks for test and sdist which are both standard targets (sdist just outsources to dist/makedist right now)
 * 3e3433f8: Merged in lp:~mterry/duplicity/consolidate-tests - Consolidate all the duplicity-running code in the test framework. - This takes the four test files [1] that run duplicity itself (i.e. the high-level functional test files) and consolidates their code. Before, it was madness. Each one had its own run_duplicity method, with its own slightly tweaked features. This should reduce a lot of duplication. - [1] cleanuptest.py, finaltest.py, restarttest.py, and badupload.py
 * a31df098: Merged in lp:~fredrik-loch/duplicity/duplicity-S3-SSE - Adds support for server side encryption as requested in Bug #996660
 * 40e7f217: Drop support for Ubuntu One, since it is closing
 * 53ac8e6b: Drop support for Python 2.4 and 2.5
 * a72a5654: Add missing mock dep
 * af1e3dd3: Whoops, make dist dir first during sdist
 * 7b6dbba5: Enable/use more mordern testing tools like nosetest and tox as well as more common setup.py hooks like test and sdist
 * 2bc42d4b: Consolidate all the duplicity-running code in the test framework
 * 8898a2b8: Launchpad automatic translations update.
 * 8d82af08: Launchpad automatic translations update.
 * 3d123f7d: Added support for amazon s3 encryption by the use of --s3-use-server-side-encryption
 * 7f899e1b: Added support for serverside encryption in amazon s3
 * 94d0ae97: Convert unicode to utf8 before passing to print
 * cca9d792: Launchpad automatic translations update.
 * 9fc75658: Launchpad automatic translations update.
 * 190687df: Merged in lp:~germer/duplicity/par2 - This branch adds Par2 recovery files to duplicity. It is a wrapper backend which will create the recovery files and upload them all together with the wrapped backend. Corrupt archives will be detected and repaired (if possible) on the fly during restore. - It can be used with url-string par2+webdavs://USER@HOST/PATH - Fixes https://bugs.launchpad.net/duplicity/+bug/426282
 * 3f24305c: Merged in lp:duplicity
 * 79d21e53: Launchpad automatic translations update.
 * a0c0e817: Merged in lp:~prateek/duplicity/botoimportfix - Switches the boto backend back to using lazy imports so there are no complaints during the importing of backends.
 * 1dadc6d1: Merged in lp:~ed.so/duplicity/fix.dpbx - fix dpbx backend "NameError: global name 'rest' is not defined"
 * 0b7376f0: Fixed boto import issues
 * c253f7ab: fix dpbx backend "NameError: global name 'rest' is not defined"
 * 7a0bc36d: Launchpad automatic translations update.
 * 1c297d04: Fix boto import.
 * 98fedd16: Launchpad automatic translations update.
 * b99fac50: Merged in lp:~prateek/duplicity/s3-glacier - Fixes https://bugs.launchpad.net/duplicity/+bug/1039511 - Adds support to detect when a file is on Glacier and initiates a restore to S3. Also merges overlapping code in the boto backends - Fixes https://bugs.launchpad.net/duplicity/+bug/1243246 - Adds a --s3_multipart_max_timeout input option to limit the max execution time of a chunked upload to S3. Also adds debug message to calculate upload speed.
 * 7ee61e2e: Make sure each process in a multipart upload get their own fresh connection
 * 374d8ba0: Updated manpage and tweaked boto backend connection reset
 * e002b6e5: Launchpad automatic translations update.
 * 959f4094: Merged in lp:~mterry/duplicity/pexpect-fix - duplicity has its own copy of pexpect. Use that instead of requiring one from the system.
 * e680fb62: Fix pexpect import
 * 65139f4e: Merged in main branch
 * 2efb5ca8: Added max timeout for chunked uploads and debug lines to gauage upload speed
 * 7259b30d: Launchpad automatic translations update.
 * fe4d8d1b: Launchpad automatic translations update.
 * 494b5953: Launchpad automatic translations update.
 * 11fe594d: add documentation to manpage rename ~par2wrapperbackend.py
 * 4b16b79f: Merged in lp:duplicity
 * 00053c4f: Launchpad automatic translations update.
 * 10387872: Merged in lp:~mterry/duplicity/gpg-encode - getpass.getpass(prompt) eventually calls str(prompt). Which is a no go, if the prompt contains unicode. Here's a patch to always pass getpass() a byte string. - Our tests didn't catch this because they always set PASSPHRASE. I've added a test that passes the passphrase via stdin.
 * bb87391a: Add test that includes unicode characters to check the gpg prompt
 * caadb52f: Encode prompt phrase before passing to getpass
 * 94f84ad8: Launchpad automatic translations update.
 * 16bb7a93: Launchpad automatic translations update.
 * 81ec14cb: Applied two patches from mailing list message at: https://lists.nongnu.org/archive/html/duplicity-talk/2014-01/msg00030.html "Added command line options to use different prefixes for manifest/sig/archive files" This resolves https://bugs.launchpad.net/duplicity/+bug/1170161 and provides a workaround for https://bugs.launchpad.net/duplicity/+bug/1170113
 * 6679b2b1: Launchpad automatic translations update.
 * 40fd41f5: Update to translations.
 * f5270b1d: Merged in lp:~mterry/duplicity/argv-encode - Use the system filename encoding to print the args in unicode.
 * caf92c99: Merged in lp:~louis-bouchard/duplicity/remove-allow-concurrency - remove the --allow-concurrency switch but leave the lock
 * c15abb38: Remove --add-concurrency option and enhance the error message the case where an existing lockfile is detected
 * 4cf02458: Merged in lp:~louis-bouchard/duplicity/allow-concurrency-manpage
 * bb0d0c61: Reformat --allow-concurrency text and add mention of stale lockfile
 * 10ea19c7: Update manpage with new --add-concurrency option
 * dcdf87df: Merged in lp:~louis-bouchard/duplicity/add-allow-concurrency - Implement locking mechanism to avoid concurrent execution under the same cache directory. This is the default behavior. - Also implement --alllow-concurrency option to disable the locking if required. - This functionality adds a dependency to python-lockfile
 * cae03365: Add the --allow-concurrency option to disable the locking mechanism that this patch implements. By default, only one instance of duplicity will be allowed to run at once. When using this switch it disable the locking mechanism to allow more than one instance to run simultaneously (LP: #1266763)
 * 2bd57f0e: Merged in lp:~mterry/duplicity/boto-list-fix to fix bzr screwup.
 * 9f8a9310: Raise exception if we can't connect to S3 rather than just silently pretending there are no files
 * 110a253e: Restored patch of gdocsbackend.py from original author (thanks ede) * Applied patch from bug 1266753: Boto backend removes local cache if connection cannot be made
 * 48fa54ff: ede Fri 2014-01-03 11:37:54 +0100 recommit: implement fix as suggested by original autor
 * 9cf0f755: Encode sys.argv using system filename encoding before printing
 * 9fbda155: recommit: implement fix as suggested by original autor http://lists.nongnu.org/archive/html/duplicity-talk/2013-11/msg00017.html
 * 12ee08bc: Reformat to be more consistent. Remove tabs.
 * 2bea3a08: Reverted changes to gdocsbackend.py
 * c5010041: Fix conflicts.
 * 33431886: Restored missing line from patch of gdocsbackend.py
 * 5fa5a941: leftover from previous commit (thx Kostas for paying attention)
 * 2602ef1b: implement fix as suggested by original autor http://lists.nongnu.org/archive/html/duplicity-talk/2013-11/msg00017.html
 * 2fcbe124: Merged in lp:~mterry/duplicity/encoding - This branch hopefully fixes two filename encoding issues: Users in bug 989496 were noticing a UnicodeEncodeError exception which happens (as far as I can tell) because some backends (like webdav) are returning unicode filenames from list(). When these filenames are combined with the utf8 translations of log messages, either (A) the default ascii encoding can't handle promoting the utf8 bytes or -- if there aren't any utf8 bytes in the translation -- (B) the resulting unicode string raises an error later when log.py tries to upgrade the string again to unicode for printing. - This fix is largely implemented by adding a wrapper for backend list() implementations. This wrapper ensures that duplicity internals always see a byte string. (I'd like to eventually use this same wrapping strategy to implement generic retry support without backends having to add any logic, but that's just a thought for the future.) - That is, the fix for issue #1 is completely inside backend.py and the changes to backends/*.py. - The rest of the invasive changes deal with filenames that may not be valid utf8. This is much rarer, but possible. For proper handling of this, we need to print using unicode, and convert filenames from the system filename encoding to unicode, gracefully handling conversion errors. Some of the filenames we print are remote names. Who knows what encoding they are in; it could be different than the system filename encoding. 99% of the time, everything will be utf8 and we're fine. If we do get conversion errors, the only effect should be some question mark characters in duplicity logging output. - I tried to convert as much of the actual codebase to use unicode for printing. But I stopped short of adding an assert in log.py to enforce unicode, because I didn't want to go through all the backend code and manually adjust those bits without being able to test each one.
 * 1df228ea: Nuke tabs.
 * 01895aca: Merged in lp:~ed.so/duplicity/debian.dav.mkdir - upstream debian patch "webdav create folder recursively" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * fe3f5aad: Merged in lp:~ed.so/duplicity/debian.paramiko.log - upstream debian patch "paramiko logging" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * c16cf908: Merged in changes from main trunk.
 * 36044b6e: Merged in lp:~verb/duplicity/boto-min-version - Update documentation and error messages to match the current actual version requirements of boto backend.
 * 5f8fe311: upstream debian patch "webdav create folder recursively" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * 237c4d89: upstream debian patch "paramiko logging" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * f6fa0a7e: Fix help printing
 * 56b3ee4a: Promote filenames to unicode when printing to console and ensure that filenames from backend are bytes
 * 4640a479: fix the fix for dropbox backend
 * 4101b54a: remove obsolete cfpyrax+http:// scheme from manpage
 * 4bd62bf9: add mega documentation
 * 4e00d48d: some formatting fixes to rman issues on website display
 * 028a1d9d: Launchpad automatic translations update.
 * 036de639: Changed to default to pyrax backend rather than cloudfiles backend. To revert to the cloudfiles backend use '--cf-backend=cloudfiles'
 * 4e484660: Merged in lp:~jkrauss/duplicity/pyrax - Rackspace has deprecated python-cloudfiles in favor of their pyrax library, which consolidates all Rackspace Cloud API functionality into a single library. Tested it with Duplicity 0.6.21 on both Arch Linux and FreeBSD 8.3.0.
 * e1fec0e6: Launchpad automatic translations update.
 * 9ef392ed: Applied patch to fix "Access GDrive through gdocs backend failing" - see https://lists.nongnu.org/archive/html/duplicity-talk/2013-07/msg00007.html
 * b51463db: Launchpad automatic translations update.
 * 1fab5357: Merged in lp:~mterry/duplicity/normalize-before-using - Avoid throwing an exception due to a None element in a patch sequence.
 * 95df8f41: Merged in lp:~mterry/duplicity/disappearing-source - When restarting a backup, we may accidentally skip the first chunk of one of the source files. To reproduce this,: 1) interrupt a backup 2) delete the source file it was in the middle of 3) restart the backup
 * ee8dd80b: Merged in lp:~mterry/duplicity/manifest-oddities - We may accidentally end up with an oddly inconsistent manifest like so:
 * fde872b5: Merged in lp:~mterry/duplicity/log-path-type - Any backup browser built on top of duplicity will need to indicate which files in the backup are folders and which are files. The current logging information doesn't provide this detail. So I've added a field to the log.InfoCode.file_list output that includes the path type.
 * f9321c19: Merged in lp:~gliptak/duplicity/415619 - Better error message when chown fails
 * e109bda0: Merged in lp:~verb/duplicity/bucket_root_fix - Fix bug that prevents backing up to the root of a bucket with boto backend.
 * 06926823: Avoid throwing exception because of None element in patch sequence
 * 4726879e: Merge latest manifest-oddities changes
 * 3986c9b0: Fix test comments
 * 0d3b0cef: Handle a disappearing source file across restarts better
 * 1bcd1c80: Don't keep dangling volume info in manifest
 * cef2b4c7: Show path type in log when listing files
 * b16ee066: Fixed cfpyrax entry in man page
 * c1b35ad4: Added Pyrax backend for Rackspace Cloud
 * 7caa7271: Added Pyrax backend for Rackspace Cloud
 * 37a4000c: Merged in changes from main branch
 * ab713a60: Better error message for chown fail
 * 1dfc2573: Launchpad automatic translations update.
 * a1b2101c: Merged in lp:~mterry/duplicity/argv - Fix use of argv when calling os.execve
 * 98932e4f: Merged in lp:~mterry/duplicity/catch-seq-copy-error - Any* exception when running patch_seq2ropath should be ignored (though logged) and duplicity should move on. This covers the two asserts in that function (bug 1155345 and bug 720525) as well as errors that happen during file copying (bug 662442).
 * 217e92d4: Don't chop the first argument off when restarting (in an admittedly difficult-to-reach bit of code)
 * 1a4aa113: Fix some spacing
 * a02036f3: Wrap whole seq2ropath function in a general try/except rather than a more focused approach -- any problem patching a file should be ignored but logged before moving on
 * a11414b0: If a common exception happens when collapsing a non-file patch, just log it and continue
 * 6044c97a: Launchpad automatic translations update.
 * c5bb6814: Merged lp:~mterry/duplicity/ignore-missing to fix patch for 1216921.
 * ad290d68: Launchpad automatic translations update.
 * 8492a2ac: Applied patch from bug 1216921 to fix ignore_missing().
 * 73dfb75d: Or better yet, just drop the stanza, it shouldn't be needed
 * 07e9ef8f: Fix else: to be except Exception:
 * 7b2ae2b6: Fix util.ignore_missing; patch by Matthias Witte
 * e0171fda: Fixes for merging multi boto backend.
 * a2dd6b53: Fixes https://bugs.launchpad.net/duplicity/+bug/1218425
 * 19ef3689: Fixed get_connection for new generic storage
 * 3e3f4231: Fixed merge conflicts after merging in changes from main branch, mostly due to Google Storage class addition
 * a7bb0acc: Merge Conflicts
 * 1ef4dd24: Trying fix to properly destroy S3 connections.
 * 29c0d27b: Update boto minimum version requirements
 * 5ff55064: Launchpad automatic translations update.
 * eabfe4c8: Changes for 0.6.22.
 * 6a9d1ba7: Launchpad automatic translations update.
 * 4ac7249d: Merged in lp:~ed.so/duplicity/man.page - update paramiko links - add command parameters to synopsis - add --compare-data - some polishing and several improvements
 * 005735f8: Launchpad automatic translations update.
 * 5e9ff25a: update paramiko links add command parameters to synopsis add --compare-data some polishing several improvements
 * fe1ef811: Launchpad automatic translations update.
 * ff13d3c1: Applied patch from Eric S Raymond to man page to fix markup problems.
 * 33bdf60c: Merged in lp:~ckornacker/duplicity/megacloud - Add support for Mega (mega.co.nz) backend.
 * 0a20e18e: Merged in lp:~verb/duplicity/boto-gcs - These patches add support for Google Cloud Storage via the boto backend. - boto has supported GCS in interoperability mode for a few years now. This change adds support by taking advantage of boto's storage_uri abstraction layer.
 * cb07b9a7: Merged in lp:~mhu-s/duplicity/swiftbackend - This branch adds support for Swift, the OpenStack Object Storage service. See https://blueprints.launchpad.net/duplicity/+spec/swiftbackend
 * 5cc3bac0: Merged in lp:~scowcron/duplicity/ftp_password_pexpect - Use common backend.Backend get_password() rather than _ssh_pexpect.py specific code.
 * a4e72bb4: README update for BOTO version requirement
 * 3648b7e5: Added support for AWS S3 Glacier
 * a4d6dd1a: Add documentation for GCS to duplicity.1
 * 37a90ce7: Add config template for testing boto backend with GCS
 * 104d82c2: Add support for Google Cloud Storage to boto backend (single threaded only)
 * 565075bd: explicitly set umask in test_tarfile.py
 * 4cabce87: fix requesting filename
 * 8b86f45b: add par2 wrapper backend
 * f43b92ce: Adds doc
 * 5e54c19b: better handling of authentication alternatives
 * 8ae78889: updates copyright
 * c331d3e3: Use FTP_PASSWORD with pexpect backend without requiring --ssh-askpass.
 * eb510e3f: fixes data size type
 * 30598ff9: fixes missing argument
 * 9187ae1e: fixes wrong environment variable being used
 * d7e67c56: adds OpenStack Swift backend
 * 29931b85: Added commentS
 * 34bc310c: Added max proc rule for multipart S3 uploads.
 * da12b172: adapt to mega.py API changes
 * f0457133: cleanup copyright notice
 * 98a57b22: adding Mega backend for mega.co.nz
 * ddc7a38e: Launchpad automatic translations update.
 * ebe88b73: Applied duplicity-ftps.patch from https://bugs.launchpad.net/duplicity/+bug/1104069 - Don't try to delete an empty file list.
 * c384c445: Applied blocksize.patch from https://bugs.launchpad.net/duplicity/+bug/897423 - New option --max-blocksize (default 2048) to allow increasing delta blocksize.
 * 90663fd9: Merged in lp:~jnoster/duplicity/dpbx-added - The application key was approved as "production" one after some changes to the code to suit the requirements of Dropbox team (the keys are now obfuscated, for instance).
 * 3e664e8f: Merged in lp:~juan-f/duplicity/progress - From time ago, there are people asking for a progress bar estimation in duplicity. There is even a script that circumvents the issue, getting info from the log so as to estimate the progress status ( https://github.com/quentin/Duplicity-progress ) but does not give enough feedback and the estimation is rather plain. - I have developed a set of heuristics that gather information from the deltas and the transfer ratios of the backend so as to forecast % of progress, estimation of remaining time and average speed, for both full and incremental backup uploads. - The current implementation works for boto backend, but to port the other backends to use this feature would be quite easy (we can discuss the details if interested). - The algorithm is activated by the --progress command line flag, and will perform a first-pass dry-run to collect evidence for all the deltas. Next it will trigger the real upload, while a thread statistically estimates the ratio of changes and compression for the data in/out, and uses these ratios to forecast time remaining and % of completion. - The progress data will be logged each 3 seconds, or the --progress-rate flag.
 * eb093938: Merged in lp:~tblue/duplicity/paramiko-fix-delete-retry - This fixes bug #1115715, which is really annoying. Basically it makes using the Paramiko backend with the default settings impossible.
 * 9e45e1d2: Actually merge in lp:~tblue/duplicity/paramiko-1.10.0 as previously reported.
 * b4dc4c23: Merged in lp:~townsend/duplicity/fix-1161599-2 - The fix in revno. 912 didn't take into account that the parameter "body" passed into request() is overloaded, so when it was NULL or of a type other than file, it would fail. This checks if "body" is of type "file" before actually seek()'ing back to the beginning of the file.
 * 08f05c3e: Merged in lp:~tblue/duplicity/paramiko-1.10.0 - This fixes bug #1156746, making the Paramiko backend compatible with Paramiko 1.10.0. It keeps compatibility with older Paramiko versions.
 * 8c377bc1: The fix in revno. 912 didn't take into account that the parameter "body" passed into request is overloaded, so when it was NULL or of a type other than file, it would fail. This checks if "body" is of type "file" before actually seek()'ing back to the beginning of the file.
 * b401bac0: Launchpad automatic translations update.
 * b855cb86: Transient socket or HTTP errors will cause a retry of the PUT for a backup. This would then lead to 400 Bad Request errors from the server. This MP:
 * c1cac33c: Launchpad automatic translations update.
 * 3da9f8be: Fixes the case where the file pointer to the backup file was not being set back to the beginning of the file when an error occurs. This causes subsequent retries to fail with 400 Bad Request errors from the server. This is due to a change in revno. 901 where a file handle is used instead of a bytearray. * Fixes the removal of Content-Length from the header in revno. 901. Content-Length is required according to the Ubuntu One API documentation.
 * 5599a6a0: no more cleartext credentials in the code
 * 1515016c: Application Key & Secret get obfuscated to fit the rq of Dropbox.
 * 35982e61: progress: Removed an unneeded if
 * 755e84b7: progress: Fixes for the previous commit after extensive testing: Fixed the index computation for the rotating cache of Snapshots - Moved the start point for the Log progress thread after a proper computation of the starting volume in case of restart, and adapted code for it
 * 1f5e6538: progress: Cover the sigtar and manifest upload with the progress reporting. Now the last 1% will be dedicated to this upload and properly report stallment when network goes off while this happens.
 * f04be11d: progress: Fixed a missing condition for when the progress flag is not used
 * 9b675891: progress: Cap data progress upload from 0..99% and show 100% only when sigtar and manifest file has uploaded correctly
 * 1d46d37e: progress: Avoid completed percentage to drops between backup retries when backup fails and has to be restarted. The current progress is offset by the previous uncompleted backup from the last volume that upload correctly. To achieve it, the progress tracker now snapshots the current progress to the cache each completed volume, then recovers this information later when retrying a failed backup.
 * 8ca1e834: crosser's patch applied
 * cc9f7011: progress: The algorithm now will drop the confidence interval adaptively when overpassing the 100%. This may happen when the sigma is large due to a very heterogeneous distribution of the size of deltas in files. In this case, the C.I. will be drop by half to adapt to the variability. If it happens again, it will disregard the sigma and trust the mean only.
 * 6cd00741: progress: Simplified computation of progress to compute an upper bound, fit to a smooth curve. This method embraces better more "change distribution" scenarios and is much simpler to compute. And also, full backups will assume 1:1 correspondence in change distribution, so progress bars during full will be computed linearly, which is closer to reality.
 * 0fcaafd3: Make the Paramiko backend work with Paramiko 1.10.0
 * 450fef93: propagate exceptions upward to facilitate retries
 * fa520f7b: Launchpad automatic translations update.
 * 2c43e47e: Typo fixed
 * ec693e6c: log.py had no Error() to supplement Info(), Warn(), and Debug() - fixed.
 * c56c5656: 1. usage note added (on separate Dropbox account). 2. extraneous and useless mkdir call was removed in put() method.
 * 3e868273: Even more logging for unhandled exceptions to catch Error connecting to "api-content.dropbox.com"
 * 8d0a387a: Traceback logging added for semi-unhandled exceptions to catch that strange .encode() call error.
 * 8f3ee3a5: Launchpad automatic translations update.
 * be2189ca: Merged in lp:~ed.so/duplicity/verify.data - add switch --compare-data, to selectively enable formerly always disabled data comparison on verify runs
 * b829133d: Merged in lp:~jnoster/duplicity/dpbx-added - Add Dropbox backend - NB! In order to use the backend one must: 1. Install Dropbox Python SDK first. 2. Run the duplicity with Dropbox backend (dpbx://) first time *interactively* to catch and follow the oAuth URL.
 * e3363344: Applied patches from Laszlo Ersek to rdiffdir to "consume a chain of sigtar files in rdiffdir delta mode" which supports incremental sigtar files.
 * a7ae62f7: renamed to --compare-data to make it reusable on other actions e.g. force data comparision on backup runs where files were modified but mtime was not set properly by buggy software
 * 985f2c01: add switch --verify-data, to selectively enable formerly always disabled data comparison on verify runs
 * 09b9cccf: note on first run was added to the man page
 * 94af862d: THE BACKEND ITSELF HAS BEEN FINALLY ADDED.
 * 4ca6f37b: man page fixed to mention dpbx: backend
 * bf76ba47: Dropbox backend (dpbx:) has been added.
 * 2c52b624: progress: Reporting speed in bps for log file
 * a0956b09: Paramiko backend, delete(): Terminate when all files have been deleted successfully.
 * 111091ce: progress: Changed verbosity to NOTICE, so progress messages appears by default when --progress flag is on
 * 04795617: progress: Added average speed to the log file
 * 91ec6c4b: progress: Fixed a typo in if clause
 * 75530d8a: progress: Bugfixed a posible division by zero
 * 8dab2b11: progress: New feature to compute progress of compress & upload files The heuristics try to infer the ratio between the amount of data collected by the deltas and the total size of the changing files. It also infers the compression and encryption ration of the raw deltas before sending them to the backend. With the inferred ratios, the heuristics estimate the percentage of completion and the time left to transfer all the (yet unknown) amount of data to send. This is a forecast based on gathered evidence.
 * 4f86a904: Launchpad automatic translations update.
 * 2fa0a5d9: Merged in lp:~duplicity-team/duplicity/po-updates - Updated translations
 * 2029bc9e: Launchpad automatic translations update.
 * 3934cf1d: Merged in lp:~mterry/duplicity/py3rsync - This branch lets one build the _librsync module with Python 3. You can't really do anything useful with it, but it's a nicely-isolated piece to add Python 3 support for. - The changes are a mix of modernization and #ifdef logic. - All tests still pass in Python 2.7 and 2.4. I tested manually that the module worked as expected in Python 3.
 * d3da045c: Merged in lp:~mterry/duplicity/pygi - Python bindings for the gobject stack (used in the gio backend) have changed from static to dynamically-generated bindings. The old static bindings are deprecated. So here's a branch to change the gio backend from old to new ones.
 * 9ce1c4fd: Merged in lp:~ed.so/duplicity/webdav.manpage - explanation of webdav changes above
 * ae1a6fd8: Merged in lp:~ed.so/duplicity/webdav.fix-retry - added ssl certificate verification (see man page) - more robust retry routine to survive ssl errors, broken pipe errors - added http redirect support
 * add46c50: make _librsync module compile under Python 3
 * 75e19be7: Use PyGI instead of older pygobject style for gio backend
 * a6001725: Launchpad automatic translations update.
 * 84f20106: move man page changes to a separate uptodate merge branch
 * a6e87fa0: webdav manpag updates
 * 3e5c8a80: Launchpad automatic translations update.
 * 767108da: Add auto-ctrl-c-test.sh to help stress-test restart support
 * 74894ff5: manpage - document ssl cert verification in man page backend.by - retry_fatal decorator accepts now premature fatal errors and supplys a retry_count instance variable webdavbackend.py - added ssl cert verification - added http redirect support - added always create new connection on retrys - much more debug output for problem pinpointing commandline.py, globals.py - added ssl cert verification switches errors.py - add FatalBackendError for signalling exactly that
 * 249c836a: Launchpad automatic translations update.
 * 5ecc26c8: Launchpad automatic translations update.
 * 2ac5020d: Merged in lp:~mterry/duplicity/static-corruption - This branch fixes three possible ways a backup could get data-corrupted. Inspired by bug 1091269. A) If resuming after a volume that ended in a one-block file, we would skip the first block of the next file. B) If resuming after a volume that ended in a multi-block file, we would skip the first block of the next file. C) If resuming after a volume that spanned a multi-block file, we would skip some data inside the file. - A and B are because when finding the right place in the source files to restart the backup, the iteration loop didn't handle None block numbers very well (which are used to indicate the end of a file). - C is what bug 1091269 talks about. This was because data block sizes would get smaller as the difftar file got closer and closer to the volsize. Standard block sizes were 64 * 1024. But say we were close to the end of the difftar... When resuming, duplicity doesn't know the custom block sizes used by the previous run, so it uses standard block sizes. And it doesn't always match up, as you can imagine. So we would leave chunks of data out of the backed up file. - Tests added for these cases. - This branch is called 'static-corruption' because all these issues occur even when the source data doesn't change. I still think there are some corruption issues when a file changes in between duplicity runs. I haven't started looking into that yet, but that's next on my list. - C only happened without encryption (because the gpg writer function already happened to force a constant data block size). A and B happened with or without encryption.
 * c6a2620e: use a copy of file1 rather than writing out a new small file so that it is clearer the first block is skipped rather than the whole file
 * 8df1f767: add test to confirm expected behavior if new files appear before we restart a backup
 * 34f19d4b: whoops, fix a test I broke with last commit because I didn't add get_read_size to the mock writer
 * e7763f3c: Fix block-loss when restarting inside a multi-block file due to block sizes being variable
 * a01444dd: Fix block-loss when restarting after a volume ends with a multi-block file; fixes test_split_after_large()
 * 5f452905: Fix block-loss when restarting after a volume ends with a small file; fixes test_split_after_small()
 * e657a1b6: Add more tests for various restart-over-volume-boundary scenarios
 * 09f64ac6: move non-encryption-specific tests to the right class
 * 132ef094: tests: add a WithoutEncryption class to restarttest.py
 * 9c9e134f: Launchpad automatic translations update.
 * 23704a6f: reconnect on errors as a precaution against ssl errors see https://bugs.launchpad.net/duplicity/+bug/709973
 * 4de510a7: Fixed 1091269 Data corruption when resuming with --no-encryption - Patches from Pascual Abellan that make block size consistent and that add no-encryption option to manual-ctrl-c-test.sh. - Modified gpg.py patch to use 64k block size so unit test passes.
 * 1587043d: Launchpad automatic translations update.
 * 7ff4a26d: Merged in lp:~ed.so/duplicity/u1_and_manpage - Manpage - document Ubuntu One required python libs - added continuous contributors and backend author notes - U1backend - lazily import non standard python libs, fixes http://article.gmane.org/gmane.comp.sysutils.backup.duplicity.general/5753 - fix "not bytearray" prevents PUT with python 2.6 - don't hang after putting in credentials (cause it silently retries in background) but go through with backup
 * 16ee96c8: python3 fix reuse normalized url from oauth
 * 3a28c754: why bother reading when we can deliver a filehandler alltogether
 * 735d9a5b: fix "not bytearray" prevents PUT with python 2.6
 * 86a24886: don't hang after putting in credentials (cause it silently retries in background) but go through with backup
 * 95ce100a: fix imports not being global
 * 4194bf61: Manpage - document Ubuntu One required libs - added continous contributors and backend author notes
 * 5828f0a0: Launchpad automatic translations update.
 * fb4fadc6: Merged in lp:~ed.so/duplicity/manpage - Clear up PASSPHRASE reusage as sign passphrase. Minor fixes.
 * ae55ce1a: Merge changes from trunk.
 * 12290278: Merged in lp:~ed.so/duplicity/webdav.fix-retry - bugfix: webdav retrying broke on ERRORS like "error: [Errno 32] Broken pipe" in socket.pyas reported here https://answers.launchpad.net/duplicity/+question/212966 added a more generalized 'retry_fatal' decorator which makes retrying backend methods even easier
 * c8cc3b59: Launchpad automatic translations update.
 * 61427a2e: Merged in lp:~carlos-abalde/duplicity/gdocs-backend-gdata-2.0.16.-upgrade - Upgrade of GoogleDocs backend to python gdata lib >= 2.0.15: Stop using get_everything method.
 * 206f75ea: Merged in lp:~mterry/duplicity/u1-utf8 - Make sure u1backend returns filenames as utf8
 * 42f34339: Merged in lp:~lenharo-h/duplicity/duplicity - Generate encrypted backups without revealing the user's key id via option --hidden-encrypt-key
 * 7bc38dd0: Merge changes from trunk.
 * ff74220d: add correct error code catch only exceptions again
 * 08f80821: catch exceptions only
 * 026e37cb: show error value instead of class
 * fd066260: bugfix: webdav retrying broke on ERRORS like "error: [Errno 32] Broken pipe" in socket.pyas reported here https://answers.launchpad.net/duplicity/+question/212966
 * 4f3e0f46: Launchpad automatic translations update.
 * a6affde5: Make sure u1backend returns filenames as utf8
 * ec5ca50e: Now files are directly uploaded to destination folder/collection. This also fixes bug that created a copy of all files in the root folder/collection in Google Drive
 * be09ab36: Added --hidden-encrypt-key testcases.
 * f03cc02d: Nuke tabs.
 * 82a4f985: Added more details in man page.
 * 6f1fe3b5: Fixed a typo in man mage.
 * 3d33dcfa: Allows duplicity to encrypt backups with hidden key ids. See --hidden-recipient in man gpg(1)
 * 8b49ea03: Launchpad automatic translations update.
 * 413c8146: avoid using TestCase.addCleanup, which isn't in older python versions
 * 3336d52f: Merged in lp:~ed.so/duplicity/lftp.netrc - Allow .netrc auth for lftp backend * Merged in lp:~mterry/duplicity/946988 - This fixes bug 946988 by not duplicating the checks for when we should ask for the password (those same checks are done more correctly inside get_passphrase). And add a test to reproduce the bug.
 * 7a6c76fc: allow .netrc auth for lftp backend
 * 942a5b07: clear up PASSPHRASE reusage as sign passphrase minor fixes
 * 10d447fc: don't duplicate a test for whether we should get passphrase in two places -- one of them will be out of sync
 * d9740efc: Launchpad automatic translations update.
 * 3d022869: Launchpad automatic translations update.
 * fad1bcd8: Merged in lp:~ed.so/duplicity/manpage - more formatting fixes, clarifications in sections EXAMPLES, FILE SELECTION
 * 021e7fc5: Merged in lp:~satwell/duplicity/caching - Add a cache for password and group lookups. This significantly improves runtime with very large password and group configurations.
 * f74455fb: Add a cache for password and group lookups. This significantly improves runtime with very large password and group configurations.
 * 094c55f4: Launchpad automatic translations update.
 * 48034079: Launchpad automatic translations update.
 * 839d7278: Merged in lp:~mterry/duplicity/u1-ascii-error - Fix for u1backend unicode error. Patch by Paul Barker.
 * f119ee19: Merged in lp:~mterry/duplicity/delete-new-sig-in-cache - In duplicity 0.6.20, we fixed bug 1031269. This means that we no longer leave sig files on the remote location. Leaving sig files on the remote location also caused a bug with deleting cache files. Code used to leave remote new-sig but delete the locale cache new-sig; this meant that we would keep downloadoing the new-sig all the time from remote. We had worked around that by just not deleting the new-sig in the cache, which was sort of the wrong side of that problem to tackle. Now that we handle the remote new-sigs better (by deleting them), I don't think we need this code anymore. Patch by az@debian.org.
 * 2be12d16: Merged in lp:~mterry/duplicity/u1-oauthlib - As the Ubuntu packager for duplicity, I would prefer u1backend.py used oauthlib instead of oauth. oauthlib is well maintained upstream (unlike oauth), has a python3 port (for the future), and is in Ubuntu main (so is oauth right now, but hopefully in the future we can drop it to universe, in which case duplicity can't use it anymore).
 * 416e663a: port u1backend to oauthlib
 * 03f2eaec: we no longer need to preserve new-sigs in the cache, since we fixed the bug keeping them on the remote side
 * ee3685fe: Fix U1 backend's ascii error. Patch by Paul Barker
 * bcf491b1: more formatting fixes, clarifications in sections EXAMPLES, FILE SELECTION
 * 02798bdf: Launchpad automatic translations update.
 * a70d8a91: Merged in lp:~ed.so/duplicity/24syntaxfix - fix python 2.4 vs 2.5 syntax error
 * 2ef5be12: fix python 2.4 vs 2.5 syntax error
 * 9e8fb03f: Launchpad automatic translations update.
 * 7b4227a9: Remove dist/mkGNUchangelog script. * Prep files for 0.6.20 release.
 * e0d07c9e: Launchpad automatic translations update.
 * 6db4f0f9: Applied patch from az for bug #1066625 u1backend + add delay between retries
 * be328f6f: Launchpad automatic translations update.
 * 6f59ceae: Merged in lp:~mterry/duplicity/u1-402 + Switch the code we check for out-of-space in u1backend.
 * 794d7ccc: u1backend: interpret http code 402 as no-space-left rather than 507
 * 3cdba9ae: Launchpad automatic translations update.
 * beccd6eb: 1039001 --exclude-if-present and --exclude-other-filesystems causes crash with inaccessible other fs
 * 91855cb4: 995851 doc improvement for --encrypt-key, --sign-key
 * 894bcebc: 1066625 ubuntu one backend does not work without gnome/dbus/x11 session
 * c924ba74: Launchpad automatic translations update.
 * 40f15e9b: Updated Changelog.GNU
 * 3ec33eac: Merged in lp:~ed.so/duplicity/ssh.manpage + added gdocs and rsync REQUIREMENTS + added cloudfiles documentation
 * 7d305b3a: Merged in lp:~ed.so/duplicity/gpginterface + refactor GnuPGInterface to gpginterface.py reasoning can be found in README
 * d5e39a0b: added gdocs, rsync REQUIREMENTS
 * 71f79a2b: some clarifications in README
 * 2e341f57: refactor GnuPGInterface to gpginterface.py reasoning can be found in README
 * 32592701: some refinements add cloudfiles documentation
 * 9bb3145d: Launchpad automatic translations update.
 * 2b30203d: Merged in lp:~ed.so/duplicity/gpg.tmp + place gpg.py tempfiles in duplicity's tmp subfolder which is cleaned whatever happens
 * bd3adb53: place gpg.py tempfiles in duplicity's tmp subfolder which is cleaned whatever happens
 * 7f192112: sort urls alphabetically add abs vs. relative file urls
 * ae60317b: typo
 * 6c3b0fe0: minor fix
 * bdfa6eab: some clarifications mostly for ssh pexpect backend
 * 9d1e75a7: Launchpad automatic translations update.
 * f7cb2688: tests: apparently on hardy chroots, /bin can be smaller than 3MB compressed, so instead of using /bin in test_multi_volume_failure, use largefiles
 * 1c658b55: tests: whoops, I had accidentally disabled one of the new tests for ignoring double entries in a tarball
 * c24c515a: tests: don't use subprocess.check_output, which was only added in Python 2.7
 * 85e0cf60: Launchpad automatic translations update.
 * 551a72c7: don't use unittest.TestCase.assertSetEqual, which isn't supported in older Python versions
 * 2908e913: Merged in lp:~ed.so/duplicity/ssh-pexpect-msgbug + Fixes 'UnboundLocalError: local variable 'msg' referenced before assignment' in _ssh_pexpect.py
 * a2a6413f: probably fix
 * b9830e76: Launchpad automatic translations update.
 * 907c5ed3: Wrap CHANGELOG to col 80.
 * e74e1cb6: Merged in lp:~mterry/duplicity/ropath.index + This branch does two main things: 1) Skips base dir entries when compiling the list of deleted delta iters. (this gracefully recovers from the sort of situations that lead to bug 929067). I'm reasonably confident this is an uninvasive change, but please confirm. 2) Overwrites the sigtar file on backup-restart. This is because AFAICT, duplicity will rewrite the entire sigtar each restart. But we were opening the sigtar file as "ab", so we'd just dump the contents on top of the previous contents. Which was causing some confusion in bug 929067. If I'm wrong that we don't always rewrite the entire sigtar each time, this needs some rethink. Please also confirm that. + In addition, I added two tests for the above two changes and make some improvements elsewhere in the restarttest.py file while I was at it.
 * f7b9925b: Merged in lp:~gregretkowski/duplicity/cf-retry-delete + This will retry cloudfile delete commands. With large numbers of archive files over mediocre links transient network errors will occasionally cause deletes to fail and these should be retried.
 * f40a2667: Merged in lp:~ed.so/duplicity/duplicity.manpage + disabled hyphenation and block justification for better readablility of command line examples. + reformatted REQUIREMENTS section for hopefully better online rendering + minor clarifications
 * 97f1d00c: Merged in lp:~mterry/duplicity/leftover-sigtar + So currently, duplicity does not delete signature files when doing a remove-all-but-n operation. Seems wrong, since those signature files are now useless and take up space. + This branch does several things: 1) Make remove-all-but-n operate on chains. In practice it did before, since the sets it operated on always came from complete chains (i.e. it never used only some of the sets from a chain) 2) Add a new method to get all signature chains before a certain time. 3) Use this new method to also delete signature chains during remove-all-but operations. + And it cleans up the cleanuptest.py file: 1) Removes crufty, unused code 2) Disallows changing the destination folder for the test, which no one would ever want to do and isn't really supported anyway 3) Add some additional checks to the existing test 4) Adds two new methods to test remove-all-but-n and remove-all-inc-of-but-n-full
 * ad6b4282: Merged in lp:~mterry/duplicity/1031277 + ssh: actually delete all the requested files, not just the first one
 * fb319b7d: gracefully handle multiple duplicate base dir entries in the sigtar; avoid writing such entries out
 * 81090bb9: Retry cloudfiles deletes
 * 26a4f829: missing space
 * 00492820: disabled hyphenation and block justification for better readablility of command line examples. - reformatted REQUIREMENTS section for hopefully better online rendering - minor clarifications
 * f1c326a9: delete signature files when doing remove-all-but
 * fd9efbbe: ssh: actually delete all the requested files, not just the first one
 * ff07e9d7: Launchpad automatic translations update.
 * d896bf7b: Merged in lp:~mterry/duplicity/utf8-po.
 * c8934d9d: make sure translations are in utf-8
 * 0bab416d: Launchpad automatic translations update.
 * 940e7526: Fix dates.
 * a7912af7: Launchpad automatic translations update.
 * 41838d05: Merged in lp:~ed.so/duplicity/duplicity.tmpspacefix
 * c2f668b6: Merged in lp:~ed.so/duplicity/duplicity.helpfix
 * a93b84d1: use tempfile.TemporaryFile() so unused temp files are deleted automagically
 * d1891e1b: propbably solve bug 'Out of space error while restoring a file' see bug tracker/mailing list https://bugs.launchpad.net/duplicity/+bug/1005901 http://lists.gnu.org/archive/html/duplicity-talk/2012-09/msg00000.html
 * baf8a76b: fix rare 'TypeError: encode() argument 1 must be string, not None' read here http://lists.nongnu.org/archive/html/duplicity-talk/2012-09/msg00016.html
 * cdf18535: Launchpad automatic translations update.
 * 2296c62a: Launchpad automatic translations update.
 * d5aef9ea: Launchpad automatic translations update.
 * 0f0c74b3: log.py: add a couple comments to reserve error codes 126 and 127 because they conflict with running duplicity under pkexec (very similar to how 255 is reserved because gksu uses it)
 * 584249cf: Add note on GnuPGInterface and multiple GPG processes.
 * 0e884144: Merged in lp:~ed.so/duplicity/backend_fixes
 * 306a3f8d: fixed ssh/gio backend import warnings + ssh paramiko backend imports paramiko lazily now + gio backend is not imported automatically but on request when --gio option is used - added a warning when --ssh-backend is used with an incorrect value
 * 36929ff3: Launchpad automatic translations update.
 * c4b97805: Merged in lp:~ed.so/duplicity/ssh-fixes
 * 1e93da6a: ssh paramiko backend respects --num-retries now - set retry delay for ssh backends to 10s - ssh pexpect backend + sftp part does not claim 'Invalid SSH password' although it's only 'Permission denied' now + sftp errors are now more talkative - gpg.py + commented assert which broke otherwise working verify run
 * 267304cd: ssh paramiko backend respects --num-retries now - set retry delay for ssh backends to 10s - ssh pexpect backend + sftp part does not claim 'Invalid SSH password' although it's only 'Permission denied' now + sftp errors are now more talkative - gpg.py + commented assert which broke otherwise working verify run
 * eb17f783: Launchpad automatic translations update.
 * aec7ae1c: A couple more warning error codes that Deja Dup is interested in noticing.
 * a7d1c2b6: If the gio backend wants to ask a question during its mount phase, it previously just aborted. This branch allows it to continue, though not to make an intelligent answer.
 * 858d6a97: add a couple more warning codes for machine consumption of warnings
 * 78a9e00f: allow answering gio mount questions (albeit naively)
 * 89cca698: Launchpad automatic translations update.
 * 82fc0722: Merged in lp:~ed.so/duplicity/0.6-readd_sshpexpect - readd ssh pexpect backend as alternative - added --ssh-backend parameter to switch between paramiko,pexpect - manpage -- update to reflect above changes -- added more backend requirements - Changelog.GNU removed double entries
 * 80856295: add missing files
 * 9c5eddbe: readd ssh pexpect backend as alternative - added --ssh-backend parameter to switch between paramiko,pexpect - manpage -- update to reflect above changes -- added more backend requirements - Changelog.GNU removed double entries
 * 2bc755d0: Merged in lp:~ed.so/duplicity/0.6-ssh_add_missinghostkey
 * 610509f4: Merged in lp:~carlos-abalde/duplicity/gdocs-backend-gdata-2.0.16.-upgrade.
 * 72566545: changelog entry
 * 8ab1103f: add missing_host_key prompt similar to ssh procedure
 * 0829a760: Fixing most basic stuff. Pending all testing
 * 35fc9f11: Launchpad automatic translations update.
 * 950387c2: Merged in lp:~ed.so/duplicity/0.6-ssh_config
 * 902cc5d4: Merged in lp:~ed.so/duplicity/0.6-webdav_fixes.
 * 8ccd8610: Merged in lp:~ed.so/duplicity/0.6-manpage
 * d47e8aea: changelog entry
 * d479a42a: added REQUIREMENTS section - restructure SYNOPSIS/ACTIONS to have commands sorted by backup lifecycle - added restore and some more hints when --time or --file-to-restore are supported - replaced scp:// with sftp:// in examples as this is the suggested protocol anyway - added an intro text to ACTIONS section - adapted --ssh-askpass description to latest functionality
 * 5beedd2d: empty listbody for enhanced webdav compatibility - bugfix: initial folder creation on backend does not result in a ResponseNotReady anymore
 * ba0df708: add ssh_config support (/etc/ssh/ssh_config + ~/.ssh/config) to paramiko sshbackend
 * 7bfb1fed: Launchpad automatic translations update.
 * 464e6c37: Launchpad automatic translations update.
 * 88a07dbd: Changes for 0.6.18.
 * f4a31994: Use correct dir name for cleanup.
 * c939cb1e: Adjust roottest.py to new test dir structure.
 * 2826b57a: Changes for 0.6.18.
 * 44e81701: Some code/import changes to make the ssh and boto backends compatible with Python 2.4.
 * 9df7aa00: Changes for 0.6.18.
 * 011602ea: Changes for 0.6.18.
 * 233c2e97: Fix for bug 931175 'duplicity crashes when PYTHONOPTIMIZE is set'
 * dc067370: Launchpad automatic translations update.
 * c478610e: Remove duplicate line.
 * 38b92c15: File /etc/motd may not exist in test environment. Use __file__ instead to point to a known plaintext source file.
 * 67881872: Remove tests for 884371. Can't test that yet.
 * 8e62b1a4: Raise log level on backend import failure so it will be visible under default conditions.
 * 3d52426d: Launchpad automatic translations update.
 * 52f54a82: Fix for bug 929465 -- UnsupportedBackendScheme: scheme not supported in url: scp://u123@u123.example.com/foo/
 * b6e2d149: Launchpad automatic translations update.
 * 6f6a7b39: Applied patch from 930727
 * af39c1a4: Launchpad automatic translations update.
 * 4d9aa767: Merged in lp:~mterry/duplicity/nopexpect
 * eca60d26: Merged in lp:~mterry/duplicity/testfixes
 * 13f0ae94: a couple small code fixes to help tests pass
 * 01218050: drop unused pexpect.py
 * b4a0d2e6: Launchpad automatic translations update.
 * 852525ea: Applied patch by Alexander Zangerl from bug 909031, "SSH-Backend: Creating dirs separately causes a permissons-problems".
 * 05dd1839: Merged in lp:~nguyenqmai/duplicity/file-prefix-option.
 * 2fde6153: Merged in lp:~mterry/duplicity/memleak
 * faaeec4d: Merged in lp:~mterry/duplicity/always-delay
 * 1c9a57fb: Merged in lp:~tobias-genannt/duplicity/nocompress
 * a0a35f36: Added patch for testing of bug 884371, 'Globbing patterns fail to include some files if prefix is "**"'
 * ab26887c: Applied patch from 916689 "multipart upload fails on python 2.7.2"
 * 1d66cbb8: Applied patch from 884638 and fixed version check to allow Python 2.5 and above.
 * 229edf66: Don't have TarFile objects cache member TarInfo objects; it takes too much space
 * 57de8e1c: change the way the file_naming regular expressions are created to support --file-prefix option
 * 34cc813f: always delay a little bit when a backend gives us errors
 * 2d7479f2: Launchpad automatic translations update.
 * 4dfe1952: changelog update - fixed comment
 * 5bb4d22f: Added option to not compress the backup, when no encryption is selected
 * 61f6ff8c: Merged in lp:~mterry/duplicity/resume-inc
 * 76cc35cc: Merged in lp:~mterry/duplicity/more-test-fixes
 * 9ce1adbc: resuming an incremental results in a 'Restarting backup, but current encryption settings do not match original settings' error because curtime is incorrectly set away from previous incremental value
 * 85f3c57e: tests: make other-filesystem check more robust against certain directories being mounts or not
 * cb7d934d: tests: use backup source that is more likely to be larger than 1M compressed
 * 004872f0: tests: add delay between backups to avoid assertion error
 * b5bb67fd: Fix extraneous '.py' that keeps import from working.
 * 7ce47940: Launchpad automatic translations update.
 * f36218bc: Launchpad automatic translations update.
 * 5f82601b: Launchpad automatic translations update.
 * 5717a5c7: Changes for 0.6.17
 * d64cf9cf: Not used.
 * 0c19ee78: Run tests using virtualenv for each.
 * 65272366: Make adjustments for the new structure. - Adjust boto requirements to be 1.6a or higher. - Cleanup install scripts.
 * 2cdf5539: Some doc changes including new requirements.
 * 71f867db: Don't assume dir location for Python.
 * d8c80f2f: Added --rsync-options flag to allow user to pass options to rsync at will.
 * e43b865b: 878964: Resuming a backup with a different password should throw an error
 * 82b669e8: Launchpad automatic translations update.
 * f08bc2fb: 411145 Misleading error message: "Invalid SSH password"
 * 6c09ea06: Launchpad automatic translations update.
 * 2b13e611: Split botobackend.py into two parts, _boto_single.py which is the older single-processing version and _boto_multi.py which is the newer multi-processing version. The default is single processing and can be overridden with --s3-use-multiprocessing.
 * 4576a545: The function add_filename was rejecting anything non-encrypted as a legit file. This fixes that problem and the bug.
 * e0ef28f2: Fix to allow debugging from pydev. The check for --pydevd must be done after command line is parsed.
 * 7ddb81ff: Launchpad automatic translations update.
 * 3f667da6: Merged in bzr merge lp:~summer-is-gone/duplicity/tz-incremental-fix.
 * f239acb4: Remove random_seed from VCS, adjust .bzrignore.
 * cf16c3a2: Remove localbackend.testing_in_progress since all it accomplished was to make the local backend test fail.
 * 0eb881a6: Merged in lp:~mterry/duplicity/ship-tests and moved a couple of things around to get manual tests working
 * aa4fb3c8: Adds --rsync-options to command line Allows uer to pass additional options to the rsync backend Commit include paragraph in man page, new global variable, and the small changes needed to the backend itself
 * abb88f85: Launchpad automatic translations update.
 * 76ababef: -- Applied patch 0616.diff from bug 881070. -- Fixed compile issues in reset_connection. -- Changed 'url' to 'parsed_url' to make consistent with backends.
 * ad45b4ae: Make tarball layout match bzr layout much more closely; ship tests in tarballs and adjust things so that they can work
 * 01c59bde: rename auto/ to tests/
 * c682a27d: undo accidental changes to run-tests and convert pathtest and rdiffdirtest (for both of which, I uncommented a failing test I didn't understand)
 * 3294254d: move some more custom scripts to manual/
 * 4f704e84: move some things around; converge on one script for running any kind of test or list of tests
 * c45b12b1: convert patchdirtest to auto; rip out its root-requiring tests and move them to roottest script; fix roottest script to work now with the new rootfiles.tar.gz, whoops
 * c36292be: convert finaltest to auto; workaround an ecryptfs bug with long filenames in the test
 * 627b92d6: drop state file random_seed from test gnupg home
 * 06408bbe: convert gpgtest to auto; add testing keys to the suite, so testers don't have to make their own; delete gpgtest2, as it didn't do anything
 * 644a3f2c: drop unused darwin tarball and util file
 * a2c84c39: convert GnuPGInterfacetest and dup_timetest to auto
 * aa460b0b: convert file_namingtest, parsedurltest, and restarttest to auto
 * 9cc476a6: convert manifesttest, selectiontest, and test_tarfile to auto
 * cfdf2c73: convert cleanuptest, dup_temptest, and misctest to auto
 * 9f8b0b0d: convert statisticstest to auto; make sure tests are run in English and in US/Central timezone
 * c018b6ea: convert statictest to auto
 * 4e1c7bc2: convert tempdirtest to auto
 * 6e8a7b29: convert logtest to auto
 * 403d23cd: convert lazytest to auto
 * e80f7737: clean up run scripts a little bit, rename testfiles.tgz to rootfiles.tgz
 * b344a140: make diffdirtest auto
 * f4522b01: make badupload auto
 * c309d70e: make collectionstest auto
 * f9353295: Changed functions working with UTC time file format from localtime() to gmtime() and timegm()
 * f249586b: Fixed time_separator global attribute usage in some tests
 * d410d331: Made proper setUp method for tests in dup_timetest.py.
 * 5bab1a01: move all manual tets into their own subdirectory
 * dd67d19f: Launchpad automatic translations update.
 * 60878a89: Launchpad automatic translations update.
 * 31263693: check that we have the right passphrase when restarting a backup
 * 41245460: Launchpad automatic translations update.
 * 47744f66: Changes for 0.6.16.
 * 01e52f1f: Changes for 0.6.16.
 * ba6c2ce0: Launchpad automatic translations update.
 * 296b2539: Merge in lp:~duplicity-team/duplicity/po-updates
 * 9cfe2b1a: Merge in lp:~duplicity-team/duplicity/po-updates
 * b9cc11d9: Remove Eclipse stuff from bzr.
 * 568191a0: Launchpad automatic translations update.
 * 5d6c8133: Launchpad automatic translations update.
 * 00ce3b98: Update .pot and add all languages to LINGUAS list file.
 * df982461: Merged in lp:~ed.so/duplicity/UnicodeDecodeError
 * 8f13b64a: some links for UnicodeDecodeError
 * eed47ab6: fix UnicodeDecodeError: 'ascii' codec can't decode byte on command usage
 * 4f78bdc5: Remove evil tab characters causing indent errors.
 * 4697a0d4: 838162 Duplicity URL Parser is not parsing IPv6 properly
 * 90b24877: 676109 Amazon S3 backend multipart upload support
 * a6d7790a: 739438 Local backend should always try renaming instead of copying
 * 04e1cd72: Merge in lp:~ed.so/duplicity/manpage
 * e9848da6: Checkpoint
 * 5ecac98e: updated --verbosity symmetric and signing
 * edfaf069: Merged in lp:~mterry/duplicity/rbNoneNone
 * e58f0d70: Merged in lp:~ross-ross-williams/duplicity/gpg-agent-fix
 * 23ae8bfc: Merged in lp:~mterry/duplicity/fix-local-backend-validation
 * 6720b9db: Merged in lp:~mterry/duplicity/partial-encryption
 * 056659af: Merged in lp:~mterry/duplicity/tarfile
 * 4d086080: make sure sig_path is a regular file before opening it
 * 6c32cbe5: Launchpad automatic translations update.
 * 77c85dc5: gpg2 will not get the passphrase from gpg-agent if --passphrase-fd is specified. Added tests to disable passphrase FD if use_agent option is true.
 * b9148167: use cached size of original upload file rather than grabbing it after put() call. Some backends invalidate the stat information after put (like local backend after a rename)
 * a57db05e: allow upgrading partial chain encryption status
 * 2ae61949: Merged lp:~duplicity-team/duplicity/check-volumes
 * 1c2e27cb: 832149: Uploads to Rackspace fail silently
 * aca786f3: Launchpad automatic translations update.
 * 0143ee7e: make query_info a little easier to use by guaranteeing a well-formated return dictionary
 * 49b06bfb: add rackspace query support
 * 33c28199: add query support to boto backend
 * db41967b: make clear the difference between sizes from errors and backends that don't support querying
 * b86ae0b7: cloudfiles: allow listing more than 10k files
 * c3e073de: Launchpad automatic translations update.
 * 22ed575b: Launchpad automatic translations update.
 * a14f8caa: add query_info support to u1 backend
 * 16f3575d: first pass at checking volume upload success
 * 69b965e7: Launchpad automatic translations update.
 * 0eacf4b1: Launchpad automatic translations update.
 * a68272f8: make tarfile.py 2.4-compatible
 * 2d3ecd0b: use python2.7's tarfile instead of whichever version comes with user's python
 * 61a5fb6b: usability enhancement: sign passphrase prompt has no second verification prompt anymore, symmetric passphrases are still verified
 * 9ade606e: Sync with master.
 * 3644890f: drop sign passphrase verification prompt
 * 6463f91e: bugfix of rev767 on using sign key duplicity claimed 'PASSPHRASE variable not set'
 * 6d0ea7c7: Launchpad automatic translations update.
 * 51fde49f: use a proper fake TarFile object when reading an empty tar
 * d28dfaaf: handle empty headers better than passing ignore_zeros -- instead handle ReadErrors
 * bdf7c1e8: remove another non-2.4-ism I introduced
 * 4518277d: and update trailing slashes in test too
 * aa5249c9: fix how trailing slashes are used to be cross-python-version compatible
 * c13cbe6d: whoops, forgot an import
 * b9512c7d: handle different versions of tarfile
 * a75a0bea: first pass at dropping tarfile
 * ea829a39: Changes for 0.6.15.
 * d51867df: fixes to unit tests to support SIGN_PASSPHRASE.
 * ca81e19c: introduce --numeric-owner parameter patch courtesy of Lukas Anzinger <l.anzinger AT gmail.com> - duplicity:restore_check_hash 'Invalid data - *** hash mismatch' lists the offending filename
 * 399bf1b0: Remove use of virtualenv.
 * 6ebd26f4: Ignore ENOENT (file missing) errors where it is safe. - Set minimum Python version to 2.4 in README.
 * aff8fc93: typo fix
 * 021da5d5: numowner & hash mismatch verbosity
 * 44ddc4a7: 824678 0.6.14 Fails to install on 8.04 LTS (Hardy)
 * 03604019: 823556 sftp errors after rev 740 change
 * 251ed9da: Launchpad automatic translations update.
 * d61acaf9: Launchpad automatic translations update.
 * 9c8f966d: Launchpad automatic translations update.
 * 12710740: Merged in lp:~carlos-abalde/duplicity/google-docs
 * 89ba0329: Merged in lp:~mterry/duplicity/u1-fixes
 * 35308c8f: Fixed indentation: 2 to 4 spaces
 * 69d11ff9: some u1 backend fixes: handle errors 507 and 503; add oops-id to message user sees so U1 folks can help
 * 8d548787: Launchpad automatic translations update.
 * 82a61514: Fetching user password correctly (i.e. not using directly self.parsed_url.password)
 * 87e9aab3: Now using backend.retry(fn) decorator to handle API retries
 * 4f36869b: Added subfolders support + several minor improvements and fixes
 * f2b70a33: Merged in lp:~ed.so/duplicity/encr-sign-key2
 * bd0ac726: Merged in lp:~ed.so/duplicity/encr-sign-key2
 * a553c12a: 818178 Shouldn't try to delete files it knows don't exist
 * 5910fc48: Merged in lp:~mterry/duplicity/retry-u1
 * 231f9137: Don't try to delete partial manifests from backends
 * 8fb9d679: Added support for captcha challenges
 * 85ed08d4: retry operations on u1 backend
 * 30246e92: Replacing get_doclist by get_everything in put & delete methods. Raisng BackendException's in constructor
 * cb405342: Replaces get_doclist by get_everything when retrieving remote list of files in backup destination folder
 * 6b558250: Added authentication instruction for accounts with 2-step verification enabled
 * 023f6d8a: A couple of assert + missing local_path.setdata on remote file get
 * 1969ff54: Better error logging + retries for each API op
 * a14c20f3: Improved upload: check duplicated file names on destination folder + better error handling
 * 4e2a42f7: Improved API error handling
 * 4f030838: Checking Google Data APIs Python libraries are present
 * ff05cb8c: Fixed URI format
 * d407b022: First usable prototype
 * 37536676: Merged lp:~mterry/duplicity/815635
 * 1a5f46f2: Merged lp:~mterry/duplicity/report-encrypted-chains
 * 10518940: Merged lp:~mterry/duplicity/more-accurate-sync
 * 1552d356: when copying metadata from remote to local archive, first copy to a temporary file then move over to archive
 * 535bf0f9: report whether a chain is encrypted or not
 * 13ae0a14: be more careful about what we try to synchronize
 * b294ff43: introduce --encrypt-sign-key parameter - duplicity-bin::get_passphrase skip passphrase asking and reuse passphrase if sign-key is also an encrypt key and a passphrase for either one is already set - add _() gettext to text in duplicity-bin::get_passphrase - document changes and minor additions in manpage
 * 0a840928: Launchpad automatic translations update.
 * 0da0e804: 703142 AssertionError: assert len(chain_list) == 2
 * 6164bdb5: 794576 Transport endpoint is not connected
 * 3d883c94: pay attention to local partials when sync'ing metadata and make sure we don't end up with three copies of a metadata file
 * cd0757c2: ignore ENOTCONN when scanning files
 * 3a0b492c: Really restore threaded_waitpid().
 * 9efc650f: Merged in lp:~mterry/duplicity/guard-tarinfo
 * 590360be: Detabify. Tabs are evil.
 * 7ddf182e: Restore previous version with threaded_waitpid().
 * 9db787bb: also guard the recursive call
 * 6138aa2c: guard tarinfo object from being None
 * d5a30d2e: Launchpad automatic translations update.
 * e764cd37: Ignore 404 errors when we try to delete a file on Ubuntu One.
 * 2c97f84a: Update to duplicity messages.
 * ff619b17: u1backend: ignore file-not-found errors on delete
 * fd68961b: Launchpad automatic translations update.
 * afbfb0f9: 777377 collection-status asking for passphrase
 * 9d1eb667: 680425 Endless retype passphrase when typo 793096 Allow to pass different passwords for --sign-key and --encrypt-key
 * c10193e0: duplicity.1: move information about the PASSPHRASE and SIGN_PASSPHRASE environment variables to the Environment Variables section - duplicity.1: add information about the limitation on using symmetric+sign to the bugs section - In the passphrase retrieval function get_passphrase, do not switch from "ask password without verifying" to ask+verify if the passphrase was empty - Allow an empty passphrase for signing key - Make clear in the verification prompt whether the encryption passphrase or the signing passphrase is being confirmed - Fix passphrase retrieval for sym+sign (duplicity-bin and gpg.py) - Allow sym+sign with limitation (see comments and manual page)
 * 6b2b7d0f: 797758 Duplicity ignores some FatalErrors
 * d9d98d1b: Checkpoint
 * 1bb63046: always catch Exceptions, not BaseExceptions
 * 0f806321: 794123 Timeout on sftp command 'ls -1'
 * 4200c69a: Checkpoint.
 * 5c7a7701: 487720 Restore fails with "Invalid data - SHA1 hash mismatch"
 * 46962d29: Fixed boolean swap made when correcting syntax.
 * 22a342c4: Fix syntax for Python 2.4 and 2.5.
 * 91bf1ab7: Fix syntax for Python 2.4 and 2.5.
 * b17b6e16: Fix CHANGELOG.
 * d1427316: 782337 sftp backend cannot create new subdirs on new backup
 * a2abe8f1: 782294 create tomporary files with sftp
 * e2614427: Merged in lp:~mterry/duplicity/retry-decorator
 * c5a0898e: Merged in lp:~mterry/duplicity/u1-status
 * 1e2f4844: Checkpoint.
 * 6be4adce: Merged in lp:~mterry/duplicity/gio-name
 * 847d1974: Merged in lp:~mterry/duplicity/levelName
 * 01937ce9: u1: allow any success status, not just 200
 * d922ce3b: move logging code up to retry decorator; fixes use of 'n' variable where it doesn't belong
 * e5cc030f: 452342 Provide Ubuntu One integration
 * 0448a683: 792704 Webdav(s) url scheme lacks port support
 * f1eef4f1: 782321 duplicity sftp backend should ignore removing a file which is not there
 * 96fde75b: 778215 ncftpls file delete fails in ftpbackend.py
 * 614fdc86: 507904 Cygwin: Full Backup fails with "IOError: [Errno 13] Permission denied"
 * 28a41495: 761688 Difference found: File X has permissions 666, expected 666
 * 335f90e6: 739438 [PATCH] Local backend should always try renaming instead of copying
 * 87ab281e: 705499 "include-filelist-stdin" not implemented on version 0.6.11
 * 06791d1a: Sync with repository.
 * c910e57b: 512628 --exclude-filelist-stdin and gpg error with/without PASSPHRASE
 * c174bbd8: 512628 --exclude-filelist-stdin and gpg error with/without PASSPHRASE
 * 8414503f: invalid function description fixed for get_passphrase in duplicity-bin - function get_passphrase in duplicity-bin accepts argument "for_signing" which indicates that a passphrase for a signing key is requested - introduces the SIGN_PASSPHRASE environment variable for passing a different passphrase to the signing key - commandline option --encrypt-secret-keyring=path introduced to set a custom location for the secret keyring used by the encryption key - manual page updated with SIGN_PASSPHRASE and --encrypt-secret-keyring - ask for a new passphrase if the passphrase confirmation failed to prevent an endless retype - improved some comments in the code - due to the difference in the handling of the signing and encryption passphrase, the passphrase is asked later in the duplicity-bin
 * dc097e65: Launchpad automatic translations update.
 * cc62b446: add retry decorator for backend functions; use it for giobackend; add retry to giobackend's list and delete operations
 * 737e5433: giobackend: use name, not display name to list files
 * dad90c9e: fix MachineFilter logic to match new level name code
 * a145c4b6: Cautiously avoid using levelname directly in log module. It can be adjusted by libraries.
 * 5d8f293d: update man page
 * c323ed1c: drop test file
 * f0122479: further fixups
 * 5cda8820: further upload work
 * e7e2dc0d: start of u1 support
 * 10b3f35a: as restoring is non-destructive by default (overideable with --force) there is no need to raie fata errors if not supported in/exclude parameters are given as parameters. see also: http://lists.gnu.org/archive/html/duplicity-talk/2011-04/msg00010.html
 * a0420422: Launchpad automatic translations update.
 * 2d690c8f: Launchpad automatic translations update.
 * e089c51d: Launchpad automatic translations update.
 * 7179fcb0: Insure Python 2.4 compatible.
 * 38f595b9: 433591 AttributeError: FileobjHooked instance has no attribute 'name'
 * 039a6b9d: Merged in lp:~ed.so/duplicity/0.6-add_sftp.
 * 6d50057b: link sftp to ssh backend, thus enabling sftp:// urls modified explanation in manpage minor changes in manpage
 * 35bbf82f: Boto has refactored too many times, so back off and just use Exception rather than searching.
 * c2b66f03: Launchpad automatic translations update.
 * 01f9bfe1: Boto moved S3ResponseError, so allow for different imports.
 * 00cac647: Launchpad automatic translations update.
 * 651853e4: Changes for 0.6.13.
 * 53e112e6: Changes for 0.6.13.
 * f0d802b4: Changes for 0.6.13.
 * 953c01c6: Check for presence of bucket before trying to create.
 * 809c0ae3: 579958 Assertion error "time not moving forward at appropriate pace"
 * c2648e3d: Add in ftpsbackend.py. Missed it.
 * 8d7ee7da: Launchpad automatic translations update.
 * 21d5a57c: 613244 silent data corruption with checkpoint/restore
 * a87841a0: Add a manual test for Ctrl-C interrupts. This could be automated, but I find that the old hairy eyeball works quite well as is.
 * 82ec82e1: Use python-virtualenv to provide a well-defined environment for testing multiple versions of Python.
 * d2a5bb39: Add (undocumented) option --pydevd to allow easier debugging when executing long chains of duplicity executions.
 * a105ab3c: Remove threaded_waitpid(). We still need GnuPGInterface because of the shift bug in the return code and the ugly mix of tabs and spaces. All has been reported to the author.
 * 451507c9: Replace 2.5 'except...as' syntax.
 * eea65596: Changes for 0.6.12.
 * 259c72dd: Various fixes for testing. All tests pass completely.
 * 3c855f6a: Add test for new ftps backend using lftp.
 * 09c4bbf6: Some FTP sites return 'total NN' in true ls fashion, so ignore line during listing of files.
 * b165d582: Fix typo on fix for 700390.
 * 2989fc0e: Miscellaneous fixes for testing.
 * 46153c18: 700390 Backup fails silently when target is full (sftp, verbosity=4)
 * 0f1f3156: 581054 Inverted "Current directory" "Previous directory" in error message
 * 16a30107: 626915 ftps support using lftp (ftpsbackend)
 * f379c38c: 629984 boto backend uses Python 2.5 conditional
 * 0247be60: 670891 Cygwin: TypeError: basis_file must be a (true) file, while restoring inremental backup
 * f1756250: 655797 symbolic link ownership not preserved
 * 672d4073: lp:~blueyed/duplicity/path-enodev-bugfix
 * 937db5fe: Merged: lp:~blueyed/duplicity/path-enodev-bugfix
 * 150e3682: 629136 sslerror: The read operation timed out with cf
 * 1b585422: 704314 Exception in log module
 * 7ce410e0: 486489 Only full backups done on webdav
 * 2aa2635d: 620163 OSError: [Errno 2] No such file or directory
 * aebe7218: Merged in lp:~mterry/duplicity/backend-log-codes3
 * d5dd60e0: Launchpad automatic translations update.
 * 3495e1da: Launchpad automatic translations update.
 * cb7670ee: use log error codes for common backend errors
 * 5956374a: 681980 Duplicity 0.6.11 aborts if RSYNC_RSH not set
 * a66e2290: Launchpad automatic translations update.
 * f957edfe: Changes for 0.6.11
 * de7d0ce7: Changes for 0.6.11
 * 4f8f7c70: 433970 Add an option to connect to S3 with regular HTTP (and not HTTPS)
 * 9b39bb7e: 631275 missing ssh on rsyncd url - rsync: Failed to exec ssh: ...
 * d8ab4052: 674506 RsyncBackend instance has no attribute 'subprocess_popen_persist'.
 * e058a66e: Merged lp:~ed.so/duplicity/survive_spaces.
 * f881139c: Merged lp:~ed.so/duplicity/sign_symmetric2.
 * 7d029f0e: Merged lp:~duplicity-team/duplicity/po-updates.
 * 1b17c2d9: 669225 sftp: Couldnt delete file: Failure only logged on level 9.
 * f1a98535: Fix CHANGELOG.
 * 3f98e562: Merged in lp:~l2g/duplicity/use-py.test
 * 3549cc95: solve bug 631275 rsync 3.0.7 persists on either rsync:// _or_ :: module notation both together and it interpretes it as a dest for rsh
 * f0b3eac6: protect rsync from possibly conflicting remote shell environment setting
 * c0b1c6b4: restored backend:subprocess_popen_* methods moved ncftpls workaround into ftpbackend introduced new backend:popen_persist_breaks setting for such workarounds enhanced backend:munge_password rsyncbackend: rsync over ssh does not ask for password (only keyauth supported)
 * ae94b42f: survive spaces in path on local copying with encryption enabled
 * bff7fbf2: allow signing of symmetric encryption
 * 1561890c: Catch "Couldn't delete file" response in sftp commands.
 * d0b822ae: 637556 os.execve should get passed program as first argument
 * 22394d6e: Launchpad automatic translations update.
 * c7b2f15d: Add --s3-unencrypted-connection (bug 433970)
 * 8c994e69: Launchpad automatic translations update.
 * 3ac4871e: Launchpad automatic translations update.
 * 3f5b00a5: Delete duplicity.spec -- autocreated.
 * 163b920b: Replace ternary operator with simple if statement. Python 2.4 does not support the ternary operator.
 * 3de4a188: Upgrade setup dependency to Python 2.4 or later.
 * 9f166f55: Launchpad automatic translations update.
 * c609fde0: Changes for 0.6.10.
 * 59acfb14: Changes for 0.6.10.
 * 93f32c2b: 612714 NameError: global name 'parsed_url' is not defined
 * 850a6714: 589495 duplicity --short-filenames crashes with TypeError
 * fa72b27a: 589495 duplicity --short-filenames crashes with TypeError
 * 82666d3d: Merged in lp:~olivierberger/+junk/dupl-542482
 * 0112a93a: merge with latest release upstream : 0.6.09
 * aa0c1db7: 613448 ftpbackend fails if target directory doesn't exist
 * e4a4ffaf: 615449 Command-line verbosity parsing crash
 * a36a145e: Man page improvements and clarification.
 * 9a70a96a: Final changes for 0.6.09.
 * 3be1b877: 582962 Diminishing performance on large files
 * 0daf13bf: Fix to warning message in sshbackend.
 * 159e582c: Launchpad automatic translations update.
 * 399d919c: Upgraded tahoebackend to new parse_url.
 * 5b6ea8cc: Merged in lp:~duplicity-team/duplicity/po-updates
 * eb3a2571: 502609 Unknown error while uploading duplicity-full-signatures
 * 11f08987: 567738 --ssh-options options passing options to ssh do not work
 * d6b34493: When using listmatch filenames are now unqouted so colons and other special characters don't cause problems.
 * aeaff30f: Added test for SpiderOak backend (it should probably just fail in most cases since the API is still very unstable).
 * 79e217f6: Add ability to retry failed commands.
 * 678e995d: Handle exceptions when listing files and display coresponding HTTP status code on HTTPError exception
 * 56270867: First version of SpiderOak DIY backend.
 * 0baa9903: Merged lp:~mterry/duplicity/backend-log-codes2
 * 77b3a3dd: support new backend-error log codes
 * 98191b74: Merge changes from 0.6-series.
 * 08cb394e: Launchpad automatic translations update.
 * b950d179: Merged in lp:~duplicity-team/duplicity/po-updates
 * 794f12de: 576564 username not url decoded in backend (at least rsync)
 * cdeeec8e: 579958 Assertion error "time not moving forward at appropriate pace"
 * b2729219: 550455 duplicity doesn't handle with large files well (change librsync.SigGenerator.sig_string to a list)
 * 25d018d2: Fix remove-older-than which would no longer work Differentiate the function name from global option name for remove_all_but_n_full
 * 3773b046: support new backend-error log codes
 * 242c4ea4: Launchpad automatic translations update.
 * e536df18: Added bits of manpage
 * 9ac1c704: Adding the remove-all-inc-of-but-n-full variant to remove_all_but_n_full() : remove only incremental sets from a backup chain selected as older than the n last full
 * bd4a2342: Adding the 2 new remove-all-but commands as global markers
 * cbb2df4d: Adding new remove-all-inc-of-but-n-full command as a variant of remove-all-but-n-full
 * 419794fd: Fix small typo in comments
 * 5dcab172: Launchpad automatic translations update.
 * fab0ddc3: Launchpad automatic translations update.
 * 363948e2: Changes for 0.6.08b
 * 97865ea5: Manually apply patch from http://bazaar.launchpad.net/~duplicity-team/duplicity/0.7-series/revision/637 which did not make it into 0.6.
 * 72b5d159: Changes for 0.6.08a
 * ba3b3c8f: Changes for 0.6.08a
 * fc4e7460: Launchpad automatic translations update.
 * fa6f1b1b: don't crash when asked to encrypt, but not passed any gpg_options. my bad
 * 3223f7a4: Changes for 0.6.08
 * 114e279b: #532051 rdiffdir attempts to reference undefined variables with some command arguments
 * 6e76c84b: #532051 rdiffdir attempts to reference undefined variables with some command arguments
 * a761afe3: #519110 Need accurate man page info on use of scp/sftp usage.
 * ffb5fbd4: #519110 Need accurate man page info on use of scp/sftp usage.
 * 3e3e374a: lp:~mterry/duplicity/use-gpg-options-0.7
 * 07b25402: Merged lp:~mterry/duplicity/use-gpg-options-0.6
 * a5a2f5ef: use global gpg options
 * 3e1b7997: use global gpg options
 * e24317a3: lp:~mterry/duplicity/fix-gpg-options-crash-0.7
 * 0c9c034f: Merged lp:~mterry/duplicity/fix-gpg-options-crash-0.6
 * 7d73f532: fix time command line handling
 * aec3661b: fix time command line handling
 * 3d424195: and handle initial, empty value for extend commandline actions
 * 2a96d0c5: and handle initial, empty value for extend commandline actions
 * da37f709: fix crash on empty gpg-options argument
 * d5ddbaa0: fix crash on empty gpg-options argument
 * fbd4fd15: Launchpad automatic translations update.
 * 5dc30955: Changes for 0.6.07.
 * 575d1bde: Merged lp:~duplicity-team/duplicity/po-updates.
 * aceca5e4: #520470 - Don't Warn when there's old backup to delete
 * 99e3fd85: #520470 - Don't Warn when there's old backup to delete
 * f5934cb3: Patch #505739 - "sslerror: The read operation timed out" with S3
 * 2a34b0ac: Patch #505739 - "sslerror: The read operation timed out" with S3
 * 4cd4be7f: Patch 522544 -- OSError: [Errno 40] Too many levels of symbolic links
 * 40dd860c: Patch 522544 -- OSError: [Errno 40] Too many levels of symbolic links
 * f562f679: Patched #497243 archive dir: cache desynchronization caused by remove*
 * 77ff7fe3: Patched #497243 archive dir: cache desynchronization caused by remove*
 * c8c1380f: Merge with trunk.
 * a02ecb2c: Merge with trunk.
 * 9a331eb0: logging: fix logging to files by opening them with default of 'a' not 'w'
 * d903ece7: logging: fix logging to files by opening them with default of 'a' not 'w'
 * 0b69ff32: Launchpad automatic translations update.
 * 7662b58c: Launchpad automatic translations update.
 * 8862988f: merge lp:~mterry/duplicity/rename
 * 48e6e707: make a comment reserving 255 as an error code (used by gksu)
 * bb1d5158: make a comment reserving 255 as an error code (used by gksu)
 * c14317bd: Patch 501093 SSHBackend doesn't handle spaces in path
 * 737472e7: Try again -- remove Eclipse/PyDev control files from bzr.
 * 7d543773: Eclipse settings should not be in bzr.
 * e6e0ae01: No longer needed.
 * 1174158d: Fix real errors found by PyLint. Remove unneeded includes. Tag spurious errors so they don't annoy.
 * 989dba60: Fix problem in put() where destination filename was not being passed properly.
 * df34a827: Merged in lp:~mterry/duplicity/rename
 * 179263fa: add --rename argument
 * 97491136: Launchpad automatic translations update.
 * 5704f6d7: merge lp:~mterry/duplicity/optparse
 * a247dadf: add back accidentally-dropped --use-scp option from commandline merge
 * 231d03b4: Launchpad automatic translations update.
 * f0803fa1: Merged in lp:~mterry/duplicity/typos
 * 3f36b9c3: Fix CHANGELOG.
 * fb5d85cf: Merged in lp:~mterry/duplicity/typos
 * 8a1f7b64: Merged in lp:~duplicity-team/duplicity/po-updates
 * 1b4f73d0: Merged in lp:~mterry/duplicity/optparse
 * 0a1574b4: Merged in lp:~mterry/duplicity/typos-0.6
 * 5fead24d: whoops, remove debug code
 * 78b16f8f: whoops, and this typo
 * 81de6b05: whoops, and this typo
 * 9d32fdfb: fix some typos found when using pydev+eclipse (backported from 0.7 line)
 * fb54df1c: fix some typos found when using pydev+eclipse
 * 771b771e: don't set xdg dirs in duplicity-bin now that globals.py is restored
 * ff04099d: use defaults from globals.py for commandline options
 * 07569e54: fix an undefined variable usage
 * 76685d9c: Launchpad automatic translations update.
 * d498c61a: fix a few typos
 * d976cb17: fix typo with log-fd support
 * 829b4369: first pass at getopt->optparse conversion
 * 40c39db8: Remove antiquated file.
 * 277ac899: Remove antiquated file.
 * 00f821ae: Remove requirement for GnuPGInterface, we have our own.
 * d86be841: Remove requirement for GnuPGInterface, we have our own.
 * 8b935943: 459511 --tempdir option doesn't override TMPDIR
 * 6cfe33fd: 459511 --tempdir option doesn't override TMPDIR
 * 682919d9: 487686 re-add scp backend and make available via command line option Option --use-scp will use scp, not sftp, for get/put operations.
 * 6c800b67: 487686 re-add scp backend and make available via command line option Option --use-scp will use scp, not sftp, for get/put operations.
 * ca207ed1: Applied patch 467391 to close connection on a 401 and retry with authentication credentials.
 * 9404f571: Applied patch 467391 to close connection on a 401 and retry with authentication credentials.
 * ba8a5481: Launchpad automatic translations update.
 * 7d816fd2: CVS no longer used, so no longer needed.
 * ac655ed0: Merged in translations.
 * 373c62e9: Merged in translations.
 * f0625381: Checkpoint.
 * c182ce95: Checkpoint.
 * ba80a7eb: Launchpad automatic translations update.
 * 05112ee6: Changes for 0.6.06
 * 02440453: lp:~duplicity-team/duplicity/po-updates
 * b679e5ed: lp:~duplicity-team/duplicity/po-updates
 * b888131f: Merge in lp:~duplicity-team/duplicity/i18n-for-0.7
 * 20449edc: Merge of lp:~mterry/duplicity/list-old-chains
 * aff29e78: Merge of lp:~mterry/duplicity/list-old-chains-0.6
 * e832876e: Launchpad automatic translations update.
 * 01c4614f: merge old-chain signature work from 0.7 branch; keep old sigs around, allow listing them, warn if a too-old listing is requested
 * 092c1514: warn if we don't have signatures for the given date period
 * 3d2e1c6e: allow deleting old signatures with cleanup --extra-clean
 * f0a52c69: don't delete signature chains for old backups; allow listing old backup chain files
 * e6fb79ac: Merged in lp:~duplicity-team/duplicity/po-updates
 * f65270fc: Merged in lp:~duplicity-team/duplicity/po-updates
 * 7f04eaf6: Launchpad automatic translations update.
 * 7717fbb2: add missing par2_utils.py to dist tarball
 * 7fb1e80d: Remove .cvsignore
 * 351fccc6: Remove unused __future__ imports.
 * ea35998a: Remove unused __future__ imports.
 * eb2f1a33: Add entry for patches from Stéphane Lesimple for par2.
 * 2e202ad0: Applied patch from Stéphane Lesimple found at: https://bugs.launchpad.net/duplicity/+bug/426282/comments/5 patch skips the par2 files when building up the sets and chains of backups
 * dda11605: Applied patch from Stéphane Lesimple found at: https://bugs.launchpad.net/duplicity/+bug/426282/comments/4 patch avoids storing all the par2 files into the local cache
 * 23fc4f67: Fixed 435975 gpg asks for password in 0.6.05, but not in 0.5.18
 * 1a81b7cd: Fixed 435975 gpg asks for password in 0.6.05, but not in 0.5.18
 * 2f2b72dd: i18nized a few error messages in duplicity.selection
 * 57c95771: More strings internationalized in asyncscheduler and commandline
 * 6b2dfcca: Launchpad automatic translations update.
 * bc22fe11: Merge with trunk.
 * fdc724d0: Merge with trunk.
 * 2beda711: Merged in lp:~duplicity-team/duplicity/po-updates
 * ce1cabad: Fix problems with unittests under Jaunty. It appears that redirection in os.system() has changed for the worse, so a workaround for now.
 * 4e2ab71d: Fix problems with unittests under Jaunty. It appears that redirection in os.system() has changed for the worse, so a workaround for now.
 * 9ad616c0: Launchpad automatic translations update.
 * 30314a08: Launchpad automatic translations update.
 * e063e18e: Adding conftest.py for py.test configuration hooks (right now just setting up temporary directories)
 * 8fd5bce4: Launchpad automatic translations update.
 * ad46d337: Use py.path to simplify a little
 * c4ebc8a2: Don't try to change dirs in cleanup_test_files for now. Actually, this file probably won't be here much longer.
 * d7c120be: Criss-cross merge. 'Scuse my mess.
 * 5eadaa71: Fix non-root-based test skipping
 * 5764f7b7: ugh, I'm the worst; add missing import
 * 17fb9938: ugh, I'm the worst; add missing import
 * 4984ecf5: add extra information to the 'hostname changed' log message, split it from the 'source dir changed' message
 * 06086034: whoops, use error code 42, not 41 -- that's for par2
 * 53b5652e: add extra information to the 'hostname changed' log message, split it from the 'source dir changed' message
 * 34ef867a: Launchpad automatic translations update.
 * 6ef2b98d: Expose test files' root directory as config.test_root
 * 68461ba7: New helper module for tests; have backendtest.py make use of it
 * 641599ca: I think these are all my own changes, not a trunk merge. Sorry for confusion.
 * ceaf01e8: trunk merge
 * 8238cb27: Launchpad automatic translations update.
 * 881ef818: Applied "426282 [PATCH] par2 creating support", corrected some coding format issues and made sure all unit tests passed.
 * 31091122: Launchpad automatic translations update.
 * 1dd476ff: Refactored. Put in py.test.skip to skip tests when tarfile can't be used.
 * 0ba0c85e: commit.py already adjusts sys.path, so anything that imports commit doesn't need to
 * f958f34b: Launchpad automatic translations update.
 * 7541fb98: Allow testing/config.py to find duplicity even when run outside testing/. Added a missing import.
 * d6f0815d: Launchpad automatic translations update.
 * 5f00aa38: Merged in lp:~mterry/duplicity/iterate-warnings
 * 09d182b6: Merged in lp:~mterry/duplicity/iterate-warnings
 * d772f22a: add some machine codes to various warnings when iterating over source files
 * 96fe3297: Merged in lp:~duplicity-team/duplicity/po-updates
 * 6b3ca9d2: Clean up testing run scripts.
 * 45885a8d: Merged in lp:~duplicity-team/duplicity/po-updates
 * eddc29cf: Clean up testing run scripts.
 * b6a11e39: 422477 [PATCH] IMAP Backend Error in delete()
 * 38cf79ed: 422477 [PATCH] IMAP Backend Error in delete()
 * b7980127: Additional Portuguese and brand-new Bulgarian translations
 * ca2444b6: merge latest 0.6
 * 063de5e9: Merged in lp:~l2g/duplicity/bug-411375
 * 1ed55efe: Merged in lp:~duplicity-team/duplicity/po-updates
 * 85547cc7: Translation of Spanish and Portuguese has begun
 * 8c22a8d1: Updated existing PO files with Rosetta translations
 * 0dfe5885: Change message "--cleanup option" to "'cleanup' command"
 * cde889ca: Merged in lp:~l2g/duplicity/flag-transl-comments which cleared up how\ntranslation comments should be passed to the translators cleanly now.
 * 3b4f36fb: Applied patches from Kasper Brand that fixed device file handling. http://lists.gnu.org/archive/html/duplicity-talk/2009-09/msg00001.html
 * b4bda3b7: When generating PO[T] files, only use code comments starting with "TRANSL:" for notes to the translators. "TRANSL:" is filtered out of the POT file with sed after it's generated.
 * a8bcaa70: Changes for 0.6.05.
 * a73ed8e8: Merged in ~l2g/duplicity/test-compat from Larry Gilbert which made the testing compatible across more systems. Also fixed the remaining collectionstest bug which was trying to test with no cache present.
 * 65b608b3: Test separate filesystems using /dev instead of /proc (more widely used)
 * 678a16cb: dd on Darwin (and FreeBSD?) doesn't like e.g. "bs=1K", so changed it to "bs=1024"
 * dcc9db4c: "cp -pR" seems to be a better analogue to "cp -a". This may not be perfect but it won't hang on a fifo copy like "cp -pr".
 * 347d2c5e: Got test_get_extraneous working in collectionstests.py

rel.1.2.3 / 2023-05-09
======================

 * 2437da04:chg: Fix tools release-prep & makechangelog.
 * 3ef92b09:chg: Fix tools/release-prep.
 * 6bed4876:fix: Use cryptography == 3.4.8.
 * 5aca6d29:new: Xorriso backend for optical media
 * de39e34c:fix: Warn rather than fail on op-not-supported restore errors
 * 2d83b920:fix: Fixes #701 - unable to resume full backup to B2.
 * 220a5c6f:chg: Fix spelling errors.
 * 6cb82cf5:fix: Fixes #698 - backups without GPG decryption key.
 * 5dc39789:fix: Fixes #698 - backups without GPG decryption key.
 * 01359578:chg: Cleanup. Add 'unsquashfs -l' test from @ede.
 * 6e3af59b:fix: Fixes #686 - PCA backend does not unseal volumes.
 * 1d5ff95b:fix: Revert to medieval string formatting.
 * dfcc1611:fix: Revert to medieval string formatting.
 * 6ad573bb:fix: Revert to medieval string formatting.
 * 308b4053:fix: Revert to medieval string formatting.
 * 3e8dd7d6:fix: Remove dependency scanner.
 * 1db7652c:fix: Fix PEP8 and todo issues.
 * 395553ee:fix: Misc fixes to testing/build environ.
 * dcd29f0c:fix: Encoding errors when logging. Fixes #693.
 * cf2e2093:fix: Onedrive may hang indefinitely. Fixes #695.
 * 305aa82d:chg: Update Makefile 'make clean' list.
 * cd6d2b96:chg: fix run website ci call after pushes/releases
 * 4af6f3ea: fix typo
 * d823ae7e: try to fix
 * f9a155cc:new: Onedrive for Business Support
 * 1811956b:chg: Update version for Launchpad.

rel.1.2.2 / 2023-01-26
======================

 * 545fda03:chg: Update duplicity.pot.
 * e011b550:fix: Fix to work with b2sdk 1.19.0
 * ddacbf93:fix: Fix #692. Redundant --encrypt option added in gpg.py.
 * 72a373af:fix: Regression on issue #147, change password for incremental.
 * 00ef3807: Merge remote-tracking branch 'origin/main'
 * e11ccfc1:fix: Crash if a socket is listed with --files-from. Fixes #689.
 * 9acfb505: add detailed step-by-step instructions
 * 17a7c1d0:chg: More changes to get release process working.

rel.1.2.1 / 2022-12-02
======================

 * 0a3617a5: Merge remote-tracking branch 'origin/main'
 * d7b9a522:chg: Fix for setuptools changes. Add testing data files to mix.

rel.1.2.0 / 2022-12-01
======================

 * c082b722:chg: Update duplicity.pot.
 * 0d7b7422:fix: Fix for issue #683.
 * a4820c80:chg: Remove gpg_error_codes.py / update duplicity.pot.
 * 767322fc:chg: Fix name in .gitlab-ci.yml.
 * fda4ad84:chg: Go back to standard tests, no master image.
 * 9dfe8f8e:chg: Go back to standard tests, no master image.
 * 9153c5f8:chg: Go back to standard tests, no master image.
 * df06df9e:chg: Go back to standard tests, no master image.
 * 244100a1:chg: Go back to standard tests, no master image.
 * e81f8d96:chg: Go back to standard tests, no master image.
 * 198e2e42:chg: Add testing for Python 3.11.
 * bc158f7d:new: Add rsync style --files-from=FILE. Fixes #151.
 * f692aa03:chg: Update deprecation messages. Cleanup.
 * 76f92788:chg: Reformat / cleanup Makefile.
 * 102271fc:chg: Fixup help entries in Makefile.
 * e5feb6a1:chg: Remove targets xlate-*. Add target pot.
 * 55163f1e:chg: Change Crowdin commit message.
 * dc432294:fix: Azure Blob Storage backend fails to resume. Fixes #149.
 * 456e04d8:fix: Went to aggressive on cleanup().
 * 3de878f3:chg: Update po/duplicity.pot.
 * 9a8fc346:chg: Cleanup and make sure setup cleans po dir.
 * 9c508e46:chg: fix version, oversight in previious commit
 * 2c487cbe:chg: fix snap build for non-amd64 archs
 * f9a9d894:chg: Add filter mode to log line. #138
 * 91b237cb:chg: Fix emacs mode line.
 * a1034c89:fix: Fix about 20 pep8 issues.
 * b46fc2fc:new: Add literal include/excludes. Fixes #138.
 * 1ecdce37:fix: More fixes to po/update-po.
 * 98420557:fix: Fix po/update-pot to leave po/LINGUAS in po.
 * c93a1e2a:fix: Nuke LP translations.

rel.1.0.1 / 2022-10-03
======================

 * b49f1360:fix: Revert changes to gpg_failed().
 * 6647ee7c:chg: Various cleanups to code and tests.
 * 6b0782b4: Merge remote-tracking branch 'origin/main'
 * 35531fe4:chg: Accept all .po files for LINGUAS gen.
 * a7e097d0:chg: Build control files for update-pot.
 * 99ce4986: Update Crowdin configuration file
 * ded1dcb2:chg: Accept all .po files for update-pot.
 * 3af2de3d:chg: Build control files for update-pot.
 * 93e961a7: Update Crowdin configuration file
 * 05f45f6b: Update Crowdin configuration file
 * 5d8e9dcd: Update Crowdin configuration file
 * a357124c:chg: Add tags to commit message.

rel.1.0.0 / 2022-09-23
======================

 * ae903f71:chg: Update README-SNAP.md to show options.
 * 6d52f4c5:chg: Add instructions for building snaps.
 * 34979fef:fix: Replace pydrive with pydrive2. Fixes #62
 * 3ff04c94:chg: add missing license metadata
 * 471ebbcb:chg: More docker cleanup.
 * 8dd26af7:chg: trigger website rebuild on pushes/tags
 * 491b13fa:chg: More docker cleanup.
 * 1fb1c457:chg: More docker cleanup.
 * 63c498b6:chg: Optimize build of duplicity_test image.
 * 409d4506:fix: GDrive backend: Add environment args for configuring oauth flow
 * 3a7ef19f:fix: GDrive backend: For Google OAuth, switch to loopback flow
 * 8fe456d7:fix: Reduce number of GPG file descriptors, add GPG translatable errors
 * 78af1f8f: Merge remote-tracking branch 'alpha/main'
 * 43f5f524: Merge remote-tracking branch 'origin/main'
 * c8c114cd: Merge remote-tracking branch 'alpha/main'
 * fbdb3fdd:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * bf9241da:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * 57707d2b:chg: Fold requirements.dev into requirements.txt. Del requirements.dev.
 * 1f304715:fix: Remove sign-build step. Does not work.
 * 9e0f6126:fix: Add back overzealous removal of 'import re'.
 * 91fa0e6e: Merge remote-tracking branch 'origin/main'
 * a27f73a2: Merge branch 'main' of gitlab.com:AlphaPrime/duplicity
 * 03329645: Merge remote-tracking branch 'origin/main'
 * a7d2c2a6:fix: webdav listing failed on responses with namespace 'ns0'
 * 68a84d19:chg: Action and Audience must be lowercased.
 * 1334c25d: Merge branch 'main' of gitlab.com:duplicity/duplicity
 * ec539183:chg: New os_options for SWIFT backend.
 * d72bb66e: Merge branch 'main' of gitlab.com:duplicity/duplicity
 * c8a9cfdb:fix: Fix build of apsw/sqlite3 bundle. Don't store apsw in repo.
 * 8e878459:chg: Change from master to main branch naming.
 * 9f2f1cfe:chg: Better defaults for S3 mac procs and chunk sizing
 * 2ff7159c:chg: --s3_multipart_max_procs applies to BOTO3 backend also
 * 89e6e1e3:fix: Make sure that FileChunkIO#name is a string, not a bytes-like object.
 * 54f8e1b4:fix: Fix possible memory leaks. Fixes #128. Fixes #129.
 * 5e98cb12:chg: Fix modeline, change utf8 to utf-8 to make emacs happy.
 * 5e71cce7:chg: Replace pexpect.run with subprocess_popen in par2backend.
 * a08b291c:fix: Additional fixes/checks for pexpect version. Fixes #125.
 * 39b32d6c:fix: Fixes #125. Add use_poll=True to pexpect.run in par2backend.
 * 01fa2d3a:fix: Fix issue #78 - Retry on SHA1 mismatch.
 * 7e35d748:chg: Add py310 to list of versions supported.
 * 37cfe5c4:chg: Fix script pushsnap to handle errors.
 * 6e57d2ac:chg: Add returncode to BackendException for rclonebackend.
 * 23468839:chg: snap use core20 coreutils if none in PATH env var
 * 6d2d80d8:chg: Need to install python3 for pages.
 * afc0b287: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * a7fc617b:chg: Don't push to savannah any more.
 * 7756a6e8:chg: Fix version for builds.
 * d52ad37e:fix: Install requirements.dev.

rel.0.8.23.3 / 2022-05-15
=========================

 * a011b94e:chg: Fix PEP8 issue.
 * 9245c1f5:fix: Fix LP bug #1970124 - obscure error message.
 * 0e70ed16:new: Add --webdav-headers to webdavbackend. Fixes #94
 * e56b667e:chg: Remove build on merge request and unused variables.
 * 18381850: pkg:fix: make extra sure correct python binary is used
 * 2d12276f:chg: Cosmetic changes only.
 * 7cc73769:chg: Make pages manual deploy.
 * 9aa44f42: Merge remote-tracking branch 'origin/clean-dist'
 * 12e8ac1b:chg: Changelog removed, remove needs.
 * 653585da:chg: Only build pip and snap, don't push.
 * 37dcb310:new: Add tests for Python 3.10.
 * dd599682:chg: Remove deploy jobs needing secret keys.
 * 22d14619:chg: Fix misspelled stage name.
 * 76d245b2:chg: fix deps format.
 * d9aa0b12:chg: fix deps format.
 * 615bdece:chg: Add requirements.dev to tox.ini.
 * 9806fb8c:chg: Include pydevd in requirements.txt.
 * 6a7d5e95:chg: Go back to ubuntudesktop/gnome-3-38-2004.
 * ac9b4c34:chg: Add tools dir to changes list in deploy-template.
 * 896215f7:chg: Try snap with utuntu:20.04. Fix artifacts loc.
 * 2f9a2bc4:chg: Some debugging statements.
 * cbc8aebd:chg: Some debugging statements.
 * 485bfd05:chg: Set up the SSH key and the known_hosts file.
 * 3a925989:chg: Set up config for git.
 * 0cc9f301:chg: Clone repo so setuptools-scm works properly.
 * 0a5c6606:chg: Move setuptools* to .dev. Nuke report.xml artifact.
 * 8f6a7251:chg: Add some more requirements.
 * b87e4c6f:chg: Install git and intltool for changelog.
 * e51415c5:chg: Add changes: to deploy-template.
 * 49c237ff:chg: Fix syntax.
 * 828cdd18:chg: Minimize CI/CD overhead.
 * b6f013c5:chg: Split requirements into .txt and .dev.
 * 11b2654d:chg: Standardize startup sequence.
 * 20580972:chg: Do not supply user/password to twine, just access token.
 * 9184d7f9:chg: Do not supply user/password to twine, just access token.
 * 0fe19035:new: Make sdist only provide necessary items for build.
 * 18188734:chg: Add default never to .test-template.
 * 6b725113:chg: Change PYPI_ACCESS_TOKEN back to variable and just echo it.
 * 02da3787:chg: Just cp PYPI_ACCESS_TOKEN to ~/.pypirc
 * 3f44b793:chg: Fix usage of PYPI_ACCESS_TOKEN.
 * 965fd066:chg: fix conflicts
 * ff7a2c0c:chg: Set to run deploy only after a push event.
 * 9c58e0ba: Optimize CI/CD to only run when needed
 * d864027a:chg: Whoops, can't run deploy on source branch to merge.
 * a4a87d35:chg: Use rules in templates. Always run on merge requests.
 * 67d1383f:chg: Always run pipeline on merge request event.
 * 7e101fdb:chg: Make sure we run all during merge requests.
 * 57252583:chg: Add deploy-template to only run when source changes.
 * 22e4ee09:chg: Fix to only run tests if source code changes.
 * 3b4d7aff:chg: If no changes, exit 0 to allow pip and snap builds.
 * 6374e6a2:chg: Set up pypi access token for uploading.
 * 017ceb98:new: Add changelog to deploy stage to build CHANGELOG.md.
 * 31247471:chg: keep pip build artifacts for 30 days as pipeline artifacts
 * 8a0f4d32: Merge remote-tracking branch 'origin/rclone_options'
 * 10151728: Merge branch 'duplicity-core20' of git@gitlab.com:duplicity/duplicity.git into duplicity-core20
 * 312dbf78:chg: Skip tests, not ci, so we can build snaps, pips, pages, etc.
 * c746f9e9:chg: Allow non-Docker environs to sign snaps.
 * fc2cf7ad:chg: Allow GitLab CI to upload snaps to the store.
 * bae3ade6:chg: Update or add copyright and some cosmetic changes.
 * f93128e0:new: enable CI snapcraft amd64 builds with docker
 * cd2e65b7:chg: Remove install of snapcraft, snap, snapd.
 * 21e018b4:chg: Add grpcio-tools to top to get latest version.
 * 8967e4e4:chg: Remove conflicting build env variable. Nuke evil tabs.
 * 5ec6355a:chg: Allow duplicity-core20 to run deploy steps, for now.
 * 41abbf34:chg: Install snapcraft snap snapd.
 * 98412f92:fix: Nuke a couple of false pylint errors, use inline disable.
 * b067a864:fix: Nuke a couple of false pylint errors, fix spelling.
 * c1b537d6:chg: Allow pip and snap builds from branches for now.
 * e994c158:chg: Add build_snap and build_pip back.
 * 0cfae837:fix: Nuke a couple of false pylint errors.
 * 31f3dcdc: Merge remote-tracking branch 'origin/master' into duplicity-core20
 * cad2280f:chg: More tests for tools/testsnap
 * 4dacc383:chg: More snapcraft.yaml fixups.
 * 5dd3e9ba:new: fix other archs, expose rdiffdir
 * b39d4c30:fix: minor formatting fix
 * f9c7f27b:fix: fixup some minor formatting issues
 * 74d4cf44:new: demote boto backend to legacy ...
 * e5e43680:new: promote boto3 backend to default s3:// backend ...
 * 5644d9c6:chg: Add further checks to testing for backup and multi-lib.
 * a64bf5d7:chg: Remove SNAPCRAFT_PYTHON_INTERPRETER per edso, no change on U20.
 * a032ac2d:chg: Try to force Python 3.8 only.
 * 22429e6f:chg: More detailed error message.
 * 878c6f08: Merge branch 'duplicity-core20' into 'master'
 * a1e3fbbf: upgrade to base core20
 * 5c869121:chg: Divide makesnap into makesnap, testsnap, and pushsnap.
 * a41b64db: Merge branch 'website_links' into 'master'
 * 9e922c43:chg: Revert to core18. core20 is still unusable.
 * 599e4d02: switch website to gitlab.io, promote duplicity.us
 * 1469f870: fix website link

rel.0.8.22 / 2022-03-04
=======================

 * 78a97566:fix: Add --no-files-changed option. Fixes issue #110.
 * 696af30f:chg: Changes to run on Focal with core20.
 * acd9cd53:chg: Use multiple -m options on commit to split comment.
 * 0ab4f353:chg: Remove build-pip and build-snap. Build locally for now.
 * a3ffd0f1:chg: Remove build-pip and build-snap. Build locally for now.
 * 617bdd66:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 268b60b7:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 39f5bd28:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 841b3322:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 0c083f3e:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * 55c1426e:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * c0f59944: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 88bacdb1:chg: Swap over to image 'cibuilds/snapcraft:core20`.
 * a65b7c50:chg: Remove sudo.
 * 26d5e59a:chg: core20 usess py38, not py36.
 * 525c91cc: Revert "chg:dev:core20 usess py38, not py36."
 * 05eda582:chg: core20 usess py38, not py36.
 * 4a92c512:chg: Attempt core20 again.
 * 6c392d3f:chg: Fix syntax.
 * dd98873c:chg: Remove unneeded Dockerfiles. Rename.
 * 1083e28a:chg: Try remote snap build.
 * 45ae382b:chg: Remove unneeded Dockerfiles. Rename.
 * 743098ad:chg: Cosmetic fixes.
 * b1fb6f5d:chg: Try forcing snaps to use python3.6 in 18.04.
 * 56647f11:chg: Add check for correct platform.
 * 9a781a82:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 88694bf2:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 2c580dc9:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 35d97470:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 7b164b74:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * b10d6aa2:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * f526c381:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 5983a938:chg: Use snapcraft snap instead of deb. See LP bug 1948597.
 * 45efab30:chg: Add warning for replicate command. See issue #98.
 * b5e969eb: Merge branch 'filecoin-backend' into 'master'
 * 5cc5243c: Slate Backend
 * 10cdf659:fix: Fix use of sorted() builtin (does not sort in place).
 * 10b26bd7:chg: Minor tweaks.
 * bcf8ba0b:chg: Add wheels to .gitignore.
 * d59b24dd:chg: Cosmetic changes.
 * 956f590a:chg: Add collection-status at end of test.
 * fe0df600:fix: Revert snapcraft.yaml to build on core18. core20 was flakey.
 * 8828726a:fix: Fix #107 - TypeError in restart_position_iterator.
 * 050e61e6:fix: Need to pass kwargs to BaseIdentitu.
 * 5e05e41e:fix: Fix __init__ in hubic.py. Fixes #106.
 * 73c27c75:fix: Try building snap on core20.
 * b750a051:fix: Try building snap on core20.
 * 5b61f768:fix: Somehow missed boto when doing #102. Now supported.
 * b3735ed3:new: Add --use-glacier-ir option for instant retrieval. Fixes #102.
 * c127ac3c:new: Add manual test for issue 100.
 * 17726042:chg: Remove gpg socket files during clean.
 * 0f19b9c4:new: Add option --show-changes-in-set <index> to collection-status.
 * b8bb7c74:chg: Back off to default image.
 * cbeb050e:chg: Try adding apt-get upgrade.
 * 9a7c9a04:chg: Add .test-template to allow skipping qual and tests.
 * 1807e383:chg: Try build with apt-get update
 * 5b49b202:chg: Try building snap on 20.04.
 * d92d97b7: Merge branch 'mr-origin-75'
 * 9354a3a9:fix: Fix logic of skipIf test.
 * 27a7be8b:chg: More changes to xlate-* for LP translations.
 * dbcd107e: Skip tests for ppc64le also
 * 95a9a97a:chg: Add targets to manually import/export translations.
 * b9eb3065:chg: Update duplicity.pot for LP translation.
 * 0344757e:chg: Ignore 'LP translations' commits.
 * 7299b9a3: chg:pks:Revert commit of LP translations.
 * a6057fa8: Revert "chg:pkg:Import LP translations."
 * b86986e6:chg: Import LP translations.
 * 96aac6ba:fix: Fix data_files AUTHORS to CONTRIBUTING.md.
 * 4e2687e7:chg: Revert "Put out first 'post' release to fix pypi issue".
 * 5a475484:chg: Put out first 'post' release to fix pypi issue.
 * c817367b:chg: Rename AUTHORS to CONTRIBUTING.md.
 * 31ec7fcb:chg: Rename dist dir to tools to avoid collision with setuptools.

rel.0.8.21 / 2021-11-09
=======================

 * 09fb2258:new: Add release-prep.sh for release preparation.
 * 473cad82:new: Add py310 to envlist to test against python 3.10.
 * 7b8a4fb7:chg: When buiilding for amd64 build snap locally, else remote.
 * b47f8927:fix: Fix #93 - dupliicity wants private encryption key.
 * a474913d:fix: PAR2 backend failes to create par2 file with spaces in name.
 * 44bf6591:fix: Fix bug 930151 - Restore symlink changes target attributes (2)
 * b581ed55:fix: Fix LP bug 930151 - Restore a symlink changes target attributes
 * 36bc6f31:fix: Fix #89 part 2 - handle small input files where par2 fails.
 * 18da3c90:fix: Fix PEP8 issue.
 * 2b2f3844:fix: Fix #90 - rclone backend fails with spaces in pathnames.
 * aeb5fef4:fix: Fix #89 - Add PAR2 number volumes option.
 * 6758c85c:fix: Fix #88 - Add PAR2 creation failure error message.
 * 23ef057a:fix: Fix bug #87, Restore fails and stops on corrupted backup volume
 * 41e1f655:fix: Fix bug #86, PAR2 backend fails on restore, with patch supplied.
 * f9b5d595:fix: Fixed Catch-22 in pyrax_identity.hubic. Debian bug #996577
 * c226afd2:chg: Fix command line warning messages.
 * cdc9b322:chg: Fix clean command to include module doc .rst files.
 * 5dbaa300:chg: Forgot to add myst-parser. Comment out tests for now.
 * 9374a3e2: new:Add update of API docs to deploy step.
 * c4be773d: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * a1739d2e: Merge branch 'issue73' into 'master'
 * a696cbec: resolve os option key naming mismatch
 * a5c334ee: Merge branch 'master' into 'master'
 * 94660bc3: Set up gdrive client credentials scope correctly
 * 2b89e026: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * 722adba5: Merge branch 'y0va-master-patch-75623' into 'master'
 * 1740a378: Merge branch 'issue85' into 'master'
 * d68942c8: upgrade docker test environment
 * 5d4c5405: don't query for filesize.
 * 0df160ac: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 091b30d0: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * d2d44259: Merge branch 'mr4' into 'master'
 * df28b403: Fix TypeError.
 * 1cc44caa:chg: Whoops, left out import sys.
 * 9c947315:chg: Skip test to allow py27 and py35 to pass.
 * 1d4423d0:fix: Fix issue #81 - Assertion fail when par2 prefix forgotten.
 * 327889cb:chg: Some tweaks to run cleaner.
 * 72d8d13b:fix: Fix issue #79 - Multibackend degradation.
 * 90568faa:fix: Add verbose exception on progress file failure.
 * 9919a815: Merge branch 'mr3' into 'master'
 * ed20f75d: Merge branch 'mr2' into 'master'
 * fe258ed8: Merge branch 'mr1' into 'master'
 * 4dadba9f: SSHPExpectBackend: Implement _delete_list method.
 * b96ed08e: MultiBackend: Don't log username and password.
 * 732c3021: Fix NameError.
 * ffb460f9:chg: Fix typo in test selection.
 * 4a11e7f3: Merge branch 'onedrive-token-take2' into 'master'
 * 7b3bc248: onedrive: Support using an external client id / refresh token
 * 71fe723f: Merge branch 'fix-tmdir' into 'master'
 * 93de75a8: Merge branch 'date' into 'master'
 * 5c229a9b: fix functional tests when _runtestdir is not /tmp
 * db811f66: Allow to override manpage date with SOURCE_DATE_EPOCH
 * 06d26725: Merge branch 'origin/merge-requests/61'
 * b3fe383b:chg: Remove redundant call to pre_process_download_batch.
 * a61c9c62:chg: Fix mismatch between pre_process_download[_batch] calls.
 * 822e42ba: Improved management of volumes unsealing for PCA backend For PCA backend, unseal all volumes at once when restoring them instead of unsealing once at a time. Use pre_process_download method already available in dup_main. Need to implement it on BackendWrapper and Multibackend as well.

rel.0.8.20 / 2021-06-26
=======================

 * d52fd888: Remove backup file.
 * 5387dc5c: Don't skip CI
 * 544410d9: Merge branch 'master' into 'master'
 * 4a5259c4: Add support for new b2sdk V2 API
 * df8d93fe:chg: build_ext now builds inplace for development ease.
 * d54b0083:chg: Remove lockfile to avoid user confusion.
 * a2402806:fix: Release lockfile only once.
 * b840f28f:fix: Release lockfile only once.
 * 49a56fdf: Merge branch 'master' into 'master'
 * ff191987:chg: Fix Support DynamicLargeObjects inside swift backend
 * 97a25712: Merge branch 'issue#68' into 'master'
 * 3b348c6c: have duplicity retry validate_block so object storage can report correct size
 * f0ff1dfe:chg: Fix makechangelog to output actual problems.
 * 68c1d6ef: Merge branch 'master' into 'master'
 * 7a59b038: Replace b2sdk private API references in b2backend with public API
 * 9350ca36:chg: Add dependency scanning.
 * 891c51c1:chg: Make sure changelog is only change to commit.
 * 0e9e3d34:chg: Fix indentation.
 * 6b56b36d:fix: Support -o{Global,User}KnownHostsFile in --ssh-options
 * 5d066a07:fix: Add pydrive2 to requirements.txt.
 * 9e6404c3:chg: Add support for --s3-multipart-chunk-size, default 25MB
 * b6687771:chg: Add interruptable:true as default.
 * 80838f44:chg: Fix snapcraft commands.
 * d45a47b0:chg: Fix snaplogin file use.
 * 55d5177d:chg: Add deployment for pip and snap builds.
 * b7cde699:chg: Add build_pip job.
 * 32190327: Merge branch 'master' into 'master'
 * 718ccc90: Update b2 backend to use *public* b2sdk API.
 * ae75c303:chg: Fix PEP8 issue.
 * 50d9748f: Merge branch 'bullfrogalj/duplicity-master'
 * 395f5098: b2sdk 1.8.0 refactored minimum_part_size to recommended_part_size (the value used stays the same)
 * 4931ce25:chg: More cleanup for snap builds.
 * 65cac1ac:chg: Move arch selection to dist/makesnap.
 * 4c821645:chg: Try snap build on all architectures.
 * dc2999c3:chg: Build for i386, amd64, armhf.
 * bed245e3:chg: Move to remote build of armfh and amd64.
 * 106dddcd:chg: Attempt remote build of armfh
 * 4791d1c1:fix: Fix error message on gdrivebackend.
 * b7232093:chg: More cleanup on requirements.
 * 22ac3476:chg: megatools no longer supports py35.
 * 489bf845:chg: Get more stuff from pypi than repo. Some cleanup.
 * e444c0b2:chg: Fix spaces before inline comments.
 * bfc795e2:chg: Enable access-member-before-definition in pylintrc.
 * 30b25ff5:chg: Fix indentation.
 * e8d676a5:fix: Fix issue #57 SSH backends - IndexError: list index out of range
 * 5f5a1254:chg: Module gdata still does not work on py3.
 * 04181977:chg: Tweak requirements for gdrivebackend. Cosmetic changes.
 * aab7a8dd: Merge branch 'PR-backend-gdrive-mydrive' into 'master'
 * 9828a9e4: added Google MyDrive support updated man pages and --help text

rel.0.8.19 / 2021-04-29
=======================

 * 8cd1f698:chg: Display merge comments. Better formatting.
 * 8877fe30: Merge branch 'develop' into 'master'
 * b96715f0: Fix "Giving up after 5 attempts. timeout: The read operation timed out"
 * 09c77c3b: Merge branch 'master' into 'master'
 * 83c71c60:chg: Clean up readability. Minor changes.
 * c1d7aad7:fix: gdata module passes on py27 only.
 * 64fa23a5:fix: Restore pylintrc, add requirement
 * 45c51c94:fix: Fix unadorned string in restored pylint test.
 * 656f75f9:fix: Restored pylint test. Fixed one issue found.
 * d0bd7cde:fix: More py27 packages bit the dust.
 * 89b8328a: Merge branch 'fix-uexec-returns-None' into 'master'
 * 2a57495e: fix util.uexc: do not return None
 * 5dcad5dd:fix: util.uexec() will return u'' if no err msg in e.args.
 * dc7a3794:fix: util.uexec() should check for e==None on entry.
 * dd9dd567:fix: Mark skip those not usable on py27. Fix version.
 * 5fdc15be:fix: Uncomment backends. Mark skip those not usable on py27.
 * aa001e6a: Merge branch 'boxbackend' into 'master'
 * 057d2244: Implement Box backend
 * 5396ccb0: Merge branch 'megav3' into 'master'
 * 31ab3d81: Implement megav3 backend to to cater for change in MEGACmd
 * e9648cda:fix: Lock in some module versions to last supporting py27.
 * d913ce48: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * 53a9cc8d:fix: Allow py27 to fail CI. Restrict mock pkg to 3.05.
 * 2d7bbe53: Merge branch 'use-new-azure-python-packages' into 'master'
 * acb838f4: fix documentation for azure backend
 * ebe5233d: Merge branch 'master' into 'master'
 * a88cb5a9: Fix typo
 * 51ae6f35: Merge branch 'master' into 'master'
 * 4fd3edad: Add IDrive backend
 * 87d2684b: Merge branch 'master' into 'master'
 * bdf0b648: Progress bar improvements
 * 7340e625: fix;usr:Fixes bug #1652953 - seek(0) on /dev/stdin crashes
 * 0a562b65:fix: Fix bug #1547458 - more consistent passphrase prompt
 * 9d8a9b45:fix: Fixes bug #1454136 - SX backend issues
 * fc5f6ec1:fix: Fixes bug 1918981 - option to skip trash on delete on mediafire
 * 99b04d59:fix: Fix bug 1919017 - MultiBackend reports failure on file deletion
 * b2d93ee0: Don't sync when removing old backups
 * 965e2753:new: Merge branch 'google-drive-v3' into 'master'
 * 9c63d987: Add a new Google Drive backend (gdrive:)
 * 9b0bde34:fix: Recomment, py2 does not support all backends.
 * 4289933d:fix: Add azure-storage module requirement. Uncomment all.
 * c93bd167:chg: Cosmetic chnges.
 * c97b40b9: Merge branch 'azurev12' into 'master'
 * 1a3441f3: Replaced original azure implementation
 * 386be5e5: Revert "fix:pkg:Remove requirement for python3-pytest-runner. Not used."
 * 90e7e2ac:fix: Remove requirement for python3-pytest-runner. Not used.
 * 80b0c6cb: Fixed code smells
 * 8abe2a85: Azure v12 support
 * 7d20de03:fix: Install older version of pip before py35 deprecation.
 * 035d8200:fix: Add py27 and py35 back to CI.
 * 266a4926:fix: Fix setup.py to handle Python 2 properly.
 * cd138801:chg: Make testing/manual/bug1893481 into a tarball, not directory.
 * fd9ed218: Merge branch 'feature/list-required-volumes-on-restore-dry-run' into 'master'
 * 790020b6: List required volumes when called with 'restore --dry-run'
 * 3ddab5af:chg: Add Makefile and update docs.
 * f6a12e81: Merge branch 'swrmr-master-patch-23969' into 'master'
 * 101e689c: Fix sorting of BackupSets by avoiding direct comparison
 * 97483705: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 311d3df0:fix: Fixes #41 - par2+rsync (non-ssh) fails
 * 44002ea9: Merge branch 'master' into 'master'
 * 96391273: Update mailing list link
 * 2a7dbc64: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * 0094f090: Fixes #16 - Move from boto to boto3.
 * 2fa3d1cd: py27 EOL 01/2020, py35 EOL 01/2021, remove tests.
 * 81b3549b: Move py27 tests to ub16 and py35 tests to ub18.
 * 37cc12ed: Fixes #16 - Move from boto to boto3.
 * f6da0837: py27 EOL 01/2020, py35 EOL 01/2021, remove tests.
 * 65c89286: Remove 2to3 from ub16 builds.
 * 8ce428ac: Move py35 back to ub16, try 2.
 * ece24b34: Move py35 back to ub16.
 * bf014deb: Move py27 tests to ub16 and py35 tests to ub18.
 * 9f12c93f: Fixes #33, remove quotes from identity filename option.
 * 0c9a88a9: Fix to correctly build _librsync.so.
 * c9389c7c: Fix to add --inplace option to build_ext.
 * edf21727: Rename pylintrc to .pylintrc
 * 93582082: Merge branch 'fix-prefix-affinity-registration' into 'master'
 * ac38d35e: Move testfiles dir to a temp location.
 * 1405363a: Merge remote-tracking branch 'alpha/testfiles'
 * e7e32b24: Skip unicode tests that fail on non-Linux systems like macOS.
 * a465c71a: Multibackend: fix indentation error that was preventing from registering more than one affinity prefix per backend
 * f59387d4: Update .gitlab-ci.yml to need code test to pass.
 * 58382383: Remove basepython in code and coverage tests.
 * beba827d: Add report.xml.
 * a983b1c3: Bulk replace testfiles with /tmp/testfiles

rel.0.8.18 / 2021-01-09
=======================

 * 842430f0: Merge branch 'onedrive-token' into 'master'
 * eef8c4ef: onedrive: Support using an external client id / refresh token
 * 92e41953: Update .gitlab-ci.yml to need code test to pass.
 * cc1da7b3: Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git
 * 2b565107: Fix issue #29 Backend b2 backblaze fails with nameprefix restrictions.
 * 791b9c46: Fix issue #26 Backend b2 backblaze fails with nameprefix restrictions
 * 627f32c7: Fix unadorned strings.
 * 926a23a9: Merge branch 'Rufflewind-master-patch-11811' into 'master'
 * dcb092e3: Add report.xml.
 * 71c24f77: Remove basepython in code and coverage tests.
 * 48a3809a: Report errors if B2 backend does exist but otherwise fails to import
 * a045a151: Fix pep8 warning.
 * 93560714: Added option --log-timestamp to prepend timestamp to log entry.
 * 7e2b4e28: Merge branch 'master' of gitlab.com:duplicity/duplicity
 * bbaae91b: Improve patch for Python 3.10.
 * a03fff45: Merge branch 'master' into 'master'
 * 31bd397a: Improve.
 * 2d04491c: Conditionalize for Python version.
 * 9c63dcb8: Patch for Python 3.10.

rel.0.8.17 / 2020-11-11
=======================

 * 427cef55: Fixup ignore_regexps for optional text.
 * 4e67d575: Fix issue #26 (again) - duplicity does not clean up par2 files.
 * c22e9f1c: Fix issue #26 - duplicity does not clean up par2 files.
 * ac042f27: Fix issue #25 - Multibackend not deleting files.
 * 4657aab6: Adjust setup.py for changelog changes.
 * 89d7c6c5: Delete previous manual changelogs.
 * cce7b74d: Tools to make a CHANGELOG.md from git commits.
 * 15026d95: Merge branch 'exc-if-present-robust' into 'master'
 * b39b8e24: Make exclude-if-present more robust
 * d2631093: Merge branch 'no-umask' into 'master'
 * 480dc695: Drop default umask of 0077
 * c108cf67: Comment out RsyncBackendTest, again.
 * ef333fc3: Fix some unadorned strings.
 * 03851d83: Fixed RsyncBackendTeest with proper URL.
 * a0b257bb: Merge branch 'Yump-issue-23' into 'master'
 * 5308d97a: Fix issue #23
 * 389f032f: rclonebackend now logs at the same logging level as duplicity.
 * f1e51c69: Allow sign-build to fail on walk away. Need passwordless option.
 * 9de0b201: Merge branch 'fix-rename' into 'master'
 * 82586974: Fix --rename typo
 * 2bd172b4: Move back to VM build, not remote. Too many issues with remote.
 * 7183660b: Merge branch 'escape-quote' into 'master'
 * 14f18888: Escape single quotes in machine-readable log messages
 * 5261eba3: Uncomment review-tools for snap.
 * 4b36964d: Whoops, missing wildcard '*'.
 * 7ae54fdc: Changes to allow remote build of snap on LP.
 * e05bf96b: Changes to allow remote build of snap on LP.
 * 4990974d: Add a pylint disable-import-error flag.
 * 1d893b5f: Change urllib2 to urllib.request in parse_digest_challenge().
 * 167ca1c4: Fix Python 3.9 test in .gitlab-ci.yaml.
 * 54dd043a: Fix Python 3.9 test in .gitlab-ci.yaml.
 * c3985af7: Add Python 3.9 to .gitlab-ci.yaml.
 * 96e64946: Add Python 3.9 to the test suite. It tests sucessfuly.
 * 14239edb: Fix bug #1893481 again for Python2. Missed include.
 * b1d11d63: Fix bug #1893481 Error when logging improperly encoded filenames

rel.0.8.16 / 2020-09-29
=======================

 * 7ae2b866: Merged in s3-unfreeze-all
 * cea274ec: Merge branch 's3-unfreeze-all' into 'master'
 * c8e7d3f1: Add boto3 to list of requirements.
 * d0c826b9: Remove ancient CVS Id macro
 * 185dbda2: Merged in OutlawPlz:paramiko-progress
 * e2a25343: Merge branch 'paramiko-progress' into 'master'
 * 8f0a89da: Fixes paramiko backend progress bar
 * 36493ca4: Merged in lazy init for Boto3 network connections
 * b16e3fcc: Merge branch 'feature/lazy_init_boto3' into 'master'
 * c0671312: Initial crack at lazy init for Boto3
 * 01daabbf: Merge branch 'hostname' into 'master'
 * 1299dbdf: Record the hostname, not the fqdn, in manifest files
 * 24e39034: Merge branch 'listdir-contains' into 'master'
 * f6809e8a: Avoid calling stat when checking for exclude-if-present files
 * 0eda5a26: Fix build control files after markdown conversion.
 * 69581d68: Recover some changes lost after using web-ide.
 * 406f93f0: Paperwork
 * 01665ac2: Merge branch 's3-boto3-region-and-endpoint' into 'master'
 * 1b6070c9: Wait for Glacier batch unfreeze to finish
 * 80d2e486: Update README-REPO.md
 * f28027ed: Make code view consistent.
 * 04ad430e: Update setup.py
 * c637c81c: Update README.md
 * 0032d978: Set default values for s3_region_name and s3_endpoint_url
 * f429006c: Allow setting s3 region and endpoint
 * 84af81ec: Paperwork.
 * 278270b7: Revert "Merge branch 's3-boto3-region-and-endpoint' into 'master'"
 * e80f15b6: Adorn string as unicode
 * 26de58c5: Utilize ThreadPoolExecutor for S3 glacier unfreeze
 * ac22987e: Refine codestyle according to PEP-8
 * 9eaa245c: Adorn strings as unicode
 * 35a56260: S3 unfreeze all files at once

rel.0.8.15 / 2020-07-27
=======================

 * e63b60b0: Always paperwork.
 * f25e9740: Merge branch 's3-boto3-region-and-endpoint' into 'master'
 * 2890326d: Merge branch 'pydrive-notfound' into 'master'
 * 06331867: Merge branch 'pydriveshared' into 'master'
 * a253101c: Allow setting s3 region and endpoint
 * c097eacc: Fixed indentation
 * 768a5a1a: Added shared drive support to existing `pydrive` backend instead of a new backend
 * 717ed7a9: Fix missing FileNotUploadedError in pydrive backend
 * ba8ea919: Fix caps on X-Python-Version.
 * eb4e69e9: Fix issue #10 - ppa:duplicity-*-git fails to install on Focal Fossa
 * 3ac9ad6b: PydriveShared backend is identical to Pydrive backend, except that it works on shared drives rather than personal drives
 * a1ede31e: Include the query when parsing the backend URL string, so users can use it to pass supplementary info to the backend
 * 393d2b68: Merge branch 'patch-2' into 'master'
 * d46699e5: Merge branch 'patch-1' into 'master'
 * 1b565511: Remove python-cloudfiles from suggestions
 * 81ef5e37: Update azure requirement
 * d91c47f0: Fix bug #1211481 with merge from Raffaele Di Campli
 * ff0a701c: Merge branch 'master' into 'master'
 * fab471e2: Added `--do-not-restore-ownership` option
 * 9470355b: Fix bug #1887689 with patch from Matthew Barry
 * b17818c5: Merge branch 'fix-glacier-check' into 'master'
 * c000592a: Fix check for s3 glacier/deep
 * 4d4b1673: Change from push to upload.
 * 7f875db4: Add specific version for six.

rel.0.8.14 / 2020-07-04
=======================

 * 3b0f0e87: Set deprecation version to 0.9.0 for short filenames.
 * 9ee708c7: Fixes for issue #7, par2backend produces badly encoded filenames.
 * 6b69ae1a: Added a couple of fsdecode calls for issue #7.
 * a7bd4f65: Generalize exception for failed get_version() on LaunchPad.
 * 15f3c579: Ignore *.so files.
 * 313d62e0: Update docs
 * ec20391d: Catch up on paperwork.
 * 6eeae416: Merge branch 'mikix/rename-fix' into 'master'
 * c48022c7: Fix --rename encoding
 * 73dc2a82: Merge remote-tracking branch 'team/fix-py27-testing'
 * 9d639672: Skip tests failing on py27 under 18.04 (timing error).
 * 459a3ce0: Fix code style issue.
 * 2534bb3d: Add PATHS_FROM_ECLIPSE_TO_PYTHON to environ whan starting pydevd.
 * 30d654bd: Add *.pyc to .gitignore.
 * 4e6c3cfc: Replace compilec.py with 'setup.py build_ext', del compilec.py.
 * db90ede1: Merge branch 'master' into 'master'
 * dadbe2d2: Support PyDrive2 library in the pydrive backend
 * 26daf312: Fix unadorned string.
 * 9af28035: Fix usage of TOXPYTHON and overrides/bin shebangs.
 * 9935c757: Use default 'before_script' for py27.
 * 9cb7d1c6: Don't collect coverage unless needed.
 * 727b1a83: Merge branch 'Tidy_up_gitlab_CI_doc' into 'master'
 * fc1551a5: Tidy .gitlab-ci.yml, fix py3.5 test, add py2.7 test (allowed to fail)
 * b7c0dea6: Merge branch 'fix-py27-CI'
 * 61e33f41: Test code instead of py27 since py27 is tested elsewhere.
 * 6b7a2b06: Fix RdiffdirTest to use TOXPYTHON as well.
 * b89a30e8: Set TOXPYTHON before tests.
 * 99ece486: Put TOXPYTHON in passed environment.
 * aa472f11: More fixes for bug #1877885 - Catch quota overflow on Mega upload.
 * 433b6451: More fixes for bug #1877885 - Catch quota overflow on Mega upload.
 * 880a8f23: Undo: Try forcing python version to match tox testing version.
 * a3286a4f: Always upgrade pip.
 * fecd10c2: Try forcing python version to match tox testing version.
 * 42f8ad60: Uncomment all tests.
 * 7ee52c1c: Test just py27 for now.
 * 0f662e41: Replace bzr with git.
 * 2f4750ca: Don't load repo version of future, let pip do it.
 * 87992352: Hmmm, Gitlab yaml does not like continuation lines. Fix it.
 * c3721d3c: Fix typo.
 * a6b55799: Update to use pip as module and add py35 test.
 * 4c890bb1: Add py35 to CI tests.
 * 2c3c5353: More changes to support Xenial.
 * b22373ad: Fix typo.
 * 7e8bf753: Fix duplicity to run under Python 3.5.
 * 5a33cb90: Fix duplicity to run under Python 3.5.
 * 3b57b20f: Merge branch 'add_gitlab_testing' into 'master'
 * f299d7d1: Update .gitlab-ci.yml to update pip before installing other pip packages (to try to fix more-itertools issue: https://github.com/pytest-dev/pytest/issues/4770 )
 * 8101cd40: Don't include .git dir when building docker images.
 * 03778ed2: Merge branch 'update_pip_before_install' into 'master'
 * 951beefd: Upgrade pip before installing requirements with it. Fixes more-itertools error as newer versions of pip identify that the latest more-itertools are incompatible with python 2.
 * 15fa9aaf: Patched in a megav2backend.py to update to MEGAcmd tools.
 * f4218d83: Change log.Warning to log.Warn. Whoops!
 * eccc2566: Fixed bug #1875937 - validate_encryption_settings() fails w/S3 glacier
 * ff4fb495: Restore commented our backend requirements.
 * 952d9c1f: Fixes for rclonebackend from Francesco Magno (original author)
 * 4db16e4d: Version man pages during setup.py install.
 * 0effc6ba: More fixes for Launchpad build limitations.
 * 971d5bf2: More fixes for Launchpad build limitations.
 * a99d919d: Move setuptools_scm to setup_requires.
 * 9d312e48: Back off requirements for fallback_version in setup.py.
 * 6eba7bf0: Add some requirements for LP build.
 * 52fb798b: Make sure we get six from pip to support dropbox.
 * 44987f5d: Provide fallback_version for Launchpad builder.
 * b4449533: Remove python3-setuptools-scm from setup.py.
 * af9258d0: Add python3-setuptools-scm to debian/control.
 * 407bc33c: Try variation with hyphen seperator.
 * 5655c84e: Try python3_setuptools_scm (apt repo name). Probably too old.
 * 0954a0ad: Add setuptools_scm to install_requires.

rel.0.8.13 / 2020-05-05
=======================

 * 2af8aef0: Fixed release date
 * 13baefce: Fixed bug #1876446 - WebDAV backend creates only tiny or 0 Byte files
 * e235d0ba: Fix to run with --dist-dir command
 * f15df2e9: Fixed bug #1876778 - byte/str issues in megabackend.py
 * 87a09a5b: Fix to use 'setup.py develop' instead of sdist
 * 06097897: Fix to run with --dist-dir command
 * c0ed5f4c: Fixed bug #1875529 - Support hiding instead of deletin on B2
 * 479bae35: Uncomment upload and sign.
 * f47efa50: Reworked versioning to be git tag based.
 * 9c9ad12d: Migrate bzr to git
 * 44992e7e: Fixed bug #1872332 - NameError in ssh_paramiko_backend.py
 * 8ab56def: Fix spelling error.
 * 256bfbfa: Fixed bug #1869921 - B2 backup resume fails for TypeError
 * 807fe136: Merged in lp:~kenneth-loafman/duplicity/duplicity-pylint - Enable additional pylint warnings. Make 1st pass at correction. unused-argument, unused-wildcard-import, redefined-builtin, bad-indentation, mixed-indentation, unreachable - Renamed globals to config to fix conflict with __builtin__.glogals() - Resolved conflict between duplicity.config and testing.manual.config - Normalized emacs mode line to have encoding:utf8 on all *.py files
 * aa374b68: Fixed bug #1868414 - timeout parameter not passed to BlobService for Azure backend
 * 6bc3ff27: More changes for pylint. * Resolved conflict between duplicity.config and testing.manual.config * Normalized emacs mode line to have encoding:utf8 on all *.py files
 * 435b2f85: More changes for pylint. * Remove copy.com refs.
 * 9fde9b99: More changes for pylint.
 * 2ea9db49: More changes for pylint.
 * bf78bdd0: Enable additional pylint warnings. Make 1st pass at correction. - unused-argument, unused-wildcard-import, redefined-builtin, bad-indentation, mixed-indentation

rel.0.8.12 / 2020-03-19
=======================

 * 12b8ecea: Launchpad automatic translations update.
 * c18ebc75: Fixed bug #1867742 - TypeError: fsdecode() takes 1 positional argument but 2 were given with PCA backend
 * bcdcaca1: Launchpad automatic translations update.
 * 1b68e904: Fixed bug #1867529 - UnicodeDecodeError: 'ascii' codec can't decode byte 0x85 in position 0: ordinal not in range(128) with PCA
 * be554f8f: Launchpad automatic translations update.
 * 496cb677: Fixed bug #1867468 - UnboundLocalError (local variable 'ch_err' referenced before assignment) in ssh_paramiko_backend.py
 * 75093cd3: Launchpad automatic translations update.
 * 0333b0dc: Fixed bug #1867444 - UnicodeDecodeError: 'ascii' codec can't decode byte 0x85 in position 0: ordinal not in range(128) using PCA backend
 * 3572d388: Fixed bug #1867435 - TypeError: must be str, not bytes using PCA backend
 * c3df1917: Move pylint config from test_code to pylintrc.
 * 4482bc27: Launchpad automatic translations update.
 * a7adb236: Launchpad automatic translations update.
 * 5c5e601a: Cleaned up some setup issues where the man pages and snapcraft.yaml were not getting versioned.
 * 98d0b592: Launchpad automatic translations update.
 * c4aa171f: Fixed bug #1769267 - [enhancement] please consider using rclone as backend.
 * 2a250258: Fixed bug #1755955 - best order is unclear, of exclude-if-present and exclude-device-files - Removed warning and will now allow these two to be in any order. If encountered outside of the first two slots, duplicity will silently move them to be in the first two slots. Within those two slots the order does not matter.
 * 250ec03a: Launchpad automatic translations update.
 * 201c5321: Fixed a couple of file history bugs: #1044715 Provide a file history feature + removed neutering done between series - #1526557 --file-changed does not work + fixed str/bytes issue finding filename
 * 53effa6a: Fixed bug #1865648 - module 'multiprocessing.dummy' has no attribute 'cpu_count'. - replaced with module psutil for cpu_count() only - appears Arch Linux does not support multiprocessing
 * 03d5e0bb: Launchpad automatic translations update.
 * 0cddaf84: Launchpad automatic translations update.
 * 906a924c: Launchpad automatic translations update.
 * 56ed1920: Mod to get focal build on LP working.
 * d7042e45: Mod to get focal build on LP working.
 * eb53939f: Mod to get focal build on LP working.
 * 6034bb2d: Launchpad automatic translations update.

rel.0.8.11 / 2020-02-24
=======================

 * af0abff5: Merged in translation updates
 * b424b542: Fixed to work around par2 0.8.1 core dump on short name - https://github.com/Parchive/par2cmdline/issues/145
 * fe15fa19: Launchpad automatic translations update.
 * b8cdb056: Fixed bug #1857818 - startswith first arg must be bytes - use util.fsdecode on filename
 * 9a77c6c8: Launchpad automatic translations update.
 * 987c3814: Fixed bug #1863018 - mediafire backend fails on py3 - Fixed handling of bytes filename in url.
 * 3a802f05: Launchpad automatic translations update.
 * 2fb4cbb7: Add rclone requirement to snapcraft.yaml
 * a52b017e: Fixed bug #1236248 - --extra-clean clobbers old backups - Removed --extra-clean, code, and docs
 * 27b1963e: Launchpad automatic translations update.
 * bdfc332a: Fixed bug #1862672 - test_log does not respect TMPDIR - Patch supplied by Jan Tojnar.
 * 5113fc7d: Fixed bug #1860405 - Auth mechanism not supported - Added python3-boto3 requirement to snapcraft.yaml
 * d57502f3: Launchpad automatic translations update.
 * d40ecd57: more readthedocs munges
 * 255cb53c: don't format the po files for readthedocs
 * 2e8a6595: add readthedocs.yaml config file, try 3
 * e3dd1fa4: add readthedocs.yaml config file, try 2
 * 234874f9: add readthedocs.yaml config file
 * b9647b27: remove intltool for readthedocs builder
 * 153d292f: add python-gettext for readthedocs builder
 * a0ecf72c: add gettext/intltool for readthedocs builder
 * 38800f23: add gettext for readthedocs builder
 * 640b47d3: add intltool for readthedocs builder
 * cbfee939: add intltools for readthedocs builder
 * d7d35e13: add intltools for readthedocs builder
 * 3d23d34f: Point readthedocs.io to this repo.
 * 4ee28f18: Renamed botobackend.py to s3_boto_backend.py
 * 30baa2b6: Renamed botobackend.py to s3_boto_backend.py
 * fd6801ec: Launchpad automatic translations update.
 * 029b328e: missing comma
 * b5e46064: Merged from parent to bring in changes
 * debe63f8: Launchpad automatic translations update.
 * 190b7b9d: some code cleanup and play with docs
 * 407e2f1c: Uncomment snapcraft sign-build. Seems it's fixed now.
 * aee6c1a2: fix argument order on review-tools.
 * 0d1282e6: Reworked setup.py to build a pip-compatible distribution tarball of duplicity. * Added dist/makepip for convenience.
 * 59f4d8b9: Launchpad automatic translations update.
 * 856270cd: Adjust Dockerfiles to new requirements.
 * 25b31521: Fix bug #1861287 - Removing old backup chains fails using pexpect+sftp
 * 58b29b9f: Adjust Dockerfiles to new requirements.
 * 2595b9f8: Launchpad automatic translations update.
 * 22da8b15: Enhance setup.py/cfg to allow install by pip
 * 6afc110a: Enhance setup.py/cfg to allow install by pip
 * d5bd1007: Enhance setup.py/cfg to allow install by pip
 * 5eb15775: Launchpad automatic translations update.
 * 4b6df774: Gave up fighting the fascist version control munging on snapcraft.io. Duplicity now has the form 0.8.10.1558, where the last number is the bzr revno. Can't do something nice like having a dev/fin indicator like 0.8.10dev1558 for dev versions and a fin for release or final.
 * d2f01bfe: Renamed MulitGzipFile to GzipFile to avoid future problems with upstream author of mgzip fixing the Mulit -> Multi typo
 * beceb116: Launchpad automatic translations update.
 * 1ec8e28f: Adding missed mgzip import and adjusting untouched unit tests
 * ddb3dc40: Adding multi-core support by using mgzip instead of gzip

rel.0.8.10 / 2020-01-23
=======================

 * 5f1415a9: Launchpad automatic translations update.
 * 89226268: Fixed bug #1858207 missing targets in multibackend - Made it possible to return default value instead of taking a fatal exception on an operation by operation approach. The only use case now is for multibackend to be able to list all targets and report back on the ones that don't work.
 * 30e1a604: Launchpad automatic translations update.
 * 556a282a: Fixed bug #1858204 - ENODEV should be added to list of recognized error stringa
 * 9cbab6f7: Launchpad automatic translations update.
 * e7612fae: Comment out test_compare, again.
 * 88aed779: Launchpad automatic translations update.
 * 3899ebec: Clean up deprecation errors in Python 3.8
 * eee9f8e3: Clean up some TODO tasks in testing code.
 * 79081029: Launchpad automatic translations update.
 * aa642844: Fixed bug #1859877 - syntax warning on python 3.8
 * 6bd8193d: Move to single-sourceing the package version - Rework setup.py, dist/makedist, dist/makesnap, etc., to get version from duplicity/__init__.py - Drop dist/relfiles. It was problematic.
 * be8452c2: Launchpad automatic translations update.
 * 6367b8d2: Fixed bug #1859304 with patch from Arduous - Backup and restore do not work on SCP backend
 * 97e94fc3: Launchpad automatic translations update.
 * 3b5c952c: Revert last change to duplicity.__init__.py.
 * 84b506a4: Py27 supports unicode returns for translations - remove install that does not incude unicode - Removed some unneeded includes of gettext
 * 1efea86a: Launchpad automatic translations update.
 * 2fb8f721: Fixed bug #1858713 - paramiko socket.timeout - chan.recv() can return bytes or str based on the phase of the moon. Make allowances.
 * 4a80f13a: Switched to python3 for snaps.
 * 7d23db3d: Launchpad automatic translations update.
 * ba8a1a7f: Fix unadorned string.
 * 9fe88fe4: Launchpad automatic translations update.

rel.0.8.09 / 2020-01-07
=======================

 * afd4f346: Launchpad automatic translations update.
 * cb6faeb1: Change of plans. Skip test if rclone not present.
 * a3008af7: Add rclone to setup testing requirements.
 * 8695fed1: Revert to testing after build.
 * 1d25633a: Fixed bug #1855736 again - Duplicity fails to start - remove decode from unicode string
 * 944f1e7c: Fixed bug #1858295 - Unicode error in source filename - decode arg if it comes in as bytes
 * 73ef6f21: Add snapcraft login to makesnap
 * 87671a83: Launchpad automatic translations update.
 * f0cea7c9: Launchpad automatic translations update.
 * fbe3cb9b: Fix bug #1858153 with patch from az - mega backend: fails to create directory
 * cd96e562: Fix bug #1857734 - TypeError in ssh_paramiko_backend - conn.recv() can return bytes or string, make string
 * 6e2625ef: Fix bytes/string differences in subprocess_popen() - Now returns unicode string not bytes, like python2
 * 0e0a92b1: Launchpad automatic translations update.
 * c602d13e: Convert all shebangs to python3 for bug #1855736
 * cb09d3d1: Launchpad automatic translations update.
 * dec2e5ce: Fixed bug #1857554 name 'file' is not defined - file() calls replaced by open() in 3 places.
 * 7e2c0275: Original rclonebackend.py from Francesco Magno for Python 2.7
 * 19e03c7c: Launchpad automatic translations update.
 * 83fc9ccc: Merged in lp:~ed.so/duplicity/boto.fixup - fix manpage indention - clarify difference between boto backends - add boto+s3:// for future use when boto3+s3:// will become default s3 backend
 * 10785928: Renamed testing/infrastructure to testing/docker
 * 708ba6cb: fix manpage indention clarify difference between boto backends add boto+s3:// for future use when boto3+s3:// will become default s3 backend
 * 42782001: Launchpad automatic translations update.
 * 31719a4c: Fixed a mess I made. setup.py was shebanged to Py3, duplicity was shebanged to Py2. This meant that duplicity ran as Py2 but could not find its modules because they were under Py3. AArgh!
 * bb6fa703: Launchpad automatic translations update.
 * 4e0397c6: Fixed bug #1855736 - duplicity fails to start - Made imports absolute in dup_main.py
 * 91408ea5: Fixed bug #1856447 with hint from Enno L - Replaced with formatted string
 * da811ea3: Launchpad automatic translations update.
 * 36b41ef0: Launchpad automatic translations update.
 * ee8d3ede: Fixed bug #1855736 with help from Michael Terry - Decode Popen output to utf8
 * 175bc812: Launchpad automatic translations update.
 * 96612933: Fixed bug #1855636 with patch from Filip Slunecko - Wrong buf type returned on error. Make bytes.
 * a4203f96: Launchpad automatic translations update.
 * 2db7875a: Launchpad automatic translations update.

rel.0.8.08 / 2019-12-08
=======================

 * 69a9a4a8: Merged in translation updates
 * c3e20b71: Merged in translation updates
 * d7c5e954: Removed abandoned ref in README * Comment out signing in makesnap
 * bb60e738: Fixed bug #1854554 with help from Tommy Nguyen - Fixed a typo made during Python 3 conversion.
 * 7d4eab44: Launchpad automatic translations update.
 * ad7c1ed9: Fixed bug #1855379 with patch from Daniel González Gasull - Issue warning on temporary connection loss. * Fixed misc coding style errors.
 * 66618422: Launchpad automatic translations update.
 * aa3d2815: Disabling autotest for LP build. I have run tests on all Ubuntu releases since 18.04, so the code works. To run tests manually, run tox from the main directory. Maybe LP build will work again soon.
 * ac23d014: Merged in lp:~carlalex/duplicity/duplicity - Fixes bug #1840044: Migrate boto backend to boto3 - New module uses boto3+s3:// as schema.
 * 51124764: Launchpad automatic translations update.
 * 3b56ea8f: Update to manpage
 * 8d3fb9f1: Convert debian build to Python 3.
 * 8be9580c: Replace python with python3 in shebang.
 * 8cbf1dc0: Convert debian build to Python 3.
 * bab75735: BUGFIX: list should retun byte strings, not unicode strings
 * 2243057f: Updating comments
 * 5f261a57: select boto3/s3 backend via url scheme rather than by CLI option. Doc changes to support this.
 * df3e0fff: renaming boto3 backend file
 * 448c002e: merging from parent
 * d830967e: Adding support for AWS Glacier Deep Archive. Fixing some typos.
 * edb3da53: Manpage updates. Cleaning up the comments to reflect my current plans. Some minor clean-ups.
 * b60f8f79: updating comments
 * 241a9f2c: SSE options comitted. AES tested, KMS not tested
 * bd2f6aa8: handling storage class on backup
 * 33b5d22a: handling storage class on backup
 * e9624e93: minor clean-ups
 * a3108312: rename boto3 backend py file
 * bdae8f29: removing 'todo' comment for multi support. Defaults in Boto3 chunk the upload and attempt to use multiple threads. See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig
 * eb8d57e7: format fix
 * 5f16dd3c: Fixing status reporting. Cleanup.
 * 67cc49a9: better exception handling. Return -1 for unknwon objects in _query.
 * dcea0b29: updating comment
 * 6d49b3bf: Making note of a bug
 * fc2a94bb: removing unused imports
 * dae0fcad: Launchpad automatic translations update.
 * 98f7cba2: implementing _query for boto3
 * 357ec3bc: minor clean-up.
 * 48de8eae: Some initial work on a boto3 back end.
 * b01ea4f8: Fixed bug #1853809 - Tests failing with Python 3.8 / Deprecation warnings - Fixed the deprecation warnings with patch from Sebastien Bacher - Fixed test_globmatch to handle python 3.8 same as 3.7 - Fixed tox.ini to include python 3.8 in future tests
 * ecc58ad5: Launchpad automatic translations update.
 * 53708f04: Fixed bug #1853655 - duplicity crashes with --exclude-older-than - The exclusion setup checked for valid string only. Made the code comprehend datetime (int) as well.
 * f66795a9: Launchpad automatic translations update.
 * 6fd24aa6: Just some cosmetic changes.
 * c8affca5: Launchpad automatic translations update.
 * 5881f3d2: Fixed bug #1851668 with help from Wolfgang Rohdewald - Applied patches to handle translations.
 * 6138a4e4: Launchpad automatic translations update.
 * 6a05db95: Fixed bug #1852876 '_io.BufferedReader' object has no attribute 'uc_name' - Fixed a couple of instances where str() was used in place of util.uexc() - The file was opened with builtins, so use name, not uc_name
 * 56fa989d: Added build signing to dist/makesnap.
 * 1c190cdf: Launchpad automatic translations update.
 * 2321a7b9: Fixed bug #1852848 with patch from Tomas Krizek - B2 moved the API from "b2" package into a separate "b2sdk" package. Using the old "b2" package is now deprecated. See link: https://github.com/Backblaze/B2_Command_Line_Tool/blob/master/b2/_sdk_deprecation.py - b2backend.py currently depends on both "b2" and "b2sdk", but use of "b2" is enforced and "b2sdk" isn't used at all. - The attached patch uses "b2sdk" as the primary dependency. If the new "b2sdk" module isn't available, it falls back to using the old "b2" in order to keep backward compatibility with older installations.
 * ded9ea68: Launchpad automatic translations update.

rel.0.8.07 / 2019-11-14
=======================

 * 21776311: Launchpad automatic translations update.
 * db74a355: Fixed bug #1851727 - InvalidBackendURL for multi backend - Encode to utf8 only on Python2, otherwise leave as unicode
 * 8050d68a: Merged in lp:~mterry/duplicity/resume-encrypt-no-pass - This branch arose from a Debian patch that has been disabling the encryption validation of volume1 during restarts for years. - Debian has been preserving the ability to back up with just an encrypt key and no password (i.e. to have no secrets on the backup machine).
 * bc08cf40: Merged in lp:~mterry/duplicity/pydrive-cache-fix - The pydrive backend had another of the ongoing bytes/string issues. :) - This time, it was saving a bytes filename in its internal cache after each volume upload. Then when asked for a list of files later, it would add the byte-filenames from its cache to the results. And we'd end up thinking there were two of the same filename on the backend, which would cause a crash at the end of an otherwise successful backup, because the collections code would assert on the filenames being unique.
 * bece9960: Launchpad automatic translations update.
 * b5454112: Fix resuming without a passphrase when using just an encryption key
 * 5c11e1cd: Fix bytes/string issue in pydrive backend upload
 * 0fa0acf3: Fixed bug #1851167 with help from Aspen Barnes - Had Popen() to return strings not bytes
 * fe0a3dc4: Added dist/makesnap to make spaps automagically.
 * f0e4681a: Launchpad automatic translations update.
 * 0bbbc882: Fixed bug #1850990 with suggestion from Jon Wilson - --s3-use-glacier and --no-encryption cause slow backups
 * f733c92d: Fix header in CHANGELOG
 * e8afc051: Added b2sdk to snapcraft.yaml * Fixed bug #1850440 - Can't mix strings and bytes.
 * c5e51e00: Launchpad automatic translations update.

rel.0.8.06 / 2019-11-05
=======================

 * 67942e36: Merged in translation updates
 * 6bf82a63: Launchpad automatic translations update.
 * 35942eda: Updated snapcraft.yaml to remove python-lockfile and fix spelling.
 * 77e2da82: Updated snapcraft.yaml to remove rdiffdir and add libaft1 to stage.
 * fedad978: Updated snapcraft.yaml to include rdiffdir and did some reformatting.
 * 42597114: Launchpad automatic translations update.
 * be34c6c1: Updated snapcraft.yaml to include rdiffdir and did some reformatting.
 * 3eec3cc3: Launchpad automatic translations update.
 * 9b6412cb: Removed file() call in swiftbackend. It's been deprecated since py2.
 * 45d1e09e: Launchpad automatic translations update.
 * ab62df04: Revisited bug #1848783 - par2+webdav raises TypeError on Python 3 - Fixed so bytes filenames were compared as unicode in re.match()
 * 09ed140e: Launchpad automatic translations update.
 * 6486ce66: Removed a couple of disables from pylint code test. - E1103 - Maybe has no member - E0712 - Catching an exception which doesn't inherit from BaseException
 * d7f60b43: Added additional fsdecode's to uses of local_path.name and source_path.name in b2backend's _get() and _put. See bug #1847885 for more details.
 * 2b9c2f74: Fixed bug #1849661 with patch from Graham Cobb - The problem is that b2backend uses 'quote_plus' on the destination URL without specifying the 'safe' argument as '/'. Note that 'quote' defaults 'safe' to '/', but 'quote_plus' does not!
 * 70da2bfb: Launchpad automatic translations update.
 * 31c2b422: Fixed bug #1848166 - Swift backend fails on string concat - added util.fsdecode() where needed
 * 132e257a: Launchpad automatic translations update.
 * 79f8cce1: Fixed bug #1848783 with patch from Jacob Middag - Don't use b'' strings in re.*
 * 38005b9d: Fixed bug #1848783 with patch from Jacob Middag - Don't use b'' strings in re.*
 * d375664a: Launchpad automatic translations update.
 * de675a87: Fixed bug #1626061 with patch from Michael Apozyan - While doing multipart upload to s3 we need to report the total size of uploaded data, and not the size of each part individually. So we need to keep track of all parts uploaded so far and sum it up on the fly.
 * b13145e9: Launchpad automatic translations update.
 * b4c2e5ce: Removed revision 1480 until patch is validated.
 * 3c9f47a9: Launchpad automatic translations update.
 * 3e97961e: Fixed bug #1626061 with patch from Michael Apozyan - While doing multipart upload to s3 we need to report the total size of uploaded data, and not the size of each part individually. So we need to keep track of all parts uploaded so far and sum it up on the fly.
 * 8024316d: Fixed bug #1848203 with patch from Michael Apozyan - convert to integer division
 * 8ad88116: Fix unadorned string.
 * 42656f87: Fix unadorned string.
 * ad6bde8e: Launchpad automatic translations update.
 * 619e03ff: Updated b2 backend to work with both v0 and v1 of b2sdk * Fixed bug #1847885 - B2 fails on string concatenation. - use util.fsdecode() to get a string not bytes. - Partially fixed in bug #1843995, this applies same fix to remaining instances of the problem
 * f3f56432: In version 1 of the B2sdk, the list_file_names method is removed from the B2Bucket class.
 * 3b966fe7: complete fix for string concatenation in b2 backend
 * 6fff3e5d: Launchpad automatic translations update.
 * f71efe59: Fixed Resouce warnings when using paramiko. It turns out that duplicity's ssh_paramiko_backend.py was not handling warning suppression and ended up clearing all warnings, including those that default to off.
 * 4fd4de81: Fixed Resouce warnings when using paramiko. It turns out that duplicity's ssh_paramiko_backend.py was not handling warning suppression and ended up clearing all warnings, including those that default to off.
 * 5aa43d8d: Launchpad automatic translations update.
 * 39d5b395: Launchpad automatic translations update.

rel.0.8.05 / 2019-10-07
=======================

 * 743fbb8c: Removed a setting in tox.ini that causes coverage to be activated during testing duplicity.
 * 5f7b3102: Launchpad automatic translations update.
 * 6b27d575: Fixed bug #1846678 - --exclude-device-files and -other-filesystems crashes - assuming all options had arguments was fixed.
 * 97debaa0: Fixed bug #1844950 - ssh-pexpect backend syntax error - put the global before the import.
 * f0616e3e: Fixed bug #1846167 - webdavbackend.py: expected bytes-like object, not str - base64 now returns bytes where it used to be strings, so just decode().
 * 7d2eeb50: Fixed bug reported on maillist - Python error in Webdav backend. See: https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00026.html
 * 0e2748db: Fix bug #1844750 - RsyncBackend fails if used with multi-backend. - used patch provided by KDM to fix.
 * 17daeb0a: Fix bug #1843995 - B2 fails on string concatenation. - use util.fsdecode() to get a string not bytes.
 * c6b40602: Launchpad automatic translations update.
 * 96384e42: Clean up some pylint warnings.
 * ce663434: Add testenv:coverage and took it out of defaults. Some cleanup.
 * 56661bbf: Launchpad automatic translations update.
 * 71ea37c8: Fix MacOS tempfile selection to avoid /tmp and /var/tmp. See thread: https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00000.html
 * 2bfa38cb: Launchpad automatic translations update.
 * f4b6027e: Sort of fix bugs #1836887 and #1836888 by skipping the tests under question when running on ppc64el machines.
 * ec6a9112: Launchpad automatic translations update.
 * ec22e360: Launchpad automatic translations update.
 * 9306d8c7: Added more python future includes to support using python3 code mixed with python2.
 * bafb00f3: Fix exc.args handling. Sometimes it's (message, int), other times its (int, message). We look for the message and use that for the exception report.
 * 3a7917a2: Adjust exclusion list for rsync into duplicity_test.
 * d35e8105: Set to allow pydevd usage during tox testing.
 * 55b770d4: Launchpad automatic translations update.
 * 1cef6f5e: Don't add extra newline when building dist/relfiles.txt.
 * 1a352cf0: Changed dist/makedist to fall back to dist/relfiles.txt in case bzr or git is not available to get files list. Tox sdist needs setup.py which needs dist/makedist. * Updatated LINGUAS file to add four new translations.
 * 7ed65ab9: Launchpad automatic translations update.

rel.0.8.04 / 2019-08-31
=======================

 * 2b6ace15: Launchpad automatic translations update.
 * 2025c93e: Made some changes to the Docker infrastructure: All scripts run from any directory, assuming directory structure remains the same. - Changed from Docker's COPY internal command which is slow to using external rsync which is faster and allows excludes. - Removed a couple of unused files.
 * f14141c1: Run compilec.py for code tests, it needs the import.
 * df9e3a68: Launchpad automatic translations update.
 * 25f39eab: Merged in lp:~aaron-whitehouse/duplicity/08-docker-local-import - Convert the Docker infrastructure to pull the local branch into duplicity_test. This allows testing the local branch with the known-good Docker environment, even if it has not yet been committed to trunk. - As a consequence, remove the -r option to build-duplicity_test.sh. This functionality can be achieved by branching that revision before running the script.
 * 10071d50: Simplify README-TESTING and change this to recommend using the Docker images to test local branches in a known-good environment.
 * 0f256d01: Convert Dockerfile-19.10 to new approach (using local folder instead of remote repo) * run-tests passes on 19.10 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED: py36: InterpreterNotFound: python3.6; py37: commands succeeded; report: commands succeeded)
 * aaedefe2: Convert Dockerfile-19.04 to new approach (using local folder instead of remote repo) * run-tests passes on 19.04 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED: py36: InterpreterNotFound: python3.6; py37: commands succeeded; report: commands succeeded)
 * 0dcaf339: Edit Dockerfile-18.10 to use the local folder. * Tests all pass on 18.10 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test_unicode_filelist; TestUnicode.test_unicode_paths_asterisks; TestUnicode.test_unicode_paths_non_globbing; TestUnicode.test_unicode_paths_square_brackets)
 * 803fcfda: Use local folder instead of bzr revision, so remove the revision arguments in the setup script. * Modify Dockerfile and Dockerfile-18.04 to copy the local folder rather than the remote repository. * Tests all pass on 18.04 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test_unicode_filelist; TestUnicode.test_unicode_paths_asterisks; TestUnicode.test_unicode_paths_non_globbing; TestUnicode.test_unicode_paths_square_brackets)
 * 470b0454: Merge with trunk
 * a500b01b: Launchpad automatic translations update.
 * 3afb0573: Fix .bzrignore
 * 5ea557ee: Launchpad automatic translations update.
 * a501c16f: Merged in lp:~kaffeekiffer/duplicity/azure-filename - Encode Azure back-end paths
 * f430485e: Merged in lp:~aaron-whitehouse/duplicity/08-README-TESTING - Change README-TESTING to be correct for running individual tests now that we have moved to Tox/Pytest.
 * 79ae8e3e: Encode Azure backend file names
 * 9b488f39: Fix debian/rules file
 * 10c4d022: Fix setup.py shebang
 * 815b8a30: Fix debian/rules file
 * 37ec9c4e: Fix debian/rules file
 * aa3ccfa5: Fix debian/rules file
 * ba53e882: Fix debian/control file
 * f7c74107: Fix debian/control file
 * 17e52944: Fix debian/control file
 * 2daa432d: Fix debian/control file
 * 93ea3860: Launchpad automatic translations update.
 * ec6161f0: Fix debian/control file
 * 526d6b3f: Fix debian/control file
 * 8f7113d4: Fix debian/control file
 * 3ae92480: Fix debian/control file
 * 29f7f4e4: Fix debian/control file
 * d45850b4: Fix debian/control file
 * fb323ebf: Ran futurize selectively filter-by-filter to find the ones that work.
 * 9fe749d0: Fixed build on Launchpad for 0.8.x, so now there is a new PPA at https://launchpad.net/~duplicity-team/+archive/ubuntu/daily-dev-trunk
 * 418d74b6: Fix debian/control file
 * f32dd411: Fix debian/control file
 * 98947026: Merged in lp:~aaron-whitehouse/duplicity/08-snap-python2 - Add packaging code for Snapcraft/Snap packages
 * 2f4a1527: Add snap package creation files * Modify dist/makedist to version the snapcraft.yaml
 * 69dd94fa: Remove a mess I made.
 * e04c96d4: Fixed bug #1839886 with hint from denick - Duplicity crashes when using --file-prefix * Removed socket.settimeout from backend.py. It was already set in commandline.py. * Removed pycryptopp from README requirements
 * c9e562a5: Launchpad automatic translations update.
 * 97b1a1a6: Fixed bug #1839728 with info from Avleen Vig - b2 backend requires additional import
 * 171d2796: Launchpad automatic translations update.
 * 033468a3: Convert the docker duplicity_test image to pull the local branch into the container, rather than lp:duplicity. This allows the use of the duplicity Docker testing containers to test local changes in a known-good environment before they are merged into trunk. The equivalent of the old behaviour can be achieved by starting with a clean branch from lp:duplicity. * Expand Docker context to parent branch folder and use -f in the docker build command to point to the Dockerfile. * Simplify build-duplicity_test.sh now that the whole folder is copied (individual files no longer need to be copied)
 * 04f3925b: Change README-TESTING to be correct for running individual tests now that we have moved to Pytest.

rel.0.8.03 / 2019-08-09
=======================

 * 04a2d9ed: Launchpad automatic translations update.
 * b8dfa78b: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py * Fixed division differences with futurize
 * d4cb076c: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py * Fixed division differences with futurize
 * 9a1c01b7: More changes to provide Python test coverage: Moved bulk of code from bin/duplicity to duplicity/dup_main.py for coverage. * Fixed some 2to3 issues in dup_main.py
 * e325bf69: More changes to provide Python test coverage: Now covers functional tests spawning duplicity - Does not cover bin/duplicity for some reason
 * cbc43b60: Fixed bugs #1838427 and #1838702 with a fix suggested by Stephen Miller. The fix was to supply tarfile with a unicode grpid, not bytes.
 * 1a6b84fa: Launchpad automatic translations update.
 * 4c472b66: Some changes to provide Python test coverage: Coverage runs with every test cycle - Does not cover functional tests that spawn duplicity itself. Next pass. - After a run use 'coverage report html' to see an overview list and links to drill down. It shows up in htmlcov/index.html.

rel.0.8.02 / 2019-07-31
=======================

 * 18a18456: Fix dist/makedist to run on python2/3
 * 7a988974: Fix dist/makedist to run on python3
 * 3336388d: Fix dist/makedist to run on python3
 * 0836c689: One last change for bug #1829416 from charlie4096
 * eddd7fec: Merged in po-updates. * Fixed bug #1829416 with help from charlie4096 - onedrive: Can’t convert ‘bytes’ object to str implicitly
 * 58fd09d4: Enhanced build_duplicity_test.sh - Use -h to get help and defaults - Takes arguments for distro, revno, help - Distros supported are 18.04, 18.10, 19.04, 19.10 - Revnos are passed to bzr -r option
 * 64a3a6aa: Fix so Docker image duplicity_test will update and pull new bzr revisions if changed since last build.
 * ebd4ee2a: Remove speedup in testing backup. The math was correct, but it's failing on Docker and Launchpad testing.
 * aaf0d2ae: Fix language classifiers in setup.py
 * 305d09f8: Removed python-gettext from setup.py. Whoops!
 * 03e9891b: Move pytest-runner setup requirement to a test requirement
 * 6eda8ed6: Merged in lp:~stragerneds/duplicity/duplicity - Cache results of filename parsing for speedup
 * 88ca568e: Merged in lp:~limburgher/duplicity/dropbox - Fixes bug #1836611 dropbox mixing bytes and strings
 * a49aa3ad: Fixed bug #1836829 progress.py: old_div not defined - also fixed old_div in _boto_multi.py
 * e20454ee: Fixed bug #1836829 progress.py: old_div not defined - also fixed old_div in _boto_multi.py
 * bfa61765: Remove python-gettext from requirements.txt. Normal Python installation includes gettext. * Mod README to include Python 3.6 and 3.7
 * e50d24d5: Correct types for os.join in Dropbox backend.
 * bc233f3b: Launchpad automatic translations update.
 * 721da2ea: Optimize loading backup chains; reduce file_naming.parse calls

rel.0.8.01 / 2019-07-14
=======================

 * bcb6b16a: Merged in po-updates.
 * a7606bcb: Comment out HSIBackendTest since shim is not up-to-date.
 * d9fc4788: Install python3.6 and 3.7 explicitly in Dockerfile. Tox and Docker now support testing Python 2,7, 3.6, and 3.7.
 * 823e8b61: Launchpad automatic translations update.
 * 7a5fa399: Launchpad automatic translations update.
 * 962de9b9: Make sure test filenames are bytes not unicode. * Fix test_glob_to_regex to work on Python 3.7
 * 0f834dad: Going back to original. No portable way to ignore warning.
 * 430da799: Another unadorned string.
 * 50b0d92e: Cleanup some trailing spaces/lines in Docker files.
 * 1b5ac0a8: Fix so we start duplicity with the base python we run under.
 * 5665b259: Adjust POTFILES.in for compilec.py move.
 * ee9c705c: Ensure _librsync.so is regenned before toc testing.
 * 8727a9b6: Add encoding to logging.FileHandler call to make log file utf8
 * b89b562a: Fix warning in _librsync.c module.
 * a6554f6f: Fix some issues found by test_code.py (try 2)
 * f9daa529: Fix some issues found by test_code.py.
 * aa886fef: Fix reversed port assignments (FTP & SSH) in docker-compose.yml.
 * 05da4b27: Fix reimport problem where "from future.builtins" was being treated the differently than "from builtins". They are both the same, so converted to shorter form "from builtins" and removed duplicates.
 * 9f7bb7a0: Merged in lp:~mterry/duplicity/s3fsdecode - Fix s3 backups by encoding remote filenames
 * 273caccb: Merged in lp:~aaron-whitehouse/duplicity/08-dockerfixes - Update duplicity_test Dockerfile: Use 18.04 instead of 16.04 * Use Ubuntu 18.04 version of pip * Add Python3 and 2to3 as a dependencies * Set docker locale as UTF-8
 * 76a85ead: Merged lp:~mterry/duplicity/boto-import - A couple functions in the boto backend were using the boto module without importing it first.
 * e954ea6d: Normalize shebang to just python, no version number * Fix so most testing/*.py files have the future suggested lines - from __future__ import print_function from future import standard_library standard_library.install_aliases()
 * 70469ff1: Fix s3 backups by encoding remote filenames
 * b1d1eb5f: Merge with trunk
 * 29bcab2f: Add 2to3 as a dependency to dockerfile
 * 49de31f7: Add tzdata back in as a dependency and set DEBIAN_FRONTEND=noninteractive so no tzdata prompt
 * 02e7ad38: Set docker container locale to prevent UTF-8 errors
 * 852e8c0a: Change dockerfile to use 18.04 instead of 16.04 and other fixes.
 * 24fbfb5c: Fix s3 backups by importing the boto module
 * 2f98c6e4: Launchpad automatic translations update.
 * 7218e8fb: Fixed failing test in testing/unit/test_globmatch.py - Someone is messing with regex. Fix same. - See https://bugs.python.org/issue29995 for details
 * 83f91b98: Fixed bug #1833559 0.8 test fails with 'duplicity not found' errors - Fixed assumption that duplicity/rdiffdir were in $PATH
 * be2e480a: Fixed bug #1833573 0.8.00 does not work on Python 2 - Fixed shebang to use /usr/bin/python instead of python2
 * ebd1fe4d: Launchpad automatic translations update.
 * 2aa4ed25: Fix some test_code errors that slipped by.
 * d6b4316a: Merged in lp:~kaffeekiffer/duplicity/azure-python3-fix - Use util.fsencode to encode file string
 * c85a0c74: Fixed bug #1831178 sequence item 0: expected str instance, int found - Simply converted int to str when making list
 * 1f4c4c1d: Fix some import conflicts with the "past" module - Rename collections.py to dup_collections.py - Remove all "from future.utils import old_div" - Replace old_div() with "//" (in py27 for a while). - All tests run for py3, unit tests run for py3. The new import fail is "from future import standard_library"
 * 985f9972: Fix Azure backend for python 3
 * 76bc2621: Spaces to tabs for makefile.
 * 7a42d7ee: Change to python3 for build
 * 991e5d86: Merged in lp:~mterry/duplicity/uexc-string - The return type of util.uexc should always be a string.
 * 2490325d: Have uexc to always return a string
 * 053d8a6b: Launchpad automatic translations update.
 * fbd72d9e: Add requirements for python-gettext
 * dcf33fcd: Merged in lp:~mterry/duplicity/gio-pydrive-fsdecode - Fix gio and pydrive backends to use fsdecode
 * d34e66bd: Fix gio and pydrive backends to use fsdecode
 * c06359c6: Launchpad automatic translations update.
 * 82f02488: Launchpad automatic translations update.
 * 52221fc8: Launchpad automatic translations update.
 * d8fdf56c: Launchpad automatic translations update.
 * 9292535c: Launchpad automatic translations update.
 * 6a5f2336: Launchpad automatic translations update.
 * 07bba80f: Launchpad automatic translations update.
 * ae0e9d16: Launchpad automatic translations update.
 * 00c30a35: Launchpad automatic translations update.
 * fdb8bbc3: Launchpad automatic translations update.
 * 6836d561: Launchpad automatic translations update.
 * 17af0786: Launchpad automatic translations update.
 * d206c2c5: Launchpad automatic translations update.
 * ee5787f0: Launchpad automatic translations update.
 * aa3fa6c6: Launchpad automatic translations update.
 * 550d8012: Launchpad automatic translations update.
 * cee1fd9a: Launchpad automatic translations update.
 * f1b547e2: Launchpad automatic translations update.
 * bc46b0c8: Launchpad automatic translations update.
 * 92d86431: Launchpad automatic translations update.
 * 991522ca: Launchpad automatic translations update.
 * 5b61f46e: Launchpad automatic translations update.
 * 1049e14f: Launchpad automatic translations update.
 * efa8ca70: Launchpad automatic translations update.
 * 53ee36df: Launchpad automatic translations update.
 * 3ca3e519: Launchpad automatic translations update.
 * 0943000d: Launchpad automatic translations update.

rel.0.8.00 / 2019-05-29
=======================

 * 8400543b: Merged in lp:~stragerneds/duplicity/duplicity - improve test backup speed - insure all test output is read
 * 292794b7: Fix TestGlobToRegex.test_glob_to_regex for py3.6 and above - see https://bugs.python.org/issue29995 for details
 * 2a0d0b65: Remove unnecessary sleeping after running backups in tests
 * fc08bacb: Minimize time spent sleeping between backups
 * dc7bd07a: Ensure all duplicity output is captured in tests
 * 06390fec: Some more work on unadorned strings - Fixed test_unadorned_string_literals to list all strings found - Added bin/duplicity and bin/rdiffdir to list of files tested - All unadorned strings have now been adorned
 * d9f74dd8: Fixed bug #1828662 with patch from Bas Hulsken - string.split() had been deprecated in 2, removed in 3.7
 * be3b9284: Merged in lp:~mgorse/duplicity/0.8-series - Python 3 fixes to imapbackend.py - Fix bug 1828869: refresh CollectionsStatus after sync
 * 3d023e4a: Fix some unadorned strings.
 * f564050e: Fix some unadorned strings.
 * 8ac4addf: Fix to allow >=2.7 or >=3.5
 * db73e4fd: Fix to always compile _librsync before testing.
 * 4f09d240: setup.py: allow python 2.7 again
 * 23c2b151: Bug #1828869: update CollectionsStatus after sync
 * 103eb008: imap: python 3 fixes
 * d7259db1: sync: handle parsed filenames without start/end times
 * ee057caf: More PEP 479 fixes
 * 2478ed7d: Manual merge of lp:~yajo/duplicity/duplicity - Support partial metadata sync. - Fixes bug #1823858 by letting the user to choose partial syncing. Only the metadata for the target chain will be downloaded. If older (or newer) chains are encrypted with a different passphrase, the user will be able to restore to a given time by supplying only the passphrase for the chain selected by the `--restore-time` option when using this new option. - A side effect is that using this flag reduces dramatically the sync time when moving files from one to another location, in cases where big amounts of chains are found.
 * 4484a428: Change to Python >= 3.5
 * 179cf6e2: Merged in lp:~brandon753-ba/duplicity/aws-glacier - Adds support for for a command line option to store data on AWS S3 Glacier.
 * 08571c42: Fix bug #1811114 with revised onedrivebackend.py from David Martin - Adapt to new Microsoft Graph API
 * b4784000: Removed last mention of copy.com from man page with help from edso.
 * 0f5d5fbc: Merged in lp:~aaron-whitehouse/duplicity/08-style-fixes - Fix pylint style issues (over-indented text, whitespace on blank lines etc) - Removed "pylint: disable=bad-string-format-type" comment, which was throwing an error and does not seem to be needed.
 * 2c38570a: Merged in lp:~aaron-whitehouse/duplicity/08-uexc-fix - Fix for Bug #1770929 with associated test cases (thanks to Pete Zaitcev (zaitcev) in Bug #1797928 for the head start).
 * 116494b7: Merged in lp:~mgorse/duplicity/0.8-series - More python 3 fixes
 * 115ec850: Added documentation on how to use the new AWS S3 Glacier option.
 * 1dc87cd3: Fix pylint style issues (over-indented text, whitespace on blank lines etc) * Removed "pylint: disable=bad-string-format-type" comment, which was throwing an error and does not seem to be needed.
 * 674b26e3: Accomodate unicode input for uexc and add test for this.
 * 674ddc56: Convert deprecated .message to args[0]
 * 7145e132: Add test case for lp:1770929 * Added fix (though using deprecated .message syntax)
 * 3d1ce634: Fixed a typo in prior commit
 * 5f095648: Added support for AWS glacier storage class
 * 8b2819d3: Attempt to port sx backend to python 3
 * 4b4b8af8: rsync: py3 fixes
 * 1d3b6e26: ncftp: py3 fixes
 * 9d96f559: test_selection.py: fix an invalid escape sequence on py3
 * 36c638e1: Fix sync_archive on python 3
 * bc78a077: ssh_pexpect: py3 fixes
 * e37b3628: Pull from main branch
 * 7e4a8a14: Fixed bug #1817375 with hint from mgorse - Added 'global pexpect' at end of imports
 * b65719d9: Merged in lp:~mterry/duplicity/pydrive-root - Just a tiny fix to clean up the temporary file we create to find the root ID. It's a little surprising for the user if they wind up with this file called "i_am_in_root" that they don't know where it came from. Almost sounds like they were hacked.
 * fcb838c2: Merged in lp:~mgorse/duplicity/0.8-series - More changes for unicode and py3 support
 * f951446a: pydrive: delete temporary root file
 * 71b82651: __unicode__ -> __str__
 * 6254813b: Fix a regex substitution on python 3
 * 2f779058: Return temporary filenames as bytes
 * b40afc6e: Modify some generators to return when finished
 * 1404dd4f: Fix lftp breakage introduced by the python 3 changes
 * a551e766: Bug #1813214 was marked fixed in 0.7.13. There were still a couple of copy.com references remaining in the docs and web. Got those nuked, finally.
 * 80d7726c: Merged in lp:~vam9/duplicity/0.8-series-s3-kms-support - Added s3 kms server side encryption support with kms-grants support.
 * b31e017d: Merged in lp:~okrasz/duplicity/duplicity - Add --azure-blob-tier that specifies storage tier (Hot,Cool,Archive) used for uploaded files.
 * 34049a7c: Putting option in man in alphabetical order + description improvement.
 * 37d420a8: Adds setting to specify Azure Blob standard storage tier.
 * 1a52132e: Fixed bug #1803896 with patch from slawekbunka - Add __enter__ and __exit__ to B2ProgressListener
 * 9fe379a4: Merged in lp:~mgorse/duplicity/0.8-series - First pass at a python 3 port.
 * cb782f9f: tox: Target py3, rather than py36
 * 424b5f67: Fix some punctuation.
 * 8cdfeb13: Fixed bug #1798206 and bug #1798504 * Made paramiko a global with import during __init__ so it would not be loaded unless needed.
 * 7c786665: Merged in lp:~mcuelenaere/duplicity/duplicity - Make sure we don't load files completely into memory when transferring them from/to the remote WebDAV endpoint.
 * 232858dc: _librsyncmodule.c: Use s in format parameters again under python 2
 * 715b917d: Fix comment from last commit
 * 1cd4ddb9: compilec.py: work around conflict with collections.py vs. built-in collections module
 * 081348d2: First pass at a python 3 port
 * 58023921: tox: pass LC_CTYPE
 * 6e86cbec: Change WebDAV backend to not read/write files into memory, but stream them from/to disk to/from the remote endpoint
 * 59d431a2: Fixed but #1797797 with patch from Bas Hulsken - use bytes instead of unicode for '/' in filenames
 * ed799c8a: Merged in lp:~mgorse/duplicity/0.8-series - Run futurize --stage1, and adjust so that tests still pass.
 * 390d96a8: Run futurize --stage1 on rdiffdir
 * 27c17514: Run futurize --stage1 on bin/duplicity
 * fffc3ed0: Run futurize --stage1, and adjust so that tests still pass.
 * 93c96426: Merged in lp:~mgorse/duplicity/0.8-series - Adorn some remaining strings
 * 2c06eb6f: Adorn some remaining strings
 * 934387af: Merged in lp:~qsantos/duplicity/fix-unmatched-rule-error - There are actually two commits: the first fixes a very minor detail in the README regarding the Python version that should be used; the second fixes the way exceptions are handled when an incorrect rule is specified, and display the nice error message rather than an obscure stack trace.
 * f49b5b4b: Fix error message on unmatched glob rules
 * e6af3f99: Fix required Python version in README
 * 18e928e8: Fixed bug #1795227 global name Dropbox is not defined - Applied patch from Pedro Gimeno to restore globals
 * f1b89200: Merged in lp:~mgorse/duplicity/0.8-series - Adorn more strings in duplicity/*.py
 * a5d26b8d: Annotate more strings in duplicity/*.py
 * 23827636: Added s3 kms server side encryption support with kms-grants support.
 * a2ff2c6f: Merged in lp:~mgorse/duplicity/0.8-series - Adorn some duplicity/*.py strings. I've avoided submitting anything that I think might require significant discussion; I think that reviewing will be easier this way. Mostly annotated strings as unicode, except for librsync.py.
 * 4d7fd83c: Adorn strings in some duplicity/*.py files. Several files are still tbd.
 * dccaf443: Unicode fixes
 * 6376ca03: Make files executable.
 * 93c35867: Mark adorned all but one of testing/unit.
 * cf6682d7: Released some things without proper paperwork: Adorned strings in testing/, testing/functional/, and testing/unit * Added AUTHORS file listing all copyright claimants in headers
 * 7bde96b9: Missed a couple. Simple sort.
 * a0d8d569: Add AUTHORS file.
 * 3d6fe201: Checkpoint: Fixing unadorned strings for testing/unit/*.
 * 12b84974: Fixed unadorned strings for testing/functional/*.
 * 0177ae86: Fixed unadorned strings for testing/*.
 * b9062f81: Reverted back to rev 1317 and reimplemented revs 1319 to 1322
 * d0f86da9: Reverted back to rev 1317 and reimplemented revs 1319 to 1322
 * 0cfe0a20: Whoops, my bad! Released before fully testing. Reverting to rev 1317 and proceeding from there with unadorned string conversion.
 * c4b6b71e: Move docs/conf.py to ignored. Sphinx rewrites it.
 * 731a7251: Fix a misspelling
 * 74c261a4: Fix 2to3 error found with newer 2to3 module.
 * c929c9fb: Nuke remnants of copycom and acdcli backends * Regen docs
 * 28bd5c37: Fixed unadorned strings to unicode in duplicity/*/* - Some fixup due to shifting indenataion not matching PEP8. - Substituted for non-ascii char in jottlibbackend.py comment.
 * d31af044: Fixed unadorned strings to unicode in duplicity/backends/* - Some fixup due to shifting indenataion not matching PEP8.
 * 4ae4dda1: Fixed unadorned strings to unicode in duplicity/backends/* - Some fixup due to shifting indenataion not matching PEP8.
 * f6540a98: Added function to fix unadorned strings (testing/fix_unadorned_strings.py) - Fixes by inserting 'u' before token string - Solves 99.9% of the use cases we have - Fix unadorned strings to unicode in bin/duplicity and bin/rdiffdir - Add import for __future__.print_function to find_unadorned_strings.py
 * 7fb142ee: Fix unadorned strings to unicode.
 * c5baf72a: Add gpg sockets to ignore list.
 * f0dddeff: Add fix_unadorned_strings.py to ignore list.
 * c3ad7ee1: Add function to fix unadorned strings by inserting 'u' before. Solves 99.9% of the use cases we have.
 * b8c9e5f5: Add import for __future__.print_function
 * 2c536a03: Merged in lp:~aaron-whitehouse/duplicity/08-adorn-strings - Adorning string literals (normally to make these unicode), in support of a transition to Python 3. See https://blueprints.launchpad.net/duplicity/+spec/adorn-string-literals - Adorn string in duplicity/globmatch.py. - Adorn strings in testing/unit/test_globmatch.py - Adorn strings in selection.py - Adorn strings in functional/test_selection.py and unit/test_selection.py - Remove ignores for these files in test_code.py
 * 7c1b991b: Adorn globs in functional/test_selection.py and unit/test_selection.py * Remove ignores for these files in test_code.py
 * a1a6d7dc: Remove selection.py exception from test_code.py
 * 1205d8d1: Adorn globs in selection.py
 * 03e593e2: Merge with trunk
 * cd2021ee: Fixed bug #1780617 Test fail when GnuPG >= 2.2.8 - Relevant change in GnuPG 2.2.8: https://dev.gnupg.org/T3981 - Added '--ignore-mdc-error' to all gpg calls made.
 * f830381f: Merged in lp:~excitablesnowball/duplicity/s3-onezone-ia - Add option --s3-use-onezone-ia S3 One Zone Infrequent Access Storage
 * 3e0e0b95: Add support for S3 One Zone - Infrequent Access storage class.
 * b51dbfe4: Adorn strings in testing/unit/test_globmatch.py
 * 09478739: Adorn string literals in duplicity/globmatch.py.
 * b33d5baa: Merged in lp:~aaron-whitehouse/duplicity/08-unadorned-strings - Added new script to find unadorned strings (testing/find_unadorned_strings.py python_file) which prints all unadorned strings in a .py file. - Added a new test to test_code.py that checks across all files for unadorned strings and gives an error if any are found (most files are in an ignore list at this stage, but this will allow us to incrementally remove the exceptions as we adorn the strings in each file). - Adorn string literals in test_code.py with u/b
 * bb61a378: Merged in lp:~aaron-whitehouse/duplicity/08-pycodestyle - Tox changes to accommodate new pycodestyle version warnings. Ignored W504 for now and marked as a TODO. Marked W503 as a permanent ignore, as it is prefered to the (mutually exclusive) W504 under PEP8. - Marked various regex strings as raw strings to avoid the new W605 "invalid escape sequence".
 * d20cf287: Added new script to find unadorned strings (testing/find_unadorned_strings.py python_file) which prints all unadorned strings in a .py file. * Added a new test to test_code.py that checks across all files for unadorned strings and gives an error if any are found (most files are in an ignore list at this stage, but this will allow us to incrementally remove the exceptions as we adorn the strings in each file).
 * f0b1c489: Adorn string literals in test_code.py with u/b * Add test for unadorned string literals (currently only single file)
 * d088ef87: Tox changes to accommodate new pycodestyle version warnings. Ignored W504 for now and marked as a TODO. Marked W503 as a permanent ignore, as it is prefered to the (mutually exclusive) W504 under PEP8. * Marked various regex strings as raw strings to avoid the new W605 "invalid escape sequence".
 * e585fbc9: Fixed bug #x1717935 with suggestion from strainu - Use urllib.quote_plus() to properly quote pathnames passed via URL
 * 02b43b38: Fixed bug #1768954 with patch from Max Hallden - Add AZURE_ENDPOINT_SUFFIX environ variable to allow setting to non-U.S. servers
 * 33137e8f: Merged in lp:~dawgfoto/duplicity/fixup1252 * only check decryptable remote manifests - fixup of revision 1252 which introduces a non-fatal error message (see #1729796) - for backups the GPG private key and/or it's password are typically not available - also avoid interactive password queries through e.g. gpg agent
 * ecb0687f: only check decryptable remote manifests - fixup of revision 1252 which introduces a non-fatal error message (see #1729796) - for backups the GPG private key and/or it's password are typically not available - also avoid interactive password queries through e.g. gpg agent
 * fb2dd024: check last manifest only with prev. backup
 * ae648f49: Launchpad automatic translations update.
 * b7791fb3: Launchpad automatic translations update.
 * 1f8906ac: Mass update of po files from launchpad translations.
 * d61a5820: Merged in lp:~dawgfoto/duplicity/fixup1251 - Avoid redundant replication of already present backup sets. - Fixed by adding back BackupSet.__eq__ which was accidentally(?) removed in 1251.
 * 36d14ef8: Avoid redundant replication of already present backup sets - Add back BackupSet.__eq__ which was accidentally removed in 1251
 * 26aa75ae: Reduce dependencies on backend libraries - Moved backend imports into backend class __init__ method - Surrounded imports with try/except to allow better errors - Put all library dependencies in requirements.txt
 * 24ded65c: Merged in lp:~aaron-whitehouse/duplicity/08-ufn-to-fsdecode - Change util.fsdecode to use "replace" instead of "ignore" (matching behaviour of util.ufn) - Replace all uses of ufn with fsdecode - Make backend.tobytes use util.fsencode rather than reimplementing
 * aac4fe35: Make backend.tobytes use util.fsencode rather than reimplementing
 * ec5ed17e: Merge with trunk
 * 2d61cfe6: Change util.fsdecode to use "replace" instead of "ignore" (matching behaviour of util.ufn) * Replace all uses of ufn with fsdecode
 * eb2977fd: Fixes so pylint 1.8.1 does not complain about missing conditional imports. - Fix dpbxbackend so that imports require instantiation of the class. - Added pylint: disable=import-error to a couple of conditional imports
 * fe75a0ba: Update docs.
 * 5c499572: Merged in lp:~aaron-whitehouse/duplicity/08-ufn-to-uc_name - Replace util.ufn(path.name) with path.uc_name throughout.
 * 1ff3239f: Merge with trunk.
 * d14bc462: Replace util.ufn(path.name) with path.uc_name throughout.
 * 8d191e6c: More pytest changes - Use requirements.txt for dependencies - Run unit tests first, then functional - Some general cleanup
 * 43076db9: More pytest changes - Use requirements.txt for dependencies - Run unit tests first, then functional - Some general cleanup
 * 1b9be562: Converted to use pytest instead of unittest (setup.py test is now discouraged) - We use @pytest.mark.nocapture to mark the tests (gpg) that require no capture of file streams (currently 10 tests). - The rest of the tests are run normally
 * dbccb1af: Remove precise-lpbuild. EOL as of April 28, 1917.
 * 783ca0ad: Remove unused import.
 * 80c16f0d: First cut converting to pytest. - 'setup.py test' now uses pytest. We still use tox for correct virtualenv setup. All seem to be current best practices since 'setup.py test' use is discouraged. - Global --capture=no option to allow gpg tests to complete successfully. Future should only turn off capture to the gpg tests themselves. Creates a still messy output.
 * db112ff6: Merged in lp:~aaron-whitehouse/duplicity/08-unicode - Many strings have been changed to unicode for better handling of international characters and to make the transition to Python 3 significantly easier, primarily on the 'local' side of duplicity (selection, commandline arguments etc) rather than any backends etc.
 * 0e2e7e21: Various code tidy-ups pre submitting for merge. None should change behaviour.
 * 43f58747: Change fsdecode to use globals.fsencoding * Add 'ANSI_X3.4-1968' to the list of fsencodings that globals.fsencode treats as probably UTF-8
 * e19213ae: Merge in lp:~mterry/duplicity/unicode-future
 * 4530e3f3: Sync with trunk.
 * 97133837: Merge with trunk * Add back in testing/testfiles.tar.gz (accidentally made unversioned in previous commit when doing manual merge of archives) * PEP8 error (from trunk)
 * 52c57195: Fix PEP8 issues.
 * f8e79d63: Merged in lp:~crosser/duplicity/fix-small-file-upload - Fixed small file upload changes made in Dropbox SDK v7.1
 * 082bd26f: Merge with trunk (including manual merge of testfiles.tar.gz to add select-unicode to the version without the non-UTF8 file)
 * 24810c8f: dpbxbackend: fix small files upload (API change)
 * 763cb7e2: Specify debian dependency too
 * 1954afa9: Specify future requirement
 * 75119fcb: Merged in lp:~crosser/duplicity/dpbx-fix-file-listing - Fixed bug #1639664 "Dropbox support needs to be updated for Dropbox SDK v7.1"
 * d32c97b4: Merged in lp:~crosser/duplicity/fix-oauth-flow - Fixed bug #1638236 "BackendException with oauth2client 4.0.0"
 * 880daf2c: dpbxbackend: check for specific API error for missing folder
 * 678e5604: The "new" Dropbox OAuth API return objects rather than tuples. Adjust auth flow to that.
 * 4f6f481c: The "new" Dropbox API for directory listing raises an exception when the directory is empty (and duplicity directory will be empty on the first run). We actually want and empty list of files if the list of files is emtpy. So catch the ListFolderError and continue.
 * be790ce2: More fixes for Unicode handling - Default to 'utf-8' if sys.getfilesystemencoding() returns 'ascii' or None - Fixed bug #1386373 with suggestion from Eugene Morozov
 * 8748ad4d: Fixed bug #1733057 AttributeError: 'GPGError' object has no attribute 'decode' - Replaced call to util.ufn() with call to util.uexc(). Stupid typo!
 * 25dbbdf3: Fix attribution for patch of 1448094 to Wolfgang Rohdewald.
 * 909a703e: Merge with trunk (and fix PEP error in backends/pydrivebackend.py)
 * 188e3cc9: Remove non-UTF8 filename from testfiles.tar.gz.
 * e114c215: Fixed bug #1730902 GPG Error Handling - use util.ufn() not str() to handle encoding
 * 425ced22: Fixed bug #1723890 with patch from Killian Lackhove - Fixes error handling in pydrivebackend.py
 * 7f19c95a: Fixed bug #1720159 - Cannot allocate memory with large manifest file since 0.7.03 - filelist is not read if --file-changed option in collection-status not present - This will keep memory usage lower in non collection-status operations
 * d51afc9b: Fix PEP8 issues in b2backend.py.
 * 84494816: Fixed bug #1724144 "--gpg-options unused with some commands" - Add --gpg-options to get version run command
 * ca27552d: Fixed bug #1448094 with patch from Tomáš Zvala - Don't log incremental deletes for chains that have no incrementals
 * cb0b7ea2: Fixed bug #1654756 with new b2backend.py module from Vincent Rouille - Faster (big files are uploaded in chunks) - Added upload progress reporting support
 * 632482ad: Remove conditional pexpect in testing/functional/__init__.py -- while the commented-out text is the nicer approach in versions after pexpect 4.0, we need to support earlier versions at this stage and a single code path is simpler.
 * a6e00fd5: Patched in lp:~mterry/duplicity/rename-dep - Make rename command a dependency for LP build
 * 5291d3ae: Merge with trunk
 * 9bb2e265: Fixed bug #1714663 "Volume signed by XXXXXXXXXXXXXXXX, not XXXXXXXX" - Normalized comparison length to min length of compared keys before comparison - Avoids comparing mix of short, long, or fingerprint size keys.
 * 92f13b28: Merge with trunk.
 * fc88e038: Fix PEP8 issues.
 * 78997098: Fixed bug #1715650 with patch from Mattheww S - Fix to make duplicity attempt a get first, then create, a container in order to support container ACLs.
 * df536b03: More fixes to backend.py plus some cleanup.
 * d4eb13c4: Fix backend.py to allow string, list, and tuple types to support megabackend.py.
 * 49ae61b9: Merged in lp:~mterry/duplicity/more-decode-issues - Here's some fixes for another couple UnicodeDecodeErrors. - The duplicity/dup_time.py fixes when a user passes a utf8 date string (or a string with bogus utf8 characters, but they have to really try to do that). This is bug 1334436. - The bin/duplicity change from str(e) to util.uexc(e) fixes bug 1324188. - The rest of the changes (util.exception_traceback and bin/duplicity changes to use it) are to make the printing of exceptions prettier. Without this, if you see a French exception, you see "accept\xe9es" instead of "acceptées". - You can test all of these changes in one simple line: $ LANGUAGE=fr duplicity remove-older-than $'accept\xffées'
 * 01f6ee0e: Fix some unicode decode errors around exceptions
 * efcf2c97: Fixed bug introduced in new megabackend.py where process_commandline() takes a string not a list. Now it takes both. * Updated web page for new megabackend requirements.
 * 44106805: Fixed bug #1638033 Remove leading slash on --file-to-restore - code already used rstrip('/') so change to just strip('/')
 * ea86899e: 2017-08-31 Kenneth Loafman <kenneth@loafman.com>
 * 2ac2c464: # Fixed bug #1394386 with new module megabackend.py from Tomas Vondra - uses megatools from https://megatools.megous.com/ instead of mega.py library which has been deprecated - fixed copyright and PEP8 issues - replaced subprocess.call() with self.subprocess_popen() to standardize
 * 338489c9: # Fixed bug #1394386 with new module megabackend.py from Tomas Vondra - uses megatools from https://megatools.megous.com/ instead of mega.py library which has been deprecated - fixed copyright and PEP8 issues
 * 5300dc5f: Merged in lp:~mterry/duplicity/gpg-tag-versions - Support gpg versions numbers that have tags on them. - This can happen if you build gpg from git trunk (e.g. 2.1.15-beta20). Or if you run against the freedesktop flatpak runtime (e.g. 2.1.14-unknown).
 * f66c0863: Fix errors where log.Warn was invoked with log.warn in webdavbackend.py
 * 08938ecc: Support gpg versions with -tag suffixes
 * 832feab9: Merged in lp:~mterry/duplicity/gio_child_for_display_name - gio: be slightly more correct and get child GFiles based on display name
 * 757b7c63: Fixed PEP8 errors in bin/duplicity
 * 74eb43b2: Fixed bug #1709047 with suggestion from Gary Hasson * fixed so default was to use original filename
 * aeafea90: gio: be slightly more correct and get child GFiles based on display name
 * 20bd42da: Merged in lp:~mterry/duplicity/giobackend-display-name - giobackend: handle a wider variety of gio backends by making less assumptions; in particular, this fixes the google-drive: backend
 * 66e2bbe0: giobackend: handle a wider variety of gio backends by making less assumptions; in particular, this fixes the google-drive: backend
 * c1ee0dc0: Merge from trunk (with pylint fixes).
 * 8074c2e2: Fixed encrypted remote manifest handling to merely put out a non-fatal error message and continue if the private key is not available.
 * 754b34bf: Fixed slowness in 'collection-status' by basing the status on the remote system only. The local cache is treated as empty.
 * 6699c162: Merge from trunk
 * 7b712ca3: Fix text of last change.
 * cbdf21ad: Patched in lp:~dawgfoto/duplicity/skip_sync_collection_status - collection-status should not sync metadata - up-to-date local metadata is not needed as collection-status is generated from remote file list - syncing metadata might require to download several GBs
 * 77e588c2: collection-status should not sync metadata - up-to-date local metadata is not needed as collection-status is generated from remote file list - syncing metadata might require to download several GBs
 * 9aaa1659: Fixed PEP8 and 2to3 issues.
 * e5a8925e: Merged in lp:~xlucas/duplicity/pca-backend - Add support for OVH Public Cloud Archive backend.
 * 33448a33: Merged in lp:~xlucas/duplicity/multibackend-prefix-affinity - Support prefix affinity in multibackend.
 * 0cdb3463: Merge with trunk, turning string literals in the new testing/functional/test_replicate.py into unicode.
 * 08c6d312: Merged in lp:~dawgfoto/duplicity/replicate - Add integration test for newly added replicate command. - Also see https://code.launchpad.net/~dawgfoto/duplicity/replicate/+merge/322836.
 * df257249: add integration test for newly added replicate command
 * a79a563a: Fixed problem in dist/makedist when building on Mac where AppleDouble files were being created in the tarball. See: https://superuser.com/questions/61185/why-do-i-get-files-like-foo-in-my-tarball-on-os-x
 * 78f165c8: Fixed problem in dist/makedist when building on Mac where AppleDouble files were being created in the tarball. See: https://superuser.com/questions/61185/why-do-i-get-files-like-foo-in-my-tarball-on-os-x
 * 6b3604c2: Add support for OVH Public Cloud Archive backend.
 * 735998a7: Remove util.bytes_to_uc (as either .decode or fsdecode is preferable). * Move unicode conversion for select options from selection.py to commandline.py.
 * 28eee967: Replace util.py functions to and from unicode with direct calls to .encode and .decode, as it did not save much code, means the "strict"/"ignore"/"replace" decision can be made per call. Also helps narrow down on why sys.getfilesystemencoding() is not working as expected in some places.
 * b6bb67e7: Merge remaining file from trunk. Tests pass.
 * ec37a65b: Merged in lp:~duplicity-team/duplicity/po-updates
 * e21dc624: Merge all but bin/duplicity/ (which breaks testing.functional.test_final.FinalTest.test_asym_with_hidden_recipient_cycle )
 * 57665527: Merged in lp:~xlucas/duplicity/swift-multibackend-bug - Fix a bug when swift backend is used in a multibackend configuration.
 * c01f3572: Merged in lp:~xlucas/duplicity/swift-multibackend-bug - Fix a bug when swift backend is used in a multibackend configuration.
 * 7906bcfa: Copy.com is gone so remove copycombackend.py.
 * 454abee5: Copy.com is gone so remove copycombackend.py.
 * e60a4760: Fixed bug #1265765 with patches from Matthias Larisch and Edgar Soldin - SSH Paramiko backend now uses BufferedFile implementation to enable collecting the entire list of files on the backend.
 * 563e14cb: Fixed bug #1265765 with patches from Matthias Larisch and Edgar Soldin - SSH Paramiko backend now uses BufferedFile implementation to enable collecting the entire list of files on the backend.
 * 730e8c4e: Support prefix affinity in multibackend.
 * a66aeff7: Merge with trunk. All tests pass.
 * 773738f0: Added capability to mount user workspace for testing local code.
 * 2a8f1d8b: Added variable substitution to docker-compose.yml - .env file contains first 24 bits of subnet addr * Added teardown.sh as completion of setup.sh
 * f51b7762: Merged in lp:~aaron-whitehouse/duplicity/08-fix-man-verify - Fix description of --verify and --compare-data in the man page. Now clarifies that verify compares the restored files to hashes stored at backup date, while --compare-data compares restored files to files in target_path.
 * f3046dc4: Fix bin/duplicity.1 entries for --verify and --compare-data
 * 05750943: Merged in lp:~dernils/duplicity/docker-compose - Test Infrastructure now utilizing docker-compose
 * 16dda24a: test infrastructure now using docker-compose
 * c7c79e94: Fix bug #1672540 with patch from Benoit Nadeau - Rename would fail to move par files when moving across filesystems. - Patch uses shutil.move() to do the rename instead.
 * 08e538e4: Fix bug #1672540 with patch from Benoit Nadeau - Rename would fail to move par files when moving across filesystems. - Patch uses shutil.move() to do the rename instead.
 * fa820f96: Some changes ported 0.7 to/from 0.8 to keep up-to-date.
 * f7fa3bba: Some changes ported 0.7 to/from 0.8 to keep up-to-date.
 * ec23f426: Revisited bug #670891 with patch from Edgar Soldin - Forced librsync.PatchedFile() to extract file object from TemporaryFile() object when on Windows or Cygwin systems. This allows us to avoid the problem of tmpfile() use which creates temp files in the wrong place. - See discussion at https://bugs.launchpad.net/duplicity/+bug/670891
 * 55f64c0d: Revisited bug #670891 with patch from Edgar Soldin - Forced librsync.PatchedFile() to extract file object from TemporaryFile() object when on Windows or Cygwin systems. This allows us to avoid the problem of tmpfile() use which creates temp files in the wrong place. - See discussion at https://bugs.launchpad.net/duplicity/+bug/670891
 * 9b863088: Fix spurious warning message, return value not needed.
 * 439b457b: Merge with trunk.
 * 11fed951: Checkpoint - docker testbed mostly running - lots of format changes in setup.sh - made sure to kill off network and restart - simplified container naming and killall process - most tests run now with tox, 5 fail
 * ea598187: Go back to original requirements file.
 * 5dd05c94: May have finally fixed bug #1556553, "Too many open files...". - Applied patch from Howard Kaye, question #631423. The fix is to dup the file descriptor, and then close the file in the deallocator routine in the glue code. Duping the file lets the C code and the Python code each close the file when they are done with it. - Invalidated and removed the fix put in for bug #1320832. - Caveat: long incremental chains will still eat up a large number of file descriptors. It's a very risky practice, so I'm not inclined to fix it.
 * ce240c81: May have finally fixed bug #1556553, "Too many open files...". - Applied patch from Howard Kaye, question #631423. The fix is to dup the file descriptor, and then close the file in the deallocator routine in the glue code. Duping the file lets the C code and the Python code each close the file when they are done with it. - Invalidated and removed the fix put in for bug #1320832. - Caveat: long incremental chains will still eat up a large number of file descriptors. It's a very risky practice, so I'm not inclined to fix it.
 * 1dd8b48f: Fix spelling and rearrange some.
 * 3b7b92d9: Added lpbuild-trusty to replace lpbuild-precise pre Aaron Whitehouse's comment that there was a bug in pexpect < 3.4 that affects us.
 * 65ec8d0d: Merged in lp:~dernils/duplicity/Dockerfile - Now have subnet name and IP of the subnet for testing as a variable.
 * 56af1cca: minor changes to setup.sh
 * b1ebcb6e: minor fix to setup.sh
 * 770f3bd9: Merged in lp:~dernils/duplicity/Dockerfile - Added another backend to the docker test infrastructure, updated the setup for testing and updated the documentation.
 * ccc17566: Merged in lp:~xlucas/duplicity/swift-storage-policies - This brings support for Swift storage policies: when using a Swift backend, you can specify the policy containers should be operating on. - This is similar to AWS Cloud Storage classes (ia, rrs, glacier and so on).
 * 327d44bd: added more test infrastructure
 * 14b43efa: Merge in trunk.
 * 8cb8bcbd: Support for Swift storage policies
 * 01251d68: Merged in lp:~aaron-whitehouse/duplicity/tox_pylint_fixes - Changes needed to run-tests without pylint E0401(import-error) errors
 * 2e37b429: Changes needed to run-tests without pylint E0401(import-error) errors
 * 0c1603ea: Merge in changes from trunk. * Tests all pass except pylint test (import-error that also happens for me on trunk, so will fix there).
 * 639d82e9: Remove unnecessary unicode conversion on commandline.py filelist append. * Tests all pass (and in previous commit).
 * b625f2a2: move stdin_test.sh to manual dir
 * 3c99365d: remove run-tests-ve - not needed * move stdin_test.sh to manual dir
 * d14a7b7a: Fix comments on ignored pylint messages.
 * 43c244a0: Remove precise-lpbuild test since precise is EOL.
 * bb7cb854: precise is EOL so drop testing for it.
 * 2f26b014: Use unicode version of pexpect.spawn for version >= 4.0, but bytes version below this.
 * 4957a0b7: Adjust control for LP build process, fasteners not lockfile.
 * bf233f8d: Adjust control for LP build process, fasteners not lockfile.
 * 342c740a: Fixed bug #1320641 and others regarding lockfile - swap from lockfile to fasteners module - use an fcntl() style lock for process lock of duplicity cache - lockfile will now clear if duplicity is killed or crashes
 * 24d43cdf: Fixed bug #1320641 and others regarding lockfile - swap from lockfile to fasteners module - use an fcntl() style lock for process lock of duplicity cache - lockfile will now clear if duplicity is killed or crashes
 * 6d8ef9e4: Fixed bug #1689632 with patch from Howard Kaye - On MacOS, the tempfile.TemporaryFile call erroneously raises an IOError exception saying that too many files are open. This causes restores to fail randomly, after thousands of files have been restored.
 * 809a9fe7: Fixed bug #1689632 with patch from Howard Kaye - On MacOS, the tempfile.TemporaryFile call erroneously raises an IOError exception saying that too many files are open. This causes restores to fail randomly, after thousands of files have been restored.
 * 1a30fe90: Fixed bug #1320832 with suggestion from Oskar Wycislak - Use chunks instead of reading it all in swiftbackend
 * e9ffef2f: Moved some things around in testing/infrastructure to clean up
 * ab3c6c85: Moved Dockerfile for duplicitytest into testinfrastructure/duplicity_test
 * b0d311d4: Merged in lp:~dernils/duplicity/DockerfileConvenience - Add a few files that are the beginning of further infrastructure based on docker. It contains a Dockerfile for a simple ftp server (used for backend testing) and a setup script that can be used to set up the complete test environment.
 * 7808481a: added furhter files for test infrastructure
 * 03840343: Fixed bug #1320832 with suggestion from Oskar Wycislak - Use chunks instead of reading it all in swiftbackend
 * 6835af96: Merge with trunk. All py27 tests pass, lpbuildd-precise still fails.
 * 47a95531: Merged in lp:~dernils/duplicity/DockerfileConvenience - Added a few tools to the Dockerfile that make life easier
 * efe339d2: added ftp client to Dockerfile
 * 2ae1059e: Updated Dockerfile
 * c7b890aa: Make all tests pass on py27 tox environment. * lpbuildd-precise tests still fail because the outdated pexpect (2.4) has issues with unicode (pexpect.spawn does not support unicode and spawnu.readline fails).
 * 36e56f8b: bzr does not honor perms so fix the perms at the start of the testing and avoid annoying error regarding testing/gnupg having too lenient perms
 * 918751ae: Replace incoming non-ASCII chars in commandline.py
 * 3b6c196a: Merged in lp:~marix/duplicity/add-azure-arguments - Using the Azure backend to store large amounts of data we found that performance is sub-optimal. The changes on this branch add command line parameters to fine-tune some parameters of the Azure storage library, allowing to push write performance towards Azure above 1 Gb/s for large back-ups. If a user does not provide the parameters the defaults of the Azure storage library will continue to be used.
 * 74759285: Merged in lp:~marix/duplicity/add-azure-arguments - Using the Azure backend to store large amounts of data we found that performance is sub-optimal. The changes on this branch add command line parameters to fine-tune some parameters of the Azure storage library, allowing to push write performance towards Azure above 1 Gb/s for large back-ups. If a user does not provide the parameters the defaults of the Azure storage library will continue to be used.
 * c93c1c79: Merged in lp:~dawgfoto/duplicity/replicate - Add replicate command to replicate a backup (or backup sets older than a given time) to another backend, leveraging duplicity's backend and compression/encryption infrastructure. * Fixed some incoming PyLint and PEP-8 errors.
 * 92be9085: unit/test_globmatch.py, unit/test_selection.py, functional/test_selection.py tests all pass. * Assume UTF-8 encoding for filelists (which also allows ASCII encoding). * Use new io module for selection filelist access. * Create new path.uc_name that is a unicode version of the path, which is then used throughout the selection code for path name matching etc. * Move selection.py to using unicode strings and uc_name versions of paths. * Made functional/__init__.py use unicode arguments to run duplicity for tests. * Use new io module in functional/test_selection.py. * Remove @unittest.expectedFailure from test_unicode_paths_square_brackets, which no longer fails. * Make unit/test_selection.py ParseTest support unicode and add test_unicode_paths_non_globbing unit test version of functional test.
 * b933ff59: We need tzdata (timezone data).
 * 2f1ff44c: Add command line arguments to fine-tune the Azure backend
 * 2b97aa2c: You need tox to run tox. Doh!
 * b953de4d: Add libffi-dev back. My bad.
 * 0b3b5d43: Merged in lp:~dernils/duplicity/Dockerfile - separated requirements into requirements for duplicity (in requirements.txt) and for testing (in tox.ini)
 * dc1d9703: fixed tox.ini
 * d95c10fe: separated pip requirements into duplicity and testing
 * 85837ecc: separated pip requirements into duplicity and testing
 * 999f9110: Remove dependencies we did not need
 * 7af42bc6: Add test user and swap to non-priviledged.
 * c191eff1: Move branch duplicity up the food chain.
 * d330b621: Simplify Dockerfile per https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ - Add a .dockerignore file - Uncomment some debug prints - quick fix for bug #1680682 and gnupg v1, add missing comma
 * 33dd14b6: Quick fix for bug #1680682 and gnupg v1, add missing comma.
 * d7e6c2c9: Quick fix for bug #1680682 and gnupg v1, add missing comma.
 * f8f6ef1c: A little reorg, just keeping pip things together.
 * 3a61ae16: More changes for testing: keep gpg1 version for future testing - some changes for debugging functional tests - add gpg-agent.conf with allow-loopback-pinentry
 * a21128bd: Merged in lp:~dernils/duplicity/Dockerfile Fixed variable name change in commandline.py
 * 07bd7b16: Edited Dockerfile
 * d18194d0: Whoops, deleted too much. Add rdiff again.
 * 4ecff083: Move pep8 and pylint to requirements.
 * 206f4e34: Add rdiff install and newline at end of file.
 * 0b03c033: delete tempfiles as soon as possible
 * 3a34a4ff: Merged in lp:~dernils/duplicity/documentation - Minor changes to README-REPO, README-TESTING - Also redo the changes to requirements.txt and Dockerfile
 * fba2acf3: Edited requirements.txt, minor changes to README-REPO and README-TESTING
 * a998ad7b: Merged in lp:~dernils/duplicity/testing - Fixed minor stuff in requirements.txt. - Added a Dockerfile for testing. - Minor changes to README files. - Added README-TESTING with some information on testing.
 * 4a8ff298: Added README-TESTING, removed hmtlcov folder
 * c8aa791d: 2017-04-20 Kenneth Loafman <kenneth@loafman.com>
 * de551270: edited requirements.txt
 * 6b3ac5cc: Cleaned test cases
 * 170e6beb: Added Dockerfile
 * ef80a04b: updated requirements.txt
 * a52f09da: updated requirements.txt
 * f1adfcb2: updated requirements.txt
 * 7e48e801: Fixed bug #1684312 with suggestion from Wade Rossman - Use shutil.copyfile instead of os.system('cp ...') - Should reduce overhead of os.system() memory usage.
 * ec24037c: Fixed bug #1680682 with patch supplied from Dave Allan - Only specify --pinentry-mode=loopback when --use-agent is not specified * Fixed man page that had 'cancel' instead of 'loopback' for pinentry mode
 * d858f13e: add replicate command - useful to replicate/archive backups to another backend - allows to partially replicate only older backup sets - checks existing backup sets on target to avoid redundant copies
 * b069613e: working on dpbx backend tests§
 * afe9d2f7: Add some commented-out debug print and move under error condition.
 * 34ddd071: working on the READMEs
 * 39455308: worked on the requirements and README
 * c2107af9: Added some experiences to the README
 * f9958d69: Launchpad automatic translations update.
 * 3d419279: Make test_selection.py use unicode string literals and still pass. * funtional/test_selection.py still fails.
 * 3c243b8c: Make path.py only accept unicode. * Make all string literals in test_selection.py unicode. * Create path.uc_name as an alternative to path.name, allowing existing code to continue using bytes during transition. * Make file writes in test_selection.py use io.open. * Tests do not yet pass.
 * 4a7a5875: Make globmatch.py deal with either unicode or string globs. * Make path.uc_name for unicode name of path (vs path.name for bytes). * Functional select test failures.
 * 1ccb1689: test_globmatch.py now passing with unicode globs/paths * test_square_bracket_options_unicode now passing
 * ae323989: glob_to_regex converted to unicode, globmatch.py not yet passing tests
 * f7b9f2b1: Merge in changes to trunk.
 * 62162260: Added future imports to globmatch.py and added future to tox.ini deps.
 * aee790b8: Added (failing) unicode test.
 * d52ea722: Add tests for square brackets.
 * 3ca67813: Add test for unicode paths with asterisks in globs.
 * 2883bfda: Added files with unicode names to testfiles and added TestUnicode.test_unicode_paths_non_globbing, which tests --include and --exclude works as expected with these files.
 * 815dafab: Fixed bug #1668750 - Don't mask backend errors - added exception prints to module import errors
 * 0456d65e: Fixed bug #1668750 - Don't mask backend errors - added exception prints to module import errors
 * c1ef0b73: Fixed bug #1671852 - Code regression caused by revision 1108 - change util.uexc() back to bare uexc()
 * 34ed2ac7: Fixed bug #1671852 - Code regression caused by revision 1108 - change util.uexc() back to bare uexc()
 * a48ee644: Skip pylint on dpbxbackend.py for now.
 * 98b1bca7: Refresh docs
 * f043c106: Merged in p:~aaron-whitehouse/duplicity/pep8_E402_fixes - Fixed PEP8 errors: E402 module level import not at top of file
 * 59e11d3b: Fixed PEP8 errors: E402 module level import not at top of file
 * 82454ae2: Merged in lp:~benoit.bertholon/duplicity/duplicity - Use the globals.archive_dir variable to store only a string in the case of a path, uses globals.archive_dir_path
 * d2d393e7: uses the globals.archive_dir variable to store only a string in the case of a path, uses globals.archive_dir_path
 * c8240211: Fixed bug #1367675 - IMAP Backend does not work with Yahoo server - added the split() as needed in 'nums=list[0].strip().split(" ")' - the other fixes mentioned in the bug report comments were already done
 * 7a1ac495: Fixed bug #1367675 - IMAP Backend does not work with Yahoo server - added the split() as needed in 'nums=list[0].strip().split(" ")' - the other fixes mentioned in the bug report comments were already done
 * 2721e86c: Fixed variable name change in last merge which broke a bunch of tests - Changed archive_dir_root back to archive_dir
 * baf4683a: Merged in lp:~benoit.bertholon/duplicity/duplicity - Fixes bug #1666194 - ProcessCommandLine function called twice fail and arglist argument not used
 * 6f6ac96f: Merged in lp:~aaron-whitehouse/duplicity/pep8_test_fixes - Fix PEP-8 testing by moving to using pycodestyle library. - Temporarily add ignores to allow these tests to pass. - Fix E305 PEP8 errors: expected 2 blank lines after class or function definition, found 1.
 * a5b40d69: Fix minor pep8 issue - line too long.
 * 841bdc9d: Merged in lp:~marix/duplicity/azure-storage-sas - This branch adds support for Shared Access Signature to the Azure backend which allows to run Duplicity with a minimal set of permissions.
 * c36a0fa6: Merged in lp:~marix/duplicity/azure-storage-0.30.0-plus - This makes the Azure backend compatible with version 0.30.0 and up of the underlying azure-storage package.
 * fab4e9d0: Change the global name archive_dir to archive_dir_root add the arglist to the optparser
 * 5d7790bb: Fix E305 PEP8 errors: expected 2 blank lines after class or function definition, found 1 * Remove E305 from pycodestyle ignores
 * b9ce119b: Fix PEP-8 testing by moving to using pycodestyle library. * Temporarily add ignores to allow these tests to pass.
 * d0c485eb: Fix backup creation using azure-storage > 0.30.0
 * 060b3281: Add support for Shared Access Signatures to the Azure backend.
 * 633af2af: Make the Azure backend compatible with azure-storage 0.30.0 and up
 * bfc8810b: Merged in lp:~aaron-whitehouse/duplicity/08-python-futurize-stage-1 - Made many of the safer changes for improved Python 3 support (python-future's futurize -stage1) without functional change to the code (and leaving the isinstance(s, types.StringType) tests unchanged). - Created Python 2/3 compatible tests for int and long. - Update setup.py to show only Python 2.7 support.
 * befa17f8: Update setup.py to show only Python 2.7 support.
 * 2aab33a7: Merge changes from trunk
 * 926ba760: Some fixes to gpg.py to handle gpg1 & gpg2 & gpg2.1 commandline issues - --gpg-agent is optional on gpg1, but on gpg2 it is used automatically - --pinentry-mode is not a valid opt until gpg2.1, so condition on that
 * 10b8aa2f: Fixed bug #1603704 with patch supplied by Maciej Bliziński - Crash with UnicodeEncodeError
 * 734d82dd: Fixed bug #1603704 with patch supplied by Maciej Bliziński - Crash with UnicodeEncodeError
 * 2c1ffb36: Fixed the documentation of --use-agent in the man page
 * 1edbdb7d: merged revision 1270 from lp:duplicity/0.7-series
 * 7840b408: Fixed bug #1657916 with patch supplied by Daniel Harvey - B2 provider cannot handle two backups in the same bucket
 * 6455ee6f: Fixed bug #1657916 with patch supplied by Daniel Harvey - B2 provider cannot handle two backups in the same bucket
 * d967c475: Merged in lp:~aaron-whitehouse/duplicity/08-refactor-unit-test-globmatch - Rename path_matches_glob_fn to select_fn_from_glob, as this more accurately reflects the return value. - Significantly refactored unit/test_globmatch.py to make this cleaner and clearer.
 * a615bbe4: Add detail about import exceptions in onedrivebackend.py
 * fdf9d468: Add detail about import exceptions in onedrivebackend.py
 * 60b4bf99: Rename path_matches_glob_fn to select_fn_from_glob, as this more accurately reflects the return value. * Significantly refactored unit/test_globmatch.py to make this cleaner and clearer.
 * 1400d884: Merged in lp:~aaron-whitehouse/duplicity/08-merge-glob-parsers - Use a single code path for glob strings whether or not these contain special characters/wildcards (glob_get_normal_sf) and remove glob_get_filename_sf and glob_get_tuple_sf. - Remove run-tests-ve as this was identical to run-tests.
 * 0855ee3d: Remove time from run-tests, in case this causes any issues (e.g. cross platform support).
 * af5eaa47: Add more scan tests.
 * 7c57cde5: Removed unused non-globbing code (_glob_get_filename_sf and _glob_get_tuple_sf). * Made run-tests time test runs. * Removed run-tests-ve, which was identical to run-tests.
 * 691d8f33: Move to using single (globing, glob_get_normal_sf) function for glob strings with and without globbing characters. No performance impact.
 * aede8aee: Make globs of "/" work with globbing code. * Make globs of "/" match everything.
 * a2a016eb: Made _glob_get_filename_sf and _glob_get_tuple_sf internal functions to ensure no unit tests depend on them directly.
 * 3832485c: Merged in lp:~matthew-t-bentley/duplicity/duplicity - Sets a user agent. Backblaze asked for this in case there are errors that originate from the Duplicity B2 backend - Only retrieves a new upload URL when the current one expires, to bring it in line with their best practices for integrations: https://www.backblaze.com/b2/docs/integration_checklist.html
 * b8ca51d0: Merged in lp:~matthew-t-bentley/duplicity/duplicity - Sets a user agent. Backblaze asked for this in case there are errors that originate from the Duplicity B2 backend - Only retrieves a new upload URL when the current one expires, to bring it in line with their best practices for integrations: https://www.backblaze.com/b2/docs/integration_checklist.html
 * 09da3ec6: Only get a new upload URL when needed. Add a user agent
 * f449626d: Fixed bug #1658283 "Duplicity 0.7.11 broken with GnuPG 2.0" - Made gpg version check more robust than just major version - Now use --pinentry-mode=loopback on gpg 2.1 and greater - Removed check for non-Linux systems, a false problem
 * 2ed3aa9b: Fix pep8 issue.
 * 437684d8: Fixed bug #1655268 "--gpg-binary option not working" - If gpg binary is specified rebuild gpg profile using new binary location
 * 82621c56: Fixed bug #1655268 "--gpg-binary option not working" - If gpg binary is specified rebuild gpg profile using new binary location
 * ca842259: Futurize -stage1 all files, leaving the isinstance(s, types.StringType) tests unchanged. * Reverted earlier changes to types.StringType test in test files. * Created python 2/3 compatible tests for int and long.
 * 27f1a028: Futurize -stage1 on py files in testing for improved python 2/3 support.
 * 0a92806f: Merged in lp:~aaron-whitehouse/duplicity/0-8-merge_selection_tests - Merge in TestExcludeIfPresent from 0.7-series, which tests the behaviour of duplicity's --exclude-if-present option. - Move and rename TestTrailingSlash2 test (was duplicate name) as in 0.7-series. - Fix PEP error on adbackend.py. - Add jottalib as a tox dep to fix pylint error. - Remove unnecessary skipUnless Linux as per 0.7-series.
 * 48840a0b: Fixed bug #1654220 with patch supplied by Kenneth Newwood - Duplicity fails on MacOS because GPG version parsing fails
 * d4a9c37d: Fixed bug #1654220 with patch supplied by Kenneth Newwood - Duplicity fails on MacOS because GPG version parsing fails
 * bcc923ec: Fixed bug #1623342 with patch supplied by Daniel Jakots - Failing test on OpenBSD because tar/gtar not found
 * bab8cfa1: Fixed bug #1623342 with patch supplied by Daniel Jakots - Failing test on OpenBSD because tar/gtar not found
 * 92235bca: Fix PEP error on adbackend.py. * Add jottalib as a tox dep to fix pylint error.
 * 1ca6251c: Merge in TestExcludeIfPresent from 0.7-series, which tests the behaviour of duplicity's --exclude-if-present option
 * 94c684d9: Move and rename TestTrailingSlash2 test.
 * 800c6935: Merged in lp:~breunigs/duplicity/amazondrive3 - As reported on the mailinglist, if a space is entered while duplicity asks for the URL, it fails. Since all important spaces are URL encoded anyway, this should be fine even if there are spaces in the URL at all. I also patched it in the onedrive backend, because it must have similar issues.
 * bac5f33a: Merged in lp:~breunigs/duplicity/amazondrive3 - As reported on the mailinglist, if a space is entered while duplicity asks for the URL, it fails. Since all important spaces are URL encoded anyway, this should be fine even if there are spaces in the URL at all. I also patched it in the onedrive backend, because it must have similar issues.
 * 8134d711: Fix Bug #1642813 with patch from Ravi - If stat() returns None, don't attempt to set perms.
 * 996bd5a1: Fix Bug #1642813 with patch from Ravi - If stat() returns None, don't attempt to set perms.
 * 108e09f8: Whoops, make a couple of changes to match series-7.
 * f3e43415: Whoops, fix bad patch * Add gpg2 dir to .bzrignore
 * 5a785806: Fix some issues with testing on MacOS * Fix problem with gpg2 in yakety and zesty
 * 0affec8f: Fix problem with gpg2 in yakety and zesty
 * ecd8404e: Some fixes for MAC where gpg2 does not implement --pinentry-mode.
 * 5316be82: Skip locked folders tests if not on Linux platform.
 * a86a9cb3: Merged in lp:~aaron-whitehouse/duplicity/Bug_1624725_files_within_folder_slash - Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters). This preserves the behaviour that an expression ending in "/" only matches a folder, but now the contents of any matching folder is included.
 * 6599b400: Merged in lp:~aaron-whitehouse/duplicity/Bug_1624725_files_within_folder_slash - Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters). This preserves the behaviour that an expression ending in "/" only matches a folder, but now the contents of any matching folder is included.
 * bbdc36fd: Temp fix for tempfile.TemporaryFile failures.
 * 302a5e2b: Fix encryption tests by specifying long key instead of short.
 * a1dfaffc: Merged in lp:~horgh/duplicity/copy-symlink-targets-721599 - Add --copy-links to copy symlink contents, not just the link itself.
 * 2604cf85: Merged in lp:~horgh/duplicity/copy-symlink-targets-721599 - Add --copy-links to copy symlink contents, not just the link itself.
 * 6a63b9a1: Improve description of new argument in man page
 * b82f9cb5: Add new argument to duplicity manpage
 * ec872c82: Add flag to copy target of symlinks rather than the link
 * 988aef92: Merged in lp:~ed.so/duplicity/manpage.fixes - Fix html output via rman on the website
 * 1ec38202: Merged in lp:~ed.so/duplicity/manpage.fixes - Fix html output via rman on the website
 * 4fac9490: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * ac573387: Revert to rev 1246.
 * 096a41d6: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 8a6f6316: Revert to rev 1246.
 * 4f9db163: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 21e6925b: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 07607695: Merged in lp:~dernils/duplicity/robust-dropbox-backend - Added new command line option --backend-retry-delay that allows to determine the time that duplicity sleeps before retrying after an error has occured. - Added some robustness to dpbxbackend.py that ensures re-authentication happens in case that a socket is changed (e.g. due to a forced reconnect of a dynamic internet connection).
 * 3ef44593: Fix bug using 40-char sign keys, from Richard McGraw on mail list - Remove truncation of argument and adjust comments
 * e20383f2: Fix bug using 40-char sign keys, from Richard McGraw on mail list - Remove truncation of argument and adjust comments
 * bbc83e22: fix html output via rman
 * 708ad52e: Merge in changes from trunk.
 * b32e079d: Added tests to ensure behaviour is as expected for expressions containing globs, as these traverse a different code path.
 * 2f2c09f4: minor fix in manpage
 * a5e50289: Added --backend-retry-delay to the manpage
 * 604eaa3a: Fixed bug #1642098 - does not create PAR2 archives when '--par2-options' is used - Missing space between par2-options plus default options
 * 9780e546: Fixed bug #1642098 - does not create PAR2 archives when '--par2-options' is used - Missing space between par2-options plus default options
 * aed5162a: added new command line option --backend-retry-delay
 * 4401adb1: added some robustness to dpbxbackend.py
 * 7ced28de: Merged in lp:~breunigs/duplicity/amazondrive2 - Fixed variable renaming issue
 * eea83340: Fixed Bug #1624725, so that an include glob ending in "/" now includes folder contents (for globs with and without special characters)
 * 24b8d980: fixed missing rename in Amazon Drive backend
 * 6340c8ae: Merged in lp:~breunigs/duplicity/amazondrive - Provide a native backend for AmazonDrive
 * 756796be: Merged in lp:~havard/duplicity/jottacloudbackend - Adds support for a new backend, jottacloud.com, using the scheme `jottacloud:/<folder>`. - Reverse-engineered library, `jottalib`: http://github.com/havardgulldahl/jottalib - Here's how you set up jottalib https://github.com/havardgulldahl/jottalib/wiki
 * b4a4f6da: Fixed bug #1621194 with code from Tornhoof - Do backup to google drive working without a service account
 * 61d36e9f: Fixed bug #1621194 with code from Tornhoof - Do backup to google drive working without a service account
 * c6c08f12: rename to just "AD" to avoid any possible trademark issues
 * 8f945f92: Merged in lp:~mwilck/duplicity/duplicity - GPG: enable truly non-interactive operation with gpg2 - This patch fixes the IMO unexpected behavior that, when using GnuPG2, a pass phrase dialog always pops up for saving backups. This is particularly annoying when trying to do unattended / fully automatic backups.
 * db3e4ddf: Merged in lp:~mwilck/duplicity/duplicity - GPG: enable truly non-interactive operation with gpg2 - This patch fixes the IMO unexpected behavior that, when using GnuPG2, a pass phrase dialog always pops up for saving backups. This is particularly annoying when trying to do unattended / fully automatic backups.
 * 3e9f18b4: document peculiarities of AmazonDrive
 * 504582c7: add and document native AmazonDrive backend
 * 12f7dd9e: Added inline comment to globmatch.py explaining glob matching. * Removed trailing / from Path() unittests, as paths used in duplicity do not normally have these, even if they are folders. * Added unit test to show files within a matched folder are included without a trailing slash. * Fixed return value of test_slash_star_scans_folder unittest from include to scan.
 * bcbaaecd: Add unittests and code comments to explain glob processing/regex behaviour.
 * 85a2fd05: GPG: enable truly non-interactive operation with gpg2
 * a3d2a830: Add more tests for trailing slash behaviour.
 * 5627cdae: Added (failing) test to show behaviour in Bug #1624725
 * 52f23232: Fixed bug #1623342 with patch from Daniel Jakots - failing test on OpenBSD because tar/gtar not found
 * 504c6695: Fixed bug #1623342 with patch from Daniel Jakots - failing test on OpenBSD because tar/gtar not found
 * fc5cc01f: Merged in lp:~aaron-whitehouse/duplicity/bug_1620085_exclude-if-present-locked-folder - Fixes Bug #1620085: --exclude-if-present gives OSError looking for tag in locked folders
 * 8d61f9d9: remove uses_netloc directive
 * d214849a: JottaCloudBackend: Don't return bytestrings in _list()
 * 1f8cf169: Adding JottaCloud backend
 * 4b71ccaa: Fixed bug #1620085: OSError when using --exclude-if-present with a locked directory in backup path. * Added tests for errors on locked files.
 * 258ffdb2: Add functional tests for --exclude-if-present.
 * d1b4cc58: Move and rename second TestTrailingSlash block to TestTrailingSlash2.
 * 853e1b4b: Add requirements.txt - Remove module mocks in conf.py
 * 9cc3f0f2: OK, finally grokked how to mock out _librsync, but it did mean having to change librsync.py with a conditional. Would have preferred a cleaner solution. - Fixed the remaining warnings in READTHEDOCS build, including the removal of a couple of files that were extraneous.
 * 32011970: Try autodoc_mock_imports...
 * afc6e9ae: Try autodoc_mock_imports...
 * 27ec8a7f: Try autodoc_mock_imports...
 * b512dc18: Try fully qualified module name, again.
 * 39c49814: Remove fully qualified name.
 * cc110e6a: Resolve recursion in Mock.
 * 03991aae: Try fully qualified and not qualified module names.
 * c5a8ea74: Try without _librsync.
 * bac86efb: Try fully qualified module name.
 * 5226d7e7: Try with virtualenv.
 * 885498a7: Try again...
 * 20271a44: Mock sucks, big time!
 * 66592f03: Mock sucks, big time!
 * 31a0b938: Mock sucks!
 * 0e4015d5: Try MagicMock.
 * ff178e9a: Try MagicMock.
 * dd573593: Fix build on RTD.
 * 7f27522d: Fix build on RTD.
 * 302c6d7f: Fix build on RTD.
 * e36df243: Fix build on RTD.
 * 811174f2: Fix build on RTD.
 * 7c746284: Remove _build dir from git. Fix some names, authors.
 * 77874763: Merged in lp:~mstoll-de/duplicity/duplicity - Backblaze announced a new domain for the b2 api
 * 4da1f3c9: Merged in lp:~mstoll-de/duplicity/duplicity - Backblaze announced a new domain for the b2 api
 * f37f8e00: Fixed bugs #815510 and #1615480 - Changed default --volsize to 200MB
 * e9cb5c33: Fixed bugs #815510 and #1615480 - Changed default --volsize to 200MB
 * 55712fd4: First pass at some Sphinx docs for moving to readthedocs.org
 * eef444be: Merged in lp:~fenisilius/duplicity/acd_init_mkdir - Allow duplicity to create remote folder
 * 5ca8a194: Merged in lp:~fenisilius/duplicity/acd_init_mkdir - Allow duplicity to create remote folder
 * 5fca1c44: Fixed bug #1612472 with patch from David Cuthbert - Restore from S3 fails with --with-prefix-archive if prefix includes '/' * Merged in lp:~arashad.ahamad/duplicity/duplicity_latest - Changes for connecting to IBM Bluemix ObjectStorage. See man page.
 * de408708: Merged in lp:~arashad.ahamad/duplicity/duplicity_latest - Changes for connecting to IBM Bluemix ObjectStorage. See man page.
 * 986b663c: Fixed bug #1612472 with patch from David Cuthbert - Restore from S3 fails with --with-prefix-archive if prefix includes '/'
 * 0899a9a8: Added documentation for connecting to IBM Bluemix ObjectStorage
 * 36dc2014: Added support to connect IBM Bluemix ObjectStorage
 * 2fa3afdd: Restore testing/gnupg/gpg.conf and testing/gnupg/README.
 * b912fdee: Whoops, committed too much!
 * 4fcd098b: Fixed conflict in merge from Martin Wilck and applied - https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301492 - merge fixes setsid usage in functional testing.
 * ad533083: Fixed conflict in merge from Martin Wilck and applied - https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301492 - merge fixes setsid usage in functional testing.
 * b54e2a57: Remove -w from setsid in functional tests.
 * f0d4f0a6: Merged in lp:~mwilck/duplicity/duplicity - Speedup of path_matches_glob() by about 8x. See https://code.launchpad.net/~mwilck/duplicity/duplicity/+merge/301268 for more details.
 * 81483199: Merged in lp:~mwilck/duplicity/0.7-series - Speedup of path_matches_glob() by about 8x. See https://code.launchpad.net/~mwilck/duplicity/0.7-series/+merge/301332 for more details.
 * ae2ca117: Fix unit test failures for {Old,Short}FilenamesFinalTest
 * dd75a6f9: Fix failures of unit tests with --hidden-encrypt-key
 * f94a306d: selection.py: use closure for matching paths with glob expressions
 * 86827d41: selection.py: glob_get_normal_sf: use closure path_matches_glob_fn
 * b1ddf387: globmatch: path_matches_glob_fn: return closure for path match
 * 0ce2edcf: Merged in lp:~aaron-whitehouse/duplicity/07-fix_deja_dup_error_on_locked_files - Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (e.g. deja dup; Bug #1605939).
 * c9ce84a5: Merged in lp:~aaron-whitehouse/duplicity/07-fix_deja_dup_error_on_locked_files - Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (e.g. deja dup; Bug #1605939).
 * d6977486: Revert log.Error to log.Warn, as it was prior to the merge in rev 1224, as this was affecting other applications (deja dup).
 * ab61d44a: Fixed bug #1600692 with patch from Wolfgang Rohdewald - Allow symlink to have optional trailing slash during verify.
 * 89480ad4: Fixed bug #1600692 with patch from Wolfgang Rohdewald - Allow symlink to have optional trailing slash during verify.
 * 75575fe1: Merged in lp:~aaron-whitehouse/duplicity/remove-python26 - Remove Python 2.6 support references and tests.
 * 2bdfcb31: Fix date in CHANGELOG. Release date was 2016-07-02, not 01.
 * 643b85ec: Fix date in CHANGELOG. Release date was 2016-07-02, not 01.
 * 4802af3d: Remove import of unittest2 for Python <2.7, now that Python 2.7 is the minimum version.
 * 4ffed34b: Remove Python 2.6 settings from tox.ini
 * ca63ac7d: Merge with trunk.
 * 628ba0ee: Changes from 0.7.08
 * 3c78a4e7: Merged in lp:~aaron-whitehouse/duplicity/PEP8_W503_fixes - Fix PEP8 W503 errors (line break before binary operator) and enable the PEP8 test for this in test_code.CodeTest. * Merged in lp:~aaron-whitehouse/duplicity/PEP8_line_length - Set line length error length to 120 (matching tox.ini) for PEP8 and fixed E501(line too long) errors. * Merged in lp:~duplicity-team/duplicity/po-updates
 * 0bd37cc4: Properly remove line too long errors (E501) from PEP8 ignores.
 * 7c0a0601: Fixed lines longer than 120 chars.
 * 75f44379: Set line length error length to 120 (matching tox.ini) and fixed PEP8 E501(line too long) errors.
 * 6b6e9abf: Fix PEP8 W503, line break before binary operator.
 * 70216f8a: Remove Python 2.6 support from the test suite and references to it from README and README-REPO.
 * a6ae75e0: Merge 0.7-series changes to README-REPO.
 * c44227b5: Merge 0.7 series changes to README
 * b25f954f: Merge 0.7 series changes to tox.ini
 * 0bb6379b: Fixed bug #1594780 with patches from B. Reitsma - Use re.finditer() to speed processing
 * a04231ee: Merged in lp:~aaron-whitehouse/duplicity/fix_stat_errors - Only give an error about not being able to access possibly locked file if that file is supposed to be included or scanned (i.e. not excluded). Fixes Bug #1089131
 * c62e273b: Fixed README-REPO to no longer mention 0.6-series
 * c3c7b50d: Only give an error about not being able to access possibly locked file if that file is supposed to be included or scanned (i.e. not excluded).
 * 75712a46: Fixed bug #822697 ssh-options not passed in rsync over ssh - Added globals.ssh_options to rsync command line * Increased default volume size to 200M, was 25M
 * cf92c3c2: Merged in lp:~aaron-whitehouse/duplicity/fix_pep8 - Fix PEP8 error in onedrivebackend.py (space before bracket)
 * d642a0d4: Fix PEP8 error in onedrivebackend.py (space before bracket).
 * d9ee1a17: Fix pep8 issues from last two patch sets.
 * c565f06d: Merged in lp:~mstoll-de/duplicity/b2-reauth - Fixes bug #1588503 b2: large uploads fail due to expired auth token
 * b0dca827: Fixed bug #1589038 with patches from Malte Schröder - Added ignore_case option to selection functions
 * 9bfc42fa: b2 reauth: use other log level
 * 928f188e: Handle expired auth token
 * c2a412b4: Fixed bug #1586992 with patches from Dmitry Nezhevenko - Patch adds _delete_list to Par2Backend. And _delete_list fallbacks to _delete calls if wrapped backend has no _delete_list.
 * 3949daff: Fixed bug #1586934 with patches from Dmitry Nezhevenko - fixes error handling in wrapper
 * 0e512463: Fixed bug #1573957 with patches from Dmitry Nezhevenko - upload last chunk with files_upload_session_finish to avoid extra request - upload small files using non-chunked api
 * 8b9df748: Merged in lp:~ghoz/duplicity/swift-prefix - adds the abiliy to use path in the swift backend, in order to have multiple backups to the same container neatly organized.
 * 5fb7b933: Adds prefix support to swift backend
 * 66de12b5: Merged in lp:~noizyland/duplicity/fix_azurebackend_typo - Fix typo in error handling code
 * 56a249ef: Fix typo in error handling code.
 * 9afe9cdc: Add missing build-dep apparently now not installed by default with python2 in xenial+
 * a6c632cc: Fixed bug #1570293 - removed flush() after write. - revert to previous version
 * 4791057c: Fixed bug #1571134 and #1558155 - used patch from https://bugs.debian.org/820725 but made changes to allow the user to continue using the old version
 * 63481d30: Remove unused (default) argument.
 * 96a52837: Fixed bug #1569523 - bug introduced in improper fix of bug #1568677 - gotta love those inconsistent APIs
 * 46d5dec0: Blasted JIT imports got me again!
 * fa2e1117: Fixed bug #1568677 - bug introduced by incomplete fix of bug 1296793 - simplified setting of bucket locations
 * 7bcc6635: Fixed bug 1568677 with suggestions from Florian Kruse - bug introduced by incomplete fix of bug 1296793
 * f7496854: Merged in lp:~duplicity-team/duplicity/po-updates
 * 01134968: Launchpad automatic translations update.
 * 928efc08: Fix bug reported on the mailing list from Mark Grandi (assertion error while backing up). In file_naming.parse() the filename was being lower cased prior to parsing. If you had used a prefix with mixed case, we were writing the file properly, but could not find it in the backend.
 * 617e33b7: Merged in lp:~aaron-whitehouse/duplicity/split_glob_matching_from_select - Move glob matching code out of selection.py's Select function and into globmatch.py.
 * 803f2e28: Re-added import of re, as re.compile still used in selection.py.
 * 015f19c5: Move complexity of matching paths to globs into globmatch.py path_matches_glob, rather than in selection.py Select.
 * 9dc4b19c: Merged in lp:~aaron-whitehouse/duplicity/improve_present_get_sf_man_page - Improve man page entry for --exclude-if-present
 * 2c59a455: Move ignorecase handling out of re.compile to use .lower() instead.
 * 0e0bdf1f: Remove glob_get_prefix_res from selection.py, now that it has moved to globmatch.py.
 * c755ede2: Move content of glob_get_prefix_res to globmatch.py glob_get_prefix_regexs.
 * 36b748a2: Improve man page entry for --exclude-if-present
 * a46f8cb1: Fixed globmatch tests. Tests pass.
 * 67148780: Resync with trunk.
 * a3285c69: Move glob_to_re to globmatch.py. Moved associated tests into test_globmatch.py.
 * 69e97350: Applied patch from Dmitry Nezhevenko to upgrade dropbox backend: update to SDK v2 - use chunked upload
 * f44fa10b: More fixes to dist/makedist to make it more OS agnostic. * Merged in lp:~ed.so/duplicity/webdav.lftp.ssl-overhaul duplicity.1, commandline.py, globals.py - added --ssl-cacert-path parameter backend.py - make sure url path component is properly url decoded, in case it contains special chars (eg. @ or space) lftpbackend.py - quote _all_ cmd line params - added missing lftp+ftpes protocol - fix empty list result when chdir failed silently - added ssl_cacert_path support webdavbackend.py - add ssl default context support for python 2.7.9+ (using system certs eg. in /etc/ssl/certs) - added ssl_cacert_path support for python 2.7.9+ - gettext wrapped all log messages - minor refinements
 * 81611555: path may be unset
 * add32b34: duplicity.1, commandline.py, globals.py - added --ssl-cacert-path parameter backend.py - make sure url path component is properly url decoded, in case it contains special chars (eg. @ or space) lftpbackend.py - quote _all_ cmd line params - added missing lftp+ftpes protocol - fix empty list result when chdir failed silently - added ssl_cacert_path support webdavbackend.py - add ssl default context support for python 2.7.9+ (using system certs eg. in /etc/ssl/certs) - added ssl_cacert_path support for python 2.7.9+ - gettext wrapped all log messages - minor refinements
 * 36b0a8e7: Reverted changes made in rev 1164 w.r.t. getting the source from VCS rather than local directory. Fixes bug #1548080.
 * a1161693: Move the logic of the glob_to_re method into the glob_to_regex function in globmatch.py.
 * 93aa03bd: Launchpad automatic translations update.
 * ad074a27: Merged in lp:~rye/duplicity/mediafire - Backend for https://www.mediafire.com - Requires https://pypi.python.org/pypi/mediafire/ installed.
 * 7236b401: Backed out changes made by patching for bug #1541314. These patches should not have been applied to the 0.7 series.
 * ca3dbff4: Added acdclibackend.py from Stefan Breunig and Malay Shah - renamed from amazoncloudbackend to stress use of acd_cli * Fixed some 2to3 and Pep8 issues that had crept in
 * 2b9da532: Merged in lp:~harningt/duplicity/multibackend-mirror - This changeset addresses multibackend handling to permit a mirroring option in addition to its "stripe" mode to make it a redundancy tool vs space-expansion tool. To do this without changing the configuration too much, I used the query string that would generally go unused for files to specify behavior that applies to all items inside the configuration file.
 * c37502e2: Fixed bug 1474994 Multi backend should offer mirror option - added query parameter option to multi-backend - added mode parameter to alter how the backend list is operated on (mirror/stripe) - added onfail parameter to alter how backend failure is handled - updated man-page with documentation
 * dad54f89: Checkpoint, merge latest.
 * ab567e18: Use built-in username/password support in backends.py.
 * 7b44bb65: Remove custom logging, add usage info.
 * fe15531d: Merge changes from trunk.
 * 976fdc71: Fixed a patching error in ssh_pexpect_backend.py * Merged in lp:~fpytloun/duplicity/webdav-gssapi-fix - Make kerberos optional for webdav backend
 * f69c567c: Make kerberos optional for webdav backend
 * aceb2aa8: Launchpad automatic translations update.
 * 2d019468: Applied patch from kay-diam to fix error handling in ssh pexpect, fixes bug #1541314
 * fd716e55: Fix bug #1540279 - mistake in --help
 * 527a1827: Clean up pep8 issues.
 * 5bd26830: Launchpad automatic translations update.
 * e6ff1efb: Fix for bug #1538333 - assert filecount == len(self.files_changed) - added flush after every write for all FileobjHooked files which should prevent some errors when duplicity is forcibly closed.
 * d0cfccca: Add more pylint ignore warnings tags * Adjust so test_restart.py can run on Mac as well
 * 0f278926: Merged in lp:~fpytloun/duplicity/webdav-gssapi - support GSSAPI authentication in webdav backend
 * c1863b1c: Support GSSAPI authentication in webdav backend
 * 985cced7: Launchpad automatic translations update.
 * 6ec9575a: Checkpoint,merge in current changes.
 * 134281ef: Fix submitter name in changelogs. - Change comment to be correct.
 * 60761e5d: Fixed bug #1492301 with patch from askretov (manually refresh oauth).
 * d0bf7d7a: Fixed bug #1379575 with patch from Tim Ruffling (shorten webdav response).
 * 14052b49: Fixed bug #1375019 with patch from Eric Bavier (home to tmp).
 * fc8e0576: Fixed bug #1369243 by adjusting messages to be more readable.
 * c7be51a0: Fixed bug #1260666 universally by splitting the filelist for delete before passing to backend.
 * 478a84a4: Pep8 corrections for recently released code.
 * 2cccd9ad: Merged in lp:~mifchip/duplicity/duplicity - fix bug #1313964, absolute path doesn't work for FTP
 * 133e2e93: Bug #1313964 fix. lstrip('/') removed all the slashes, it was an issue.
 * 5e52bcb3: Fixed bug #1296793 - Failed to create bucket - use S3Connection.lookup() to check bucket exists - skips Boto's Exception processing for this check - dupe of bug #1507109 and bug #1537185
 * 6d087451: Checkpoint,merge in current changes.
 * f3e2186b: Create folder recursively
 * a469aa92: Use upload session context manager
 * 91d4f8c9: Applied changes from ralle-ubuntu to fix bug 1072130. - duplicity does not support ftpes://
 * 0b6ff26f: Allow importing module, but fail on init
 * c7cf0c30: MediaFire Backend - initial version
 * cd6b4b5f: Undo changes to test_restart.py. GNU tar is needed. * Fix minor pep8 nit in collections.py
 * 6dca915e: Applied patch from abeverly to fix bug #1475890 - allow port to be specified along with hostname on S3 - adjusted help text and man page to reflect the change
 * 8ef955f6: Launchpad automatic translations update.
 * a31ddfe7: Applied patch from shaochun to fix bug #1531154, - --file-changed failed when file contains spaces
 * c072e977: Fix stupid issue with functional test path for duplicity
 * e8e265aa: Make test_restart compatible with both GNUtar and BSDtar
 * d23eed28: Partial fix for bug #1529606 - shell code injection in lftpbackend - still need to fix the other backends that spawn shell commands
 * 1c3b1cf5: Random stuff: supply correct path for pydevd under Mac - fix some tests to run under Mac as well
 * 622f1a06: Checkpoint: remove RPM stuff from makedist - have makedist pull directly from VCS, not local dir - update po translation directory and build process - clean up some odd error messages - move Pep8 ignores to tox.ini
 * e50dea6f: Checkpoint: remove RPM stuff from makedist - have makedist pull directly from VCS, not local dir - update po translation directory and build process - clean up some odd error messages - move Pep8 ignores to tox.ini
 * 7581d295: 2to3 cleanup.
 * 9ceac23f: Pep8 cleanup.
 * 2b917d21: Fix date.
 * 860a6dd0: Merged in lp:~matthew-t-bentley/duplicity/b2 - A couple fixes allowing multiple backups to be hosted in different folders in the same bucket as well as some logging for -v9.
 * 6bdc912f: Make sure listed files are exactly in the requested path Thanks to Andreas Knab <knabar@gmail.com> for the pull request
 * cccb718c: Set fake (otherwise unused) hostname for prettier password prompt Thanks to Andreas Knab <knabar@gmail.com> for the patch
 * aa47b91f: Add debugging for b2backend
 * af89609f: Merged in lp:~matthew-t-bentley/duplicity/b2 - Allow multiple backups in the same bucket. - Fixes #1523498.
 * 2d2ec83e: Allow multiple backups in the same bucket
 * 08a86ebe: Merged in lp:~matthew-t-bentley/duplicity/b2 - Fix import and error typos.
 * 1397a1f7: Merge and re-add missing error
 * cba442a5: Fix missing import and typos
 * 92c8de65: Merge from upstream
 * 4ae00a13: Merged in lp:~matthew-t-bentley/duplicity/b2 - Adds a backed for BackBlaze's (currently beta) B2 backup service. - This adds backends/b2backend.py, modifies log.py to add an error code and modifies commandline.py to add the b2:// example to the help text. * Fix perms on duplicity/backends/multibackend.py
 * 593569df: Undo changes to po files
 * f1d502b3: Remove unnecessary requirements section in manpage
 * 11c6d955: Merged in lp:~noizyland/duplicity/azurebackend-fixes - Support new version of Azure Storage SDK - Refactor _list method to support containers with >5000 blobs
 * 21495794: Documentation
 * 5140a452: Merge from master
 * ff7bbd35: Add help text for b2
 * cd8c3585: Add basic error handling
 * dac0b75b: Support new version of Azure Storage SDK * Refactor _list method to support containers with >5000 blobs
 * 96081f0a: Make sure which() returns absolute pathname.
 * e3408a41: Remove some print statements.
 * 365be9e7: Fix bug #1520691 - Shell Code Injection in hsi backend - Replace use of os.popen3() with subprocess equivalent. - Added code to expand relative program path to full path. - Fix hisbackend where it expected a list not a string.
 * 92689752: Add BackBlaze B2 backend. Still needs some work (error handling, etc)
 * aea12f7a: Fix missing self.
 * 97cd948d: Fix bug #1520691 - Shell Code Injection in hsi backend - Replace use of os.popen3() with subprocess equivalent.
 * 8b6b88dd: Merged in lp:~feraudet/duplicity/fix - Fix missing SWIFT_ENDPOINT_TYPE env var, bug 1519694.
 * 0556a1ab: Fix #1519694
 * 63b81445: Merged in lp:~michal-s/duplicity/duplicity - Fix azurebackend storage class import
 * dd6bcc79: debugged storage class import
 * f23b85c4: Fixed bug #1511308 - Cannot restore no-encryption, no-compression backup - Corrected code to include plain file in write_multivolume() - Added PlainWriteFile() to gpg.py
 * 2861c1dc: Merged in lp:~ed.so/duplicity/tempfile.tempdir - make sure packages using python's tempfile create temp files in duplicity's temp dir
 * c5f4d543: make sure packages using python's tempfile create temp files in duplicity's temp dir
 * 18617ce0: Reversed previous changes to lockfile. Now it will take any version extant in the LP build repository. (PyPi is not avail in LP build).
 * 654545ea: Reversed previous changes to lockfile. Now it will take any version extant in the LP build repository. (PyPi is not avail in LP build).
 * d0cb8ac1: Try adding spaces.
 * 335b975e: Try lockfile>=0.11.0 (use full version number).
 * 19d349e5: Revert last change.
 * 2c942bd1: Try lockfile==0.11.0 instead of lockfile>=0.9
 * e1f357ee: Merged in lp:~michal-s/duplicity/duplicity - WindowsAzureMissingResourceError and WindowsAzureConflictError changed due to SDK changes.
 * 13b2be76: WindowsAzureMissingResourceError and WindowsAzureConflictError classes changed due to SDK changes
 * 61b7f64b: Cleanup issues around Launchpad build, mainly lockfile >= 0.9.
 * 9d177145: Merged in lp:~ed.so/duplicity/setup.shebang - Having the python interpreter searched in the PATH is much more flexible than the /usr/bin/python inserted into our scripts shebang by setuptools. This patch prevents that. don't touch my shebang! :)
 * 5c2f0c70: Modded tox.ini to use the latest lockfile.
 * 99e7f6f4: also check python version number upper bound. we run on 2.6 and 2.7 currently
 * 7049c83f: Applied patch from Alexander Zangerl to update to changes in lockfile API 0.9 and later. Updated README to notify users.
 * e6cd24ac: don't touch my shebang
 * 7e807390: Add __pycache__.
 * 4c0e3e4b: Upgrade to newest version of pep8 and pylint. Add three ignores to test_pep8 and one to test_pylint to get the rest to pass. They are all valid in our case.
 * f983c746: Fix header date.
 * d1e47ac7: The ptyprocess module no longer supports Python 2.6, so fix tox.ini to use an older version. Make explicit environs for all tests.
 * 578a3000: Merged in lp:~mnjul/duplicity/s3-infreq-access - This adds support for AWS S3's newly announced Infrequent Access storage class and is intended to implement Blueprint: https://blueprints.launchpad.net/duplicity/+spec/aws-s3-std-ia-class . - A new command line option, --s3-use-ia, is added, and boto backend will automatically use the correct storage class value depending on whether --s3-use-rrs and --s3-use-ia is set. Command line parser will prompt error if both --s3-use-ia and --s3-use-rrs are used together, as they conflict with each other. - The manpage has been updated giving a short explanation on the new option. Its wording derives from Amazon's official announcement: https://aws.amazon.com/about-aws/whats-new/2015/09/announcing-new-\ amazon-s3-storage-class-and-lower-glacier-prices/
 * 6e842ecc: Add support for AWS S3 Standard - Infrequent Access storage class
 * 5560909f: Merge changes from trunk.
 * 1478924f: Merged in lp:~bmerry/duplicity/pydrive-id-cache - This fixes the issue a number of users (including myself) have been having with duplicity creating files with duplicate filenames on Google Drive. It keeps a runtime cache of filename to object ID mappings, so that once it has uploaded an object it won't be fooled by weakly consistent directory listings.
 * 7eeebb03: Fix up broken merge
 * 18e53be3: Merge in master
 * d5e31752: Add more logging info
 * 58921fc0: Fix bug #1494228 CygWin: TypeError: basis_file must be a (true) file - The problem that caused the change to tempfile.TemporaryFile was due to the fact that os.tmpfile always creates its file in the system temp directory, not in the directory specified. The fix applied was to use os.tmpfile in cygwin/windows and tempfile.TemporaryFile in all the rest. This means that cygwin is now broken with respect to temp file placement of this one file (deleted automatically on close).
 * 3a23b29b: Fix bug #1493573. Correct option typo in man page.
 * 98483d0e: Updated man pages to reflect more contributors.
 * d482620e: Sync with v0.7.
 * d282298a: Merged in lp:~germar/duplicity/par2removefix - After reorganisation in revision 981 and the fix for bug #1406173 the par2backend does not remove .par2 files anymore when removing duplicity-*.gpg files. - This banch adds an unfiltered_list() method which is used in delete() and delete_list()
 * 710a9648: par2 backend remove par2 files
 * 4862d3ca: Merged in lp:~w.baranowski/duplicity/selection_debug - This little patch logs debug messages concerning path selection process, and so allows users to debug their include/exclude configuration.
 * c086efd6: Added debug msgs to the routine checking path selection
 * 01dc76af: Refactored the selection.Select.Select method; fewer exit points now
 * ded95170: Fixed Bug 1438170 duplicity crashes on resume when using gpg-agent with patch from Artur Bodera (abodera). Applied the same patch to incremental resumes as well.
 * 3d797ad9: Launchpad automatic translations update.
 * 7008e2ae: Merged in lp:~aaron-whitehouse/duplicity/disable_code_tests_for_lpbuildd - Set RUN_CODE_TESTS to 0 for lpbuildd tox profile, reflecting its value on the Launchpad build server (and therefore skipping PEP8, 2to3 and pylint). More accurately reflects the system we are mimicking and saves approximately 1 minute per test run.
 * 7728b5eb: Rename tox profile for Launchpad's Precise build server to "lpbuildd-precise" for clarity (and to make it clear it should be removed once Precise is no longer supported).
 * b7c7ef9a: Set RUN_CODE_TESTS to 0 for lpbuildd tox profile, reflecting its value on the Launchpad build server (and therefore skipping PEP8, 2to3 and pylint). More accurately reflects the system we are mimicking and saves approximately 1 minute per test run.
 * d912d18c: Merged in lp:~aaron-whitehouse/duplicity/launchpad_tox_profile - Add tox testing profile that mimics the packages installed on the Launchpad build server, to reduce the likelihood of tests passing our test suite, but failing on the build server (e.g. because of the out-of-date mock version).
 * 44d6c8a3: Fixed Bug 1476019 S3 storage bucket not being automatically created with patch from abeverley
 * 86188a9c: Fixed Bug 1476019 S3 storage bucket not being automatically created with patch from abeverley
 * 613ec3ee: Add further instructions in README-REPO on how to test against one environment.
 * 4f5b303b: Add lpbuilldd as an additional tox profile, replicating the setup of the launchpad build server.
 * 3137b303: Merged in lp:~aaron-whitehouse/duplicity/fix_patch_error - Change use of mock.patch in unit tests to accommodate the obsolete version of python-mock on the build server.
 * edec989f: Change use of mock.patch to accommodate the obsolete version of python-mock on the build server (and avoid the following error: TypeError: patch() got an unexpected keyword argument 'return_value' )
 * 172463df: Merged in lp:~aaron-whitehouse/duplicity/fix_2to3_issues - Fixed 2to3 issues. Updated README-REPO with more test information. Updated pylint and test_diff2 descriptions to make it clear these require packages to be installed on the sytem to pass. All tests pass on Python 2.6 and Python 2.7 as at this revision.
 * 6deea84c: Merged in lp:~dag-stenstad/duplicity/swift_authversion_3_support - Added support for Openstack Identity v3 in the Swift backend.
 * 0dfc1c61: Fixed 2to3 issues. Updated README-REPO with more test information. Updated pylint and test_diff2 descriptions to make it clear these require packages to be installed on the system to pass. All tests pass on Python 2.6 and Python 2.7 as at this revision.
 * 7d371d62: Added support for Identity v3.
 * abd25de9: Merged in lp:~aaron-whitehouse/duplicity/improve_tox_and_python2-6_testing - Testing improvements, particularly in relation to testing against Python version 2.6: tox.ini fixed so that it is possible to run individual tests against both Python 2.6 and 2.7; * updated test_code.py to use unittest2 for Python versions < 2.7 (instead of failing); * ./run-tests now correctly runs all tests against both Python 2.6 and 2.7; and * improved testing directions in README-REPO.
 * 94a49ec8: Merged back to trunk.
 * 896ed7a2: Delete redundant second sys import in test_code.py.
 * 00afa726: Fixed tox.ini to correctly run individual tests. Updated test_code.py to use unittest2 for Python versions < 2.7 (instead of failing). Improved testing directions in README-REPO.
 * 309e6320: Merged in lp:~aaron-whitehouse/duplicity/trailing_slash_match_dirs - Made globs with trailing slashes only match directories, not files, fixing Bug #1479545.
 * 82870b12: Made globs with trailing slashes only match directories, not files, fixing Bug #1479545.
 * 941febca: Added functional unittests to exhibit current behaviour of trailing slashes in globs. See Bug #1479545.
 * f40f0866: Merged in lp:~aaron-whitehouse/duplicity/reenable_tests - Re-enable unit.test_selection tests that had been temporarily commented out.
 * 2b7349e9: Re-enable tests that had been temporarily commented out.
 * 1fc62707: Merged in lp:~aaron-whitehouse/duplicity/bug_884371 - Fixed Bug #884371 - Stopped an exclude glob trumping an earlier scan glob, but also ensured that an exclude glob is not trumped by a later include. This fix is important, as without it files that are specified to be included are not being backed up as expected. - Fixed Bug #932482 - a trailing slash at the end of globs no longer prevents them working as expected.
 * f86a0740: Add test_glob_re unit test back in.
 * 485e45c0: Remove unnecessary use of mock.patch in unit.test_selection.py.
 * a9135d6f: Remove special casing for final glob in glob list as no longer necessary.
 * d8634bdb: Fixed Bug #932482 by checking for a trailing slash in each glob and removing it if present. Enabled tests checking this behaviour. PEP8 fixes along the way.
 * bfb96cfd: Stopped an exclude glob trumping an earlier scan glob, but also ensured that an exclude glob is not trumped by a later include. Fixed Bug #884371. Activated the (expectedFailure) tests that were failing because of this bug.
 * cd4203df: Additional tests to exhibit current exclude/scan interaction and implement two functional tests as unit tests.
 * 46226977: Added unit tests for negative square brackets ([!a,b,c] and [!1-4]).
 * 936cffb7: Added test cases (unit and functional) to test the current behaviour of selection.py.
 * 5a2fe8fc: Fixed bug 1471348 Multi back-end doesn't work with hubiC (again) - hubiC should reach up to duplicity.backend.__init__
 * 308960c6: Fixed bug 1471348 Multi back-end doesn't work with hubiC - added init of appropriate superclass in both cases.
 * 406fc410: Merged in lp:~aaron-whitehouse/duplicity/reactivate_progress_test - Re-enable the test of the --progress option (test_exclude_filelist_progress_option), which was marked as an expected failure. The issue causing this test to fail was fixed in revision 1095 and the test now passes.
 * d32c8895: Merged in lp:~aaron-whitehouse/duplicity/fix_POTFILES.in_and_run-tests - Fixed two filename references in po/POTFILES.in, a mistake which crept in in rev 1093 and caused testing/run-tests to fail with "IndexError: list index out of range".
 * a2bd3b16: Fixed two filename references in po/POTFILES.in, a mistake which crept in in rev 1093 and caused testing/run-tests to fail with "IndexError: list index out of range".
 * 6a4b7ae2: Re-enable the test of the --progress option (test_exclude_filelist_progress_option), which was marked as an expected failure. The issue causing this test to fail was fixed in revision 1095 and the test now passes.
 * 87e5b4df: Merged in lp:~ed.so/duplicity/gpg.binary - new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * eff9cf33: Merged in lp:~ed.so/duplicity/gpg.binary - new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * 8f5dfd5a: new parameter --gpg-binary allows user to point to a different gpg binary, not necessarily in path
 * f93b73c9: Fixed bug 1466582 - reduce unnecessary syscall with --exclude-if-present - with patch from Kuang-che Wu to make sure resulting path is a directory.
 * 1fe73a19: Fixed bug 1466582 - reduce unnecessary syscall with --exclude-if-present - with patch from Kuang-che Wu to make sure resulting path is a directory.
 * 05f82469: Fix missing argument in _error_code
 * 2e07af43: Fixed bug 1466160 - pydrive backend is slow to remove old backup set - with patch from Kuang-che Wu to implement _delete_list().
 * ca93dac6: Fixed bug 1466160 - pydrive backend is slow to remove old backup set - with patch from Kuang-che Wu to implement _delete_list().
 * dc44ebac: Fixed bug 1452263 - par2 option not working on small processors - with patch from Kuang-che Wu to ignore default 30 second timeout.
 * f905b999: Fixed bug 1465335 - pydrive still use files in trash can - with patch from Kuang-che Wu to ignore trashed files.
 * c6095a89: Add an ID cache to the PyDrive backend.
 * 92babc5c: Fixed bug 791794 - description of --gpg-options is misleading, Simply needed to add the '--' before the options as in "--opt1 --opt2=parm".
 * 8f85ba05: Fix a couple of PEP8 glitches.
 * 07d695cf: Merged in lp:~raymii/duplicity/fix-swiftbackend-max-10000-files-in-list - Swiftclient by default returns at max 10000 files. By adding full_listing=True we make sure all objects are returned. Ref: https://lists.nongnu.org/archive/html/duplicity-talk/2015-05/msg00060.html and http://docs.openstack.org/developer/python-swiftclient/swiftclient.html#swiftclient.client.get_container
 * dbcc35d1: Merged in lp:~ed.so/duplicity/gdocs.pydrive - make pydrive new gdocs default backend - keep gdata backend as gdata+gdocs://
 * 507b2b71: Add full_listing=True so that swiftclient returns more than 10000 objects. Default is False.
 * add8b625: manpage - some reordering, update "A NOTE ON SSH BACKENDS" to the new prefix+ changes
 * bff388e7: make pydrive new gdocs default backend keep gdata backend as gdata+gdocs://
 * 8e9579d3: Merged in lp:~bmerry/duplicity/pydrive-regular - This implements the proposal made by somebody else (http://lists.gnu.org/archive/html/duplicity-talk/2015-02/msg00037.html) to allow the pydrive backend to work with a normal drive account instead of a service account. It seems to be working for me: I was able to migrate seamlessly from the gdocs backend. It's set up so that a service account can still be used, depending on which environment variable is set. The man page is updated to describe how to use the new functionality.
 * 99d19983: Support using PyDrive with a regular Google account, instead of a service account.
 * ec708e90: Merged in lp:~noizyland/duplicity/fix-progress - Fixes bug 1264744. selection.filelist_globbing_get_sfs leaves the filelist file object's position at the end of the file. When the --progress option is used the filelists need to be read twice. On the second read nothing is read from the file because file has already been read and the position is EOF. This patch calls seek(0) on the filelist to reset the position to BOF so that subsequent read() calls will return data. * Added pylint ignore error in webdavbackend.py.
 * 8968ac69: Perform seek(0) on filelist before read().
 * 9bd2949f: Reset filelist position to beginning of file after calling read(). This allows file to be read again.
 * e4900da1: Merge in lp:~sjakthol/duplicity/onedrive-error-message - Add proper error message for OneDrive backend when python-requests or python-requests-oauthlib is not installed (bug 1453355).
 * efa361be: Add proper error messages for OneDrive backend when python-requests or python-requests-oauthlib is not installed (bug 1453355).
 * 62989df4: Added ability to get single file status from collection-status with patch from jitao (bug 1044715), like so: $ duplicity collection-status --file-changed c1 file://./foo
 * 02046370: Launchpad automatic translations update.
 * 8b03ed82: Launchpad automatic translations update.
 * bf6429e5: Enable --ignore-errors flag in rdiffdir
 * a37e7d52: Fixed bug 1448249 and bug 1449151 thanks to David Coppit. - When patching, close base file before renaming
 * cd0b62a0: Fixed bug 1444404 with patch from Samu Nuutamo - rdiffdir patch crashes if a regular file is changed to a non-regular file (symlink, fifo, ...)
 * 71cc1bde: Merge in lp:~cemsbr/duplicity/duplicity - Fix bug 1432229 in Copy.com backend: Reply header has no content-type for JSON detection. Now, we also check whether the content starts with '{'.
 * b9b032dc: Fix bug 1432229 in Copy.com backend - Reply header has no content-type for JSON detection. Now, we also check whether the content starts with '{'.
 * 5ce18820: Launchpad automatic translations update.
 * 31b155da: Launchpad automatic translations update.
 * c3d3d530: Move requirements section lower in manpage.
 * 5af43184: Merge in lp:~stynor/duplicity/multi-backend - A new backend that allows use of more than one backend stores (e.g. to combine the available space from more than one cloud provider to make a larger store available to duplicity).
 * ea7aa648: logging cleanup
 * 967e0ffe: typo - missing quote
 * 23bcafe5: add doc
 * 231328db: add doc
 * 0843ac19: adjust delete to make unit tests pass
 * 8b518418: document json format
 * dc3b7365: improved logs; dont allow low level retry to kick in
 * 4f5535a1: initial working code - tested with gdocs and file backends
 * 2ad3929b: Fix bug 1437789 with patch from pdf - par2backend.py incorrect syntax in get()
 * 264942d3: Fix bug 1434702 with help from Robin Nehls - incorrect response BackendException while downloading signatures file.
 * 6d91174f: Fix bug 1432999 with hint from Antoine Afalo.
 * 7a45f8d1: Merged in lp:~aaron-whitehouse/duplicity/filelist_combine - Merged globbing and non-globbing filelists to use the same code path and all accept globbing characters. Added deprecation warning to the --exclude-globbing-filelist and include-globbing-filelist options in commandline.py and hid them from help output. Updated the manual (and unit tests) accordingly. - Note that this does trigger a change in behaviour for duplicity. Previously, include patterns in include-filelist did not match files in a directory that was included, so /usr/local in an include file would not have matched /usr/local/doc. Now, this folder would be included, as would occur if --include or the old --include-globbing-filelist was used. Additional lines will therefore need to be added to filelists to unambiguously exclude unwanted subfolders, if this is intended. - Mark --include-filelist-stdin and --exclude-fielist-stdin for deprecation and hide from --help output.
 * be67633a: Updated duplicity.pot
 * 520c952a: Merge in changes to rebase against dev.
 * e9c395cf: Changed tests to test filelist, rather than globbing filelist, except for one functional globbing test of each type to ensure this continues to work until it is deliberately removed. Changed naming of tests etc accordingly.
 * acb05514: Removed unnecessary tests (post merging of non-globbing and globbing filelists) and created a globbing version of the one test that was only written for non-globbing filelists.
 * 891c262d: Updated manual to remove references to globbing filelists and stdin filelists and make consequential changes to the description of include-filelist and exclude-filelist behaviour.
 * 66c6e9e8: Merge in lp:~duplicity-team/duplicity/po-updates
 * 1083ca4c: remove extraneous string format arg in previous scp fix.
 * a3506ebd: Fix for --pydevd debug environment and location under Eclipse. * Fix for bug where scp was actually working as scp and not working with rsync.net because of using extraneous test command in restricted shell. Was trying "test -d 'foo' || mkdir -p 'foo'", now only "mkdir -p foo".
 * 286b41a6: Note Bug #1423367 was fixed in the previous commit.
 * 82193cf7: Mark --include-filelist-stdin and --exclude-fielist-stdin for deprecation and hide from --help output. Add additional tests in stdin_test.sh to test --include-filelist-stdin and that /dev/stdin is an adequate replacement.
 * 7dd7c606: Added bash script (stdin_test.sh) showing that filelists from stdin were working as expected despite the changes.
 * 9c4dedeb: Really fix bug 1416344 based on comment #5 by Roman Tereshonkov
 * cf31894c: Fix _librsyncmodule.c compilation, bug 1416344, thanks to Kari Hautio.
 * b2a52295: Fix spelling error in manpage, bug 1419314.
 * 99ee3463: Added deprecation warning to the --exclude-globbing-filelist and include-globbing-filelist options in commandline.py and hid them from help output. Commented out functions relating to non-globbing filelists. Commented out unit tests related to non-globbing filelists.
 * 6542cb2d: Made non-globbing filelists use the globbing code path (ie made all filelists globbing), as per: http://lists.nongnu.org/archive/html/duplicity-talk/2015-01/msg00011.html Fixed Bug #1408411 in the process, as this issue was limited to the non-globbing code path.
 * 74b7727e: Coalesce CHANGELOG
 * 1efe81c4: Misc fixes for the following PEP8 issues: E401 - see http://pep8.readthedocs.org
 * 10177806: Misc fixes for the following PEP8 issues: E231, E241, E251, E261, E262, E271, E272, E301, E302, E303, E502, E701, E702, E703, E711, E721, W291, W292, W293, W391 - see http://pep8.readthedocs.org
 * b47cd765: Misc fixes for the following PEP8 issues: E231, E241, E251, E261, E262, E271, E272 - see http://pep8.readthedocs.org
 * bc750aff: Misc fixes for the following PEP8 issues: E231, E241 - see http://pep8.readthedocs.org
 * 7f8e3ffb: Misc fixes for the following PEP8 issues: E231, E241 - see http://pep8.readthedocs.org * Fixes for 2to3 issues
 * ca887059: Merged in lp:~aaron-whitehouse/duplicity/bug_932482_trailing_slashes_and_wildcards_error - Added functional and unit tests to show Bug #932482 - that selection does not work correctly when excludes (in a filelist or in a commandline option) contain both a single or double asterisk and a trailing slash.
 * 28e762a7: Added functional and unit tests to show Bug #932482 - that selection does not work correctly when excludes (in a filelist or in a commandline option) contain both a single or double asterisk and a trailing slash.
 * 9d0cf7d1: Merged in lp:~aaron-whitehouse/duplicity/bug_884371_asterisks_in_includes - Added tests to unit/test_selection.py and funtional/test_selection.py to show the behaviour reported in Bug #884371, i.e. that selection is incorrect when there is a * or ** on an include line of a filelist or commandline --include.
 * d8e2bf31: Added credit to Elifarley Cruz for one of the test cases.
 * 985f7a03: Added functional tests to functional/test_selection.py to show Bug #884371 (* and ** not working as expected) applies to commandline --include.
 * dd2debde: Added tests to unit/test_selection.py and funtional/test_selection.py to show the behaviour reported in Bug #884371, i.e. that selection is incorrect when there is a * or ** on an include line.
 * 969c7951: Merged in lp:~angusgr/duplicity/exclude-older-than - Add "--exclude-older-than" commandline option, that allows you to only back up files with a modification date newer than a particular threshold. * Additional pep8 cleanup.
 * 28e77c9c: Ongoing pep8 corrections.
 * 8c58b82e: Add option --exclude-older-than to only include recently modified files.
 * f7904f9d: Applied patch from Adam Reichold to fix bug # 1413792
 * 1e57bd33: Fixed bug # 1414418 - Aligned commandline.py options and help display contents. - Aligned commandline.py options and manpage contents. * Changed --s3_multipart_max_timeout to --s3-multipart-max-timeout to be consistent with commandline option naming conventions.
 * 9b4749ff: Launchpad automatic translations update.
 * 42fe989b: Misc fixes for the following PEP8 issues: 201, 202, 203 - see http://pep8.readthedocs.org
 * 322a6ab4: Misc fixes for the following PEP8 issues: E127, E128 - see http://pep8.readthedocs.org
 * 34b4fec0: Misc fixes for the following PEP8 issues: E111, E121, E122, E124, E125, E126 - see http://pep8.readthedocs.org
 * 03c55c9b: Remove 'gs' and 's3+http' from uses_netloc[]. Fixes Bug 1411803.
 * 8d96f690: Merged in lp:~duplicity-team/duplicity/po-updates
 * 1426220e: Fixed variable typo in commandline.py that was causing build fails.
 * e699b413: Fixed some tabs/spaces problems that were causing install failures.
 * 33bc2354: Merged in lp:~user3942934/duplicity/pydrive - Currently duplicity uses gdocs backend for Google Drive backups. gdocs uses deprecated API and don't allow backups for managed Google accounts. (see https://bugs.launchpad.net/duplicity/+bug/1315684) - Added pydrive backend that solves both of those problems. Published also on https://github.com/westerngateguard/duplicity-pydrive-backend.
 * 6de78376: Merged in lp:~noizyland/duplicity/fix_azurebackend_container_names - Azure Backend examples have underscores in the container names. These are not valid Azure container names. The underscores have been replaced with hypens and a note about valid container names added to the man page. - Also corrects a problem where Azure Exceptions were returing unicode strings that were not being handled correctly.
 * f1f7a743: Changed passing keyfile via query in URL to passing the key by environment variable. Fixed manpage accordingly. Restored Azure info in manpage that was somehow mistakenly deleted.
 * 1b8d13ef: removed underscores from example Azure container names - added Azure container name rules to man page - handle unicode messages correctly in Azure Exceptions
 * ee8deda5: Launchpad automatic translations update.
 * 4a83a2ab: Merged in lp:~aaron-whitehouse/duplicity/progress_option_error - Added test_exclude_globbing_filelist_progress_option into functional/test_selection.py, which shows the error reported in Bug #1264744 - that the --exclude-globbing-filelist does not backup the correct files if the --progress option is used. Test is marked as an expected failure so as not to cause the test suite to fail.
 * be86d843: Added test_exclude_globbing_filelist_progress_option into functional/test_selection.py, which shows the error reported in Bug #1264744 - that the --exclude-globbing-filelist does not backup the correct files if the --progress option is used. Test is marked as an expected failure so as not to cause the test suite to fail.
 * 4a4a6943: fixed URI parsing
 * e160fa73: Merged in lp:~vincegt/duplicity/swift_regionname - Fixes bug #1376628 - Add mapping of SWIFT_REGIONNAME to select region inside SWIFT when a provider proposes more than one region.
 * 7ca0db5b: Fixed some recently added 2to3 and pep8 issues.
 * 9e5fec9c: Add SWIFT_REGIONNAME parameter to select SWIFT REGION. See bug #1376628
 * c931c09f: added pydrive backend aimed to replace the deprecated gdocs backend
 * da8d763c: Merged in lp:~noizyland/duplicity/azurebackend - Add backend for Azure Blob Storage Service
 * eb81b0af: Merged in lp:~9-sa/duplicity/FixBug1408289 - Fix bug #1408289 - Wrong attribute name prevented raise of client exception, working now
 * f99f0d06: Launchpad automatic translations update.
 * 7abafcce: modified: duplicity/backends/azurebackend.py
 * 19a60910: modified: duplicity/backends/azurebackend.py
 * e873f732: modified: bin/duplicity.1 duplicity/commandline.py
 * fb4eeb8c: Fix Bug #1408289
 * 873c8b18: added: duplicity/backends/azurebackend.py
 * 121878d3: Merged in lp:~hooloovoo/duplicity/process_filelists_for_spaces_etc - Process filelists to remove imperfections such as blank lines, comments and leading/trailing whitespace. Also correctly processes quoted folders containing spaces in their names. Extensive unit and functional tests to test these changes (and selection more generally). - The branch does add an additional folder to testfiles.tar.gz called select2. This included a folder with a trailing space, to test the quote test. The subfolders also have clearer names than in the "select" folder (eg "1sub2sub3") which makes it easier to keep track of issues in tests.
 * 11adc9d5: Merged in lp:~hooloovoo/duplicity/filelist_select_bug_1408411 - Adds functional test cases that fail because of Bug #1408411 (commented out), to assist in fixing that bug.
 * 2e81845d: Merged in lp:~stapelberg+ubuntu/duplicity/add-onedrive-backend - Add a Microsoft OneDrive backend
 * 9a678c83: selection.py modified to pre-process lines for both globbing and non-globbing filelists to: remove leading and trailing whitespace; process quoted filenames correctly; remove blank lines; and ignore full-line comments. Added tests to unit/test_selection.py and functional/test_selection.py to cover these. Added a new folder select2 to the testfiles.tar.gz for the new functional tests (clearer names and a folder with trailing whitespace).
 * 0c75f13d: Added functional test cases to show the issue reported in Bug #1408411 (Filelist (non-globbing) should include a folder if it contains higher priority included files - https://bugs.launchpad.net/duplicity/+bug/1408411).
 * f0034f64: Add a backend for Microsoft OneDrive
 * 8913a2f0: Fixed bug 1278529 by applying patch supplied in report - Use get_bucket() rather than lookup() on S3 to get proper error msg.
 * a0baa290: Misc fixes for the following PEP8 issues: E211, E221, E222, E225, E226, E228 - see http://pep8.readthedocs.org
 * f8534ac1: Fixed bug 1406173 by applying patch supplied in report - Ignore .par2 files in remote file list * Removed redundant shell test testing/verify_test.sh
 * a9a8efc5: Merged in lp:~hooloovoo/duplicity/add-else-to-badupload-try-except - Badupload test previously did not have an else in the try-except. The test passed if the except was triggered, but would also pass if the test did not trigger an error at all.
 * d765a5e3: Merged in lp:~hooloovoo/duplicity/add-additional-verify-tests-for-corrupted-archives - Add tests to test_verify.py to test that verify fails if the archive file is corrupted. Changed file objects to use the with keyword to ensure that the file is properly closed. - Small edit to find statement in verify_test.sh to make it work as expected (enclose string in quotes).
 * d7ac6bb6: Add comments to the verify_test.sh script matching up the tests in there to the tests implemented in test_verify.py. All the tests in the shell script have now been implemented, so the shell script should perhaps be deleted.
 * d10d3783: Add tests to test_verify.py to test that verify fails if the archive file is corrupted. Changed file objects to use the with keyword to ensure that the file is properly closed. Small edit to find statement in verify_test.sh to make it work as expected (enclose string in quotes).
 * 39c23600: Add else to try-except in badupload functional test, to catch where the test passes successfully instead of throwing an error (as it should).
 * 3b6f29a0: Merge in lp:~hooloovoo/duplicity/test-verify-improvements - Fix up test_verify, which was a bit of a mess: Simplify test_verify.py to just do a simple backup and verify on a single file in each test. - Modify tests to correctly use --compare-data option. - Add tests for when the source files have atime/mtime manipulated. * Fix duplicity verify to ignore the file system when globals.compare_data is False. This means that verify only validates the viability of the backup itself unless --compare-data is specified. * Reenable test_verify_changed_source_file test
 * 6548cd8b: Simplify test_verify.py to just do a simple backup and verify on a single file in each test. Modify tests to correctly use --compare-data option and to add tests for verify when the source files have the atime/mtime manipulated.
 * d04f2de7: Make ssh an unsupported backend scheme * Temporarily disable RsyncBackendTest and test_verify_changed_source_file
 * 9f19cf08: Merge in lp:~ed.so/duplicity/move_netloc - move netloc usage definitions into respective backends - fix "[Question #259173]: rsync backend fails" https://answers.launchpad.net/duplicity/+question/259173
 * 06e70895: Tests to validate that duplicity does not check filesystem source during verify unless --compare-data is specified
 * 24a9a21f: move netloc usage definitions into respective backends
 * 53e1a19d: Added in tests including compare_data
 * e992570a: Added test_verify_changed_source_file test to flag up the issue mentioned in Bug #1354880
 * 863405a5: Merge in lp:~andol/duplicity/signkeyformat - Allow --sign-key to use short format, long format alt. full fingerprint.
 * 4be5d27b: Source formatted, using PyDev, all source files to fix some easily fixed PEP8 issues. Use ignore space when comparing against previous versions.
 * 0f5b1d6a: Merged in lp:~ed.so/duplicity/paramiko.identyfile - fix identity file parsing of --ssh-options for paramiko - manpage fixes
 * 1c72710e: Launchpad automatic translations update.
 * c7f04590: fix identity file parsing of --ssh-options for paramiko manpage fixes
 * 05c1e5a7: Modded .bzrignore to ignore *.egg test dependencies, normalized, sorted.
 * 1523ad68: Manually merged in lp:~m4ktub/duplicity/0.6-reliability - Per fix proposed in Bug #1395341.
 * a2f58826: Fix changelogs comments.
 * 582a0be5: Fixed bug 1255453 with changes by Gaudenz Steinlin, report backend import results, both normal and failed, at INFO log level.
 * 859da7c0: Fixed bug 1236248 with changes by az, manpage warning about --extra-clean.
 * 297f001c: Fixed bug 1385599 with changes by Yannick Molin. SSL settings are now conditioned on protocol ftp or ftps.
 * 107e8b07: Merged in lp:~adrien-delhorme/duplicity/hubic - Add Hubic support through pyrax and a custom pyrax_identity module.
 * 1954151e: In webdavbackend.py: Fixed bug 1396106 with change by Tim Ruffing, mispelled member. - Added missing 'self.' before member in error message.
 * 47e1b7b7: Merge lp:duplicity onto lp:~adrien-delhorme/duplicity/hubic
 * 8b85a694: Update man page
 * eef544b3: Update man page Add hubic identity module
 * d3d5a066: Undid move of testing/test_code.py. Instead I fixed it so that it would not run during PPA build. It now needs the setting RUN_CODE_TESTS=1 in the environment which is supplied in the tox.ini file.
 * fcd868ad: Moved testing/test_code.py to testing/manual/code_test.py so PPA builds would succeed. Should be moved back later.
 * 3061442c: Remove valid_extension() check from file_naming.py. It was causing failed tests for short filenames. Thanks edso.
 * 039a1475: Launchpad automatic translations update.
 * 0e37b5fb: Partial fix for PPA build failures, new backend name.
 * 2d504e91: Merged in lp:~ed.so/duplicity/fix.dpbx.import - fix dpbx import error import lazily
 * 7f1e77ff: fix dpbx import error import lazily
 * 243a54d6: Fix for failing PPA builds. FTP backend has variable class names.
 * 1da0b737: Fix files list.
 * 8721f718: Merged in lp:~hooloovoo/duplicity/fix-typo-in-test-description - Fixed spelling mistake/typo in a description of a test.
 * 99bf9bb8: Merged in lp:~mterry/duplicity/missing-unicode-escape - Convert restore_dir to unicode before printing.
 * 9d48b9b3: Merged in lp:~ed.so/duplicity/lftp.ncftp.and.prefixes - retire --ssh-backend, --use-scp parameters - introduce scheme prefixes for alternative backend selection e.g. ncftp+ftp://, see manpage - scp is now selected via scheme e.g. scp:// - added lftp fish, webdav(s), sftp support
 * c61dd5be: Launchpad automatic translations update.
 * 94daf2bd: Launchpad automatic translations update.
 * e7ef8d5e: Escape filename before printing in unicode
 * 7341ee90: Launchpad automatic translations update.
 * 16b8dc05: Add Hubic backend
 * 563872ba: Fix typo ('hidding' to 'hiding')
 * a1bbf1cb: Support older versions of dpkg-parsechangelog
 * c6904d76: add https cert verification switches
 * 721ada4e: more manpage fixes/reformatting retire parameters --ssh-backend, --use-scp, functionality is achieved via scheme:// setting now add lftp webdav support add lftp fish support fix assertionerror when using par2+ backend
 * eeed0460: Some small testing fixes to work on older copies of mock and pylint
 * 36a7ed39: manpage: document ftp changes/minor enhancements
 * 5f81a422: allow ftp backend selection via prefix
 * 8564ede3: rename lftp/ncftp backends
 * e20cf24c: restore ncftp backend
 * 740c2680: Allow --sign-key to use short format, long format alt. full fingerprint.
 * 978f01f0: Minor tweaks to debian/control to fix building on older versions of Ubuntu
 * 49f41060: Merged in lp:~mterry/duplicity/debian-dir - Add a debian/ directory to make it easier to manage the PPAs for duplicity.
 * 6fdcfcc0: Fix Edgar's name
 * 5eafaa70: Merged in lp:~mterry/duplicity/code-nits - Fix some pylint/pep8 nits that prevented the test_code.py test from passing.
 * 560c5297: Add debian packaging
 * 46c2757d: Avoid super() on old-style class
 * 58afd4d4: Fix pylint/pep8 nits so that tests pass
 * 6c00b3ba: Launchpad automatic translations update.
 * 4cd0793c: Launchpad automatic translations update.
 * de5a5c2d: Adjust unit tests to expect single FTP backend
 * aa975a08: Merged in lp:~moritzm/duplicity/duplicity - Use lftp for both FTP and FTPS
 * 403dbbe7: Minor accounting fix.
 * 9c3a19a0: Merged in lp:~johnleach/duplicity/1315437-swift-container-create - Check to see if the swift container exists before trying to create it, in case we don't have permissions to create containers. Fixes #1315437
 * 651c3635: Clean up imports.
 * e77362dd: Launchpad automatic translations update.
 * daad5bf6: Merged in lp:~ed.so/duplicity/0.7-dpbx.importfix - fix this showstopper with the dropbox backend "NameError: global name 'rest' is not defined"
 * 6f3653da: Launchpad automatic translations update.
 * a7791340: Merged in lp:~jflaker/duplicity/BugFix1325215 - The reference to "--progress_rate" in the man page as a parameter is incorrect. Should be "--progress-rate".
 * cc80b44d: Merged in lp:~hooloovoo/duplicity/updated-README-REPO - Changes to README-REPO to reflect the restructuring of the directories.
 * 4474749d: use lftp for both FTP and FTPS
 * 657bc374: Launchpad automatic translations update.
 * 8b437e7e: Fixed bug 1375304 with patch supplied by Aleksandar Ivanovic
 * b3e1eb1e: Change the branch for stable. lp:duplicity/stable doesn't exist and so I've changed this to lp:~duplicity-team/duplicity/0.6-releases as this is the only non-Windows, non-dev branch.
 * f4ee5071: Corrected the extra dot in the stable branch line at step 1.
 * b1b6fe41: Updated README-REPO to reflect restructuring of directories. See https://answers.launchpad.net/duplicity/+question/252898
 * 22876d60: Launchpad automatic translations update.
 * 66586f0b: Merged in lp:~jeffreydavidrogers/duplicity/duplicity - This change fixes two small typos in the duplicity man page.
 * d4682f33: Merged in lp:~ed.so/duplicity/manpage.verify - clarify verify's functionality as wished for by a user surprised with a big bandwidth bill from rackspace.
 * 433945e4: Added sxbacked.py, Skylable backend. Waiting on man page updates.
 * e0d09bb1: Fix two small typos in duplicity man page
 * fcd7e6ec: clarify verify's functionality as wished for by a user surprised with a big bandwidth bill from rackspace.
 * 7922b6d6: Launchpad automatic translations update.
 * cfb27d78: Fixed bug 1327550: OverflowError: signed integer is greater than maximum - Major and minor device numbers are supposed to be one byte each. Someone has crafted a special system image using OpenVZ where the major and minor device numbers are much larger (ploop devices). We treat them as (0,0).
 * 4fda94b6: Merged in lp:~antmak/duplicity/0.7-par2-fix - Useful fix for verbatim par2cmdline options (like "-t" in par2-tbb version)
 * 50030189: Restore accidental deletion.
 * d6edff08: Merged in lp:~mterry/duplicity/webdav-fixes - This branch fixes two issues I saw when testing the webdav backend: 1) Errors like the following: "Attempt 1 failed. BackendException: File /tmp/duplicity-LQ1a0i-tempdir/mktemp-u2aiyX-2 not found locally after get from backend". These were caused by the _get() method not calling setdata() on the local path object, so the rest of the code thought it didn't exist. - 2) Some odd issues from stale responses/data. We have a couple places in webdavbackend.py where we close the connection before making a request because of this problem. But I've changed it to do it every time, more reliably, by putting a _close() call inside the request() method. - With this, the webdav backend seems fine to me.
 * b61b3054: Merged in lp:~ed.so/duplicity/webdav200fix-0.7 - webdav backend fix "BackendException: Bad status code 200 reason OK. " when restarting an interrupted backup and overwriting partially uploaded volumes.
 * 2ea8ad5d: Merged in lp:~3v1n0/duplicity/copy.com-backend - I've added a backend for Copy.com cloud storage, this supports all the required operations and works as it should from my tests. - You can use it by calling duplicity with something like: copy://account@email.com:your-password@copy.com/duplicity - The only thing I've concerns with is the optimized support for _delete_list which can't be enabled here because the test_delete_list tries also to delete a not-existing files, and it requires the backend not to raise an exception in that case (is this somewhat wanted or could we do the same as for _delete or _query?)
 * 1da69e82: Fix setdata() not being called a better way
 * 801ca58c: README: add copy.com requirements
 * 3a953e96: Add copy.com to man file
 * 41956543: CopyComBackend: import non-main modules only when needed
 * bd7aa3bd: CopyComBackend: remove unneded upload checks
 * 3556ef05: CopyComBackend: implement _query method
 * 61f2ea5c: CopyComBackend: disable the _delete_list support, it won't work if a file doesn't exist
 * 52920bd9: CopyComBackend: add ability to delete list of files
 * fd61d5a9: Backends: Add Copy.com support, implement basic operations
 * c65c4005: Use writefileobj instead of direct write, for less code and so that we call setdata()
 * 5bccfe6e: More reliably reset webdav connection
 * 0f03bf94: webdav backend fix "BackendException: Bad status code 200 reason OK. " when restarting an interrupted backup and overwriting partially uploaded volumes.
 * 502e56f7: Added user defined verbatim options for par2
 * ef09d9a2: Update shebang line to python2 instead of python to avoid confusion.
 * 6ea7efd1: Merged in lp:~mterry/duplicity/py2.6.0 - Support python 2.6.0. - Without this branch, we only support python >= 2.6.5 because that's when python's urlparse.py module became its more modern incarnation. (I won't get into the wisdom of them making such a change in the middle of the 2.6 lifecycle.) - Also, the version of lockfile that I have (0.8) doesn't work with python 2.6.0 or 2.6.1 due to their implementation of threading.current_thread().ident returning None unexpectedly. So this branch tells lockfile not to worry about adding the current thread's identifier to the lock filename (we don't need a separate lock per thread, since our locking is per process). - I've tested with 2.6.0 and 2.7.6 (both extremes of our current support).
 * ed76750e: Support py2.6.0
 * 6be84f05: Clean up indentation mismatches.
 * c74e7d69: Launchpad automatic translations update.
 * 7593a854: Misc format fixes.
 * 0994d867: Launchpad automatic translations update.
 * 0b7a7bb8: Applied expat fix from edso. See answer #12 in https://answers.launchpad.net/duplicity/+question/248020 * Forward-ported from r980 in 0.6-series
 * 569ae2cf: First cut of 0.7.00 Changelog.
 * e38a6ec6: Launchpad automatic translations update.
 * d819aef6: Fix running ./testing/manual/backendtest to be able to find config.py and fix the tests in testing/manual/ to not be picked up by ./setup.py test
 * 512be37c: Launchpad automatic translations update.
 * bfe2f48d: Merged in lp:~mterry/duplicity/encode-exceptions - Because exceptions often contain file paths, they have the same problem with Python 2.x's implicit decoding using the 'ascii' encoding that we've experienced before. So I added a new util.uexc() method that uses the util.ufn() method to convert an exception to a unicode string and used it around the place. - Bugs fixed: 1289288, 1311176, 1313966
 * 3d055110: Launchpad automatic translations update.
 * 113c18df: Convert exceptions to unicode
 * c1b66937: Merged in lp:~mterry/duplicity/backend-unification - Reorganize and simplify backend code. Specifically: Formalize the expected API between backends and duplicity. See the new file duplicity/backends/README for the instructions I've given authors. - Add some tests for our backend wrapper class as well as some tests for individual backends. For several backends that have some commands do all the heavy lifting (hsi, tahoe, ftp), I've added fake little mock commands so that we can test them locally. This doesn't truly test our integration with those commands, but at least lets us test the backend glue code. - Removed a lot of duplicate and unused code which backends were using (or not using). This branch drops 700 lines of code (~20%) in duplicity/backends! - Simplified expectations of backends. Our wrapper code now does all the retrying, and all the exception handling. Backends can 'fire and forget' trusting our wrappers to give the user a reasonable error message. Obviously, backends can also add more details and make nicer error messages. But they don't *have* to. - Separate out the backend classes from our wrapper class. Now there is no possibility of namespace collision. All our API methods use one underscore. Anything else (zero or two underscores) are for the backend class's use. - Added the concept of a 'backend prefix' which is used by par2 and gio backends to provide generic support for "schema+" in urls -- like par2+ or gio+. I've since marked the '--gio' flag as deprecated, in favor of 'gio+'. Now you can even nest such backends like par2+gio+file://blah/blah. - The switch to control which cloudfiles backend had a typo. I fixed this, but I'm not sure I should have? If we haven't had complaints, maybe we can just drop the old backend. - I manually tested all the backends we have (except hsi and tahoe -- but those are simple wrappers around commands and I did test those via mocks per above). I also added a bunch more manual backend tests to ./testing/manual/backendtest.py, which can now be run like the above to test all the files you have configured in config.py or you can pass it a URL which it will use for testing (useful for backend authors).
 * ccbbdd1a: further fixes
 * ff6f7366: Launchpad automatic translations update.
 * c097a29f: Merge from trunk
 * 4f31caa1: Minor fixes
 * 4e7b05fb: Merged in lp:~mterry/duplicity/py3-map-filter - In py3, map and filter return iterable objects, not lists. So in each case we use them, I've either imported the future version or switched to a list comprehension if we really wanted a list.
 * 65d0cd72: Launchpad automatic translations update.
 * 4c4c95dd: Fix map usage for py3 readiness
 * 06deaa30: Fix filter usage for py3 readiness
 * c71b132e: Fixed bug #1312328 WebDAV backend can't understand 200 OK response to DELETE - Allow both 200 and 204 as valid response to delete
 * f2e008e6: Add ftp backend test
 * 11eda7cd: Drop popen_subprocess_persist in favor of just the basic version; add ftps backend test
 * 1edb42c5: And test hsi backend too
 * bc587643: Add fake tahoe executable, so we can test the tahoe backend
 * 6a3e73c2: Add support for backend prefixes, allow rsync backend to use local paths, and add some more tests
 * 60d229a1: Add some backend tests, clean up par2backend, and general fixes
 * 57d60822: Checkpoint
 * 5a249225: Launchpad automatic translations update.
 * c3a42168: # Merged in lp:~mterry/duplicity/more-test-reorg - Here's another test reorganization / modernization branch. It does the following things: Drop duplicity/misc.py. It is confusing to have both misc.py and util.py, and most of the code in misc.py was no longer used. I moved the one function that was still used into util.py. - Consolidated the various ways to run tests into just one. I made tox runs go through ./setup.py test, rather than nosetests. And I made the ./testing/run-tests scripts just call tox. Now we no longer need nosetests as a test dependency (although you can still use it if you want). - Added two more code quality automated tests: a pep8 one and a pylint one. I disabled almost all checks in each program that gave a warning. These tests just establish a baseline for future improvement. - Moved the test helper code into TestCase subclasses that all tests can use. And used more code sharing and setUp/tearDown cleverness to remove duplicated code. - Reorganized the tests in ./testing/tests into ./testing/functional and ./testing/unit -- for whether they drive duplicity as a subprocess or whether they import and test code directly. Each dir can have specialized TestCase subclasses now. - Renamed the files in ./testing/unit to more clearly indicate which file in ./duplicity they are unit testing. - Added some helper methods for tests to set environment and globals.* parameters more safely (i.e. without affecting other tests) by automatically cleaning up any such changes during test tearDown. - Removed test_unicode.py, since it is kind of dumb. It used to be more useful, but now with py2.6, we are just testing that one line of code in it is actually there.
 * 066332cd: Add overrides dir
 * 314342e5: more minor fixes
 * fd3122df: Move rootfiles.tar.gz into manual directory
 * 75ebecb9: Add initial pep8 and pylint tests
 * e545a156: Minor fixes
 * 578b6fef: Make run-tests scripts go through tox, this makes all our standard test-running modes ultimately go through ./setup test
 * f3a4ef57: Drop little-used misc.py
 * 0d869fb3: More reorg of testing/
 * f496496e: Launchpad automatic translations update.
 * f98e4f2e: Merged in lp:~mterry/duplicity/encode-for-print - Encode translated strings before passing them to 'print'. - The print command can only apparently handle bytes. So when we pass it unicode, it freaks out. There were only four instances I saw where we used print, so I figured it was easiest to just convert them to use the log framework too. - That way all user-visible strings go through that framework and are subject to the same encoding rules.
 * 13bc6376: Merged in lp:~mterry/duplicity/drop-static - Drop static.py. - This is some of the oldest code in duplicity! A bzr blame says it is unmodified (except for whitespace / comment changes) since revision 1. - But it's not needed anymore. Not really even since we updated to python2.4, which introduced the @staticmethod decorator. So this branch drops it and its test file.
 * 60e44710: Merged in lp:~mterry/duplicity/2.6isms - Here's a whole stack of minor syntax modernizations that will become necessary in python3. They all work in python2.6. - I've added a new test to keep us honest and prevent backsliding on these modernizations. It runs 2to3 and will fail the test if 2to3 finds anything that needs fixing (with a specific set of exceptions carved out). - This branch has most of the easy 2to3 fixes, the ones with obvious and safe syntax changes. - We could just let 2to3 do them for us, but ideally we use 2to3 as little as possible, since it doesn't always know how to solve a given problem. I will propose a branch later that actually does use 2to3 to generate python3 versions of duplicity if they are requested. But this is a first step to clean up the code base.
 * b9ffc77a: Drop static.py
 * 00fa793f: Launchpad automatic translations update.
 * 38df685b: Fix subprocess usage to work in py2.6 and fix a missing unicode
 * 80fdb92d: Solve has_key 2to3 fix
 * 6093a463: Move imports fix to the 'don't care' section
 * fd2b94f8: Solve import 2to3 fix
 * be7d9f6c: Solve numliterals 2to3 fix
 * 820bb1af: Solve long 2to3 fix
 * a349695c: Move urllib fix to the 'don't care' section
 * 3ec71378: Solve basestring 2to3 fix
 * cd9d5655: Move long and raw_input fixes to the 'don't care' section
 * 970b0b56: Solve reduce 2to3 fix
 * daaf6e51: Solve raise 2to3 fix
 * 239a5299: Mark callable and future fixes as things we explicitly don't care about
 * 059e9685: Solve apply 2to3 fix
 * 112c8e9c: Solve idioms 2to3 fix
 * 56cc7911: Solve ws_comma 2to3 fix
 * cae2beb5: Solve renames 2to3 fix
 * 401812da: Solve except 2to3 fix
 * bce34123: Add test_python3.py to test readiness of source code to run under python3 directly
 * ae5e99a8: Merged in lp:~mterry/duplicity/drop-pexpect - Drop our local copy of pexpect in favor of a system version. - It's only used by the pexpect ssh backend (and if you're opting into that, you probably can expect that you will need pexpect) and the tests. - I've done a quick smoketest (backed up and restored using --ssh-backend=pexpect) and it seemed to work fine with a modern version of pexpect.
 * b2b3e57b: Merged in lp:~mterry/duplicity/fix-drop-u1 - Looks like when the drop-u1 branch got merged, its conflict got resolved badly. Here is the right version of backend.py to use (and also drops u1backend.py from POTFILES).
 * 97b2a775: fix typo
 * 435df384: Drop local copy of pexpect -- only used by one of our ssh backends and our tests
 * 437651f7: Fix drop-u1 merge
 * 45589568: Merged in lp:~mterry/duplicity/drop-u1 - Ubuntu One is closing shop. So no need to support a u1 backend anymore.
 * d39d528f: Merged in lp:~mterry/duplicity/require-2.6 - Require at least Python 2.6. - Our code base already requires 2.6, because 2.6-isms have crept in. Usually because we or a contributor didn't think to test with 2.4. And frankly, I'm not even sure how to test with 2.4 on a modern system.
 * 4199ac7a: Merged in lp:~mterry/duplicity/modern-testing - Enable/use more modern testing tools like nosetests and tox as well as more common setup.py hooks like test and sdist. - Specifically: move setup.py to toplevel where most tools and users expect it * Move and adjust test files to work when running "nosetests" in toplevel directory. Specifically, do a lot more of the test setup in tests/__init__.py rather than the run-tests scripts * Add small tox.ini file for using tox, which is a wrapper for using virtualenv. Only enable for py26 and py27 right now, since modern setuptools dropped support for <2.6 (and tox 1.7 recently dropped <2.6) * Add setup.py hooks for test and sdist which are both standard targets (sdist just outsources to dist/makedist right now)
 * 2a307d54: Merged in lp:~mterry/duplicity/consolidate-tests - Consolidate all the duplicity-running code in the test framework. - This takes the four test files [1] that run duplicity itself (i.e. the high-level functional test files) and consolidates their code. Before, it was madness. Each one had its own run_duplicity method, with its own slightly tweaked features. This should reduce a lot of duplication. - [1] cleanuptest.py, finaltest.py, restarttest.py, and badupload.py
 * 54761df7: Merged in lp:~fredrik-loch/duplicity/duplicity-S3-SSE - Adds support for server side encryption as requested in Bug #996660
 * 276f5fc2: Drop support for Ubuntu One, since it is closing
 * 41f6585e: Drop support for Python 2.4 and 2.5
 * a25fa2a9: Add missing mock dep
 * 1d382604: Whoops, make dist dir first during sdist
 * 3fa04a92: Enable/use more mordern testing tools like nosetest and tox as well as more common setup.py hooks like test and sdist
 * 5c0120c2: Consolidate all the duplicity-running code in the test framework
 * 66c0ecc0: Launchpad automatic translations update.
 * ceb0d8d2: Launchpad automatic translations update.
 * a73d6a2e: Added support for amazon s3 encryption by the use of --s3-use-server-side-encryption
 * a8fe7326: Added support for serverside encryption in amazon s3
 * 142230df: Convert unicode to utf8 before passing to print
 * 84441189: Launchpad automatic translations update.
 * 48f2c6b4: Launchpad automatic translations update.
 * b423bb3a: Merged in lp:~germer/duplicity/par2 - This branch adds Par2 recovery files to duplicity. It is a wrapper backend which will create the recovery files and upload them all together with the wrapped backend. Corrupt archives will be detected and repaired (if possible) on the fly during restore. - It can be used with url-string par2+webdavs://USER@HOST/PATH - Fixes https://bugs.launchpad.net/duplicity/+bug/426282
 * 94d51434: Merged in lp:duplicity
 * 0b90a438: Launchpad automatic translations update.
 * 1b97ea44: Merged in lp:~prateek/duplicity/botoimportfix - Switches the boto backend back to using lazy imports so there are no complaints during the importing of backends.
 * e27aeec9: Merged in lp:~ed.so/duplicity/fix.dpbx - fix dpbx backend "NameError: global name 'rest' is not defined"
 * 28929959: Fixed boto import issues
 * 41eb484c: fix dpbx backend "NameError: global name 'rest' is not defined"
 * ee0b83bc: Launchpad automatic translations update.
 * 7748ea06: Fix boto import.
 * 008eb8ad: Launchpad automatic translations update.
 * 424a624d: Merged in lp:~prateek/duplicity/s3-glacier - Fixes https://bugs.launchpad.net/duplicity/+bug/1039511 - Adds support to detect when a file is on Glacier and initiates a restore to S3. Also merges overlapping code in the boto backends - Fixes https://bugs.launchpad.net/duplicity/+bug/1243246 - Adds a --s3_multipart_max_timeout input option to limit the max execution time of a chunked upload to S3. Also adds debug message to calculate upload speed.
 * 9048bbe2: Make sure each process in a multipart upload get their own fresh connection
 * 74695411: Updated manpage and tweaked boto backend connection reset
 * d90ed2f4: Launchpad automatic translations update.
 * 58bde8d7: Merged in lp:~mterry/duplicity/pexpect-fix - duplicity has its own copy of pexpect. Use that instead of requiring one from the system.
 * 378d4091: Fix pexpect import
 * 989bf214: Merged in main branch
 * 2b46bdff: Added max timeout for chunked uploads and debug lines to gauage upload speed
 * 3a7e654a: Launchpad automatic translations update.
 * 54883115: Launchpad automatic translations update.
 * 032b79af: Launchpad automatic translations update.
 * b00457ef: add documentation to manpage rename ~par2wrapperbackend.py
 * f24d08a4: Merged in lp:duplicity
 * 44651652: Launchpad automatic translations update.
 * 4abb3192: Merged in lp:~mterry/duplicity/gpg-encode - getpass.getpass(prompt) eventually calls str(prompt). Which is a no go, if the prompt contains unicode. Here's a patch to always pass getpass() a byte string. - Our tests didn't catch this because they always set PASSPHRASE. I've added a test that passes the passphrase via stdin.
 * 47ed870a: Add test that includes unicode characters to check the gpg prompt
 * 39b81ebd: Encode prompt phrase before passing to getpass
 * 0023db8d: Launchpad automatic translations update.
 * f18be8f6: Launchpad automatic translations update.
 * 3d86da90: Applied two patches from mailing list message at: https://lists.nongnu.org/archive/html/duplicity-talk/2014-01/msg00030.html "Added command line options to use different prefixes for manifest/sig/archive files" This resolves https://bugs.launchpad.net/duplicity/+bug/1170161 and provides a workaround for https://bugs.launchpad.net/duplicity/+bug/1170113
 * b861b0b8: Launchpad automatic translations update.
 * cdba7883: Update to translations.
 * 27020a8a: Merged in lp:~mterry/duplicity/argv-encode - Use the system filename encoding to print the args in unicode.
 * dcaddac5: Merged in lp:~louis-bouchard/duplicity/remove-allow-concurrency - remove the --allow-concurrency switch but leave the lock
 * d8a47a65: Remove --add-concurrency option and enhance the error message the case where an existing lockfile is detected
 * 96526dd6: Merged in lp:~louis-bouchard/duplicity/allow-concurrency-manpage
 * b04cddbf: Reformat --allow-concurrency text and add mention of stale lockfile
 * 512cc232: Update manpage with new --add-concurrency option
 * 7e1d3890: Merged in lp:~louis-bouchard/duplicity/add-allow-concurrency - Implement locking mechanism to avoid concurrent execution under the same cache directory. This is the default behavior. - Also implement --alllow-concurrency option to disable the locking if required. - This functionality adds a dependency to python-lockfile
 * 38249d92: Add the --allow-concurrency option to disable the locking mechanism that this patch implements. By default, only one instance of duplicity will be allowed to run at once. When using this switch it disable the locking mechanism to allow more than one instance to run simultaneously (LP: #1266763)
 * 2980f125: Merged in lp:~mterry/duplicity/boto-list-fix to fix bzr screwup.
 * 56f0ebc4: Raise exception if we can't connect to S3 rather than just silently pretending there are no files
 * f288ec31: Restored patch of gdocsbackend.py from original author (thanks ede) * Applied patch from bug 1266753: Boto backend removes local cache if connection cannot be made
 * 3ed2644b: ede Fri 2014-01-03 11:37:54 +0100 recommit: implement fix as suggested by original autor
 * e9e276fb: Encode sys.argv using system filename encoding before printing
 * 2bfdd781: recommit: implement fix as suggested by original autor http://lists.nongnu.org/archive/html/duplicity-talk/2013-11/msg00017.html
 * 52116849: Reformat to be more consistent. Remove tabs.
 * 97e50192: Reverted changes to gdocsbackend.py
 * 68669b89: Fix conflicts.
 * 23fe017d: Restored missing line from patch of gdocsbackend.py
 * b16838ce: leftover from previous commit (thx Kostas for paying attention)
 * fc461415: implement fix as suggested by original autor http://lists.nongnu.org/archive/html/duplicity-talk/2013-11/msg00017.html
 * e7e56733: Merged in lp:~mterry/duplicity/encoding - This branch hopefully fixes two filename encoding issues: Users in bug 989496 were noticing a UnicodeEncodeError exception which happens (as far as I can tell) because some backends (like webdav) are returning unicode filenames from list(). When these filenames are combined with the utf8 translations of log messages, either (A) the default ascii encoding can't handle promoting the utf8 bytes or -- if there aren't any utf8 bytes in the translation -- (B) the resulting unicode string raises an error later when log.py tries to upgrade the string again to unicode for printing. - This fix is largely implemented by adding a wrapper for backend list() implementations. This wrapper ensures that duplicity internals always see a byte string. (I'd like to eventually use this same wrapping strategy to implement generic retry support without backends having to add any logic, but that's just a thought for the future.) - That is, the fix for issue #1 is completely inside backend.py and the changes to backends/*.py. - The rest of the invasive changes deal with filenames that may not be valid utf8. This is much rarer, but possible. For proper handling of this, we need to print using unicode, and convert filenames from the system filename encoding to unicode, gracefully handling conversion errors. Some of the filenames we print are remote names. Who knows what encoding they are in; it could be different than the system filename encoding. 99% of the time, everything will be utf8 and we're fine. If we do get conversion errors, the only effect should be some question mark characters in duplicity logging output. - I tried to convert as much of the actual codebase to use unicode for printing. But I stopped short of adding an assert in log.py to enforce unicode, because I didn't want to go through all the backend code and manually adjust those bits without being able to test each one.
 * 1b2b953c: Nuke tabs.
 * 51bac048: Merged in lp:~ed.so/duplicity/debian.dav.mkdir - upstream debian patch "webdav create folder recursively" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * 3fcf2e56: Merged in lp:~ed.so/duplicity/debian.paramiko.log - upstream debian patch "paramiko logging" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * 5045b9c6: Merged in changes from main trunk.
 * 810cbe7e: Merged in lp:~verb/duplicity/boto-min-version - Update documentation and error messages to match the current actual version requirements of boto backend.
 * 4b2e8518: upstream debian patch "webdav create folder recursively" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * 0d8cbdbe: upstream debian patch "paramiko logging" http://patch-tracker.debian.org/package/duplicity/0.6.22-2
 * bdf48a09: Fix help printing
 * fe24d6dd: Promote filenames to unicode when printing to console and ensure that filenames from backend are bytes
 * fab4eff2: fix the fix for dropbox backend
 * c3716fc2: remove obsolete cfpyrax+http:// scheme from manpage
 * abdd306d: add mega documentation
 * 22944531: some formatting fixes to rman issues on website display
 * 786d086e: Launchpad automatic translations update.
 * b2eb2b0d: Changed to default to pyrax backend rather than cloudfiles backend. To revert to the cloudfiles backend use '--cf-backend=cloudfiles'
 * 3614e6db: Merged in lp:~jkrauss/duplicity/pyrax - Rackspace has deprecated python-cloudfiles in favor of their pyrax library, which consolidates all Rackspace Cloud API functionality into a single library. Tested it with Duplicity 0.6.21 on both Arch Linux and FreeBSD 8.3.0.
 * 5822860b: Launchpad automatic translations update.
 * b06ab120: Applied patch to fix "Access GDrive through gdocs backend failing" - see https://lists.nongnu.org/archive/html/duplicity-talk/2013-07/msg00007.html
 * 4edff903: Launchpad automatic translations update.
 * c146023b: Merged in lp:~mterry/duplicity/normalize-before-using - Avoid throwing an exception due to a None element in a patch sequence.
 * 568d6017: Merged in lp:~mterry/duplicity/disappearing-source - When restarting a backup, we may accidentally skip the first chunk of one of the source files. To reproduce this,: 1) interrupt a backup 2) delete the source file it was in the middle of 3) restart the backup
 * 7bcc034d: Merged in lp:~mterry/duplicity/manifest-oddities - We may accidentally end up with an oddly inconsistent manifest like so:
 * 35e5faf8: Merged in lp:~mterry/duplicity/log-path-type - Any backup browser built on top of duplicity will need to indicate which files in the backup are folders and which are files. The current logging information doesn't provide this detail. So I've added a field to the log.InfoCode.file_list output that includes the path type.
 * 7248e315: Merged in lp:~gliptak/duplicity/415619 - Better error message when chown fails
 * a0e4e7cb: Merged in lp:~verb/duplicity/bucket_root_fix - Fix bug that prevents backing up to the root of a bucket with boto backend.
 * c3988296: Avoid throwing exception because of None element in patch sequence
 * d51e2ed5: Merge latest manifest-oddities changes
 * d22f6c79: Fix test comments
 * daee1290: Handle a disappearing source file across restarts better
 * d6cab07e: Don't keep dangling volume info in manifest
 * bc85f340: Show path type in log when listing files
 * 9ea7abda: Fixed cfpyrax entry in man page
 * 0d02dc1c: Added Pyrax backend for Rackspace Cloud
 * 465d1db7: Added Pyrax backend for Rackspace Cloud
 * b07a8502: Merged in changes from main branch
 * 4e3af095: Better error message for chown fail
 * 1a96d688: Launchpad automatic translations update.
 * 78dda8c9: Merged in lp:~mterry/duplicity/argv - Fix use of argv when calling os.execve
 * 21744e42: Merged in lp:~mterry/duplicity/catch-seq-copy-error - Any* exception when running patch_seq2ropath should be ignored (though logged) and duplicity should move on. This covers the two asserts in that function (bug 1155345 and bug 720525) as well as errors that happen during file copying (bug 662442).
 * d18a08c1: Don't chop the first argument off when restarting (in an admittedly difficult-to-reach bit of code)
 * a6b9ea76: Fix some spacing
 * 303acc04: Wrap whole seq2ropath function in a general try/except rather than a more focused approach -- any problem patching a file should be ignored but logged before moving on
 * fc57d20e: If a common exception happens when collapsing a non-file patch, just log it and continue
 * eaa6c877: Launchpad automatic translations update.
 * 29a899f5: Merged lp:~mterry/duplicity/ignore-missing to fix patch for 1216921.
 * 7cdfe84e: Launchpad automatic translations update.
 * 151da79d: Applied patch from bug 1216921 to fix ignore_missing().
 * 4b56fb79: Or better yet, just drop the stanza, it shouldn't be needed
 * 07ef136e: Fix else: to be except Exception:
 * b1ed62e5: Fix util.ignore_missing; patch by Matthias Witte
 * a8ce24a0: Fixes for merging multi boto backend.
 * 3301b3e7: Fixes https://bugs.launchpad.net/duplicity/+bug/1218425
 * 0bbd1020: Fixed get_connection for new generic storage
 * c4278b57: Fixed merge conflicts after merging in changes from main branch, mostly due to Google Storage class addition
 * bf188e1c: Merge Conflicts
 * ad5d0fdc: Trying fix to properly destroy S3 connections.
 * 9daa4183: Update boto minimum version requirements
 * 40d7e5c7: Launchpad automatic translations update.
 * 5810c824: Changes for 0.6.22.
 * 07173a80: Launchpad automatic translations update.
 * 5631c245: Merged in lp:~ed.so/duplicity/man.page - update paramiko links - add command parameters to synopsis - add --compare-data - some polishing and several improvements
 * f70758d9: Launchpad automatic translations update.
 * debb240c: update paramiko links add command parameters to synopsis add --compare-data some polishing several improvements
 * b4046a2e: Launchpad automatic translations update.
 * 65871192: Applied patch from Eric S Raymond to man page to fix markup problems.
 * b172cd73: Merged in lp:~ckornacker/duplicity/megacloud - Add support for Mega (mega.co.nz) backend.
 * 3e751e2a: Merged in lp:~verb/duplicity/boto-gcs - These patches add support for Google Cloud Storage via the boto backend. - boto has supported GCS in interoperability mode for a few years now. This change adds support by taking advantage of boto's storage_uri abstraction layer.
 * fd4cc267: Merged in lp:~mhu-s/duplicity/swiftbackend - This branch adds support for Swift, the OpenStack Object Storage service. See https://blueprints.launchpad.net/duplicity/+spec/swiftbackend
 * 13d67fb9: Merged in lp:~scowcron/duplicity/ftp_password_pexpect - Use common backend.Backend get_password() rather than _ssh_pexpect.py specific code.
 * cddbe01a: README update for BOTO version requirement
 * eed8373e: Added support for AWS S3 Glacier
 * 8684f5cb: Add documentation for GCS to duplicity.1
 * ca7ed56b: Add config template for testing boto backend with GCS
 * 912634a9: Add support for Google Cloud Storage to boto backend (single threaded only)
 * d896b3c5: explicitly set umask in test_tarfile.py
 * 82c4e715: fix requesting filename
 * d8c1d7ba: add par2 wrapper backend
 * ba346914: Adds doc
 * de65dc87: better handling of authentication alternatives
 * 3dc3a33d: updates copyright
 * 33290406: Use FTP_PASSWORD with pexpect backend without requiring --ssh-askpass.
 * c0859af3: fixes data size type
 * abbd2f56: fixes missing argument
 * 990abe0a: fixes wrong environment variable being used
 * 6bd4a92e: adds OpenStack Swift backend
 * d191fb81: Added commentS
 * 72c0106d: Added max proc rule for multipart S3 uploads.
 * 191826c2: adapt to mega.py API changes
 * bccdc3ee: cleanup copyright notice
 * 63b08034: adding Mega backend for mega.co.nz
 * 509ae240: Launchpad automatic translations update.
 * be308264: Applied duplicity-ftps.patch from https://bugs.launchpad.net/duplicity/+bug/1104069 - Don't try to delete an empty file list.
 * a19850d8: Applied blocksize.patch from https://bugs.launchpad.net/duplicity/+bug/897423 - New option --max-blocksize (default 2048) to allow increasing delta blocksize.
 * 39bcb8a2: Merged in lp:~jnoster/duplicity/dpbx-added - The application key was approved as "production" one after some changes to the code to suit the requirements of Dropbox team (the keys are now obfuscated, for instance).
 * 50cfc2b2: Merged in lp:~juan-f/duplicity/progress - From time ago, there are people asking for a progress bar estimation in duplicity. There is even a script that circumvents the issue, getting info from the log so as to estimate the progress status ( https://github.com/quentin/Duplicity-progress ) but does not give enough feedback and the estimation is rather plain. - I have developed a set of heuristics that gather information from the deltas and the transfer ratios of the backend so as to forecast % of progress, estimation of remaining time and average speed, for both full and incremental backup uploads. - The current implementation works for boto backend, but to port the other backends to use this feature would be quite easy (we can discuss the details if interested). - The algorithm is activated by the --progress command line flag, and will perform a first-pass dry-run to collect evidence for all the deltas. Next it will trigger the real upload, while a thread statistically estimates the ratio of changes and compression for the data in/out, and uses these ratios to forecast time remaining and % of completion. - The progress data will be logged each 3 seconds, or the --progress-rate flag.
 * 14469f10: Merged in lp:~tblue/duplicity/paramiko-fix-delete-retry - This fixes bug #1115715, which is really annoying. Basically it makes using the Paramiko backend with the default settings impossible.
 * 362fc150: Actually merge in lp:~tblue/duplicity/paramiko-1.10.0 as previously reported.
 * f31b378b: Merged in lp:~townsend/duplicity/fix-1161599-2 - The fix in revno. 912 didn't take into account that the parameter "body" passed into request() is overloaded, so when it was NULL or of a type other than file, it would fail. This checks if "body" is of type "file" before actually seek()'ing back to the beginning of the file.
 * 59d5cbe2: Merged in lp:~tblue/duplicity/paramiko-1.10.0 - This fixes bug #1156746, making the Paramiko backend compatible with Paramiko 1.10.0. It keeps compatibility with older Paramiko versions.
 * 09736990: The fix in revno. 912 didn't take into account that the parameter "body" passed into request is overloaded, so when it was NULL or of a type other than file, it would fail. This checks if "body" is of type "file" before actually seek()'ing back to the beginning of the file.
 * d14cf43b: Launchpad automatic translations update.
 * be6692f1: Transient socket or HTTP errors will cause a retry of the PUT for a backup. This would then lead to 400 Bad Request errors from the server. This MP:
 * 23d9a8a4: Launchpad automatic translations update.
 * 219774a8: Fixes the case where the file pointer to the backup file was not being set back to the beginning of the file when an error occurs. This causes subsequent retries to fail with 400 Bad Request errors from the server. This is due to a change in revno. 901 where a file handle is used instead of a bytearray. * Fixes the removal of Content-Length from the header in revno. 901. Content-Length is required according to the Ubuntu One API documentation.
 * 75b54ab3: no more cleartext credentials in the code
 * a16e6c4f: Application Key & Secret get obfuscated to fit the rq of Dropbox.
 * 6b5995f2: progress: Removed an unneeded if
 * f463dfd6: progress: Fixes for the previous commit after extensive testing: Fixed the index computation for the rotating cache of Snapshots - Moved the start point for the Log progress thread after a proper computation of the starting volume in case of restart, and adapted code for it
 * 9e392446: progress: Cover the sigtar and manifest upload with the progress reporting. Now the last 1% will be dedicated to this upload and properly report stallment when network goes off while this happens.
 * d26b3a8d: progress: Fixed a missing condition for when the progress flag is not used
 * b31ae715: progress: Cap data progress upload from 0..99% and show 100% only when sigtar and manifest file has uploaded correctly
 * 8b455e47: progress: Avoid completed percentage to drops between backup retries when backup fails and has to be restarted. The current progress is offset by the previous uncompleted backup from the last volume that upload correctly. To achieve it, the progress tracker now snapshots the current progress to the cache each completed volume, then recovers this information later when retrying a failed backup.
 * 5e338b93: crosser's patch applied
 * dba8bddf: progress: The algorithm now will drop the confidence interval adaptively when overpassing the 100%. This may happen when the sigma is large due to a very heterogeneous distribution of the size of deltas in files. In this case, the C.I. will be drop by half to adapt to the variability. If it happens again, it will disregard the sigma and trust the mean only.
 * b286bcbc: progress: Simplified computation of progress to compute an upper bound, fit to a smooth curve. This method embraces better more "change distribution" scenarios and is much simpler to compute. And also, full backups will assume 1:1 correspondence in change distribution, so progress bars during full will be computed linearly, which is closer to reality.
 * 09a44c9b: Make the Paramiko backend work with Paramiko 1.10.0
 * 6e8c4848: propagate exceptions upward to facilitate retries
 * 2c5cb65f: Launchpad automatic translations update.
 * 7800ce88: Typo fixed
 * eb8b450b: log.py had no Error() to supplement Info(), Warn(), and Debug() - fixed.
 * d45f68d1: 1. usage note added (on separate Dropbox account). 2. extraneous and useless mkdir call was removed in put() method.
 * 94b4923b: Even more logging for unhandled exceptions to catch Error connecting to "api-content.dropbox.com"
 * b625bdb3: Traceback logging added for semi-unhandled exceptions to catch that strange .encode() call error.
 * 5d344934: Launchpad automatic translations update.
 * 0952ada8: Merged in lp:~ed.so/duplicity/verify.data - add switch --compare-data, to selectively enable formerly always disabled data comparison on verify runs
 * 8b220ef5: Merged in lp:~jnoster/duplicity/dpbx-added - Add Dropbox backend - NB! In order to use the backend one must: 1. Install Dropbox Python SDK first. 2. Run the duplicity with Dropbox backend (dpbx://) first time *interactively* to catch and follow the oAuth URL.
 * 84b07d2c: Applied patches from Laszlo Ersek to rdiffdir to "consume a chain of sigtar files in rdiffdir delta mode" which supports incremental sigtar files.
 * f5e31d15: renamed to --compare-data to make it reusable on other actions e.g. force data comparision on backup runs where files were modified but mtime was not set properly by buggy software
 * 4db3e6dc: add switch --verify-data, to selectively enable formerly always disabled data comparison on verify runs
 * d71d8fe3: note on first run was added to the man page
 * 10ebfa5e: THE BACKEND ITSELF HAS BEEN FINALLY ADDED.
 * fe8cb8f8: man page fixed to mention dpbx: backend
 * 2818371a: Dropbox backend (dpbx:) has been added.
 * 537fe9be: progress: Reporting speed in bps for log file
 * 9826c37a: Paramiko backend, delete(): Terminate when all files have been deleted successfully.
 * 91172de8: progress: Changed verbosity to NOTICE, so progress messages appears by default when --progress flag is on
 * 8f294fd0: progress: Added average speed to the log file
 * 475bcf9e: progress: Fixed a typo in if clause
 * 93bd7b10: progress: Bugfixed a posible division by zero
 * b8220a1f: progress: New feature to compute progress of compress & upload files The heuristics try to infer the ratio between the amount of data collected by the deltas and the total size of the changing files. It also infers the compression and encryption ration of the raw deltas before sending them to the backend. With the inferred ratios, the heuristics estimate the percentage of completion and the time left to transfer all the (yet unknown) amount of data to send. This is a forecast based on gathered evidence.
 * d3514201: Launchpad automatic translations update.
 * 49c13fb4: Merged in lp:~duplicity-team/duplicity/po-updates - Updated translations
 * 89e4b01c: Launchpad automatic translations update.
 * a47e2f5f: Merged in lp:~mterry/duplicity/py3rsync - This branch lets one build the _librsync module with Python 3. You can't really do anything useful with it, but it's a nicely-isolated piece to add Python 3 support for. - The changes are a mix of modernization and #ifdef logic. - All tests still pass in Python 2.7 and 2.4. I tested manually that the module worked as expected in Python 3.
 * 3f72f986: Merged in lp:~mterry/duplicity/pygi - Python bindings for the gobject stack (used in the gio backend) have changed from static to dynamically-generated bindings. The old static bindings are deprecated. So here's a branch to change the gio backend from old to new ones.
 * a3e9ac27: Merged in lp:~ed.so/duplicity/webdav.manpage - explanation of webdav changes above
 * 45738439: Merged in lp:~ed.so/duplicity/webdav.fix-retry - added ssl certificate verification (see man page) - more robust retry routine to survive ssl errors, broken pipe errors - added http redirect support
 * e88ca043: make _librsync module compile under Python 3
 * f4225a3a: Use PyGI instead of older pygobject style for gio backend
 * 0f26fc9e: Launchpad automatic translations update.
 * 6e86fc5c: move man page changes to a separate uptodate merge branch
 * 75958f28: webdav manpag updates
 * 3032843b: Launchpad automatic translations update.
 * 1a2e9490: Add auto-ctrl-c-test.sh to help stress-test restart support
 * dbe152e6: manpage - document ssl cert verification in man page backend.by - retry_fatal decorator accepts now premature fatal errors and supplys a retry_count instance variable webdavbackend.py - added ssl cert verification - added http redirect support - added always create new connection on retrys - much more debug output for problem pinpointing commandline.py, globals.py - added ssl cert verification switches errors.py - add FatalBackendError for signalling exactly that
 * b7f3f58d: Launchpad automatic translations update.
 * b49451f1: Launchpad automatic translations update.
 * 5eb9ff00: Merged in lp:~mterry/duplicity/static-corruption - This branch fixes three possible ways a backup could get data-corrupted. Inspired by bug 1091269. A) If resuming after a volume that ended in a one-block file, we would skip the first block of the next file. B) If resuming after a volume that ended in a multi-block file, we would skip the first block of the next file. C) If resuming after a volume that spanned a multi-block file, we would skip some data inside the file. - A and B are because when finding the right place in the source files to restart the backup, the iteration loop didn't handle None block numbers very well (which are used to indicate the end of a file). - C is what bug 1091269 talks about. This was because data block sizes would get smaller as the difftar file got closer and closer to the volsize. Standard block sizes were 64 * 1024. But say we were close to the end of the difftar... When resuming, duplicity doesn't know the custom block sizes used by the previous run, so it uses standard block sizes. And it doesn't always match up, as you can imagine. So we would leave chunks of data out of the backed up file. - Tests added for these cases. - This branch is called 'static-corruption' because all these issues occur even when the source data doesn't change. I still think there are some corruption issues when a file changes in between duplicity runs. I haven't started looking into that yet, but that's next on my list. - C only happened without encryption (because the gpg writer function already happened to force a constant data block size). A and B happened with or without encryption.
 * 6610ab9f: use a copy of file1 rather than writing out a new small file so that it is clearer the first block is skipped rather than the whole file
 * 31be83bb: add test to confirm expected behavior if new files appear before we restart a backup
 * 137efc02: whoops, fix a test I broke with last commit because I didn't add get_read_size to the mock writer
 * 7dc43438: Fix block-loss when restarting inside a multi-block file due to block sizes being variable
 * c90c4c63: Fix block-loss when restarting after a volume ends with a multi-block file; fixes test_split_after_large()
 * 649ee782: Fix block-loss when restarting after a volume ends with a small file; fixes test_split_after_small()
 * d54ca34b: Add more tests for various restart-over-volume-boundary scenarios
 * 56e58748: move non-encryption-specific tests to the right class
 * ade354ba: tests: add a WithoutEncryption class to restarttest.py
 * 4990faac: Launchpad automatic translations update.
 * 2ad3d0e5: reconnect on errors as a precaution against ssl errors see https://bugs.launchpad.net/duplicity/+bug/709973
 * aed583bb: Fixed 1091269 Data corruption when resuming with --no-encryption - Patches from Pascual Abellan that make block size consistent and that add no-encryption option to manual-ctrl-c-test.sh. - Modified gpg.py patch to use 64k block size so unit test passes.
 * 614fc318: Launchpad automatic translations update.
 * ff27716b: Merged in lp:~ed.so/duplicity/u1_and_manpage - Manpage - document Ubuntu One required python libs - added continuous contributors and backend author notes - U1backend - lazily import non standard python libs, fixes http://article.gmane.org/gmane.comp.sysutils.backup.duplicity.general/5753 - fix "not bytearray" prevents PUT with python 2.6 - don't hang after putting in credentials (cause it silently retries in background) but go through with backup
 * 561d37f3: python3 fix reuse normalized url from oauth
 * c1488929: why bother reading when we can deliver a filehandler alltogether
 * a3003006: fix "not bytearray" prevents PUT with python 2.6
 * 754b4bb9: don't hang after putting in credentials (cause it silently retries in background) but go through with backup
 * 951a6218: fix imports not being global
 * 27e3c5bb: Manpage - document Ubuntu One required libs - added continous contributors and backend author notes
 * 43f49001: Launchpad automatic translations update.
 * d1bc8bfc: Merged in lp:~ed.so/duplicity/manpage - Clear up PASSPHRASE reusage as sign passphrase. Minor fixes.
 * adb318bf: Merge changes from trunk.
 * d642bb28: Merged in lp:~ed.so/duplicity/webdav.fix-retry - bugfix: webdav retrying broke on ERRORS like "error: [Errno 32] Broken pipe" in socket.pyas reported here https://answers.launchpad.net/duplicity/+question/212966 added a more generalized 'retry_fatal' decorator which makes retrying backend methods even easier
 * 6383ecf2: Launchpad automatic translations update.
 * a00155c5: Merged in lp:~carlos-abalde/duplicity/gdocs-backend-gdata-2.0.16.-upgrade - Upgrade of GoogleDocs backend to python gdata lib >= 2.0.15: Stop using get_everything method.
 * 973281eb: Merged in lp:~mterry/duplicity/u1-utf8 - Make sure u1backend returns filenames as utf8
 * 5ed459ec: Merged in lp:~lenharo-h/duplicity/duplicity - Generate encrypted backups without revealing the user's key id via option --hidden-encrypt-key
 * 6ee1b193: Merge changes from trunk.
 * e40229a4: add correct error code catch only exceptions again
 * 37ddaf7f: catch exceptions only
 * 1ff7fad1: show error value instead of class
 * 17461679: bugfix: webdav retrying broke on ERRORS like "error: [Errno 32] Broken pipe" in socket.pyas reported here https://answers.launchpad.net/duplicity/+question/212966
 * 072c7ae3: Launchpad automatic translations update.
 * 456a802b: Make sure u1backend returns filenames as utf8
 * 41c3230a: Now files are directly uploaded to destination folder/collection. This also fixes bug that created a copy of all files in the root folder/collection in Google Drive
 * 3d80db63: Added --hidden-encrypt-key testcases.
 * bdfda325: Nuke tabs.
 * cb2e74a5: Added more details in man page.
 * 94deaa7e: Fixed a typo in man mage.
 * c95c685b: Allows duplicity to encrypt backups with hidden key ids. See --hidden-recipient in man gpg(1)
 * 2570137c: Launchpad automatic translations update.
 * 28106aba: avoid using TestCase.addCleanup, which isn't in older python versions
 * 25b8d581: Merged in lp:~ed.so/duplicity/lftp.netrc - Allow .netrc auth for lftp backend * Merged in lp:~mterry/duplicity/946988 - This fixes bug 946988 by not duplicating the checks for when we should ask for the password (those same checks are done more correctly inside get_passphrase). And add a test to reproduce the bug.
 * bd350695: allow .netrc auth for lftp backend
 * 574de9c6: clear up PASSPHRASE reusage as sign passphrase minor fixes
 * 87a2e20c: don't duplicate a test for whether we should get passphrase in two places -- one of them will be out of sync
 * 3ef2fcfa: Launchpad automatic translations update.
 * 9b07d0aa: Launchpad automatic translations update.
 * 30442b16: Merged in lp:~ed.so/duplicity/manpage - more formatting fixes, clarifications in sections EXAMPLES, FILE SELECTION
 * 31aeff19: Merged in lp:~satwell/duplicity/caching - Add a cache for password and group lookups. This significantly improves runtime with very large password and group configurations.
 * 4fdc75bd: Add a cache for password and group lookups. This significantly improves runtime with very large password and group configurations.
 * a0e435a7: Launchpad automatic translations update.
 * c1839dc5: Launchpad automatic translations update.
 * ec1b6784: Merged in lp:~mterry/duplicity/u1-ascii-error - Fix for u1backend unicode error. Patch by Paul Barker.
 * 7c5b121b: Merged in lp:~mterry/duplicity/delete-new-sig-in-cache - In duplicity 0.6.20, we fixed bug 1031269. This means that we no longer leave sig files on the remote location. Leaving sig files on the remote location also caused a bug with deleting cache files. Code used to leave remote new-sig but delete the locale cache new-sig; this meant that we would keep downloadoing the new-sig all the time from remote. We had worked around that by just not deleting the new-sig in the cache, which was sort of the wrong side of that problem to tackle. Now that we handle the remote new-sigs better (by deleting them), I don't think we need this code anymore. Patch by az@debian.org.
 * 0890e155: Merged in lp:~mterry/duplicity/u1-oauthlib - As the Ubuntu packager for duplicity, I would prefer u1backend.py used oauthlib instead of oauth. oauthlib is well maintained upstream (unlike oauth), has a python3 port (for the future), and is in Ubuntu main (so is oauth right now, but hopefully in the future we can drop it to universe, in which case duplicity can't use it anymore).
 * 68b062ed: port u1backend to oauthlib
 * c3b32d83: we no longer need to preserve new-sigs in the cache, since we fixed the bug keeping them on the remote side
 * cdedcf6b: Fix U1 backend's ascii error. Patch by Paul Barker
 * 6f267279: more formatting fixes, clarifications in sections EXAMPLES, FILE SELECTION
 * 78affbfb: Launchpad automatic translations update.
 * 4aa41ee0: Merged in lp:~ed.so/duplicity/24syntaxfix - fix python 2.4 vs 2.5 syntax error
 * c4403978: fix python 2.4 vs 2.5 syntax error
 * 4179a372: Launchpad automatic translations update.
 * 6b336171: Remove dist/mkGNUchangelog script. * Prep files for 0.6.20 release.
 * 2bc0a41a: Launchpad automatic translations update.
 * b1294de0: Applied patch from az for bug #1066625 u1backend + add delay between retries
 * 52ef2f61: Launchpad automatic translations update.
 * aa197595: Merged in lp:~mterry/duplicity/u1-402 + Switch the code we check for out-of-space in u1backend.
 * 1d53a50b: u1backend: interpret http code 402 as no-space-left rather than 507
 * b598ade3: Launchpad automatic translations update.
 * e54b37a1: 1039001 --exclude-if-present and --exclude-other-filesystems causes crash with inaccessible other fs
 * dd280fbe: 995851 doc improvement for --encrypt-key, --sign-key
 * 5312531b: 1066625 ubuntu one backend does not work without gnome/dbus/x11 session
 * 09014514: Launchpad automatic translations update.
 * c827bef6: Updated Changelog.GNU
 * ecc3f0a4: Merged in lp:~ed.so/duplicity/ssh.manpage + added gdocs and rsync REQUIREMENTS + added cloudfiles documentation
 * 6d49a3bb: Merged in lp:~ed.so/duplicity/gpginterface + refactor GnuPGInterface to gpginterface.py reasoning can be found in README
 * 9afc3154: added gdocs, rsync REQUIREMENTS
 * 5675ab6f: some clarifications in README
 * c89dd113: refactor GnuPGInterface to gpginterface.py reasoning can be found in README
 * 983eed3a: some refinements add cloudfiles documentation
 * f60695db: Launchpad automatic translations update.
 * 4a7a3634: Merged in lp:~ed.so/duplicity/gpg.tmp + place gpg.py tempfiles in duplicity's tmp subfolder which is cleaned whatever happens
 * 72871731: place gpg.py tempfiles in duplicity's tmp subfolder which is cleaned whatever happens
 * f044bc99: sort urls alphabetically add abs vs. relative file urls
 * 27a2514c: typo
 * b77cc2d6: minor fix
 * a0877b72: some clarifications mostly for ssh pexpect backend
 * d59dfbfa: Launchpad automatic translations update.
 * 32e33cd7: tests: apparently on hardy chroots, /bin can be smaller than 3MB compressed, so instead of using /bin in test_multi_volume_failure, use largefiles
 * 2f7a5bdf: tests: whoops, I had accidentally disabled one of the new tests for ignoring double entries in a tarball
 * 4dbffa3c: tests: don't use subprocess.check_output, which was only added in Python 2.7
 * ab1fe512: Launchpad automatic translations update.
 * d5880386: don't use unittest.TestCase.assertSetEqual, which isn't supported in older Python versions
 * 9b3bcd4f: Merged in lp:~ed.so/duplicity/ssh-pexpect-msgbug + Fixes 'UnboundLocalError: local variable 'msg' referenced before assignment' in _ssh_pexpect.py
 * 69328f22: probably fix
 * 59f8ffc6: Launchpad automatic translations update.
 * 2b1fc1ae: Wrap CHANGELOG to col 80.
 * 4a54258a: Merged in lp:~mterry/duplicity/ropath.index + This branch does two main things: 1) Skips base dir entries when compiling the list of deleted delta iters. (this gracefully recovers from the sort of situations that lead to bug 929067). I'm reasonably confident this is an uninvasive change, but please confirm. 2) Overwrites the sigtar file on backup-restart. This is because AFAICT, duplicity will rewrite the entire sigtar each restart. But we were opening the sigtar file as "ab", so we'd just dump the contents on top of the previous contents. Which was causing some confusion in bug 929067. If I'm wrong that we don't always rewrite the entire sigtar each time, this needs some rethink. Please also confirm that. + In addition, I added two tests for the above two changes and make some improvements elsewhere in the restarttest.py file while I was at it.
 * f79c52bc: Merged in lp:~gregretkowski/duplicity/cf-retry-delete + This will retry cloudfile delete commands. With large numbers of archive files over mediocre links transient network errors will occasionally cause deletes to fail and these should be retried.
 * 6c0d5501: Merged in lp:~ed.so/duplicity/duplicity.manpage + disabled hyphenation and block justification for better readablility of command line examples. + reformatted REQUIREMENTS section for hopefully better online rendering + minor clarifications
 * bf5022e3: Merged in lp:~mterry/duplicity/leftover-sigtar + So currently, duplicity does not delete signature files when doing a remove-all-but-n operation. Seems wrong, since those signature files are now useless and take up space. + This branch does several things: 1) Make remove-all-but-n operate on chains. In practice it did before, since the sets it operated on always came from complete chains (i.e. it never used only some of the sets from a chain) 2) Add a new method to get all signature chains before a certain time. 3) Use this new method to also delete signature chains during remove-all-but operations. + And it cleans up the cleanuptest.py file: 1) Removes crufty, unused code 2) Disallows changing the destination folder for the test, which no one would ever want to do and isn't really supported anyway 3) Add some additional checks to the existing test 4) Adds two new methods to test remove-all-but-n and remove-all-inc-of-but-n-full
 * 49bac061: Merged in lp:~mterry/duplicity/1031277 + ssh: actually delete all the requested files, not just the first one
 * c182b561: gracefully handle multiple duplicate base dir entries in the sigtar; avoid writing such entries out
 * 542d8f81: Retry cloudfiles deletes
 * 468cf5c3: missing space
 * a3125350: disabled hyphenation and block justification for better readablility of command line examples. - reformatted REQUIREMENTS section for hopefully better online rendering - minor clarifications
 * c48ca2e7: delete signature files when doing remove-all-but
 * 29e17519: ssh: actually delete all the requested files, not just the first one
 * 5ef92fea: Launchpad automatic translations update.
 * ab13ee49: Merged in lp:~mterry/duplicity/utf8-po.
 * dcf9e878: make sure translations are in utf-8
 * be4d806d: Launchpad automatic translations update.
 * 6d5b3e1b: Fix dates.
 * f7ba2848: Launchpad automatic translations update.
 * 972a360c: Merged in lp:~ed.so/duplicity/duplicity.tmpspacefix
 * 3b5c6bb7: Merged in lp:~ed.so/duplicity/duplicity.helpfix
 * e88ad272: use tempfile.TemporaryFile() so unused temp files are deleted automagically
 * b55b9d67: propbably solve bug 'Out of space error while restoring a file' see bug tracker/mailing list https://bugs.launchpad.net/duplicity/+bug/1005901 http://lists.gnu.org/archive/html/duplicity-talk/2012-09/msg00000.html
 * 1ab97913: fix rare 'TypeError: encode() argument 1 must be string, not None' read here http://lists.nongnu.org/archive/html/duplicity-talk/2012-09/msg00016.html
 * f5f1035d: Launchpad automatic translations update.
 * 78ed03d7: Launchpad automatic translations update.
 * 96f61241: Launchpad automatic translations update.
 * 3f2a5d25: log.py: add a couple comments to reserve error codes 126 and 127 because they conflict with running duplicity under pkexec (very similar to how 255 is reserved because gksu uses it)
 * 41815d80: Add note on GnuPGInterface and multiple GPG processes.
 * 7a220174: Merged in lp:~ed.so/duplicity/backend_fixes
 * 0c2f22d8: fixed ssh/gio backend import warnings + ssh paramiko backend imports paramiko lazily now + gio backend is not imported automatically but on request when --gio option is used - added a warning when --ssh-backend is used with an incorrect value
 * 37a95c8c: Launchpad automatic translations update.
 * 18694157: Merged in lp:~ed.so/duplicity/ssh-fixes
 * c63aad54: ssh paramiko backend respects --num-retries now - set retry delay for ssh backends to 10s - ssh pexpect backend + sftp part does not claim 'Invalid SSH password' although it's only 'Permission denied' now + sftp errors are now more talkative - gpg.py + commented assert which broke otherwise working verify run
 * 10c101ac: ssh paramiko backend respects --num-retries now - set retry delay for ssh backends to 10s - ssh pexpect backend + sftp part does not claim 'Invalid SSH password' although it's only 'Permission denied' now + sftp errors are now more talkative - gpg.py + commented assert which broke otherwise working verify run
 * 73eec0b2: Launchpad automatic translations update.
 * bfc751e6: A couple more warning error codes that Deja Dup is interested in noticing.
 * 41ef3c0c: If the gio backend wants to ask a question during its mount phase, it previously just aborted. This branch allows it to continue, though not to make an intelligent answer.
 * 1fdecf3d: add a couple more warning codes for machine consumption of warnings
 * 71408bcb: allow answering gio mount questions (albeit naively)
 * e741f4ed: Launchpad automatic translations update.
 * e71ad6ee: Merged in lp:~ed.so/duplicity/0.6-readd_sshpexpect - readd ssh pexpect backend as alternative - added --ssh-backend parameter to switch between paramiko,pexpect - manpage -- update to reflect above changes -- added more backend requirements - Changelog.GNU removed double entries
 * ee4016c3: add missing files
 * c8967e38: readd ssh pexpect backend as alternative - added --ssh-backend parameter to switch between paramiko,pexpect - manpage -- update to reflect above changes -- added more backend requirements - Changelog.GNU removed double entries
 * deba24e9: Merged in lp:~ed.so/duplicity/0.6-ssh_add_missinghostkey
 * d4949e43: Merged in lp:~carlos-abalde/duplicity/gdocs-backend-gdata-2.0.16.-upgrade.
 * 798f7a3b: changelog entry
 * 5535cdb0: add missing_host_key prompt similar to ssh procedure
 * 2ea70980: Fixing most basic stuff. Pending all testing
 * 457714e2: Launchpad automatic translations update.
 * c85b8496: Merged in lp:~ed.so/duplicity/0.6-ssh_config
 * cb4b20a8: Merged in lp:~ed.so/duplicity/0.6-webdav_fixes.
 * 81e8be0b: Merged in lp:~ed.so/duplicity/0.6-manpage
 * 4989348c: changelog entry
 * 27862256: added REQUIREMENTS section - restructure SYNOPSIS/ACTIONS to have commands sorted by backup lifecycle - added restore and some more hints when --time or --file-to-restore are supported - replaced scp:// with sftp:// in examples as this is the suggested protocol anyway - added an intro text to ACTIONS section - adapted --ssh-askpass description to latest functionality
 * c71e940c: empty listbody for enhanced webdav compatibility - bugfix: initial folder creation on backend does not result in a ResponseNotReady anymore
 * 3e5a8715: add ssh_config support (/etc/ssh/ssh_config + ~/.ssh/config) to paramiko sshbackend
 * b7f0371d: Launchpad automatic translations update.
 * ad84ac47: Launchpad automatic translations update.
 * 5797002b: Changes for 0.6.18.
 * f12830a4: Use correct dir name for cleanup.
 * 558c36f3: Adjust roottest.py to new test dir structure.
 * 1cf73a8e: Changes for 0.6.18.
 * e92cbc41: Some code/import changes to make the ssh and boto backends compatible with Python 2.4.
 * 52054338: Changes for 0.6.18.
 * 828ac640: Changes for 0.6.18.
 * 59f1f82a: Fix for bug 931175 'duplicity crashes when PYTHONOPTIMIZE is set'
 * 9bd2b99e: Launchpad automatic translations update.
 * 7d9dcc00: Remove duplicate line.
 * 3efbb86d: File /etc/motd may not exist in test environment. Use __file__ instead to point to a known plaintext source file.
 * 0d0e970f: Remove tests for 884371. Can't test that yet.
 * a73cd262: Raise log level on backend import failure so it will be visible under default conditions.
 * 6d8c78d9: Launchpad automatic translations update.
 * d29a8c11: Fix for bug 929465 -- UnsupportedBackendScheme: scheme not supported in url: scp://u123@u123.example.com/foo/
 * 84b91506: Launchpad automatic translations update.
 * 7c345eee: Applied patch from 930727
 * 1ee92ff8: Launchpad automatic translations update.
 * e51587b8: Merged in lp:~mterry/duplicity/nopexpect
 * 702c12c6: Merged in lp:~mterry/duplicity/testfixes
 * cc909b7b: a couple small code fixes to help tests pass
 * cfbdf80d: drop unused pexpect.py
 * 7c3b13b2: Launchpad automatic translations update.
 * ce534124: Applied patch by Alexander Zangerl from bug 909031, "SSH-Backend: Creating dirs separately causes a permissons-problems".
 * 89e2979b: Merged in lp:~nguyenqmai/duplicity/file-prefix-option.
 * e4223571: Merged in lp:~mterry/duplicity/memleak
 * a8dd2349: Merged in lp:~mterry/duplicity/always-delay
 * f4bf66e3: Merged in lp:~tobias-genannt/duplicity/nocompress
 * 0665583f: Added patch for testing of bug 884371, 'Globbing patterns fail to include some files if prefix is "**"'
 * 39b99be6: Applied patch from 916689 "multipart upload fails on python 2.7.2"
 * 85f7531c: Applied patch from 884638 and fixed version check to allow Python 2.5 and above.
 * 0c366be0: Don't have TarFile objects cache member TarInfo objects; it takes too much space
 * 47630ef6: change the way the file_naming regular expressions are created to support --file-prefix option
 * f34bde7b: always delay a little bit when a backend gives us errors
 * d525e9fc: Launchpad automatic translations update.
 * 2167da58: changelog update - fixed comment
 * 69ef259c: Added option to not compress the backup, when no encryption is selected
 * d7707ccd: Merged in lp:~mterry/duplicity/resume-inc
 * 41754292: Merged in lp:~mterry/duplicity/more-test-fixes
 * 00600c86: resuming an incremental results in a 'Restarting backup, but current encryption settings do not match original settings' error because curtime is incorrectly set away from previous incremental value
 * 480de26b: tests: make other-filesystem check more robust against certain directories being mounts or not
 * 2f729a9b: tests: use backup source that is more likely to be larger than 1M compressed
 * 58016074: tests: add delay between backups to avoid assertion error
 * aceff90c: Fix extraneous '.py' that keeps import from working.
 * ce2e2058: Launchpad automatic translations update.
 * a04f5362: Launchpad automatic translations update.
 * 96fc59f0: Launchpad automatic translations update.
 * 75a80250: Changes for 0.6.17
 * 9a9f114c: Not used.
 * 6bfc9096: Run tests using virtualenv for each.
 * 8a7730a5: Make adjustments for the new structure. - Adjust boto requirements to be 1.6a or higher. - Cleanup install scripts.
 * 4685caf1: Some doc changes including new requirements.
 * 09b43d38: Don't assume dir location for Python.
 * c3a6ce5f: Added --rsync-options flag to allow user to pass options to rsync at will.
 * 94eda401: 878964: Resuming a backup with a different password should throw an error
 * dbcfce03: Launchpad automatic translations update.
 * 43206255: 411145 Misleading error message: "Invalid SSH password"
 * 93e8c01d: Launchpad automatic translations update.
 * 59e4e8e0: Split botobackend.py into two parts, _boto_single.py which is the older single-processing version and _boto_multi.py which is the newer multi-processing version. The default is single processing and can be overridden with --s3-use-multiprocessing.
 * 01fe3bc4: The function add_filename was rejecting anything non-encrypted as a legit file. This fixes that problem and the bug.
 * 76f6a040: Fix to allow debugging from pydev. The check for --pydevd must be done after command line is parsed.
 * 1453ce69: Launchpad automatic translations update.
 * aa3c5453: Merged in bzr merge lp:~summer-is-gone/duplicity/tz-incremental-fix.
 * f2e24d72: Remove random_seed from VCS, adjust .bzrignore.
 * 69a700f6: Remove localbackend.testing_in_progress since all it accomplished was to make the local backend test fail.
 * 03472c55: Merged in lp:~mterry/duplicity/ship-tests and moved a couple of things around to get manual tests working
 * eab6b63a: Adds --rsync-options to command line Allows uer to pass additional options to the rsync backend Commit include paragraph in man page, new global variable, and the small changes needed to the backend itself
 * 2b547131: Launchpad automatic translations update.
 * c83829f9: -- Applied patch 0616.diff from bug 881070. -- Fixed compile issues in reset_connection. -- Changed 'url' to 'parsed_url' to make consistent with backends.
 * 85b44aad: Make tarball layout match bzr layout much more closely; ship tests in tarballs and adjust things so that they can work
 * f91d19cd: rename auto/ to tests/
 * 68068f34: undo accidental changes to run-tests and convert pathtest and rdiffdirtest (for both of which, I uncommented a failing test I didn't understand)
 * e6316243: move some more custom scripts to manual/
 * 92fec48e: move some things around; converge on one script for running any kind of test or list of tests
 * 5f3640d9: convert patchdirtest to auto; rip out its root-requiring tests and move them to roottest script; fix roottest script to work now with the new rootfiles.tar.gz, whoops
 * 63375d59: convert finaltest to auto; workaround an ecryptfs bug with long filenames in the test
 * 4d4fc8ad: drop state file random_seed from test gnupg home
 * 9eb312e1: convert gpgtest to auto; add testing keys to the suite, so testers don't have to make their own; delete gpgtest2, as it didn't do anything
 * e23c6aca: drop unused darwin tarball and util file
 * 9fff9e9f: convert GnuPGInterfacetest and dup_timetest to auto
 * e37f4f8d: convert file_namingtest, parsedurltest, and restarttest to auto
 * 72ebfd7c: convert manifesttest, selectiontest, and test_tarfile to auto
 * dd07db65: convert cleanuptest, dup_temptest, and misctest to auto
 * 0bf65488: convert statisticstest to auto; make sure tests are run in English and in US/Central timezone
 * 937f1e90: convert statictest to auto
 * e4be9efa: convert tempdirtest to auto
 * 625dc68d: convert logtest to auto
 * 230dc49d: convert lazytest to auto
 * b65440b5: clean up run scripts a little bit, rename testfiles.tgz to rootfiles.tgz
 * bb97c56b: make diffdirtest auto
 * f5283ce2: make badupload auto
 * 41725db9: make collectionstest auto
 * e99418fe: Changed functions working with UTC time file format from localtime() to gmtime() and timegm()
 * 5e200836: Fixed time_separator global attribute usage in some tests
 * 624eca0b: Made proper setUp method for tests in dup_timetest.py.
 * 0456c552: move all manual tets into their own subdirectory
 * b17e11d8: Launchpad automatic translations update.
 * 28fc3711: Launchpad automatic translations update.
 * 8bc11bb6: check that we have the right passphrase when restarting a backup
 * 77e323bd: Launchpad automatic translations update.
 * ecadddcc: Changes for 0.6.16.
 * 8cacad97: Changes for 0.6.16.
 * e2c3b5f8: Launchpad automatic translations update.
 * d4a6a93f: Merge in lp:~duplicity-team/duplicity/po-updates
 * c7974c1e: Merge in lp:~duplicity-team/duplicity/po-updates
 * a606257f: Remove Eclipse stuff from bzr.
 * 0b0ed5c1: Launchpad automatic translations update.
 * bf4cfd55: Launchpad automatic translations update.
 * 19744678: Update .pot and add all languages to LINGUAS list file.
 * 4511faa1: Merged in lp:~ed.so/duplicity/UnicodeDecodeError
 * 1fa852a7: some links for UnicodeDecodeError
 * 17c39e45: fix UnicodeDecodeError: 'ascii' codec can't decode byte on command usage
 * d33af96d: Remove evil tab characters causing indent errors.
 * ba745b02: 838162 Duplicity URL Parser is not parsing IPv6 properly
 * 7fc36d08: 676109 Amazon S3 backend multipart upload support
 * 4d89560b: 739438 Local backend should always try renaming instead of copying
 * 129ad0eb: Merge in lp:~ed.so/duplicity/manpage
 * 26d9ac4f: Checkpoint
 * 29634dcc: updated --verbosity symmetric and signing
 * 2be832bd: Merged in lp:~mterry/duplicity/rbNoneNone
 * 79277ab1: Merged in lp:~ross-ross-williams/duplicity/gpg-agent-fix
 * 07639d1b: Merged in lp:~mterry/duplicity/fix-local-backend-validation
 * 087e3b2a: Merged in lp:~mterry/duplicity/partial-encryption
 * 96695389: Merged in lp:~mterry/duplicity/tarfile
 * ff923f7f: make sure sig_path is a regular file before opening it
 * 28320d6e: Launchpad automatic translations update.
 * f1b958a9: gpg2 will not get the passphrase from gpg-agent if --passphrase-fd is specified. Added tests to disable passphrase FD if use_agent option is true.
 * 83449d39: use cached size of original upload file rather than grabbing it after put() call. Some backends invalidate the stat information after put (like local backend after a rename)
 * cc21f0b4: allow upgrading partial chain encryption status
 * bd833b40: Merged lp:~duplicity-team/duplicity/check-volumes
 * d7d930ca: 832149: Uploads to Rackspace fail silently
 * 5fb50940: Launchpad automatic translations update.
 * b9b301e7: make query_info a little easier to use by guaranteeing a well-formated return dictionary
 * ed6f4664: add rackspace query support
 * 794ebccd: add query support to boto backend
 * f69e8431: make clear the difference between sizes from errors and backends that don't support querying
 * 7ab2da12: cloudfiles: allow listing more than 10k files
 * b573d476: Launchpad automatic translations update.
 * 426f254c: Launchpad automatic translations update.
 * 65daa352: add query_info support to u1 backend
 * 4247b782: first pass at checking volume upload success
 * 42a86092: Launchpad automatic translations update.
 * aa4e8171: Launchpad automatic translations update.
 * 9e066034: make tarfile.py 2.4-compatible
 * cac621ba: use python2.7's tarfile instead of whichever version comes with user's python
 * d7bb389b: usability enhancement: sign passphrase prompt has no second verification prompt anymore, symmetric passphrases are still verified
 * ef113aa8: Sync with master.
 * 50552cb5: drop sign passphrase verification prompt
 * 1049e91e: bugfix of rev767 on using sign key duplicity claimed 'PASSPHRASE variable not set'
 * 634c2a7f: Launchpad automatic translations update.
 * a38aed4a: use a proper fake TarFile object when reading an empty tar
 * db356204: handle empty headers better than passing ignore_zeros -- instead handle ReadErrors
 * 3a1f0952: remove another non-2.4-ism I introduced
 * 69c3549e: and update trailing slashes in test too
 * f8abf3cf: fix how trailing slashes are used to be cross-python-version compatible
 * dcc84bad: whoops, forgot an import
 * 34f7d596: handle different versions of tarfile
 * 01fcfc3a: first pass at dropping tarfile
 * 3f689297: Changes for 0.6.15.
 * d17a8b3f: fixes to unit tests to support SIGN_PASSPHRASE.
 * d5aa1a98: introduce --numeric-owner parameter patch courtesy of Lukas Anzinger <l.anzinger AT gmail.com> - duplicity:restore_check_hash 'Invalid data - *** hash mismatch' lists the offending filename
 * 685c4591: Remove use of virtualenv.
 * 81151137: Ignore ENOENT (file missing) errors where it is safe. - Set minimum Python version to 2.4 in README.
 * bb36617a: typo fix
 * a13dd1cf: numowner & hash mismatch verbosity
 * 3b7f30f8: 824678 0.6.14 Fails to install on 8.04 LTS (Hardy)
 * 2d48bf30: 823556 sftp errors after rev 740 change
 * 4f7ee4ce: Launchpad automatic translations update.
 * 7ed47ed5: Launchpad automatic translations update.
 * 85064074: Launchpad automatic translations update.
 * 5f19a14d: Merged in lp:~carlos-abalde/duplicity/google-docs
 * b7d81ea9: Merged in lp:~mterry/duplicity/u1-fixes
 * b15e28b8: Fixed indentation: 2 to 4 spaces
 * ccc203a2: some u1 backend fixes: handle errors 507 and 503; add oops-id to message user sees so U1 folks can help
 * 4a84a9b0: Launchpad automatic translations update.
 * 416d1acd: Fetching user password correctly (i.e. not using directly self.parsed_url.password)
 * e416f517: Now using backend.retry(fn) decorator to handle API retries
 * 63616048: Added subfolders support + several minor improvements and fixes
 * b56f7d9e: Merged in lp:~ed.so/duplicity/encr-sign-key2
 * e96719f6: Merged in lp:~ed.so/duplicity/encr-sign-key2
 * d128aa4c: 818178 Shouldn't try to delete files it knows don't exist
 * a9e46972: Merged in lp:~mterry/duplicity/retry-u1
 * b8d29fd8: Don't try to delete partial manifests from backends
 * 80acb166: Added support for captcha challenges
 * 298b872f: retry operations on u1 backend
 * 0a8f652d: Replacing get_doclist by get_everything in put & delete methods. Raisng BackendException's in constructor
 * d6cd079d: Replaces get_doclist by get_everything when retrieving remote list of files in backup destination folder
 * b50d5ad8: Added authentication instruction for accounts with 2-step verification enabled
 * 5236fee3: A couple of assert + missing local_path.setdata on remote file get
 * 7683bb24: Better error logging + retries for each API op
 * d91debc6: Improved upload: check duplicated file names on destination folder + better error handling
 * 23df8ca7: Improved API error handling
 * 60ee27d8: Checking Google Data APIs Python libraries are present
 * fc97adb8: Fixed URI format
 * e2a5fc0a: First usable prototype
 * 3469d519: Merged lp:~mterry/duplicity/815635
 * 1cc9d58c: Merged lp:~mterry/duplicity/report-encrypted-chains
 * cf3f939e: Merged lp:~mterry/duplicity/more-accurate-sync
 * 90b6b712: when copying metadata from remote to local archive, first copy to a temporary file then move over to archive
 * 93bc6e0a: report whether a chain is encrypted or not
 * a4308baf: be more careful about what we try to synchronize
 * 4fc4842d: introduce --encrypt-sign-key parameter - duplicity-bin::get_passphrase skip passphrase asking and reuse passphrase if sign-key is also an encrypt key and a passphrase for either one is already set - add _() gettext to text in duplicity-bin::get_passphrase - document changes and minor additions in manpage
 * 941dd279: Launchpad automatic translations update.
 * 38504fba: 703142 AssertionError: assert len(chain_list) == 2
 * ad6a7eb6: 794576 Transport endpoint is not connected
 * c4042346: pay attention to local partials when sync'ing metadata and make sure we don't end up with three copies of a metadata file
 * d0345271: ignore ENOTCONN when scanning files
 * f46d5099: Really restore threaded_waitpid().
 * 592b8904: Merged in lp:~mterry/duplicity/guard-tarinfo
 * 4634323f: Detabify. Tabs are evil.
 * b0c7544e: Restore previous version with threaded_waitpid().
 * 3c03f1c2: also guard the recursive call
 * 7ae058d7: guard tarinfo object from being None
 * 9fb2b17b: Launchpad automatic translations update.
 * b3f2c7b0: Ignore 404 errors when we try to delete a file on Ubuntu One.
 * 39a72387: Update to duplicity messages.
 * 6de059ac: u1backend: ignore file-not-found errors on delete
 * ac2f1ba0: Launchpad automatic translations update.
 * 58159e98: 777377 collection-status asking for passphrase
 * 799d07a8: 680425 Endless retype passphrase when typo 793096 Allow to pass different passwords for --sign-key and --encrypt-key
 * 7119af43: duplicity.1: move information about the PASSPHRASE and SIGN_PASSPHRASE environment variables to the Environment Variables section - duplicity.1: add information about the limitation on using symmetric+sign to the bugs section - In the passphrase retrieval function get_passphrase, do not switch from "ask password without verifying" to ask+verify if the passphrase was empty - Allow an empty passphrase for signing key - Make clear in the verification prompt whether the encryption passphrase or the signing passphrase is being confirmed - Fix passphrase retrieval for sym+sign (duplicity-bin and gpg.py) - Allow sym+sign with limitation (see comments and manual page)
 * 29c79488: 797758 Duplicity ignores some FatalErrors
 * afdd5bdd: Checkpoint
 * 6666f1dd: always catch Exceptions, not BaseExceptions
 * c5c19e88: 794123 Timeout on sftp command 'ls -1'
 * 085418f1: Checkpoint.
 * b2153461: 487720 Restore fails with "Invalid data - SHA1 hash mismatch"
 * 189e6c51: Fixed boolean swap made when correcting syntax.
 * 0548acd0: Fix syntax for Python 2.4 and 2.5.
 * 8bc7eec8: Fix syntax for Python 2.4 and 2.5.
 * 0701aee5: Fix CHANGELOG.
 * 0dddd786: 782337 sftp backend cannot create new subdirs on new backup
 * 3810ccec: 782294 create tomporary files with sftp
 * 164f9996: Merged in lp:~mterry/duplicity/retry-decorator
 * c4c74eba: Merged in lp:~mterry/duplicity/u1-status
 * 1c11001d: Checkpoint.
 * 4236cb5f: Merged in lp:~mterry/duplicity/gio-name
 * 54892033: Merged in lp:~mterry/duplicity/levelName
 * 9974ca3d: u1: allow any success status, not just 200
 * 9d5ae659: move logging code up to retry decorator; fixes use of 'n' variable where it doesn't belong
 * 828ee64f: 452342 Provide Ubuntu One integration
 * a619dfc3: 792704 Webdav(s) url scheme lacks port support
 * 3b17997e: 782321 duplicity sftp backend should ignore removing a file which is not there
 * b7a38f21: 778215 ncftpls file delete fails in ftpbackend.py
 * 39c24788: 507904 Cygwin: Full Backup fails with "IOError: [Errno 13] Permission denied"
 * b11bc84e: 761688 Difference found: File X has permissions 666, expected 666
 * ef8bc5f0: 739438 [PATCH] Local backend should always try renaming instead of copying
 * 46b40853: 705499 "include-filelist-stdin" not implemented on version 0.6.11
 * b7ba8108: Sync with repository.
 * 60334685: 512628 --exclude-filelist-stdin and gpg error with/without PASSPHRASE
 * 1f02db35: 512628 --exclude-filelist-stdin and gpg error with/without PASSPHRASE
 * a104b3ad: invalid function description fixed for get_passphrase in duplicity-bin - function get_passphrase in duplicity-bin accepts argument "for_signing" which indicates that a passphrase for a signing key is requested - introduces the SIGN_PASSPHRASE environment variable for passing a different passphrase to the signing key - commandline option --encrypt-secret-keyring=path introduced to set a custom location for the secret keyring used by the encryption key - manual page updated with SIGN_PASSPHRASE and --encrypt-secret-keyring - ask for a new passphrase if the passphrase confirmation failed to prevent an endless retype - improved some comments in the code - due to the difference in the handling of the signing and encryption passphrase, the passphrase is asked later in the duplicity-bin
 * 05cdbb9b: Launchpad automatic translations update.
 * bd5f3e6b: add retry decorator for backend functions; use it for giobackend; add retry to giobackend's list and delete operations
 * 773f89de: giobackend: use name, not display name to list files
 * df3b2bca: fix MachineFilter logic to match new level name code
 * 25b91034: Cautiously avoid using levelname directly in log module. It can be adjusted by libraries.
 * b4033450: update man page
 * bb1c01ea: drop test file
 * 14c5a784: further fixups
 * e6bf297d: further upload work
 * bc8d11e0: start of u1 support
 * a7c22404: as restoring is non-destructive by default (overideable with --force) there is no need to raie fata errors if not supported in/exclude parameters are given as parameters. see also: http://lists.gnu.org/archive/html/duplicity-talk/2011-04/msg00010.html
 * 12b29a78: Launchpad automatic translations update.
 * cad17242: Launchpad automatic translations update.
 * 1877ea0d: Launchpad automatic translations update.
 * f04ac793: Insure Python 2.4 compatible.
 * 3cc07012: 433591 AttributeError: FileobjHooked instance has no attribute 'name'
 * e230b4ea: Merged in lp:~ed.so/duplicity/0.6-add_sftp.
 * 9428b1b6: link sftp to ssh backend, thus enabling sftp:// urls modified explanation in manpage minor changes in manpage
 * c585ed5f: Boto has refactored too many times, so back off and just use Exception rather than searching.
 * 4ded4080: Launchpad automatic translations update.
 * 40133831: Boto moved S3ResponseError, so allow for different imports.
 * 020f197e: Launchpad automatic translations update.
 * 379534fe: Changes for 0.6.13.
 * 7de0838d: Changes for 0.6.13.
 * 68572d74: Changes for 0.6.13.
 * 8950f28a: Check for presence of bucket before trying to create.
 * 3b2c9572: 579958 Assertion error "time not moving forward at appropriate pace"
 * b8437489: Add in ftpsbackend.py. Missed it.
 * 4aa59161: Launchpad automatic translations update.
 * a26f936e: 613244 silent data corruption with checkpoint/restore
 * eda30f1e: Add a manual test for Ctrl-C interrupts. This could be automated, but I find that the old hairy eyeball works quite well as is.
 * a24fadb6: Use python-virtualenv to provide a well-defined environment for testing multiple versions of Python.
 * eb7368c3: Add (undocumented) option --pydevd to allow easier debugging when executing long chains of duplicity executions.
 * 6e7b5a3e: Remove threaded_waitpid(). We still need GnuPGInterface because of the shift bug in the return code and the ugly mix of tabs and spaces. All has been reported to the author.
 * f008b26d: Replace 2.5 'except...as' syntax.
 * 00365aa6: Changes for 0.6.12.
 * e8ac0444: Various fixes for testing. All tests pass completely.
 * 9895a3e4: Add test for new ftps backend using lftp.
 * afc5b4f4: Some FTP sites return 'total NN' in true ls fashion, so ignore line during listing of files.
 * 77b88ae3: Fix typo on fix for 700390.
 * 17853100: Miscellaneous fixes for testing.
 * 0f1e0101: 700390 Backup fails silently when target is full (sftp, verbosity=4)
 * f8510f79: 581054 Inverted "Current directory" "Previous directory" in error message
 * 8aefe405: 626915 ftps support using lftp (ftpsbackend)
 * 36b256fb: 629984 boto backend uses Python 2.5 conditional
 * 1d7c3b31: 670891 Cygwin: TypeError: basis_file must be a (true) file, while restoring inremental backup
 * 2be1d5fb: 655797 symbolic link ownership not preserved
 * a169eff9: lp:~blueyed/duplicity/path-enodev-bugfix
 * 6c3cd051: Merged: lp:~blueyed/duplicity/path-enodev-bugfix
 * 790cbcfa: 629136 sslerror: The read operation timed out with cf
 * 44572455: 704314 Exception in log module
 * e52db0b2: 486489 Only full backups done on webdav
 * ec8f4134: 620163 OSError: [Errno 2] No such file or directory
 * f338dd61: Merged in lp:~mterry/duplicity/backend-log-codes3
 * 0a299989: Launchpad automatic translations update.
 * 33b74c03: Launchpad automatic translations update.
 * 73865fc4: use log error codes for common backend errors
 * 2858e7f9: 681980 Duplicity 0.6.11 aborts if RSYNC_RSH not set
 * 05848f43: Launchpad automatic translations update.
 * ba880b9d: Changes for 0.6.11
 * 87e1eae0: Changes for 0.6.11
 * 595ec281: 433970 Add an option to connect to S3 with regular HTTP (and not HTTPS)
 * ca57ba64: 631275 missing ssh on rsyncd url - rsync: Failed to exec ssh: ...
 * 694672cd: 674506 RsyncBackend instance has no attribute 'subprocess_popen_persist'.
 * ddb66f20: Merged lp:~ed.so/duplicity/survive_spaces.
 * ed2bc26b: Merged lp:~ed.so/duplicity/sign_symmetric2.
 * b4d05b80: Merged lp:~duplicity-team/duplicity/po-updates.
 * c12255fc: 669225 sftp: Couldnt delete file: Failure only logged on level 9.
 * 35490f4f: Fix CHANGELOG.
 * eb993e42: Merged in lp:~l2g/duplicity/use-py.test
 * 31419ff4: solve bug 631275 rsync 3.0.7 persists on either rsync:// _or_ :: module notation both together and it interpretes it as a dest for rsh
 * f05051dc: protect rsync from possibly conflicting remote shell environment setting
 * 0d847e89: restored backend:subprocess_popen_* methods moved ncftpls workaround into ftpbackend introduced new backend:popen_persist_breaks setting for such workarounds enhanced backend:munge_password rsyncbackend: rsync over ssh does not ask for password (only keyauth supported)
 * 733da0f0: survive spaces in path on local copying with encryption enabled
 * d1249666: allow signing of symmetric encryption
 * b2077715: Catch "Couldn't delete file" response in sftp commands.
 * af8e89e4: 637556 os.execve should get passed program as first argument
 * c9c0954f: Launchpad automatic translations update.
 * 2d7a54dc: Add --s3-unencrypted-connection (bug 433970)
 * 19829eb9: Launchpad automatic translations update.
 * c52d8f0d: Launchpad automatic translations update.
 * 0dd778b2: Delete duplicity.spec -- autocreated.
 * 6f5e86fe: Replace ternary operator with simple if statement. Python 2.4 does not support the ternary operator.
 * c61e8235: Upgrade setup dependency to Python 2.4 or later.
 * 90b4540f: Launchpad automatic translations update.
 * 8266133c: Changes for 0.6.10.
 * f6655ae8: Changes for 0.6.10.
 * a89ea25d: 612714 NameError: global name 'parsed_url' is not defined
 * a3196841: 589495 duplicity --short-filenames crashes with TypeError
 * 6fcca640: 589495 duplicity --short-filenames crashes with TypeError
 * 30880432: Merged in lp:~olivierberger/+junk/dupl-542482
 * 5e6d0e99: merge with latest release upstream : 0.6.09
 * efb14c67: 613448 ftpbackend fails if target directory doesn't exist
 * 1082ea83: 615449 Command-line verbosity parsing crash
 * f2e16b29: Man page improvements and clarification.
 * 331405a9: Final changes for 0.6.09.
 * 6837d5f0: 582962 Diminishing performance on large files
 * 1d16d4be: Fix to warning message in sshbackend.
 * 5198242b: Launchpad automatic translations update.
 * 162a241c: Upgraded tahoebackend to new parse_url.
 * 4956b96f: Merged in lp:~duplicity-team/duplicity/po-updates
 * 8641456b: 502609 Unknown error while uploading duplicity-full-signatures
 * b44d91db: 567738 --ssh-options options passing options to ssh do not work
 * 0cf086b4: When using listmatch filenames are now unqouted so colons and other special characters don't cause problems.
 * 9a838eb9: Added test for SpiderOak backend (it should probably just fail in most cases since the API is still very unstable).
 * 289e73a4: Add ability to retry failed commands.
 * f14b41bc: Handle exceptions when listing files and display coresponding HTTP status code on HTTPError exception
 * b025c2c3: First version of SpiderOak DIY backend.
 * 1019df73: Merged lp:~mterry/duplicity/backend-log-codes2
 * 2d6acfb4: support new backend-error log codes
 * 31ed7822: Merge changes from 0.6-series.
 * adcff65b: Launchpad automatic translations update.
 * c16393a5: Merged in lp:~duplicity-team/duplicity/po-updates
 * 94e50364: 576564 username not url decoded in backend (at least rsync)
 * e7c06d39: 579958 Assertion error "time not moving forward at appropriate pace"
 * 73ce2c87: 550455 duplicity doesn't handle with large files well (change librsync.SigGenerator.sig_string to a list)
 * 685df898: Fix remove-older-than which would no longer work Differentiate the function name from global option name for remove_all_but_n_full
 * 2ce1edbc: support new backend-error log codes
 * d428e13f: Launchpad automatic translations update.
 * 15d9c4fe: Added bits of manpage
 * 5aeaeebf: Adding the remove-all-inc-of-but-n-full variant to remove_all_but_n_full() : remove only incremental sets from a backup chain selected as older than the n last full
 * cae55b5d: Adding the 2 new remove-all-but commands as global markers
 * a0414647: Adding new remove-all-inc-of-but-n-full command as a variant of remove-all-but-n-full
 * b2f314a6: Fix small typo in comments
 * 4533359a: Launchpad automatic translations update.
 * db05c26b: Launchpad automatic translations update.
 * 7f30340a: Changes for 0.6.08b
 * 8d565f56: Manually apply patch from http://bazaar.launchpad.net/~duplicity-team/duplicity/0.7-series/revision/637 which did not make it into 0.6.
 * 1f3ba520: Changes for 0.6.08a
 * be1ffa87: Changes for 0.6.08a
 * 784fc456: Launchpad automatic translations update.
 * 2c44fcbb: don't crash when asked to encrypt, but not passed any gpg_options. my bad
 * c060c651: Changes for 0.6.08
 * 2ee4d808: #532051 rdiffdir attempts to reference undefined variables with some command arguments
 * 76bf3267: #532051 rdiffdir attempts to reference undefined variables with some command arguments
 * 8b920fb3: #519110 Need accurate man page info on use of scp/sftp usage.
 * 328ad44b: #519110 Need accurate man page info on use of scp/sftp usage.
 * b63c251c: lp:~mterry/duplicity/use-gpg-options-0.7
 * 1e31dd5f: Merged lp:~mterry/duplicity/use-gpg-options-0.6
 * e50ae1ba: use global gpg options
 * f091b7a3: use global gpg options
 * 7bf18af8: lp:~mterry/duplicity/fix-gpg-options-crash-0.7
 * 5f42a358: Merged lp:~mterry/duplicity/fix-gpg-options-crash-0.6
 * 0a47ea37: fix time command line handling
 * dbd6bece: fix time command line handling
 * 933e0ea5: and handle initial, empty value for extend commandline actions
 * 4be18974: and handle initial, empty value for extend commandline actions
 * 6f0f7414: fix crash on empty gpg-options argument
 * 85fbe039: fix crash on empty gpg-options argument
 * 05ee5104: Launchpad automatic translations update.
 * b0e48746: Changes for 0.6.07.
 * ba72bec7: Merged lp:~duplicity-team/duplicity/po-updates.
 * e21daa76: #520470 - Don't Warn when there's old backup to delete
 * 948da94f: #520470 - Don't Warn when there's old backup to delete
 * 34f03745: Patch #505739 - "sslerror: The read operation timed out" with S3
 * 24dcba48: Patch #505739 - "sslerror: The read operation timed out" with S3
 * ee889036: Patch 522544 -- OSError: [Errno 40] Too many levels of symbolic links
 * ff34df89: Patch 522544 -- OSError: [Errno 40] Too many levels of symbolic links
 * 4bc1ee46: Patched #497243 archive dir: cache desynchronization caused by remove*
 * 45b72140: Patched #497243 archive dir: cache desynchronization caused by remove*
 * ee8078c1: Merge with trunk.
 * a03da6d0: Merge with trunk.
 * 72ea8267: logging: fix logging to files by opening them with default of 'a' not 'w'
 * b82f7be7: logging: fix logging to files by opening them with default of 'a' not 'w'
 * e98f2f03: Launchpad automatic translations update.
 * c9a4ab70: Launchpad automatic translations update.
 * 695971c9: merge lp:~mterry/duplicity/rename
 * 0071d13b: make a comment reserving 255 as an error code (used by gksu)
 * add11724: make a comment reserving 255 as an error code (used by gksu)
 * b861579b: Patch 501093 SSHBackend doesn't handle spaces in path
 * bcd2d623: Try again -- remove Eclipse/PyDev control files from bzr.
 * 20aafe2a: Eclipse settings should not be in bzr.
 * 614ae45a: No longer needed.
 * 9197b508: Fix real errors found by PyLint. Remove unneeded includes. Tag spurious errors so they don't annoy.
 * f87c1caa: Fix problem in put() where destination filename was not being passed properly.
 * fbb83a75: Merged in lp:~mterry/duplicity/rename
 * 32b10364: add --rename argument
 * 5ca25f2e: Launchpad automatic translations update.
 * db8e5665: merge lp:~mterry/duplicity/optparse
 * 0bfa6044: add back accidentally-dropped --use-scp option from commandline merge
 * 9336a606: Launchpad automatic translations update.
 * 5856eebe: Merged in lp:~mterry/duplicity/typos
 * 9fa7b1cf: Fix CHANGELOG.
 * 08e19e28: Merged in lp:~mterry/duplicity/typos
 * add41dee: Merged in lp:~duplicity-team/duplicity/po-updates
 * b8ec9488: Merged in lp:~mterry/duplicity/optparse
 * 441e83a8: Merged in lp:~mterry/duplicity/typos-0.6
 * 903f7dfd: whoops, remove debug code
 * eaac2393: whoops, and this typo
 * fc605004: whoops, and this typo
 * 30982e25: fix some typos found when using pydev+eclipse (backported from 0.7 line)
 * cbf9d97a: fix some typos found when using pydev+eclipse
 * 989fb5a6: don't set xdg dirs in duplicity-bin now that globals.py is restored
 * 8ce37750: use defaults from globals.py for commandline options
 * 46f00bc5: fix an undefined variable usage
 * a3d505e3: Launchpad automatic translations update.
 * 06bb19c7: fix a few typos
 * 93406c50: fix typo with log-fd support
 * 6ee6ec8c: first pass at getopt->optparse conversion
 * aa293b82: Remove antiquated file.
 * bb019347: Remove antiquated file.
 * 7113e1d2: Remove requirement for GnuPGInterface, we have our own.
 * 0caf63ee: Remove requirement for GnuPGInterface, we have our own.
 * 8edfe43f: 459511 --tempdir option doesn't override TMPDIR
 * ed5f85fd: 459511 --tempdir option doesn't override TMPDIR
 * 2057d62e: 487686 re-add scp backend and make available via command line option Option --use-scp will use scp, not sftp, for get/put operations.
 * 7ac6350e: 487686 re-add scp backend and make available via command line option Option --use-scp will use scp, not sftp, for get/put operations.
 * 78580205: Applied patch 467391 to close connection on a 401 and retry with authentication credentials.
 * b5e11e7a: Applied patch 467391 to close connection on a 401 and retry with authentication credentials.
 * 70e36d01: Launchpad automatic translations update.
 * 99552e19: CVS no longer used, so no longer needed.
 * dd4e271a: Merged in translations.
 * d382a4d8: Merged in translations.
 * 49f18e72: Checkpoint.
 * 5da0192b: Checkpoint.
 * 63d609f9: Launchpad automatic translations update.
 * befe1ff9: Changes for 0.6.06
 * 3fa27236: lp:~duplicity-team/duplicity/po-updates
 * 33010993: lp:~duplicity-team/duplicity/po-updates
 * 4090f07d: Merge in lp:~duplicity-team/duplicity/i18n-for-0.7
 * bee48759: Merge of lp:~mterry/duplicity/list-old-chains
 * 2d88afb7: Merge of lp:~mterry/duplicity/list-old-chains-0.6
 * fd01bd3d: Launchpad automatic translations update.
 * 4609baf8: merge old-chain signature work from 0.7 branch; keep old sigs around, allow listing them, warn if a too-old listing is requested
 * 94075ba9: warn if we don't have signatures for the given date period
 * 9983e38e: allow deleting old signatures with cleanup --extra-clean
 * 661dd0b3: don't delete signature chains for old backups; allow listing old backup chain files
 * a22bdb73: Merged in lp:~duplicity-team/duplicity/po-updates
 * df7be2b4: Merged in lp:~duplicity-team/duplicity/po-updates
 * 80c3cf57: Launchpad automatic translations update.
 * f36f5831: add missing par2_utils.py to dist tarball
 * fb840e55: Remove .cvsignore
 * a8252326: Remove unused __future__ imports.
 * b9bccea8: Remove unused __future__ imports.
 * b5513616: Add entry for patches from Stéphane Lesimple for par2.
 * 3af16c1d: Applied patch from Stéphane Lesimple found at: https://bugs.launchpad.net/duplicity/+bug/426282/comments/5 patch skips the par2 files when building up the sets and chains of backups
 * c9f9f67d: Applied patch from Stéphane Lesimple found at: https://bugs.launchpad.net/duplicity/+bug/426282/comments/4 patch avoids storing all the par2 files into the local cache
 * a6cd6ceb: Fixed 435975 gpg asks for password in 0.6.05, but not in 0.5.18
 * a9ae5cf1: Fixed 435975 gpg asks for password in 0.6.05, but not in 0.5.18
 * f6d4e3c2: i18nized a few error messages in duplicity.selection
 * 9152ef15: More strings internationalized in asyncscheduler and commandline
 * 77555532: Launchpad automatic translations update.
 * 13b49225: Merge with trunk.
 * 54b961ca: Merge with trunk.
 * 1536405f: Merged in lp:~duplicity-team/duplicity/po-updates
 * 3708a731: Fix problems with unittests under Jaunty. It appears that redirection in os.system() has changed for the worse, so a workaround for now.
 * a71a926c: Fix problems with unittests under Jaunty. It appears that redirection in os.system() has changed for the worse, so a workaround for now.
 * 1f5a3077: Launchpad automatic translations update.
 * 0d4a1a07: Launchpad automatic translations update.
 * af10a429: Adding conftest.py for py.test configuration hooks (right now just setting up temporary directories)
 * f9c16361: Launchpad automatic translations update.
 * 27676577: Use py.path to simplify a little
 * 4398c647: Don't try to change dirs in cleanup_test_files for now. Actually, this file probably won't be here much longer.
 * ba6b43be: Criss-cross merge. 'Scuse my mess.
 * 59fd1fa2: Fix non-root-based test skipping
 * 120dcac2: ugh, I'm the worst; add missing import
 * f87f2c32: ugh, I'm the worst; add missing import
 * 66a45eec: add extra information to the 'hostname changed' log message, split it from the 'source dir changed' message
 * 40918a69: whoops, use error code 42, not 41 -- that's for par2
 * f7c074d7: add extra information to the 'hostname changed' log message, split it from the 'source dir changed' message
 * 1e5d1a0c: Launchpad automatic translations update.
 * b349bf72: Expose test files' root directory as config.test_root
 * 34286845: New helper module for tests; have backendtest.py make use of it
 * 44600ba5: I think these are all my own changes, not a trunk merge. Sorry for confusion.
 * 27ffe3fa: trunk merge
 * 8af3f25e: Launchpad automatic translations update.
 * e9c6a8cc: Applied "426282 [PATCH] par2 creating support", corrected some coding format issues and made sure all unit tests passed.
 * 5b41c513: Launchpad automatic translations update.
 * a6c606fb: Refactored. Put in py.test.skip to skip tests when tarfile can't be used.
 * d78ca733: commit.py already adjusts sys.path, so anything that imports commit doesn't need to
 * ed24535a: Launchpad automatic translations update.
 * e46ac90f: Allow testing/config.py to find duplicity even when run outside testing/. Added a missing import.
 * 14e0632f: Launchpad automatic translations update.
 * 3f898d28: Merged in lp:~mterry/duplicity/iterate-warnings
 * 6fe1d847: Merged in lp:~mterry/duplicity/iterate-warnings
 * ddadd5fb: add some machine codes to various warnings when iterating over source files
 * bf00b723: Merged in lp:~duplicity-team/duplicity/po-updates
 * 00f24f84: Clean up testing run scripts.
 * e21bb5e4: Merged in lp:~duplicity-team/duplicity/po-updates
 * 5c4a7371: Clean up testing run scripts.
 * 7629654e: 422477 [PATCH] IMAP Backend Error in delete()
 * 10eac963: 422477 [PATCH] IMAP Backend Error in delete()
 * 2c2af741: Additional Portuguese and brand-new Bulgarian translations
 * 857808fe: merge latest 0.6
 * 6a3aec4b: Merged in lp:~l2g/duplicity/bug-411375
 * 20010932: Merged in lp:~duplicity-team/duplicity/po-updates
 * 8e1b61fc: Translation of Spanish and Portuguese has begun
 * bd32dc43: Updated existing PO files with Rosetta translations
 * fe7a5225: Change message "--cleanup option" to "'cleanup' command"
 * d35239fd: Merged in lp:~l2g/duplicity/flag-transl-comments which cleared up how\ntranslation comments should be passed to the translators cleanly now.
 * dd3ae0d9: Applied patches from Kasper Brand that fixed device file handling. http://lists.gnu.org/archive/html/duplicity-talk/2009-09/msg00001.html
 * ddd3a38d: When generating PO[T] files, only use code comments starting with "TRANSL:" for notes to the translators. "TRANSL:" is filtered out of the POT file with sed after it's generated.
 * 1149c5af: Changes for 0.6.05.
 * 5756de2c: Merged in ~l2g/duplicity/test-compat from Larry Gilbert which made the testing compatible across more systems. Also fixed the remaining collectionstest bug which was trying to test with no cache present.
 * 227b9e32: Test separate filesystems using /dev instead of /proc (more widely used)
 * bfdcca4d: 418170 [PATCH] file names longer then 512 symbols are not supported
 * 4d9b9284: 408059 Failure due to _logger.log failure for content with special characters: TypeError decoding Unicode not supported
 * a1e76a3d: dd on Darwin (and FreeBSD?) doesn't like e.g. "bs=1K", so changed it to "bs=1024"
 * 76256b14: "cp -pR" seems to be a better analogue to "cp -a". This may not be perfect but it won't hang on a fifo copy like "cp -pr".
 * 1c5f6102: Got test_get_extraneous working in collectionstests.py
 * 352df3cc: Unpacked testfiles.tar.gz on Mac OS X file system and repacked as new file
 * 3604e4f1: Changed options to 'cp' to be compatible with BSD style yet (hopefully) stay compatible with GNU
 * 307eb7c2: Took care of some redundancy in tar usage
 * a8078cea: Use bash "command" command to look for Python binaries beyond /usr/bin
 * 14bb5bdb: "remove-older-than" asks for passphrase even though not required; watch for correct internal action name to fix this
 * 936d8014: "remove-older-than" asks for passphrase even though not required; watch for correct internal action name to fix this
 * 56843d2e: Comment out Pydev debug startup code.
 * 093b7ed8: Merge from trunk.
 * 05b90b09: Fixed #409593 deja-dup (or duplicity) deletes all signatures
 * a678cb71: Typo in remove-older-than may have caused unnecessary passphrase prompts?
 * 8a9352b1: Typo in "remove-older-than" may have caused unnecessary passphrase prompts?
 * 09354bd0: Changes for 0.5.19.
 * 22cc0f9c: Merge GIO changes from trunk.
 * 27efedd9: allow gio backend to restore by setting correct state. LP: #407968
 * b7604198: Changes for 0.6.04.
 * 32fbabb6: Changes for 0.6.04.
 * 8a121750: Fixed 405734 duplicity fails to restore files that contain a newline character
 * b7f823b2: Fixed 403790 Backup error: No such file or directory
 * 8f02a910: Last changes for 0.6.03.
 * a5a2f2fe: Fix getrlimit usage for Cygwin, which was returning -1 for the hard limit on max open files
 * ab29fd4e: Changes for 0.6.03.
 * ae873552: Changes for 0.6.03.
 * a4df321e: Fixed 402794 duplicity public-key-only incompatible with gnupg 2.0.11.
 * 54eb92a9: Fixed 405975 duplicity.gpg.gpg_failed() breaks and spews on GnuPG error.
 * 5183c23c: Fixed 398230 Deja-dup backup fails with message: "Unable to locate last file"
 * b311b321: Fix bug 405646 Small i18n error.
 * d5fbbeb5: Minor header comment correction.
 * 02bc010a: Adjust to file renames.
 * c0529cae: merge of lp:~l2g/duplicity/doc-update.
 * f85bce69: merge of lp:~l2g/duplicity/i18n-update-1.
 * 09c9ff07: Fix restart issues when local manifest does not agree with the contents of the remote system. In all cases, clean up as needed, and restart the backup at the last known good state.
 * 535bb5f3: Refactor to put loop outside of try/except clause.
 * 645ee613: BackupSet.delete() now removes both local and remote files.
 * 8c91bb25: Make testing into a module.
 * d6ee19eb: Oops, one too many things in usage() were dictionarified
 * 52753c8a: Redid dictionary in usage to use a local hash instead of a bunch of local variables, to make things a tad more pleasant.
 * 34e65ef2: Broke up the usage() help info to simplify translation maintenance. Imported .po files from Launchpad Translation (not sure how necessary they are to have in here, but here they are.)
 * d29144f7: Updated some intltool config info
 * 8eae751f: Updated *.po and *.pot files
 * 94b3c4e1: Capture stderr as well as logger and display stderr with logger only if gpg fails. Cuts out some of the noise from gpg.
 * 9a5953ca: Split restarttest.py from finaltest.py for ease in debugging.
 * 7d861fef: fix test config to import backends (now optional).
 * a8cdfb7e: Sorry... I missed the point being made here...
 * 9c55bc57: Minor capitalization changes in the manpage
 * db71d976: CVS-README changed to REPO-README and updated with Launchpad/bzr info
 * bf1873d4: merge of lp:~scode/duplicity/misc.
 * d23cf69e: Update .bzrignore only.
 * 8da11bd5: fixed 401303 0.6.2 manpage inconsistent wrt. archive-dir/name
 * a8ad05ad: fix 377528 --file-to-restore doesn't work with trailing slash
 * 3522c2da: First pass at bug 394757 - Optional Backends https://bugs.launchpad.net/bugs/394757
 * 093d659f: ignore unicode() translation errors in log messsages.
 * 8408f770: ignore unicode() translation errors in log messsages.
 * f6225f84: Make sure 'invalid packet (ctb=14)' from gpg is not a fatal error.
 * c5632d46: Make sure 'invalid packet (ctb=14)' from gpg is not a fatal error.
 * 9b0c8443: On processes that complete before waitpid(), log them and return zero as the process.returned value. They will have already trapped in the main thread if they returned in error.
 * da0150d4: On processes that complete before waitpid(), log them and return zero as the process.returned value. They will have already trapped in the main thread if they returned in error.
 * 3f3be923: Use correct name of error class ConflictingScheme.
 * 544e51a9: Copy changes from trunk for duplicity translation.
 * c2c12227: s/pair/tuple/ (method doc fix)
 * 5d5f6e82: when doing the "sleep to make sure we have different current time than last backup": sleep for 2 seconds instead of 1, since it is an expected case that time may be moving slightly slower as a result of adjtime() and such - assert afterwards that current time really does differ from previous time
 * 1b755f90: merge latest trunk
 * 513307a8: Make Changelog.GNU close to GNU Changelog format.
 * 26bf115f: Changes for 0.6.02.
 * 8072466d: Another attempt at fixing #394629 Hang on first collection-status.
 * 28159068: Fix Bug #395826 "No such file or directory" when backing up second time
 * 6523b284: merge of lp:~scode/duplicity/archive-sync-removelocal and fixes.
 * d963c318: Fix bug #394629 Hang on first collection-status
 * 595a05a2: optimistically try to resolve final issue by passing ParseResult:s sense of what's what to get_suffix() rather than hard-coding based on manifest. not sure if this has other bad side-effects though - will discuss on ML.
 * 66b056b4: nuke accidentally added characters in comments - left control is breaking on my keyboard...
 * 1f58c463: initial stab (broken): synch both ways; i.e., remove spurious local files in addition to downloading missing ones * problem remaining with determining the correct local name
 * 28c66c7a: merge of lp:~scode/duplicity/ignore-errors
 * f38b4233: support an --ignore-errors command which is intended to mean "try to continue in the face of" errors that might possibly be okay to ignore - intended during restoration to avoid bailing out on errors that are not fatal yet would in fact produce an "incorrect" restoration - for now, only changes behavior on file meta data restoration where I happened to have a problem (I had a +t file which was impossible to restore to +t even though it was possible for it to exist and for me to read it) - be clear in the man page that this is only supposed to be used in case of problems and even then to please contact maintainer if use is needed
 * 5d6417ff: merge of lp:~scode/duplicity/misc
 * 73d6b18d: Update ignore list.
 * 2ce42e59: Fixes: [Bug 379386] Fix 'list-current-files' with missing archive dir
 * ed543c88: print archive directory in a more readable fashion #394627
 * c82b091c: merge from lp:~mterry/duplicity/po-fixes: reorganize po directory, so that we can start translating in LP
 * e8f15f36: fix po dir layout, update POTFILES.in, add pot file to bzr
 * e4a62a1f: Changes for 0.6.01.
 * 4d1c8e80: Fixed issues in Checkpoint/Restart: The --name backupname" option was added to allow the user to separate one archive from another. If not specified, the default is an MD5 hash of the target URL, which should suffice for most uses.
 * 18d813da: Fixes bug 392905. Allow omission of remote file name if the same as the source file name.
 * 59e81179: merge of lp:~kenneth-loafman/duplicity/smart-archive-v2
 * ffe561a9: merge lp:~mterry/duplicity/gio-dist-fix to distribute gio backend
 * 79a0dadc: merge from trunk
 * 1ed4a846: Fix "external file not found" to show command and file names.
 * 77147f94: actually distribute the gio backend
 * 15b90260: Change to use XDG_ convention per http://standards.freedesktop.org/basedir-spec/latest/
 * 45771e04: Change handling of smart archive dir so both archive and name can be changed.
 * 76030d90: merge of lp:~scode/duplicity/smart-default-archive
 * 49d6c3da: Misc project changes.
 * 8c9ac074: If python is run setuid, it's only partway set, so make sure to run with euid/egid of root.
 * 3eeca257: Create testfiles/output in SetUp routine so it will run standalone.
 * 0172bc40: Avoid deprecation warning for md5 in Python 2.6.
 * b52739f8: --name affects *expansion*, not default value, of --archive-dir
 * 3cfb97db: fix a man page mistake from previous merge * remove last remnants of DUPLICITY_ARGS_HASH
 * 1ca6fd7c: correct man page to claim hash of backend url rather than has of args
 * 4e9b29a5: figure out which arg is a backend url without actually instantiating a backend
 * e08882b5: make default value to --name be the has of the backend URL specifically, rather than the has of remaining args * outstanding issue: in order to figure out which arg is a backend we call get_backend(); must either fix this or feel comfortable that instantiating (and not using) a backend is side-effect free
 * f14f38a5: introduce --name parameter to specify symbolic name of a backup * change --archive-dir expansion to look for %DUPLICITY_BACKUP_NAME% * which in turn defaults to the args hash previously used for --archive-dir and %DUPLICITY_ARGS_HASH% expansion
 * cc66cf62: merge from trunk
 * 1a68d91c: Surround --gio option with try/except so user will not see traceback.
 * bcca7a3f: Make GIO tests dependent on presence of gio module.
 * ceadbb93: Fix 'get' command args.
 * 5bd4d4de: merge of lp:~cjwatson/duplicity/always-sftp
 * 3628bdf4: Add .bzrignore
 * afab0882: merge of lp:~scode/duplicity/bug-387102
 * 1bb18f12: merge of lp:~scode/duplicity/reasonable-io-blocksize
 * 880d10b2: Fix regression -- add tahoebackend back in.
 * ffce7364: s/src.name/self.src.name/ in exception handling path
 * 6687ad4b: merge log worker event info codes
 * 5af327ab: merge with trunk
 * 348c8839: Merge GIO branch, supporting the --gio argument
 * 5f26c927: merge lp:~mterry/duplicity/log-upload-events since I created conflicts with my changes
 * ea65ae65: Fix omitted changes in duplicity manpage.
 * 9a82ad82: s/self.__waiter/self.__failed_waiter/
 * e5990e3d: significantly re-design the asynch scheduler to be much simpler; instead of keeping workers and queues, simply launch a thread for each unit of work, blocking when called for by a concurrency limit or a barrier. the old design was a result of initially designing for keeping a persistent set of workers, only to then drop that idea. when dropping that idea, I should have re-done it like this from the start instead of retaining the complexity i introduced for the persistent worker design.
 * 689b44e4: GPGWriteFile: what was previously the minimum block is is now just the block size; meaning the maximum block size used for individual I/O operations, but still the minimum in terms of when to give up on the iteration * GZipWriteFile: similar change, though blocksize handling was a bit different
 * ce46165f: support expansion of %DUPLICITY_ARGS_HASH% in --archive-dir value * default to ~/.duplicity/%DUPLICITY_ARGS_HASH$ so that default behavior works well even when the user has multiple backup destinations * update the manpage accordingly
 * 526d4d6c: s/src.name/self.src.name/ in exception handling path
 * 72024dd2: Changes for 0.6.0.
 * 6af14a34: Some cleanup on the forced assertion test code to allow multiple failures and no traceback for the assert.
 * 7c6de173: Add code for testing of Checkpoint/Restore that I had been doing by hand, both single and multiple failure tests, with verify at the end.
 * 536cac13: Fix getrlimit usage for Cygwin, which was returning -1 for the hard limit on max open files.
 * 67b9af0c: After merge of Checkpoint/Restart.
 * 73bfe28a: Allow handling of unicode filenames in log messages.
 * 0df0073d: don't be so specific about exceptions we catch
 * bc8bc495: add GIO backend
 * 392229ad: add log codes for upload events
 * 2b956404: add info codes for upload events
 * 3a69f177: Changes for 0.5.18.
 * 32847b57: Changes for 0.5.18.
 * ad3836ca: Correct copyright.
 * 22222afe: Reset file type preferences.
 * a6c57b18: Changed from using ulimit external command to resource.getrlimit to check open files limit.
 * 4760307e: patch #6743: Tahoe backend for duplicity https://savannah.nongnu.org/patch/?6743
 * 2281cc61: Only half of this bug is fixed but it's still useful. bug #21792: pipe call fails with an error OSError: [Errno 24] Too many open files https://savannah.nongnu.org/bugs/?21792
 * 67b4a2a7: Added support for RackSpace's CloudFiles, cf+http.
 * c3ac854f: Add more detail on connection failure.
 * 56092ef7: Added support for RackSpace's CloudFiles, cf+http.
 * a46e5793: initial attempt at using only sftp on the client (https://savannah.nongnu.org/bugs/index.php?26464)
 * dceaf254: Changes for 0.5.17.
 * d4e43a11: Checkpoint.
 * d2f2491a: The previous revision got the wrong comment, so I cleaned up some code and checked back in. The correct release comment should be:
 * b353a059: patch #6813: Making changelist easy to read https://savannah.nongnu.org/patch/?6813
 * d1e9f057: Moved from using the df command to get temp space availability to Python's os.statvfs() call. Not all df commands work the same way.
 * d52ce1e2: I had put in some trial code that I removed incompletely that forced a full backup action. This removes the last line of that code.
 * ef1b47c7: Changes for 0.5.16.
 * a82ac7fa: Reduce max_open_files limit needed to 1024, was 2048.
 * 050c6e26: Fix argument list in FatalError call re max open files.
 * ce0a66c1: bug #24825: duplicity warn on insufficient TMPDIR space availability and low max open file limits pre-backup. https://savannah.nongnu.org/bugs/?24825
 * 061ea781: Use os.access() check on regular files and dirs only.
 * 6c28341c: Added tilde and variable expansion to the source or target argument that is not a URL.
 * 13217c74: Remove check for only one $version string.
 * 8bd567d0: bug #24825: duplicity warn on insufficient TMPDIR space availability and low max open file limits pre-backup. https://savannah.nongnu.org/bugs/?24825
 * fdaa8a91: bug #25976: Password requested when not needed. https://savannah.nongnu.org/bugs/?25976
 * d660f2cb: Make sure gettext is included first. Add variable at top of file for verbosity.
 * 53dcfba0: Add some documentation.
 * 5d10e1f8: Make sure gettext is available by importing first.
 * adaf850d: Move ssh and imap backend globals to globals.py.
 * 57dc97c7: patch #6806: More graceful handling of old --short-filename files https://savannah.nongnu.org/patch/?6806
 * 6a62f4dd: modify file name test to test short filenames even when not specifically requested to
 * 5999b0f8: accept short filenames even if not specifically requested
 * d92c0472: bug #25594: wrong backup statistics https://savannah.nongnu.org/bugs/?25594
 * 390da598: Not needed.
 * a57166bf: Changes for 0.5.15.
 * 56428bd3: If a file is unreadable due to access rights or other non-fatal errors, put out error message and continue rather than dying messily with a traceback.
 * 75564e95: Move SystemExit function back to the top and put a large note NOT to move it back down, otherwise, Exception gets invoked instead.
 * 313371f4: Remove "--restore-dir" from options[]. It's not an option and never has been.
 * 87ae3ea0: Added tilde '~' expansion and variable expansion in the options that require a filename. You can now have this "--archive-dir=~/ArchDir/$SYSNAME" if you need it. No expansion is applied to the source or target URL's.
 * 55c55e28: Unit tests were failing for ftp because of the filtering for duplicity-only filenames. Corrected this and removed the check for the filename in the first element.
 * 77a7d354: If a file is unreadable due to access rights or other non- fatal errors, put out error message and continue.
 * 6b3afc8e: FTP backend was failing on PureFTPd when the "-x ''" option was removed from the second ncftpls popen, a fix that was implemented due to bug #24741. This fix does the ls in one pass by extracting either the first or the last entry on the 'ls -l'. [Standard FTP would be nice!]
 * d9e36bba: Changes for 0.5.14.
 * 32019a97: Normalized include statements and tried to insure that all duplicity includes were from the duplicity module.
 * 4071fc45: After email voting among known duplicity contributors, the decision was reached to revert to the GPL Version 2 license, so with their consensus, duplicity is now under GPL Version 2.
 * 0056d622: The -vN option has not changed. Verbosity may also be one of: character [ewnid], or word ['error', 'warning', 'notice', 'info', 'debug']. The default is 4 (Notice). The options -v4, -vn, and -vnotice are functionally equivalent, as are the mixed-case versions, -vN, -vNotice, -vNOTICE.
 * bec92407: The -vN option has not changed. Verbosity may also be one of: character [ewnid], or word ['error', 'warning', 'notice', 'info', 'debug']. The default is 4 (Notice). The options -v4, -vn, and -vnotice are functionally equivalent, as are the mixed-case versions, -vN, -vNotice, -vNOTICE.
 * 565b1672: patch #6790: Add --exclude-if-present https://savannah.nongnu.org/patch/?6790
 * ed6fd342: Clarify recent log entries.
 * c3e6f666: Add '../' to Python path so we find our GnuPGInterface and not another.
 * c51974cd: Changed from log.Log with numbered log levels to log.Debug, log.Info, log.Notice, log.Warn, log.FatalError as below: 0 log.FatalError 1 log.Warn 2 log.Warn 3 log.Notice 4 log.Notice 5 log.Info 6 log.Info 7 log.Info 8 log.Info 9 log.Debug The -vN option has not changed at this point.
 * 81408c67: Revert to calling NcFTP utilities (ls, get, put) directly rather than scripting ncftp via pexpect. Move fatal error regarding version 3.2.0 to a warning message since it has been reported that the segfault problem does not occur on most distributions.
 * d2a108e1: Add Changelog.GNU to website and distribution to add a bit of detail showing the CVS changes via rcs2log. Added dist/mkGNUChangelog.sh.
 * 3999fd06: bug #22908: Don't block gpg-agent https://savannah.nongnu.org/bugs/?22908
 * 207930ae: Add testing/manual dir.
 * 473e5b3f: bug #25976: Signed Backups Now Required https://savannah.nongnu.org/bugs/?25976
 * 87404a21: patch #6787: import duplicity.GnuPGInterface explicitly https://savannah.nongnu.org/patch/?6787
 * 09688b6b: Project setting changes.
 * 49e06ba7: One statement per line. Indent text of error message to code level.
 * 9680f043: Fixed bug where an extra comma caused a traceback during a warning about unnecessary sig files. Plus fixed print so the real filename would show up and not a Python object representation.
 * eb7ac39d: bug #25787: Usernames with escaped @-sign are not handled properly https://savannah.nongnu.org/bugs/?25787
 * 52598504: Adjust log levels so errors show up without verbosity.
 * 2d37baa3: BackendException does not cause traceback except when verbosity is at level 9 (debug).
 * 9a644f18: Fix backends so sleep does not occur after last retry.
 * 3347d9cd: Add more error detection to FTP backend.
 * 60943654: patch #6773: Make user name optional in rsync backend https://savannah.nongnu.org/patch/?6773
 * 5665af90: bug #25853: duplicity fails with boto passwords coming from ~/.boto https://savannah.nongnu.org/bugs/?25853
 * d7fe1def: GPG errors will no longer cause tracebacks, but will produce a log entry, from gpg, similar to the following: ===== Begin GnuPG log ===== gpg: BAD0BAD0: skipped: public key not found gpg: [stdin]: encryption failed: public key not found ===== End GnuPG log ===== This will let the user know what really caused the GPG process to fail, and what really caused errors like 'broken pipe'.
 * d6a4f01b: bug #25838: Backup fails / ncftp - remote file already exists https://savannah.nongnu.org/bugs/?25838
 * 3b886dbf: Add / modify / repair Epydoc docstrings and format.
 * 93158e9d: One statement per line.
 * 40db6cf3: One statement per line.
 * 1d20ff60: Changes for 0.5.11.
 * 13d8fa8a: Bug #333057: GnuPGInterface prints exit statuses incorrectly https://bugs.launchpad.net/bugs/333057
 * ac9087e6: bug #25787: Usernames with @-sign are not handled properly https://savannah.nongnu.org/bugs/?25787
 * b9d68a70: Detabify (was tab-width 8).
 * dd6aec91: Bug #333057: GnuPGInterface prints exit statuses incorrectly https://bugs.launchpad.net/bugs/333057
 * db47661b: Fix issue on return from waitpid where the result was shifted left and not right, producing 131072 instead of 2, as it should.
 * ac6c14e8: One statement per line.
 * 1e628382: bug #25696: ncftp error with 0.5.09 https://savannah.nongnu.org/bugs/?25696
 * df0bfb00: Also log the quit command.
 * 497d9ea8: One statement per line.
 * 101fc58e: bug #15664: When restoring backup: "OverflowError: long int too large to convert to int" https://savannah.nongnu.org/bugs/?15664
 * 3681502e: One statement per line.
 * 44276dda: patch #6761: More robust pexpect handling of SSH authentication https://savannah.nongnu.org/patch/?6761
 * 7eafb41a: patch #6762: Wrong exit() used for 2.3/2.4 Python https://savannah.nongnu.org/patch/?6762
 * f5899e93: One statement per line.
 * fcfa27a8: Explain new filenames and --time-separator better.
 * 45765fe6: Changes for 0.5.10.
 * f7b1bdf3: Add deprecation warnings for options affected by old filenames.
 * 6b5bc282: bug #19988: Incompatibility to Samba/SMB share https://savannah.nongnu.org/bugs/?19988
 * da4c9fe6: One statement per line.
 * 7900040d: One statement per line.
 * c7783cc2: Module gettext should be imported and installed prior to importing any other modules. This allows long strings to be translated when put at the module level rather than at the function call level. See dup_time.py for examples.
 * 89ffa243: One statement per line and other cleanup.
 * aa92ffad: bug #25550: Error codes do not propagate from log to exit status https://savannah.nongnu.org/bugs/?25550
 * a940e0c5: bug #25097: Allow listing files from any time, not just current time https://savannah.nongnu.org/bugs/?25097
 * c8d84c80: Bug #229826 duplicity crashed with ValueError in port() https://bugs.launchpad.net/duplicity/+bug/229826
 * 9f39cdbe: Changes for 0.5.09.
 * 3493dfe5: If tempdir.py is included, but not instantiated, then deleted, it throws an exception, as happens during testing when duplicity main is not used to instantiate tempdir. The fix is to make sure instantiation has happened before calling cleanup().
 * 1251d067: These are changes to make debugging easier. - Filter ANSI control (bolding) characters from NcFTP responses. - Turn off ad for ncftp server at close of each session.
 * a0104966: bug #25530: commandline passwd not working https://savannah.nongnu.org/bugs/?25530
 * 5c42ab23: FTP is now driven with pexpect rather than NcFTP utilities. This closes the following bugs: bug #24741: ncftpls -x '' causes failure on Yahoo FTP server bug #23516: duplicity/ncftpget not closing unlinked files, ...
 * 913f9ea7: Merge from pexpect_ftp.
 * 4fd8300f: Applied retryImap2.patch from bug 25512.
 * 59177980: bug #25509: Logic error in imapbackend.py [IMAP_SERVER] https://savannah.nongnu.org/bugs/?25512
 * 12e076d6: Replace rdiff-backup with duplicity in strings.
 * ae5a3d92: Add copyright for author.
 * a1b82627: Split parsedurl test from backendtest and add test cases.
 * bb0707fa: Add NcFTP 3.2.0 exception clause to dependencies.
 * 70182fa1: Turns out going backwards in the license is not as easy as forwards. Restoring GPLv3 license until consensus reached.
 * 0e4db189: Add/update copyright statements in all distribution source files and revert duplicity to GPL version 2 license.
 * 0fcf206c: Changes for 0.5.07.
 * bf692979: Python 2.3 unittest.py tried to call to a test-local variable named 'test_id' and failed. Changed to 'my_test_id' and all is well.
 * 83708139: Original fix to disallow use of ncftpput 3.2.0 mistyped the ErrorCode used.
 * bccfd155: patch #6733: Improve error handling in imapbackend.py https://savannah.nongnu.org/patch/?6733
 * d778f2fd: Add/update copyright statements in all distribution source files and revert duplicity to GPL version 2 license.
 * 42541b51: patch #6729: New imap backend. Replaces current gmail backend https://savannah.nongnu.org/patch/?6729
 * e2869c6d: bug #25293: IOError: [Errno 22] Invalid argument https://savannah.nongnu.org/bugs/?25293
 * cde57722: Modify patch #6730: Fix timing out for SSH backend Do not take out the first line from the return buffer (#4).
 * a5f7d425: patch #6730: Fix timing out for SSH backend https://savannah.nongnu.org/patch/?6730
 * 34aa1376: patch #6729: New imap backend. Replaces current gmail backend https://savannah.nongnu.org/patch/?6729
 * 944c8e0f: Removed ref to bug 25331 since the analysis and fix were both wrong. The issue was fixed correctly in bug 25403.
 * 2d21a816: bug #25403: 0.5.06 "manifests not equal because different volume numbers" https://savannah.nongnu.org/bugs/?25403
 * fa8df0c7: bug #25403: 0.5.06 "manifests not equal because different volume numbers" https://savannah.nongnu.org/bugs/?25403
 * 55a58fa3: One statement per line.
 * 94e0005b: Move alltests list to separate file.
 * 4c165708: Add coverage output to .cvsignore.
 * 400c6f03: Turn on verbose for unit tests.
 * 4ba257e4: Fix backendtest.py so that empty URL's in config.py cause the backend test to be skipped rather than erroring. Added notes in config.py.tmpl explaining the change.
 * c050757f: Make default Python be system default version.
 * 232c72c1: Add Releases directory.
 * 54ba8d65: First pass at coverage analysis, collect the data.
 * 10b170ea: Remove LOG entries. Not needed.
 * 7a5d439d: Change to ASCII (-kkv)
 * 3d8e2b39: Run a single unit test.
 * 01254228: Increase default volume size (--volsize) to 25M from 5M. This reduces the number of volumes to accomodate larger backups.
 * 5de3f51a: bug #25379: sys.exit() causes traceback and should not https://savannah.nongnu.org/bugs/index.php?25379
 * 1f1c7c0a: Reworked patch 6701 to list collection one at a time rather than writing all as one huge list. Was causing memeory problems when the collections got large.
 * 4b922c3b: bug #25331: When --archive-dir and --encrypt-key are used together, incremental fails. https://savannah.nongnu.org/bugs/index.php?25331
 * cbffdf6c: bug #25331: When --archive-dir and --encrypt-key are used together, incremental fails. https://savannah.nongnu.org/bugs/index.php?25331
 * ef998beb: Changes for 0.5.06.
 * 8c864d2a: Fix illegal macro .PP. by removing extraneous period on end.
 * f52778f4: NcFTP version 3.2.0 will not work with duplicity since we require the use of both -f and -C options on ncftpput. 3.1.9, 3.2.1+ work fine. I put in error checks for this situation in the FTP backend code.
 * 282c0f2c: Noah Spurrier has given us permission to distribute pexpect.py along with duplicity, so this will no longer be an install requirement.
 * 01c1bc7e: Added loop to run-all-tests.sh to run all tests against all supported versions of Python if available. Looks for 2.3, 2.4, 2.5, 2.6.
 * a2ec3c43: Fix to deprecation warnings about sha and md5 modules. Uses hashlib if available, otherwise original module.
 * 16d685ab: Missed the most basic case, no selection functions. Fixed.
 * b0e7c0c1: bug #25230: --include-globbing-filelist only including first entry. https://savannah.nongnu.org/bugs/?25230
 * b4001a37: sr #106583: document the need to use the --force option https://savannah.nongnu.org/support/?106583
 * c6488151: patch #6709: Report correct number of volumes when restoring https://savannah.nongnu.org/patch/?6709
 * 90ce58d7: bug #25239: Error during clean, wrong case in duplcicity https://savannah.nongnu.org/bugs/?25239
 * f4019707: Changes for 0.5.05.
 * ea7e046d: Add po files back into distribution.
 * 30cbcb4f: Cosmetic - reformat FatalError calls at end for readability.
 * 67c2eb6a: Change "test" to "$version".
 * 24aa7ab5: Build list of .mo files to be installed from po directory.
 * bf397d19: bug #25194: Duplicity 5.04 requires python-distutils-extra... https://savannah.nongnu.org/bugs/?25194
 * 2ca892b0: Use reldate expansion to include release date.
 * 7837138e: Use os.path.join() instead of hardcoded strings - Make VersionedCopy replace $reldate as well as $version
 * a623d44c: Adjust RPM spec file for translations.
 * 3d82d753: Changes for 0.5.04.
 * fdca64e0: patch #6702: handle unknown errnos in robust.py https://savannah.nongnu.org/patch/?6702
 * 793ffdb9: patch #6700: Make duplicity translatable https://savannah.nongnu.org/patch/?6700 [not in patch - added after unit tests]
 * f574f070: patch #6701: Make current-list command machine-readable https://savannah.nongnu.org/patch/?6701
 * f32e5998: patch #6700: Make duplicity translatable https://savannah.nongnu.org/patch/?6700
 * 84ce9270: GPG was throwing "gpg: [don't know]: invalid packet (ctb=14)" and apparently this is non-fatal. There is a fix for this being rolled into GPG 2.x. http://lists.gnupg.org/pipermail/gnupg-devel/2006-September/023180.html Copied from collections.py. Fix supplied by Simon Blandford <simon@onepointltd.com>
 * 7bd01fd9: One statement per line. No other changes.
 * 701bdc1e: One statement per line. No other changes.
 * 0bd5b638: Print backend name for each test started.
 * 826658da: Remove test for assert on non-existing delete. Not all backends will raise an exception when the target of a delete does not exist.
 * 3b68b196: Log correct file name in line 67. Use diff_ropath, not basis_path.
 * bd06e6cc: Fix patch applied during Patch #6696. Applied fixiter.diff.
 * 79fa53af: patch #6697: Always log at least one progress during dry run https://savannah.nongnu.org/patch/?6697
 * 5e7372da: patch #6696: Consolidate get_delta_iter and get_delta_iter_w_sig https://savannah.nongnu.org/patch/?6696
 * 01bafc72: patch #6695: Log filenames https://savannah.nongnu.org/patch/?6695
 * c862a23e: patch #6694: Log exceptions https://savannah.nongnu.org/patch/?6694
 * 1c5da82c: patch #6693: Some FatalError's don't have codes still https://savannah.nongnu.org/patch/?6693
 * 4af0ad02: patch #6692: Print collection status in a machine-readable way https://savannah.nongnu.org/patch/?6692
 * ab1cf467: bug #24889: NCFTP cannot deal with some FTP servers https://savannah.nongnu.org/bugs/?24889
 * 5cc8e606: bug #25090: Typos and trailing whitespace in duplicity manpage https://savannah.nongnu.org/bugs/?25090
 * 0672a0b1: patch #6686: Add error codes for all fatal errors https://savannah.nongnu.org/patch/?6686
 * 434881f4: patch #6678: Add progress metering https://savannah.nongnu.org/patch/?6678
 * c8ded523: Changes for 0.5.03.
 * b41e11ad: patch #6676: Raw delta stats aren't right for multivolumes https://savannah.nongnu.org/patch/?6676
 * 1be02bc9: patch #6675: Add modelines https://savannah.nongnu.org/patch/?6675
 * f78fa30e: patch #6674: Add --log-* options to man page https://savannah.nongnu.org/patch/?6674
 * 69882a0d: patch #6673: Add --dry-run option https://savannah.nongnu.org/patch/?6673
 * f0c35b62: patch #6672: makedist doesn't ship util.py https://savannah.nongnu.org/patch/?6672
 * 0100a67d: Add log.setup() call to main() to support new logging.
 * 407cf34a: *** empty log message ***
 * b46ae395: Add log.setup() to support new logging.
 * 4496c809: Checkpoint 2 prior to 5.03.
 * d9accb3b: patch #6670: Machine Readable Output https://savannah.nongnu.org/patch/?6670
 * 87a91a71: Correct spelling of parsed_url (parsed_urk) in patch #6662.
 * e33d46ae: sr #106534: GMail backups aren't stored in the correct location https://savannah.nongnu.org/support/?106534
 * df2ef671: sr #106496: put install-from-cvs-notes in CVS-README https://savannah.nongnu.org/support/?106496
 * c6fa35e2: Checkpoint prior to 5.03.
 * b391423b: patch #6638: correct typo in reporting lack of sufficiently new boto backend https://savannah.nongnu.org/patch/?6638
 * 0bf8073c: patch #6642: make ParsedUrl() thread-safe with respect to itself https://savannah.nongnu.org/patch/?6642
 * a873a779: patch #6652: improve asynch scheduler (including the synchronous case) https://savannah.nongnu.org/patch/?6652
 * 81912cc5: patch #6662: improve s3 backend error reporting https://savannah.nongnu.org/patch/?6662
 * 4c8ee7e9: patch #6670: Machine Readable Output https://savannah.nongnu.org/patch/?6670
 * bdfe9278: bug #24775: Digest Auth for WebDAV backend https://savannah.nongnu.org/bugs/?24775
 * 1b7f5f5b: bug #24731: Documentation error: "if... if" in remove-older-than paragraph https://savannah.nongnu.org/bugs/?24731
 * ba130d75: Changes for 0.5.02
 * 784cda88: patch #6297: Add IMAP/s/gmail support https://savannah.nongnu.org/patch/index.php?6297
 * 8dca0e8e: patch #6297: Add IMAP/s/gmail support https://savannah.nongnu.org/patch/index.php?6297
 * b18e90a0: Change to one statement per line.
 * 490fc7d1: Change use of logger so that gpg logs are always collected. The log is always printed in the case of gpg IO errors. Verbosity level 5 or greater will also print the logs the same as previous versions.
 * af0784e9: Make one statement per line. No other changes.
 * 58540dd3: add -h option for help
 * 7eada2b7: bug #24274: asyncscheduler.py missing sys import https://savannah.nongnu.org/bugs/index.php?24274
 * c51562cc: bug #24260: backend.py missing re import https://savannah.nongnu.org/bugs/index.php?24260
 * f7db7fe5: Changes for 0.5.01
 * efdce64a: Ignore test log file.
 * dae7889e: Untabify all files. To compare against previous versions use 'cvs diff -w' or 'diff -w'.
 * 7052acfa: Create target dir (collection) if needed.
 * 1f967351: Ignore testfiles dir.
 * fc84c63d: Add tests for webdav and webdavs.
 * 166ee3b3: bug #24223: WebDAV backend broken in 0.5.00 https://savannah.nongnu.org/bugs/index.php?24223
 * 41b4a50d: Changes for 0.5.00
 * 2de51b91: Changes for 0.5.00
 * afbe47c7: temp2.tar was a test-created file that had to be present at the beginning of test_tarfile.py. Removed the need for it to be present and removed the file from CVS.
 * eaf676a6: Changes to get unit tests working again: resolve circular imports during unit tests - resolve exception error import - now in errors.py
 * f26a3020: patch #6623: slightly augment tempdir cleanup logging https://savannah.nongnu.org/patch/index.php?6623
 * 02ae58e8: No longer needed, see backends dir.
 * 59bf20f8: no comment
 * b33ecb85: bug #23988: scp destination fails if no username is specified https://savannah.nongnu.org/bugs/index.php?23988
 * 3a314058: bug #23985: --no-encryption option does not work in 0.4.12 https://savannah.nongnu.org/bugs/index.php?23985
 * 2e62e0ba: patch #6596: re-organize backend module structure https://savannah.nongnu.org/patch/index.php?6596
 * bb87c780: patch #6353: Concurrency for volume encryption and upload. https://savannah.nongnu.org/patch/index.php?6353
 * e7b43b47: patch #6589: S3 european bucket support https://savannah.nongnu.org/patch/index.php?6589
 * 389abbdb: Changes for 0.4.12.
 * 19c21098: bug #23362: Documentation for --version, --time-separator <char> https://savannah.nongnu.org/bugs/index.php?23362
 * 7fc564a2: Cosmetic only.
 * b80eba63: bug #23540: doc bug in man page (environment FTP_PASSWORD) https://savannah.nongnu.org/bugs/?23540
 * 64f38a6c: Dan Muresan created a patch that tries to minimize the number of password prompts. To do so, it sometimes requests a password once without confirmation; if later it turns out that a full backup is needed, the user is prompted for confirmation.
 * 2c590f50: bug #23066: ssh uris with given portnumbers are not handled correctly https://savannah.nongnu.org/bugs/index.php?23066
 * 0b555e8a: Fix sort() for Python 2.3
 * 1f47928b: Change back to requiring Python 2.3.
 * 7f1329aa: Change requirements back to Python 2.3.
 * ef45dae7: Changes for 0.4.11
 * 9a73cf06: Modified to run on Python 2.3.
 * fd31d316: bug #22826: regressions caused by boto 1.1c https://savannah.nongnu.org/bugs/?22826
 * 7f15996c: Reinstate patch #6340 with a detailed explanation. http://savannah.nongnu.org/patch/index.php?6340
 * 610f3387: Changes for 0.4.10.
 * 3c40af8e: Remove --sign for now.
 * 12bb2a44: bug #22728: FTP backend fails on empty directory https://savannah.nongnu.org/bugs/?22728
 * 19845386: Fix log.debug to log.Debug
 * 28b7a63d: patch #6453: handle absolute urls in webdav backend https://savannah.nongnu.org/patch/index.php?6453
 * af28244d: patch #6449: add additional debug level logging https://savannah.nongnu.org/patch/index.php?6449
 * 7589d3c2: patch #6403: Restore by overwriting files/directories by using --force option https://savannah.nongnu.org/patch/?6403
 * d750a281: Password should be None, not empty string.
 * e645ccd4: Add config for S3 tests.
 * ebda364b: Reformat to one statement per line.
 * bc079018: Fix problem where S3 prefix was appended with 'd'. This caused a failure in the regression tests. Unsure where it came from.
 * ae28b48a: patch #6389: Possible Fix for pagefile.sys on Win32 systems https://savannah.nongnu.org/patch/?6389
 * 9e83603d: patch #6380: add additional named logging levels https://savannah.nongnu.org/patch/?6380
 * 037fb85c: patch #6374: Duplicity --tempdir patch documentation. https://savannah.nongnu.org/patch/?6374
 * 773d436d: patch #6375: Duplicity reports the epoch for a nonexistant last full backup date https://savannah.nongnu.org/patch/?6375
 * 5a9767c3: remove sleep() from dup_time.py - not used. - make one statement per line format change.
 * c8b289f9: Remove testSleeping since sleep() removed from dup_time.py.
 * 2f57db25: Add S3 backend test.
 * 55de1532: do not store object
 * e4681006: Add requirements for source package install.
 * df3744d6: Changes for 0.4.9.
 * 30178996: Add more info on URL formats.
 * fd6b1691: Updated URL Formats in the Help Screen.
 * 7fa5e54e: Added section URL FORMAT in the duplicity man page.
 * 69578e76: Make sure to strip extraneous single colon when dealing with non-module URLs. We provide the colon as needed.
 * c6b1c3e2: bug #21909: Problematic typo in compare_verbose() method https://savannah.nongnu.org/bugs/index.php?21909
 * 7cbdf13f: patch #6357: Explicit restore action is missing from the command list, https://savannah.nongnu.org/patch/?6357
 * 6c6a2367: patch #6356: Command line option for the temporary directory root. https://savannah.nongnu.org/patch/?6356
 * d7e362a1: Added regression tests for absolute, relative, and module pathing in the rsync scheme.
 * e7386bd1: Fixed rsync URL description text in --help.
 * 26ded1b3: Added 2nd patch to bug #21475 that forces all versions of Python to use the fixed urlparse.py.
 * 15098653: Fixed so that remove-older-than and remove-all-but-n-full will not request a GPG passphrase.
 * fc000da7: Fixed regression caused by changeover to new urlparse.py. bug #21475: FTP Usernames that contain '@' are not recognized https://savannah.nongnu.org/bugs/index.php?21475
 * 507cb28a: Changes for 0.4.8.
 * 1b13d38f: Format to one statement per line.
 * 9378ae38: Allow pexpect to force the close of the child on sftp calls. We already do that with scp calls. This cleans up that exception.
 * 92fd63fa: patch #6344: S3 bad bad key key handling http://savannah.nongnu.org/patch/?6344
 * 5e4cf8a2: Replace set_password/phrase with set_environ and clarify meaning in config.py.
 * b16d0752: Complete description of install using --prefix=.
 * 5badff45: Fix version of boto needed plus formatting.
 * 3cc5b4e4: patch #6340: S3 short filename regression https://savannah.nongnu.org/patch/?6340
 * 68150356: Make sure config.py not checked in.
 * 88f2250a: Initial release.
 * b562563f: This test requires a file that no longer exists. Plus, it is unclear what this test is supposed to accomplish. Tar is tested by the other tests.
 * 0f14cdcc: First pass at getting tests up to date: -- isolate config in 'config.py' (see config.py.tmpl) -- silence noisy tests as much as possible -- fix code on both sides as needed
 * 9fde4053: Initial release.
 * 1552f7c5: Remove 2nd call to dup_time.settimestr() since it overrides the time that may be set by --current-time (used for testing).
 * 1f277c2e: Regen dup_time.curtimestr if time-separator changed.
 * 3e22fbb7: Fixed previous patch that assumed the presence of the user and password in the rsync URL.
 * e376b183: Bring tests up to date.
 * 116bdc1f: bug #21751: rsync module urls do not work in 0.4.7 https://savannah.nongnu.org/bugs/index.php?21751
 * d584d163: Changes for version 0.4.7.
 * 9293b4f1: Change to require Python 2.4 or later.
 * dcc9d5f5: Formatted list and added tempdir.py and urllib_2_5.py to the released files list.
 * 8f1646e4: Fix confusion over patches applied to different versions. Patch #6300 should now be applied completely.
 * 36b9d6ab: Hole imapbackend till next release.
 * 0737a78f: Hold till next release.
 * 6ad55408: patch #6300: Standard library replacement for ParsedUrl class https://savannah.nongnu.org/patch/?6300
 * 1ad6fe57: Backed out the following patch until bugs fixed... patch #6300: Standard library replacement for ParsedUrl class https://savannah.nongnu.org/patch/?6300
 * fc887e48: patch #6301: log sftp commands at verbosity 5 https://savannah.nongnu.org/patch/?6301
 * 227a7284: patch #6300: Standard library replacement for ParsedUrl class https://savannah.nongnu.org/patch/?6300
 * 24c8ca1d: patch #6299: re-design tempfile handling https://savannah.nongnu.org/patch/?6299
 * 05e2dafd: Move import of imapbackend to the end of the module. Circular dependency. Needs fixing.
 * 51f5fed9: Undo regression of bug #21508 contained in patch #6298: URI unquoting patch for FTP backend https://savannah.nongnu.org/patch/?6298
 * b5dcf7cf: patch #6298: URI unquoting patch for FTP backend https://savannah.nongnu.org/patch/?6298
 * a4ac52d5: patch #6297: Add IMAP/s/gmail support https://savannah.nongnu.org/patch/?6297
 * 6e31216c: patch #6297: Add IMAP/s/gmail support https://savannah.nongnu.org/patch/?6297
 * 1c25b531: patch #6292: Amazon S3 bucket creation deferral for Duplicity 0.4.6 https://savannah.nongnu.org/patch/?6292
 * b0d7f416: bug #21686: NcFTPGet 3.2.0 tempfile incompatibility https://savannah.nongnu.org/bugs/index.php?21686
 * 8f401e96: Applied patch from Eric Hanchrow to fix logging error in botoBackend, and fix delete() in rsyncBackend.
 * 0349479d: bug #21673: remove-all-but-n-full wrong arg usage https://savannah.nongnu.org/bugs/index.php?21673
 * 0aeed786: more Changes for 0.4.6.
 * 182a9bbc: Changes for 0.4.6.
 * f78de2f3: Fixed coding problem where matched_sig_chain could be referenced before it was defined.
 * 13bb26f6: https://savannah.nongnu.org/patch/index.php?6291 patch #6291: Alternative WebDAV HTTPS patch
 * 3df2df03: https://savannah.nongnu.org/patch/index.php?6289 patch #6289: Amazon S3 key prefix patch for Duplicity 0.4.5
 * b708e47e: https://savannah.nongnu.org/patch/?6284 patch #6285: security fix: eliminate use of mktemp()
 * 4af7f14d: https://savannah.nongnu.org/bugs/index.php?21651 bug #21651, add https support for webdav.
 * bb6438ff: https://savannah.nongnu.org/bugs/index.php?21657 bug #21657: ncftpls fails to create dir in ver 0.4.5
 * e96c6ec7: https://savannah.nongnu.org/bugs/index.php?21651 bug #21651, add https support for webdav.
 * b519c7af: Try, the second. See comments in the bug tracker. https://savannah.nongnu.org/bugs/index.php?21646 bug #21646: --archive-dir causes delete of remote full sigs and orphaned sig files
 * d0fc64b0: https://savannah.nongnu.org/bugs/index.php?21651 bug #21651, add https support for webdav
 * 1a1c242e: Fix release date in 0.4.5.
 * 72909c95: Changes for 0.4.5.
 * 913c351e: https://savannah.nongnu.org/bugs/index.php?21646 Fix to handling of collections when --archive-dir is used. Prior to this, duplicity would write the full sig files to both local and remote, then delete the remote. Now, it does not delete the remote full sigs.
 * 1f1da108: Changes for version 0.4.4.
 * 76516c38: Applied a patch from Gregory Hartman to correct handling of DST in time calculations. This affects backups made the night of a DST time switch.
 * a2972427: Cosmetic - Use True and False, not 1 and None.
 * 442167cc: Fix version checking code in ftpBackend.
 * 1a957ffd: Changes to commandline processing to allow non-ambiguous short strings for commands, i.e. 'i', 'inc', 'incr' for 'incremental', 'f' for 'full', etc.. A warning message is printed if the short command is not unique.
 * fa7d91c6: Changes to ftpBackend to use the login config file rather than putting the username and password on the command line. This requires the use of NcFTP 3.1.9 or later.
 * b1bdafae: Changes for 0.4.4.RC4 try 2
 * 9bd0cf63: Changes for 0.4.4.RC4
 * 3739d642: Replace with Version 3 GPL text.
 * 52e882ed: Fixed issue in --time-separator where the current time string was being set prior to setting the separator, causing errors when trying to set the --time-separator for Windows systems.
 * 983f6694: There is a new command line syntax to separate actions and options. Refer to the new man page for full details.
 * 897ef187: Correct calling sequence in calls to get_signature_chains().
 * 31aacf80: Fix so that ftpBackend.delete() does not print file list.
 * 6f287376: Fix so that file mtime is always compared in full seconds.
 * b0ad0c42: Changes for 0.4.4.RC3 -- Corrected.
 * 44a116e2: Changes for 0.4.4.RC3.
 * 8e1f0575: Add 'patch' dir to ignore list.
 * fba1d7f0: Patch from Olivier Croquette to add :port option in FTP.
 * 9343f1fb: Patch from Olivier Croquette to add --full-if-older-than=<time> option to force a full backup at <time> rather than incremental.
 * 36219114: Patch from Olivier Croquette to add :port option in FTP.
 * 7bd01d3d: Changes for 0.4.4.RC2.
 * f7727e84: Added --timeout <seconds> (default 30) to allow users to change duplicity's network timeout settings.
 * 3cc56baa: Add patch from Olivier Croquette to allow user@domain usernames, making ftp://user@domain@domain.com/path a valid URL.
 * ed9a3c8c: Add patch from Alexander Zangerl to suppress the GPG passphrase prompt when a passphrase is not needed. - full and pubkey enc: doesn't depend on old encrypted info - inc and pubkey enc and archive-dir: need manifest and sigs, which the archive dir contains unencrypted - with encryption disabled - listing files: needs manifest, but the archive dir has that - collection status: only looks at a repository
 * 7ab98add: Changes for 0.4.4.RC1.
 * e5ccad7c: https://savannah.nongnu.org/patch/index.php?6205 Add option --librsync-dir for when its not found.
 * 3c5399c2: Bug #21123: duplicity 0.4.3 does not find any backup chains https://savannah.nongnu.org/bugs/?21123
 * 846c6a06: Make tempfiles with useful names.
 * 4db851ff: Fixes manual page and usage msg for rsync url and --remove-older-than.
 * 3f44fc01: Fix for Debian bug #228388: old/aborted/offending sig files prohibit any further action.
 * bb343baa: Fixes manual page and usage msg for rsync url and --remove-older-than.
 * f428903f: Do not ask for passphrase when none is needed.
 * 9bd58bb2: Final patch for Peter Schuller's fix to max read size. The first one was broken (revision previous to this).
 * 46faa352: Add patch submitted by Peter Schuller which removes the default SSH options that ignored known hosts files and disabled strict host checking. This patch also handles the authentication failures from these issues.
 * 33884e46: Fixed so that max read size is 64k, not the volume size which can be quite large.
 * 5d4973ad: Fix release date.
 * 27fa0788: Changes for 0.4.3 release.
 * c1ed9196: Removed use of tempfile.TemporaryFile(). This fixes the restore problem on Windows that was due to Python bug 1776696 reported on Sourceforge.
 * 53a2b158: Removed hardwired options to use bzip2 compression.
 * 32efb426: Changed ssh-command to ssh-options to allow users to add options to the scp and sftp commmands.
 * c976c14e: Move get_password() to Backend class to standardize.
 * 25ba0a8f: Upgrade to GPL version 3 license.
 * 43423689: Do not pass :port part of URL to scp backend. Its taken as the target file and errors out.
 * 962883c5: Change ssh_command option to be ssh_options. This adds options to the scp and sftp commands that are used by the ssh backend.
 * 3bd8bdff: Fixed bug 20764 - unable to use port in ssh backend. https://savannah.nongnu.org/bugs/?20764
 * 13dd76fa: Changes for 0.4.3.RC12
 * b303fe34: Changes for 0.4.3.RC12
 * 13718150: Changed the file:, ftp:, and ssh: backends so that the target directory will be created at start.
 * 5cb61375: Clean up help list formatting.
 * 9db2934a: Fix index out of range in Bug 20730, triggered when there is only one incremental and no previous in list. https://savannah.nongnu.org/bugs/?20730
 * 5c49887e: Print warning if pexpect version is less than 2.1. - Fix author and maintainer settings.
 * 83a42263: Fix environment var name for ssh backend.
 * 002de24b: Changes for 0.4.3.RC11.
 * 824e0521: Add --ssh-askpass option.
 * 3e954798: Duplicity now correctly processes scp URL's of the form: scp://user@host[:port]/ where the directory spec is empty. This fixes a bug where the user could not write into the home directory on the target.
 * 94dbcb5e: patch #6094, Boto Backend Fixes for RC10
 * 5e4139b9: Changes for 0.4.3.RC10
 * 8537a6a4: Add support for: --ftp-passive, --ftp-regular, --num-retries
 * c4958468: Add support for: --ftp-passive, --ftp-regular, --num-retries
 * 8f0fc08e: Add descriptions for: --ftp-passive, --ftp-regular, --num-retries
 * aed14161: Replace missing comma in argument list.
 * 73982a41: Changes for 0.4.3.RC9. Drop ftplib.py.
 * c59ede3e: No longer needed.
 * 762b21b3: Changes for 0.4.3.RC9.
 * 3b5c4b22: Added a commandline option, '--num-retries=<int>', to set the number of retries. The default is 5.
 * 5b27baeb: New S3 backend, Boto, from Eric Evans, replaces bitBucket. Boto can be obtained from http://code.google.com/p/boto/. I did not make this a requirement for setup since its not in the normal repositories.
 * 6e4182a1: Change to a max block size of 2048 bytes for rsync difference buffer. This may slow things down for truly large files, but will give much smaller deltas on files with numerous small changes, such as database files.
 * ca267e7c: Initial release.
 * 7a1677e8: Changes for 0.4.3.RC8
 * 2bb2b17f: Bug 20039 - Andreas Schildbach: --and-- Patch 6030 - Alexander Zangerl <az@debian.org>: Duplicity now uses bzip2 for compression. This matches the way the Debian distribution handles it. I'll think about adding an option to override later, if its needed.
 * 33d621cd: Bug 20282 - Thomas Tuttle: An out of range index when checking past history in the backup sets caused a failure when trying to access later.
 * 28da3d43: Changes for 0.4.3.RC7
 * 14d9bcf6: Patch 6029 - Alexander Zangerl <az@debian.org>: http://bugs.debian.org/370206 archive-dir together with incremental backup results in crash. the patch is simple, the code in 0.4.2 did attempt to access strings as objects.
 * 4f58ca06: Patch 6033 - Alexander Zangerl <az@debian.org>: let's add a --help terse usage message and don't just direct the user to the manual. this should come handy if somebody needs to restore stuff without having the manual available.
 * ebc50975: Patch 6032 - Alexander Zangerl <az@debian.org>: a new feature patch: i've recently gotten annoyed with having gazillions of 5mb files and therefore added a --volsize option to allow the user setting the chunk size. the patch is simple and contains a manpage update as well.
 * e5835fd8: Add -u (unbuffered) to shebang line.
 * d5545eeb: Add stderr.flush() in FatalError().
 * 5c4b97cb: Bug 20179 - dAniel hAhler: When errors cause login to fail in FTP, reset and try again.
 * 0a32ec89: Not needed.
 * 3aab7fbd: Cosmetic change to force new log. The log for revision 1.28 is not correct. It should read as follows:
 * 65466e17: Changes for 0.4.3.RC6.
 * fb38cf7b: Patch 5998 - Kuang-che Wu: Cache uid and gid lookup to speed operations.
 * b0e94d89: Bug 20419 - dAniel hAhler: When errors cause an incomplete backup set, flag the error with a message, rather than erroring out. The user then knows to run --cleanup.
 * 6812788d: Changes for 0.4.3.RC5.
 * 50c0ee4d: dAniel hAhler submitted a patch to change "Error initializing file foo" (log level 2), where foo was a socket, to "Skipping socket foo" (log level 7). https://savannah.nongnu.org/patch/?5985
 * 2538a128: Change logging to flush after every write, unbuffering stdout and stderr, thus producing logs that are coherent.
 * 96b093f2: GnuPG fails when trying to access stdin on an empty passphrase. Changes allow empty passphrase on public-key encryption and now respond gracefully on empty passphrase for symmetric encryption.
 * c164daf3: Changes for 0.4.3.RC4.
 * 601685b0: Move catch of NLST errors back to self.error_retry()
 * 31550411: More FTP fixes: clean up error handling - change initial error delay to zero - move catch of NLST errors to self.list()
 * 81c1c262: Changes to release 0.4.3.RC3.
 * 9d60edad: Fix so that FTP connection/login is closed and reopened when errors 221 or 421 are reported.
 * 1fa0f02c: Changes to release 0.4.3.RC2.
 * 3f91e646: Remove GnuPGInterface.py
 * 8e6b49cc: Apply patch for bug 19998, ValueError exception.
 * 6b5dab80: Added change notices for FTP password and rsync backend.
 * 1ae37feb: Fix request password in ftpBackend if environ not set.
 * e2e0cc71: allow connection after 226 in NLST (ProFTPD) - request password in ftpBackend if environ not set - rsyncBackend was using the full URL, now uses server:path
 * 3e06fb09: Document changes for 0.4.3.
 * 38e9beb3: Do not set FTP to active mode at start of session.
 * ef5cda64: 1) WebDAV needs a Depth: 1 header otherwise infinite depth is assumed and may be restricted due to load.
 * d4a4b021: Fixes bug: https://savannah.nongnu.org/bugs/?19940
 * 92fd4bad: Applied patches: https://savannah.nongnu.org/patch/?5680 https://savannah.nongnu.org/patch/?5681
 * f4129b37: Added patches: https://savannah.nongnu.org/patch/?4486 https://savannah.nongnu.org/patch/?5183 https://savannah.nongnu.org/patch/?5185 https://savannah.nongnu.org/patch/?5412 https://savannah.nongnu.org/patch/?5413 https://savannah.nongnu.org/patch/?5680 https://savannah.nongnu.org/patch/?5681 https://savannah.nongnu.org/patch/?5682 https://savannah.nongnu.org/patch/?5794 https://savannah.nongnu.org/patch/?5830
 * 53c380b0: BitBucketBackend: if something goes wrong and we need to re-connect, dump the exception on stderr. Be very noisy so that whatever is wrong will be fixed.
 * 73acb588: Typo fix for error message
 * 7fb3fc9d: Fix a bug in the bitbucket backend: We need to get a new bits from the new bucket if we re-connect.
 * 8036c80b: Changes to the bitbucket backend: Update to work with bitbucket 0.3b. * Add some docimentation. * Implement a suggestion by Ben Escoto to move the access and secret keys to environment variables. * Implement a very simplistic error correction mechanisim that will re-connect on an operation failure and re-try the operation. Note that this is just a band-aid for issues that should be resolved at lower levels.
 * a37c96ed: Removed time_separator entry from changelog when I backed out patch
 * 387ddd3c: Went back to old time_separator, because I realized new way wouldn't handle some cases, and could break backwards compatibility
 * 59bd396a: Andre Beckedorf's patches for ftp and rsync backends, and time_separator
 * 1c4bdfd3: Checked in Brian Sutherland's Amazon S3 code
 * b1f3b294: Added --sftp-command to changelog
 * 3aef4be7: Added --sftp-command option and man page documentation
 * 8068fb10: Fixed Jiri's name. Sorry about that :-)
 * c6478c29: final changes for version 0.4.2
 * be1c3bb8: Fixes to the scp backend
 * 6f39acf7: Stop --remove-older-than from deleting current chain
 * 935440bb: Catch ftp error 450 when listing directory
 * 3a398593: cleaned up and documented --collection-status
 * 84cab1f1: asdf's tarfile large uid/gid patch
 * 9f08eb72: Jiri Tyr's scp/sftp patch
 * 80e46641: Eric Hanchrow's remove signature patch
 * d0b01e1e: A few minor updates so test pass on my system again
 * e76d0722: MDR patch allows signing with different key
 * 3021420f: Added note about passphrase confirmation
 * 6cfafa3b: When collecting password from user, make type it twice to confirm
 * 2c6c2caa: Final changes for 0.4.1
 * c644859e: Updating rpm for Fedora
 * 00fe6d69: Trying to remove...
 * 0f745173: Small changes for 0.4.1 and python 2.3
 * 192afa44: variable block size, librsync 0.9.6
 * 29a08f57: Remove large file note now that block size chosen based on file size
 * baa61183: Ported some code from rdiff-backup: choose sig block based on file length, and work with librsync 0.9.6.
 * 2aae54bd: Mention problem with /proc
 * 9e6be669: Cache pwd and group files
 * 881546eb: Added --version switch, small change to man page
 * 1ad6d570: Sebastian Wilhelmi's update for rsync backend
 * a3d00d16: Applied Stephen Isard's patch for --exclude-globbing-filelist
 * b80ad0d0: Added mention of rsync backend.
 * 8cb5ff73: added rsync contributed by Sebastian Wilhelmi
 * 42f95a82: Added test and fix for long symlink to long file bug
 * 12e6affc: Raise error (instead of exiting silently) if no files found to restore
 * 32bb8615: Added long filenames test
 * 96b86bb7: Added man page info on --short-filenames option
 * 0d1f2f6a: (version of) Helmut Schneider's patch to display mtimes with list files
 * 807a1fdd: Added --no-encryption option, fixed crash on inc when no changed files
 * 58170da3: Added --verify option, tweaked some verbosity levels
 * 80b660e2: Added compare_verbose and test to path module
 * 566bae04: Changed restore procedure. Now all sets integrated simultaneously.
 * e5f41c8e: Fixed typo in get_ropath
 * 29576647: Added a few options for only doing upload/move/checkin/etc
 * 126fb133: Changed way difftars are split between volumes to waste less space
 * d8ec20f8: Slight tweak to base36 code
 * 9eb6f599: Added extra tests for base36 conversion
 * 20a10a04: Shorted short filenames (use base36)
 * 1ae8921a: Swallow GPG logging output if verbosity 3 or less
 * 1182a54e: Added --remove-older-than option, changed --current-time behavior
 * 7056621d: Added --cleanup option
 * 3ffcd5c8: Added --force option.
 * ba2da922: Added code for finding extraneous and old files
 * 5511546a: For ssh, deleted in groups of 10 so command line doesn't overflow
 * f953182e: Fixed a few minor collections bugs, added get_extraneous
 * 2e69b142: Added note on one pass restores/verifies
 * ff629f58: Added --restore-time bug fix note
 * 8c419464: Better fix for same (current_time) bug
 * 88f01fed: Fixed minor bug erasing output dir too early
 * d5ee2814: Restores now default to current time if restore time not specified
 * fa534a59: Added undocumended --collection-status option for testing purposes
 * 45e5f1af: More misc updates for 0.3.0
 * df130253: Few last minute tweaks to prepare for 0.3.0 release
 * 2554986d: Added --ssh-command and --scp-command options
 * 7e961b73: Fixed time-must-be-int bug with --short-filenames, added test
 * abbb2b9e: Various bugfixes so ftp backend passes final test
 * 7d93fb11: Added --short-filenames option
 * 654cd122: Added ftp backend support
 * 6900fd2d: Added man page entry for --file-to-restore option
 * 57a88d5b: Added statistics reporting after successful backup
 * 061b20b7: Added --list-current-files option
 * 67602c29: Make CVS more friendly; don't depend on src symlink
 * 7e3fe092: Updated documentation on new globbing options
 * 59c47178: Fixed bug & added test when root was reg file, not dir
 * ada51467: Added --include/exclude-globbing-filelist options
 * 2e2657c3: Fixed tar '..' security bug
 * 15fc588f: Added 2 test cases: neg mtimes, missing u/gnames
 * 2dd018b1: Fixed dumb st_time/st_mtime typo
 * 4003298b: Updated with new web page/mailing list information.
 * 917b2515: Added full GPL statement in source files at request of Jaime Villate of the Savannah site. Also updated address of FSF.
 * 9d03b092: Initial checkin
