import csv

file_path = 'day.csv'


with open(file_path, mode='r') as file:
    
    reader = csv.reader(file)
    
    for row in reader:
        
        print(row)
