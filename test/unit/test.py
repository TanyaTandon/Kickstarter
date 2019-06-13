import pandas as pd
import numpy as np
import sys
import os
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from src.load_data import run_loading
from src.model import create_db
from src.clean import drop_col, drop_na


test_case1 = pd.DataFrame({'A': [1, 2, 3], 'B': [ 4,5, 6], 'C': [ 7,8, 9]})
test_case2 = pd.DataFrame({'A': [1, 2, 3,None ], 'B': [ 4, None  , 5, 6], 'C': [ 7, None  ,  8, 9]})

check_case1 = pd.DataFrame({'A': [1, 2, 3]})
check_case2 = pd.DataFrame({'A': [1, 3], 'B': [ 4, 5], 'C': [7, 8]})

config = { 'delete_columns': [ 'B', 'C']}

def test_drop_col():
    """Test the functionality of drop coloumns."""
    # load sample test data
    print(drop_col(config, test_case1))
    assert (drop_col(config, test_case1) != check_case1).sum().sum() == 0 

# def test_for_na():
#      assert (drop_na( test_case2) != check_case2).sum().sum() == 0 
