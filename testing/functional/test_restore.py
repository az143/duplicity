# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf-8 -*-
#
# Copyright 2002 Ben Escoto
# Copyright 2007 Kenneth Loafman
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


import filecmp
import os
import unittest

from testing.functional import (
    _runtest_dir,
    FunctionalTestCase,
)


class RestoreTest(FunctionalTestCase):
    """
    Test restore optionss using duplicity binary.
    Basic restere is tested in other tests.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.restore_opts = [
            "restore",
            f"file://{_runtest_dir}/testfiles/output",
            f"{_runtest_dir}/testfiles/restore_test",
        ]

        self.restore_path_opts = self.restore_opts + [
            "--path-to-restore=deleted_file",
        ]

        self.restore_curdir_opts = [
            "restore",
            f"file://{_runtest_dir}/testfiles/output",
            f"./",
        ]

    def test_restore_to_nonexisting_dir(self):
        """
        Expected behaviour is restore to target directory.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        self.restore()
        self.assertEqual(
            sorted(os.listdir(f"{_runtest_dir}/testfiles/dir1")),
            sorted(os.listdir(f"{_runtest_dir}/testfiles/restore_out")),
        )

    def test_restore_path_to_nonexisting_dir(self):
        """
        Expected behaviour is restore to target directory.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        self.restore()
        self.assertTrue(
            filecmp.cmp(
                f"{_runtest_dir}/testfiles/dir1/deleted_file",
                f"{_runtest_dir}/testfiles/restore_out/deleted_file",
            )
        )

    def test_restore_to_nonempty_dir(self):
        """
        Expected behaviour is refuse to overwrite, CmdErr 11.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        os.mkdir(f"{_runtest_dir}/testfiles/restore_test")
        open(f"{_runtest_dir}/testfiles/restore_test/foobar", "w").write("foobar")
        try:
            self.run_duplicity(options=self.restore_opts)
        except Exception as e:
            if e.exit_status != 11:
                self.fail(f"Test failed with {e.exit_status}, not 11")
            else:
                pass
        else:
            self.fail(f"{__name__} passed and should have failed with 11.")

    def test_restore_path_to_nonempty_dir(self):
        """
        Expected behaviour is refuse to overwrite, CmdErr 11.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        os.mkdir(f"{_runtest_dir}/testfiles/restore_test")
        open(f"{_runtest_dir}/testfiles/restore_test/foobar", "w").write("foobar")
        try:
            self.run_duplicity(options=self.restore_path_opts)
        except Exception as e:
            if e.exit_status != 11:
                self.fail(f"Test failed with {e.exit_status}, not 11")
            else:
                pass
        else:
            self.fail(f"{__name__} passed and should have failed with 11.")

    def test_restore_to_curdir(self):
        """
        Expected behaviour is refuse to overwrite, CmdErr 11.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        os.mkdir(f"{_runtest_dir}/testfiles/restore_test")
        os.chdir(f"{_runtest_dir}/testfiles/restore_test")
        try:
            self.run_duplicity(options=self.restore_curdir_opts)
        except Exception as e:
            if e.exit_status != 11:
                self.fail(f"Test failed with {e.exit_status}, not 11")
            else:
                pass
        else:
            self.fail(f"{__name__} passed and should have failed with 11.")

    def test_restore_path_to_curdir(self):
        """
        Expected behaviour is refuse to overwrite, CmdErr 11.
        """
        self.backup("full", f"{_runtest_dir}/testfiles/dir1")
        os.mkdir(f"{_runtest_dir}/testfiles/restore_test")
        os.chdir(f"{_runtest_dir}/testfiles/restore_test")
        try:
            self.run_duplicity(options=self.restore_curdir_opts)
        except Exception as e:
            if e.exit_status != 11:
                self.fail(f"Test failed with {e.exit_status}, not 11")
            else:
                pass
        else:
            self.fail(f"{__name__} passed and should have failed with 11.")


if __name__ == "__main__":
    unittest.main()
