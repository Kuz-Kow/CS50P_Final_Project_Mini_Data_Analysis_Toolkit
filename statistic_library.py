import sys
import math
import tabulate
from typing import Sequence, Any

type Column = Sequence[str]


def conver_column_to_int(column: Column) -> list[int]:
    
    '''
    Converting values of a column to int.
    '''
    
    
    try:
        int_column = [int(value) for value in column]
    
    except ValueError:
            raise ValueError("Wrong Value in column")
            
    return int_column

def mean(column : Column) -> float :
    
    '''
    Get's a column and calculates mean value.
    '''
    
    sum_column= 0
    
    int_column = conver_column_to_int(column)
        
    sum_column = sum(int_column)
    
    return sum_column / len(column)
    

def median(column : Column) -> float:
    
    '''
    Get's a column and calculates median value for the column.
    '''
    
    
    int_column = conver_column_to_int(column)
    
    int_column = sorted(int_column)
    
    return (int_column[len(column)//2 -1] + int_column[(len(column)//2)])/2 if len(column)%2 == 0 else int_column[(len(column)//2)]

def mode(column : Column) -> Column:
    
    '''
    Find's mode value(s) in the column.
    '''
    
    
    apperences : dict[str, int]= {}
    
    max_count : int = 0
    
    for value in column:
        if value in apperences:
            apperences[value] += 1
        else:
            apperences[value] = 1
        
        
    for _ , count in apperences.items():
        if int(value) > max_count:
            max_count = int(value)
    
    return [value for value in apperences.keys() if apperences[value] == max_count]

def standard_deviation(column : Column) -> float:
    
    '''
    Calculates standart deviation of a column
    '''
    
    
    int_column = conver_column_to_int(column)
    
    mean_value = mean(column)
    
    return math.sqrt(sum([(value - mean_value)**2 for value in int_column])/ len(int_column))

def minimum(column : Column) -> float:
    
    '''
    Finds minimum value at the column
    '''
    
    
    int_column = conver_column_to_int(column)
    
    min_value = int_column[0]
        
    for value in int_column:
        if min_value > value:
            min_value = value
        
    return min_value

def maximum(column : Column) -> float:
    
    '''
    Finds maximum value at the column
    '''
    
    
    int_column = conver_column_to_int(column)
        
    max_value = int_column[0]
        
    for value in int_column:
        if max_value < value:
            max_value = value
        
    return max_value

def frequency(column:Column) -> dict[str, int]:
    
    '''
    Calculates frequency of values in a column
    '''
    
    
    apperences :dict[str, int] = {}
        
    for value in column:
        if value in apperences.keys():
            apperences[value] = apperences[value] + 1
        else:
            apperences[value] = 1
    
    return apperences

def correlation(first_column : Column, second_column: Column)-> float:
    
    '''
    Calculates correlation of two columns values
    '''
    
    
    int_first_column = conver_column_to_int(first_column)
    
    int_second_column = conver_column_to_int(second_column)
    
    multiplied_columns = map(lambda value_1, value_2: value_1 * value_2, int_first_column, int_second_column)
    
    if min(first_column) == max(first_column):
        raise ValueError("Correlation is undefined for constant rows")
    
    elif min(second_column) == max(second_column):
            raise ValueError("Correlation is undefined for constant rows")
    
    if len(first_column) == len(second_column):
        correlation_value = (len(first_column) * sum(multiplied_columns) - (sum(int_first_column) * sum(int_second_column)))/math.sqrt((len(first_column) * sum([value**2 for value in int_first_column]) - sum(int_first_column)**2) * (len(int_first_column)* sum([value**2 for value in int_second_column]) - sum(int_second_column)**2))
        return round(correlation_value,3)
    
    else:
        raise ValueError("columns have different length")
    
def normalize(column: Column) -> list[float]:
    
    '''
    Normalizes values un the column
    '''
    
    
    int_column = conver_column_to_int(column)
    
    max_value = max(int_column)
    
    min_value = min(int_column)
    
    if max_value == min_value:
      raise ValueError("Cannot normalize a constant row")
    
    def normalize(value):
        normalized_value = (value - min_value)/(max_value - min_value)
        return round(normalized_value, 4)         
    
    return [normalize(value) for value in int_column]
    
def show_dataset(dictionary: dict[str, Any]) -> str: 
    
    '''
    Returns dataset formated by tabulate
    '''
    
    
    return tabulate.tabulate(dictionary, headers = "keys", tablefmt="grid")