# -*- coding: utf-8 -*-
'''Unit tests for Google Spreadsheet access.'''

import os
from itertools import islice

from .. import googlesheet as gs

_CUR_PATH = os.path.dirname(os.path.abspath(__file__))


def test_get_spreadsheet():
    doc = gs.get_spreadsheet()
    assert doc.sheet1.title == 'new CMGs'


def test_get_params():
    params_list = list(islice(gs.get_params('test'), None))
    assert isinstance(params_list[0]['last_updated'], str)
    assert params_list[3]['searchstring'] == '[O-][Cr](=O)(=O)[O-].[Zn+2]'


def test_get_cmgs():
    cmgs = list(islice(gs.get_cmgs('test'), None))
    assert len(cmgs) == 4
    assert len(cmgs[0].materialid) == 5


def test_params_to_json():
    gs.params_to_json('test',
                      os.path.join(_CUR_PATH, 'group_params.json'))