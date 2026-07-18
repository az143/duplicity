# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; coding:utf-8 -*-
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
import io
import os
import unittest

from testing.functional import (
    _runtest_dir,
    CmdError,
    FunctionalTestCase,
)
from duplicity import log


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

    def directory_tree_to_list_of_lists(self, parent_directory):
        directory_list = []
        for _root, dirs, files in os.walk(parent_directory):
            to_add = []
            if dirs:
                dirs.sort()
                to_add = dirs
            if files:
                files.sort()
                to_add += files
            if to_add:
                directory_list.append(to_add)
        return directory_list

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

    def test_restore_include_exclude_archive_relative(self):
        """
        Expected behaviour is restore filtering with archive-relative include/exclude patterns.
        """
        self.backup("full", "testfiles/select2")
        self.restore(
            options=[
                "--include",
                "1/1sub1/1sub1sub1/1sub1sub1_file.txt",
                "--exclude",
                "**",
            ]
        )
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertEqual(
            restored,
            [
                ["1"],
                ["1sub1"],
                ["1sub1sub1"],
                ["1sub1sub1_file.txt"],
            ],
        )

    def test_restore_include_accepts_leading_dot_slash(self):
        """
        Expected behaviour is restore filtering accepts a leading ./ on archive-relative patterns.
        """
        self.backup("full", "testfiles/select2")
        self.restore(
            options=[
                "--include",
                "./1/1sub1/1sub1sub1/1sub1sub1_file.txt",
                "--exclude",
                "**",
            ]
        )
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertEqual(
            restored,
            [
                ["1"],
                ["1sub1"],
                ["1sub1sub1"],
                ["1sub1sub1_file.txt"],
            ],
        )

    def test_restore_include_precedence_over_later_exclude(self):
        """
        Expected behaviour is first matching restore selection wins, matching backup selection precedence.
        """
        self.backup("full", "testfiles/select2")
        self.restore(
            options=[
                "--include",
                "3/3sub3/3sub3sub2/3sub3sub2_file.txt",
                "--exclude",
                "3",
                "--exclude",
                "**",
            ]
        )
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertEqual(
            restored,
            [
                ["3"],
                ["3sub3"],
                ["3sub3sub2"],
                ["3sub3sub2_file.txt"],
            ],
        )

    def test_restore_include_regexp_archive_relative(self):
        """
        Expected behaviour is restore filtering with archive-relative regular expressions.
        """
        self.backup("full", "testfiles/select2")
        self.restore(options=["--include-regexp", r"1\.py$", "--exclude", "**"])
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertEqual(restored, [["1.py"]])

    def test_restore_exclude_prunes_archive_relative_subtree(self):
        """
        Expected behaviour is an excluded restore directory prevents restoring descendants by default.
        """
        self.backup("full", "testfiles/select2")
        self.restore(options=["--exclude", "1"])
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertNotIn("1", restored[0])
        self.assertIn("2", restored[0])
        self.assertIn("3", restored[0])

    def test_restore_include_filelist_archive_relative(self):
        """
        Expected behaviour is restore filtering with archive-relative include filelists.
        """
        with io.open("testfiles/restore-include.txt", "w") as f:
            f.write("1/1sub1/1sub1sub1/1sub1sub1_file.txt\n")
        self.backup("full", "testfiles/select2")
        self.restore(options=["--include-filelist", "testfiles/restore-include.txt", "--exclude", "**"])
        restored = self.directory_tree_to_list_of_lists("testfiles/restore_out")
        self.assertEqual(
            restored,
            [
                ["1"],
                ["1sub1"],
                ["1sub1sub1"],
                ["1sub1sub1_file.txt"],
            ],
        )

    def test_restore_path_to_restore_excludes_selection_options(self):
        """
        Expected behaviour is --path-to-restore cannot be mixed with restore include/exclude filtering.
        """
        self.backup("full", "testfiles/select2")
        with self.assertRaises(CmdError) as context:
            self.restore(file_to_restore="1", options=["--include", "1/**", "--exclude", "**"])
        self.assertEqual(context.exception.exit_status, log.ErrorCode.user_error)

    def test_restore_rejects_unsupported_selection_options(self):
        """
        Expected behaviour is restore rejects selection options that require live filesystem semantics.
        """
        self.backup("full", "testfiles/select2")
        with self.assertRaises(CmdError) as context:
            self.restore(options=["--exclude-if-present", "marker"])
        self.assertEqual(context.exception.exit_status, log.ErrorCode.user_error)

    def test_restore_rejects_invalid_archive_relative_patterns(self):
        """
        Expected behaviour is restore rejects absolute and non-canonical archive-relative path patterns.
        """
        self.backup("full", "testfiles/select2")
        invalid_patterns = ["/1", "../1", "1/../1sub1", "1/./1sub1"]
        for pattern in invalid_patterns:
            with self.subTest(pattern=pattern):
                with self.assertRaises(CmdError) as context:
                    self.restore(options=["--include", pattern, "--exclude", "**"])
                self.assertEqual(context.exception.exit_status, log.ErrorCode.file_prefix_error)


if __name__ == "__main__":
    unittest.main()
