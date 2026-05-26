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


import random
import re
import unittest

import pytest

from duplicity import backend
from duplicity import config
from duplicity import dup_collections
from duplicity import dup_time
from duplicity import file_naming
from duplicity import gpg
from duplicity import manifest
from duplicity import path
from testing import _runtest_dir
from . import UnitTestCase

filename_list1 = [
    b"duplicity-full.2002-08-17T16:17:01-07:00.manifest.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol1.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol2.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol3.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol4.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol5.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol6.difftar.gpg",
    b"duplicity-inc.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.manifest.gpg",
    b"duplicity-inc.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.vol1.difftar.gpg",
    b"Extra stuff to be ignored",
]

remote_sigchain_filename_list = [
    b"duplicity-full-signatures.2002-08-17T16:17:01-07:00.sigtar.gpg",
    b"duplicity-new-signatures.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.sigtar.gpg",
    b"duplicity-new-signatures.2002-08-18T00:04:30-07:00.to.2002-08-20T00:00:00-07:00.sigtar.gpg",
]
remote_sigchain_filename_list2 = [
    b"duplicity-full-signatures.2003-08-17T16:17:01-07:00.sigtar.gpg",
]

local_sigchain_filename_list = [
    b"duplicity-full-signatures.2002-08-17T16:17:01-07:00.sigtar.gz",
    b"duplicity-new-signatures.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.sigtar.gz",
    b"duplicity-new-signatures.2002-08-18T00:04:30-07:00.to.2002-08-20T00:00:00-07:00.sigtar.gz",
]

# A filename list with some incomplete volumes, an older full volume,
# and a complete chain.
filename_list2 = [
    b"duplicity-full.2001-01-01T16:17:01-07:00.manifest.gpg",
    b"duplicity-full.2001-01-01T16:17:01-07:00.vol1.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.manifest.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol1.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol2.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol3.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol4.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol5.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol6.difftar.gpg",
    b"duplicity-inc.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.manifest.gpg",
    b"duplicity-inc.2002-08-17T16:17:01-07:00.to.2002-08-18T00:04:30-07:00.vol1.difftar.gpg",
    b"The following are extraneous duplicity files",
    b"duplicity-new-signatures.2001-08-17T02:05:13-05:00.to.2002-08-17T05:05:14-05:00.sigtar.gpg",
    b"duplicity-full.2002-08-15T01:01:01-07:00.vol1.difftar.gpg",
    b"duplicity-inc.2000-08-17T16:17:01-07:00.to.2000-08-18T00:04:30-07:00.manifest.gpg",
    b"duplicity-inc.2000-08-17T16:17:01-07:00.to.2000-08-18T00:04:30-07:00.vol1.difftar.gpg",
    b"Extra stuff to be ignored",
]

filename_list3 = [
    b"duplicity-full.2002-08-17T16:17:01-07:00.manifest.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol1.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol2.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol3.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol4.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol5.difftar.gpg",
    b"duplicity-full.2002-08-17T16:17:01-07:00.vol6.difftar.gpg",
]

remove_older_than = [
    b"duplicity-full.20251003T104900Z.vol1.difftar.gz",
    b"duplicity-full.20251003T104922Z.vol1.difftar.gz",
    b"duplicity-full-signatures.20251003T104900Z.sigtar.gz",
    b"duplicity-full-signatures.20251003T104922Z.sigtar.gz",
    b"duplicity-full.20251003T104900Z.manifest",
    b"duplicity-full.20251003T104922Z.manifest",
]

partial_filename_list = []


@pytest.fixture
def mock_manifest(monkeypatch):
    """
    Monkeypatch dup_collections to return partial manifest
    """

    def partial_manifest(*args, **kwargs):
        """
        Make a partial manifest from partial_filename_list
        """
        mf = manifest.Manifest()
        for fn in filename_list3:
            pr = file_naming.parse(fn)
            if pr.type == "full" and pr.volume_number:
                vi = manifest.VolumeInfo()
                vi.set_info(pr.volume_number, None, None, None, None)
                mf.add_volume_info(vi)
        return mf

    monkeypatch.setattr(dup_collections.BackupSet, "get_manifest", partial_manifest)


