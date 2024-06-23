import csv

input_file = 'day.csv'
output_file = 'output.csv'


with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = [row for row in reader]

for row in data:
    row.append('Processed')
    
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

print(f'Data has been written to {output_file}')
