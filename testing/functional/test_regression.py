# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf-8 -*-
#
# Copyright 2025 Kenneth Loafman
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


import os
import re
import shutil
import sys
import unittest

from testing.functional import (
    _runtest_dir,
    FunctionalTestCase,
)


class RegressionTest(FunctionalTestCase):
    """
    Test regression issues
    """

    def test_issue888(self):
        """
        Test issue 888 - collection_status --file-changed="foo bar" fails with type error
        """
        filenames = ["foo", "bar", "foo bar"]
        os.mkdir(f"{_runtest_dir}/testfiles/issue888")
        for filename in filenames:
            open(f"{_runtest_dir}/testfiles/issue888/{filename}", "w").write(f"{filename}")

        self.backup(
            "full",
            f"{_runtest_dir}/testfiles/issue888",
            options=["--no-encrypt", "--no-compress"],
        )

        self.run_duplicity(
            options=[
                "list-current-files",
                f"file://{_runtest_dir}/testfiles/output",
                f"--log-file={_runtest_dir}/testfiles/issue888/testing.out",
            ]
        )
        txt = open(f"{_runtest_dir}/testfiles/issue888/testing.out").read()
        print(txt, file=sys.stderr)
        for filename in filenames:
            self.assertRegex(
                txt,
                rf". .* {filename}\n",
                f"filename {filename} not found in list-current-files output",
            )

        for filename in filenames:
            self.run_duplicity(
                options=[
                    "collection-status",
                    f"file://{_runtest_dir}/testfiles/output",
                    "--file-changed",
                    filename,
                    f"--log-file={_runtest_dir}/testfiles/issue888/testing.out",
                ],
            )
            txt = open(f"{_runtest_dir}/testfiles/issue888/testing.out").read()
            print(txt, file=sys.stderr)
            patt = re.compile(rf".\s+File: b'{filename}'\n")
            self.assertRegex(
                txt,
                patt,
                f"filename {filename} not found in collection-status output",
            )

    def test_issue901(self):
        """
        Test issue 901 - Upgrade to 3.0.6 on Archlinux gives gcry_kdf_derive failed
        """
        self.set_environ("SIGN_PASSPHRASE", None)
        self.set_environ("FTP_PASSWORD", None)

        # self.set_environ("TESTDEBUG", "1")
        self.set_environ("PASSPHRASE", "issue901")

        # make sure we test with a clean cache and clean output
        shutil.rmtree(f"{_runtest_dir}/testfiles/cache/issue901", ignore_errors=True)
        shutil.rmtree(f"{_runtest_dir}/testfiles/output", ignore_errors=True)

        # do initial full backup
        self.backup(
            "full",
            f"{_runtest_dir}/testfiles/various_file_types",
            options=["--name=issue901"],
        )

        # make sure inc has somthing to do
        os.unlink(f"{_runtest_dir}/testfiles/various_file_types/executable")

        # do incremental backup
        self.backup(
            "inc",
            f"{_runtest_dir}/testfiles/various_file_types",
            options=["--name=issue901"],
        )

        # list current files
        self.run_duplicity(
            options=[
                "list-current-files",
                f"file://{_runtest_dir}/testfiles/output",
                "--name=issue901",
            ]
        )


if __name__ == "__main__":
    unittest.main()
