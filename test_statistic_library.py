import pytest
from statistic_library import *
import math


def test_conver_to_int():
    assert conver_column_to_int(["1","2","3","5"]) == [1,2,3,5]
    assert conver_column_to_int(["0","6","2","4"]) == [0,6,2,4]
    
def test_convert_to_int_errors():
    with pytest.raises(ValueError):
        conver_column_to_int(["1", "3", "5", "2", "0.1"])
        conver_column_to_int([0.5])
    with pytest.raises(ValueError):
        conver_column_to_int(["str"])
        
def test_mean():
    assert mean([1,2,3,4,5]) == 3
    assert mean([1,2,3,4,5,6]) == 3.5
    

def test_median():
    assert median([1,2,3,4,5]) == 3
    assert median([1,2,3,4,5,6]) == 3.5
    
def test_mode():
    assert mode([1,2,2,4,5,4,2]) == [2]
    assert mode([5,2,7,3,2,5,6,5,5]) == [5]
    assert mode([5,2,7,3,2,5,6,2,5,5,2]) == [5,2]
    
def test_standart_deviation():
    assert standard_deviation([10, 12, 14, 16, 18]) == pytest.approx(2.83, abs = 0.1)
    assert standard_deviation([4, 7, 10, 13, 16, 19]) == pytest.approx(5.12, abs = 0.1)

def test_min():
    assert min([2,4,5,6,8,0]) == 0
    assert min([6,4,10,83,4,3]) == 3
    
    
def test_max():
    assert max([2,4,5,6,8,0]) == 8
    assert max([6,4,10,83,4,3]) == 83
    
def test_frequency():
    assert frequency([2,2,4,5,2,4,1]) == {1: 1, 2: 3, 4: 2, 5: 1}
    assert frequency([3,3,4,5,2,1,1,1]) == {1: 3, 2: 1,3:2, 4: 1, 5: 1}
    
    
def test_corelation():
    assert correlation([1, 2, 3, 4, 5],[2, 3, 5, 4, 7]) == pytest.approx(0.89, abs=0.02)
    assert correlation([2, 5, 8, 11, 15],[7, 4, 13, 9, 18]) == pytest.approx(0.79, abs=0.02)

def test_corelation_error():
    with pytest.raises(ValueError):
        correlation([5, 5, 5, 5, 5],[2, 3, 5, 4, 7])


def test_normalize():
    assert normalize([10, 20, 30, 40, 50]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert normalize([5, 15, 25, 40, 60]) == [0.0, 0.1818, 0.3636, 0.6364, 1.0]