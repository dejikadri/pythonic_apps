import csv


"""
    Load a csv file and sort by a column using list and tuples
"""

with open('FL_insurance_sample.csv') as file_insure:
    csv_reader = csv.reader(file_insure)

    # get the column  headers only
    reader = csv.DictReader(file_insure)
    fieldnames = reader.fieldnames

    # Skip Column headers
    next((csv_reader))

    data = [tuple(line) for line in csv_reader]

data_sorted = sorted(data, key = lambda tp: tp[0] )
with open('sorted.csv', 'w') as sorted_file:
    csv_out = csv.writer(sorted_file)
    csv_out.writerow(tuple(fieldnames))
    for row in data_sorted:
        csv_out.writerow(row)
        #print(row)
print(tuple(fieldnames))