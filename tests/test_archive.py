"""
.. module:: test_archive.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document archive tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import nose
import os

import pyesdoc
import test_utils as tu


def _test_archive_config():
    """Test archive configuration."""
    import pyesdoc.archive.config as cfg

    tu.assert_path(cfg.DIR_ARCHIVE)
    tu.assert_int(cfg.projects, 3)
    tu.assert_int(cfg.sources, 3)
    tu.assert_int(cfg.projects[0].feeds, 5)
    tu.assert_int(cfg.projects[1].feeds, 1)
    tu.assert_int(cfg.projects[2].feeds, 1)
    tu.assert_int(cfg.get_project_sources(), 4)


def _test_archive_doc_dirs():
    """Test archive document directories."""
    import pyesdoc.archive.config as cfg
    import pyesdoc.archive.io as io

    for project, source in cfg.get_project_sources():
        for sub_dir in io.SUB_DIRECTORIES:
            doc_dir = io.get_folder(project, source, sub_dir)
            assert os.path.exists(doc_dir), doc_dir


def _test_archive_get_counts():
    """Test archive document counts."""
    import pyesdoc.archive.io as io

    tu.assert_int(len(io.get_counts()), 20)


def test():
    """Runs set of archive unit tests."""
    for func in (
        _test_archive_config,
        _test_archive_doc_dirs,
        _test_archive_get_counts
        ):
        tu.init(func, func.__doc__[5:])
        yield func