import sys
import csv
from pathlib import Path
from typing import Any

def load_csv(file_name : Path) -> dict[str, list[str]]:
    '''
    Handles loading data from a csv file
    '''
    if file_name.is_file():
        with file_name.open("r") as file:
            reader = csv.DictReader(file)
            
            header : list[str] = list(next(reader).keys())
            
            data : dict[str, list[str]] = {name: [] for name in header}  
                    
            for line in reader:
                for name in header:
                    data[name].append(line[name])
    
            return data
    else:
        sys.exit("The path to the file is not right")
        
        
def main():
    load_csv("student.csv")
        
if __name__ == "__main__":
    main()