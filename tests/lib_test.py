#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import from standard library
import os
import oppackage
import pandas as pd
# Import from our lib
from oppackage.lib import clean_data
from oppackage.lib import try_me
import pytest


# def test_clean_data():
#     datapath = os.path.dirname(os.path.abspath(oppackage.__file__)) + '/data'
#     df = pd.read_csv('{}/data.csv.gz'.format(datapath))
#     first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
#     assert list(df.columns)[:6] == first_cols
#     assert df.shape == (999, 142)
#     out = clean_data(df)
#     assert out.shape == (985, 119)

def test_try_me():
    assert try_me() == "OK"
