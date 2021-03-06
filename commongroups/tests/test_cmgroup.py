# -*- coding: utf-8 -*-
"""Unit tests for CMGroup class."""

import os
import shutil
from itertools import islice

from commongroups.env import CommonEnv
from commongroups import cmgroup as cmg

# Locate the test params to use.
_CUR_PATH = os.path.abspath(os.path.dirname(__file__))
PARAMS_JSON = os.path.join(_CUR_PATH, 'params.json')
PARAMS_LIST = cmg.params_from_json(PARAMS_JSON)

# This creates test environment directories on filesystem as a side effect.
env = CommonEnv('test')


# def test_cmgroup():
#     for params in PARAMS_LIST:
#         group = cmg.CMGroup(params, env)
#         assert group.materialid == params['materialid']
#         assert group.name == params['name']


# def test_params():
#     # Test saving parameters to file when starting a search.
#     group = cmg.CMGroup(PARAMS_LIST[0], env)
#     assert 'current_update' in group.params
#     group.init_pubchem_search()
#     params = group.get_params()
#     assert params['current_update'] is not None
#     # Test initialize new group with existing params file.
#     new_group = cmg.CMGroup(PARAMS_LIST[0], env)
#     new_params = new_group.params
#     assert new_params['current_update'] is not None


# def test_clear_data():
#     group = cmg.CMGroup(PARAMS_LIST[3], env)
#     shutil.copy(os.path.join(_CUR_PATH, 'cids.json'), group._cids_file)
#     shutil.copy(os.path.join(_CUR_PATH, 'cpds.jsonl'), group._compounds_file)
#     assert len(group.get_compounds()) == 3
#     assert len(group.get_returned_cids()) == 5
#     group.clear_data()
#     assert group.get_compounds() == []
#     assert group.get_returned_cids() == []


# def test_resume_update():
#     # Test initialize group with existing saved _cids_file (search results)
#     # and existing but incomplete _compounds_file (data/updates).
#     # Calling update_from_cids() should seamlessly resume the update.
#     group = cmg.CMGroup(PARAMS_LIST[3], env)
#     shutil.copy(os.path.join(_CUR_PATH, 'cids.json'), group._cids_file)
#     shutil.copy(os.path.join(_CUR_PATH, 'cpds.jsonl'), group._compounds_file)
#     group.update_from_cids()
#     assert len(group.get_compounds()) == 5

#     # Test what happens when _compounds_file contains CIDS that are
#     # not listed in the _cids_file. It should append compounds.
#     shutil.copy(os.path.join(_CUR_PATH, 'cpds_other.jsonl'),
#                 group._compounds_file)
#     group.update_from_cids()
#     assert len(group.get_compounds()) == 8

#     # Test what happens when _compounds_file is absent. In this case
#     # it should end up containing all the CIDs in _cids_file.
#     # group.clear_data()
#     # shutil.copy(os.path.join(_CUR_PATH, 'cids.json'), group._cids_file)
#     # group.update_from_cids()
#     # assert len(group.get_compounds()) == 5


# def test_pubchem_update():
#     group = cmg.CMGroup(PARAMS_LIST[0], env)
#     # To save time, only retrieve the first 5 CIDs.
#     # TODO: Ideally we should also test without any `listkey_count`,
#     # i.e. with a search that returns very few results.
#     group.pubchem_update(listkey_count=5)
#     assert len(group.get_compounds()) > 0


# def test_batch_cmg_search():
#     groups = list(islice(cmg.cmgs_from_json(PARAMS_JSON, env), None))

#     # To save time, only retrieve the first 3 CIDs.
#     cmg.batch_cmg_search(groups, wait=30, listkey_count=3)

#     for group in groups:
#         assert len(group.get_compounds()) > 0
#         assert group.get_compounds()[0]['IUPAC_name'] is not None
