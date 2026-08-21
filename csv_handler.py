import csv

def load_csv(file_name : str) -> dict:
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        
        header = list(next(reader).keys())
        
        data = {name: [] for name in header}  
                
        for line in reader:
            for name in header:
                data[name].append(line[name])

        return data
        
        
def main():
    load_csv("student.csv")
        
if __name__ == "__main__":
    main()