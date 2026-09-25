import sys
from statistic_library import *
import csv_handler
import time
from typing import Never
from pathlib import Path


def main() -> Never:
    '''
    Error handling if not all arguments was provieded or to much arguments.
    Calls menu if all arguments were provided
    '''
    
    if (len(sys.argv) < 2):
        sys.exit("Too few arguments. Add .csv file name")
    elif (len(sys.argv) > 2):
        sys.exit("Too many arguments.")
    else:
        menu(sys.argv[1])

def menu(file_name : str) -> Never:
    
    '''
    Handles console menu and waits for user to choose menu field
    And then sends it to do_operation function.
    '''
    
    
    data : dict[str, list[str]] = csv_handler.load_csv(Path(file_name))
    
    menu_fields : dict[str,int]= {
        "Mean" : 1,
        "Median" : 2,
        "Mode" : 3,
        "Standart deviation" : 4,
        "Min/Max": 5,
        "Frequency" : 6,
        "Corelation" : 7,
        "Normalize" : 8,
        "Show Dataset" : 9,
        "Exit" : 0
    }
    
    while True:
        print("="*18 + "\n" "MINI DATA ANALYZER" + "\n" + "="*18)
        
        print("\nDataset: " + file_name)
        print("Rows: " + f"{len(next(iter(data.values())))}")
        print("Columns: " + f"{len(data.keys())}")
        print("\nChoose  operation:\n")
        
        for key in menu_fields.keys():
            print(f"{menu_fields[key]}. " + f"{key}")
        
        try:    
            choice = int(input("\nChoice: "))
            do_operation(choice, data)
            input("Press enter to continue")
        except ValueError:
            print("Wrong input.")
            time.sleep(2)
            continue
        

def do_operation(choice : int, data : dict[str, list[str]]) -> None:
    
    '''
    Dooes choosen operation by calling
    function from static_library.py and
    prints result.
    '''
    
    
    if choice == 0:
        sys.exit()
        
    elif choice == 9:
        print(f"{show_dataset(data)}")
        return
    
    
    column  = choose_column(data)
    
    
    match choice:
        case 1:
            print(f"Mean value: {mean(data[column]):.2f}")
            
        case 2:
            print(f"Median value: {median(data[column])}")
            
        case 3:
            print(f"Mode value(s): {",".join(mode(data[column]))}")
            
        case 4:
            print(f"Standart deviation value: {standard_deviation(data[column]):.2f}")
            
        case 5:
            choise_min_max(data, column)
                
        case 6:
            print("Frequence value:")
            frequencies = frequency(column)
            for key, value in frequencies.items():
                print(f"{key} : {value:.2f}")
            
        case 7:
            print("Choose second colum")
            
            second_column = choose_column(data)
            
            print(f"Correlation columns: {correlation(data[column], data[second_column])}")
        
        case 8:
            print(f"Normalized column: {normalize(data[column])}")
        
        case _:
            print("Unknown operation.")
            
def choise_min_max(data : dict[str, list[str]], column : str):
    
    '''
    Choosing operation max or min and prints result of the operation.
    ''' 
    
    choise = input("Min/Max? ")
            
    if choise.lower() == "min":
        print(f"Min value: {minimum(data[column])}")
        
    elif choise.lower() == "max":
        print(f"Max value: {maximum(data[column])}")
        
    else:
        print("Choose min or max!")
        choise_min_max(data, column)

    
def choose_column(data : dict[str, list[str]]) -> str:
    '''
    Writes columns name and waits on user to choose one.
    '''
    
    for i ,key in enumerate(data.keys()):
        print(f"{i+1}. {key}")
    
    try:
        while True:
            choice = int(input("\nChoice(number): "))
            if choice <= len(data.keys()) and choice > 0:
                return list(data.keys())[choice-1]
            else:
                print("Wrong column number!")
                time.sleep(2)
                continue
    except ValueError:
        sys.exit("Wrong value")

if __name__ == "__main__":
    main()