class CollectionTest(UnitTestCase):
    """Test collections"""

    def setUp(self):
        super().setUp()

        self.unpack_testfiles()

        col_test_dir = path.Path(f"{_runtest_dir}/testfiles/collectionstest")
        archive_dir_path = col_test_dir.append("archive_dir")
        self.set_config("archive_dir_path", archive_dir_path)
        self.archive_dir_backend = backend.get_backend(f"file://{_runtest_dir}/testfiles/collectionstest/archive_dir")
        self.real_backend = backend.get_backend(f"file://{col_test_dir.uc_name}/remote_dir")
        self.output_dir = path.Path(f"{_runtest_dir}/testfiles/output")  # used as a temp directory
        self.output_dir_backend = backend.get_backend(f"file://{_runtest_dir}/testfiles/output")

    def set_gpg_profile(self):
        """Set gpg profile to standard "foobar" sym"""
        self.set_config("gpg_profile", gpg.GPGProfile(passphrase="foobar"))

    def test_backup_chains(self):
        """Test basic backup chain construction"""
        random.shuffle(filename_list1)
        cs = dup_collections.CollectionsStatus(None, config.archive_dir_path)
        chains, orphaned, incomplete, missing_difftar_sets = cs.get_backup_chains(filename_list1)
        if len(chains) != 1 or len(orphaned) != 0:
            print(chains)
            print(orphaned)
            assert 0

        chain = chains[0]
        assert chain.end_time == 1029654270
        assert chain.fullset.time == 1029626221

    def test_collections_status(self):
        """Test CollectionsStatus object's set_values()"""

        def check_cs(cs):
            """Check values of collections status"""
            assert cs.values_set

            assert cs.matched_chain_pair
            assert cs.matched_chain_pair[0].end_time == 1029826800
            assert len(cs.all_backup_chains) == 1, cs.all_backup_chains

        cs = dup_collections.CollectionsStatus(self.real_backend, config.archive_dir_path).set_values()
        check_cs(cs)
        assert cs.matched_chain_pair[0].islocal()

    def test_sig_chain(self):
        """Test a single signature chain"""
        chain = dup_collections.SignatureChain(1, config.archive_dir_path)
        for filename in local_sigchain_filename_list:
            assert chain.add_filename(filename)
        assert not chain.add_filename(
            b"duplicity-new-signatures.2002-08-18T00:04:30-07:00.to.2002-08-20T00:00:00-07:00.sigtar.gpg"
        )

    def test_sig_chains(self):
        """Test making signature chains from filename list"""
        cs = dup_collections.CollectionsStatus(None, config.archive_dir_path)
        chains, orphaned_paths = cs.get_signature_chains(local=1)
        self.sig_chains_helper(chains, orphaned_paths)

    def test_sig_chains2(self):
        """Test making signature chains from filename list on backend"""
        cs = dup_collections.CollectionsStatus(self.archive_dir_backend, config.archive_dir_path)
        chains, orphaned_paths = cs.get_signature_chains(local=None)
        self.sig_chains_helper(chains, orphaned_paths)

    def sig_chains_helper(self, chains, orphaned_paths):
        """Test chains and orphaned_paths values for two above tests"""
        if orphaned_paths:
            for op in orphaned_paths:
                print(op)
            assert 0
        assert len(chains) == 1, chains
        assert chains[0].end_time == 1029826800

    def sigchain_fileobj_get(self, local):
        """Return chain, local if local is true with filenames added"""
        if local:
            chain = dup_collections.SignatureChain(1, config.archive_dir_path)
            for filename in local_sigchain_filename_list:
                assert chain.add_filename(filename)
        else:
            chain = dup_collections.SignatureChain(None, self.real_backend)
            for filename in remote_sigchain_filename_list:
                assert chain.add_filename(filename)
        return chain

    def sigchain_fileobj_check_list(self, chain):
        """Make sure the list of file objects in chain has right contents

        The contents of the /tmp/testfiles/collectiontest/remote_dir have
        to be coordinated with this test.

        """
        fileobjlist = chain.get_fileobjs()
        assert len(fileobjlist) == 3

        def test_fileobj(i, s):
            buf = fileobjlist[i].read()
            fileobjlist[i].close()
            assert buf == s, (buf, s)

        test_fileobj(0, b"Hello, world!")
        test_fileobj(1, b"hello 1")
        test_fileobj(2, b"Hello 2")

    @pytest.mark.usefixtures("redirect_stdin")
    def test_sigchain_fileobj(self):
        """Test getting signature chain fileobjs from archive_dir_path"""
        self.set_gpg_profile()
        self.sigchain_fileobj_check_list(self.sigchain_fileobj_get(1))
        self.sigchain_fileobj_check_list(self.sigchain_fileobj_get(None))

    def get_filelist_cs(self, filelist, fill_archive=False):
        """
        Return set CollectionsStatus object from filelist
        """
        # Set up /tmp/testfiles/output with files from filelist

        for filename in self.output_dir.listdir():
            self.output_dir.append(filename).delete()
        for filename in filelist:
            p = self.output_dir.append(filename)
            p.touch()

        if fill_archive:
            for filename in config.archive_dir_path.listdir():
                config.archive_dir_path.append(filename).delete()
            for filename in filelist:
                if b"vol" in filename:
                    # don't add volumes to archive/cache
                    continue
                p = config.archive_dir_path.append(filename)
                p.touch()

        cs = dup_collections.CollectionsStatus(self.output_dir_backend, config.archive_dir_path)
        cs.set_values()
        return cs

    def test_get_extraneous(self):
        """
        Test the listing of extraneous files
        """
        cs = self.get_filelist_cs(filename_list2)
        assert len(cs.orphaned_backup_sets) == 1, cs.orphaned_backup_sets
        assert len(cs.local_orphaned_sig_names) == 0, cs.local_orphaned_sig_names
        assert len(cs.remote_orphaned_sig_names) == 1, cs.remote_orphaned_sig_names
        assert len(cs.incomplete_backup_sets) == 1, cs.incomplete_backup_sets

        right_list = [
            b"duplicity-new-signatures.2001-08-17T02:05:13-05:00.to.2002-08-17T05:05:14-05:00.sigtar.gpg",
            b"duplicity-full.2002-08-15T01:01:01-07:00.vol1.difftar.gpg",
            b"duplicity-inc.2000-08-17T16:17:01-07:00.to.2000-08-18T00:04:30-07:00.manifest.gpg",
            b"duplicity-inc.2000-08-17T16:17:01-07:00.to.2000-08-18T00:04:30-07:00.vol1.difftar.gpg",
        ]
        local_received_list, remote_received_list = cs.get_extraneous()
        errors = []
        for filename in remote_received_list:
            if filename not in right_list:
                errors.append("### Got bad extraneous filename " + filename.decode())
            else:
                right_list.remove(filename)
        for filename in right_list:
            errors.append("### Didn't receive extraneous filename " + filename)
        assert not errors, "\n" + "\n".join(errors)

    def test_get_olderthan(self):
        """
        Test getting list of files older than a certain time
        """
        cs = self.get_filelist_cs(filename_list2)
        oldsets = cs.get_older_than(dup_time.genstrtotime("2002-05-01T16:17:01-07:00"))
        oldset_times = [s.get_time() for s in oldsets]
        right_times = [dup_time.genstrtotime("2001-01-01T16:17:01-07:00")]
        assert oldset_times == right_times, [oldset_times, right_times]

        oldsets_required = cs.get_older_than_required(dup_time.genstrtotime("2002-08-17T20:00:00-07:00"))
        oldset_times = [s.get_time() for s in oldsets_required]
        right_times_required = [dup_time.genstrtotime("2002-08-17T16:17:01-07:00")]
        assert oldset_times == right_times_required, [
            oldset_times,
            right_times_required,
        ]

    def test_get_olderthan_signatures(self):
        cs = self.get_filelist_cs(remove_older_than, fill_archive=True)
        first_backup_ts = dup_time.genstrtotime("2025-10-03T10:49:00")
        second_backup_ts = dup_time.genstrtotime("2025-10-03T10:49:22")
        newer_than_last_ts = dup_time.genstrtotime("2025-10-03T10:59:59")

        # no older backups
        oldsets = cs.get_signature_chains_older_than(first_backup_ts)
        assert len(oldsets) == 0

        # don't return signatures from latest backup
        oldsets = cs.get_signature_chains_older_than(newer_than_last_ts)
        assert len(oldsets) == 2, f"Expected 2 sets, got {len(oldsets)}"  # local and remote sig
        assert all(
            x.end_time == first_backup_ts for x in oldsets
        ), f"Wrong sets, timestam doesn't match {first_backup_ts}"
        assert len([x for x in oldsets if x.islocal() is True]) == 1, "There should be one local and one remote set"

    @pytest.mark.usefixtures("mock_manifest")
    def test_missing_first_volume(self):
        """
        Test missing first volume
        """
        global partial_filename_list
        partial_filename_list = [f for f in filename_list3 if not re.search(b"full.*vol1", f)]
        cs = self.get_filelist_cs(partial_filename_list)
        assert len(cs.orphaned_backup_sets) == 0, cs.orphaned_backup_sets
        assert len(cs.local_orphaned_sig_names) == 0, cs.local_orphaned_sig_names
        assert len(cs.remote_orphaned_sig_names) == 0, cs.remote_orphaned_sig_names
        assert len(cs.incomplete_backup_sets) == 0, cs.incomplete_backup_sets
        assert cs.missing_difftar_sets[0].cs_missing == {1}

    @pytest.mark.usefixtures("mock_manifest")
    def test_missing_middle_volume(self):
        """
        Test missing last volume
        """
        global partial_filename_list
        partial_filename_list = [f for f in filename_list3 if not re.search(b"full.*vol3", f)]
        cs = self.get_filelist_cs(partial_filename_list)
        assert len(cs.orphaned_backup_sets) == 0, cs.orphaned_backup_sets
        assert len(cs.local_orphaned_sig_names) == 0, cs.local_orphaned_sig_names
        assert len(cs.remote_orphaned_sig_names) == 0, cs.remote_orphaned_sig_names
        assert len(cs.incomplete_backup_sets) == 0, cs.incomplete_backup_sets
        assert cs.missing_difftar_sets[0].cs_missing == {3}

    @pytest.mark.usefixtures("mock_manifest")
    def test_missing_last_volume(self):
        """
        Test missing last volume
        """
        global partial_filename_list
        partial_filename_list = [f for f in filename_list3 if not re.search(b"full.*vol6", f)]
        cs = self.get_filelist_cs(partial_filename_list)
        assert len(cs.orphaned_backup_sets) == 0, cs.orphaned_backup_sets
        assert len(cs.local_orphaned_sig_names) == 0, cs.local_orphaned_sig_names
        assert len(cs.remote_orphaned_sig_names) == 0, cs.remote_orphaned_sig_names
        assert len(cs.incomplete_backup_sets) == 0, cs.incomplete_backup_sets
        assert cs.missing_difftar_sets[0].cs_missing == {6}

    @pytest.mark.usefixtures("mock_manifest")
    def test_missing_multi_volume(self):
        """
        Test missing last volume
        """
        global partial_filename_list
        partial_filename_list = [f for f in filename_list3 if not re.search(b"full.*vol[35]", f)]
        cs = self.get_filelist_cs(partial_filename_list)
        assert len(cs.orphaned_backup_sets) == 0, cs.orphaned_backup_sets
        assert len(cs.local_orphaned_sig_names) == 0, cs.local_orphaned_sig_names
        assert len(cs.remote_orphaned_sig_names) == 0, cs.remote_orphaned_sig_names
        assert len(cs.incomplete_backup_sets) == 0, cs.incomplete_backup_sets
        assert cs.missing_difftar_sets[0].cs_missing == {3, 5}


if __name__ == "__main__":
    unittest.main()
