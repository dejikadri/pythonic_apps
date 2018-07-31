import csv

from conf.config import INSURANCE_INPUT_FILE_CSV, INSURANCE_OUT_SORTED_FILE_CSV



"""
    Loads an insurance csv file and sorts by the policy number column using list and tuples
"""
try:
    with open(INSURANCE_INPUT_FILE_CSV) as file_insure:
        csv_reader = csv.reader(file_insure)

        # get the column  headers only
        reader = csv.DictReader(file_insure)
        fieldnames = reader.fieldnames

        # Skip Column headers
        next((csv_reader))

        data = [tuple(line) for line in csv_reader]
    data_sorted = sorted(data, key=lambda tp: tp[0])




    with open(INSURANCE_OUT_SORTED_FILE_CSV, 'w') as sorted_file:
        csv_out = csv.writer(sorted_file)
        csv_out.writerow(tuple(fieldnames))
        for row in data_sorted:
            csv_out.writerow(row)
    print('File processing done ...')
except Exception as err:
    print(f'something went wrong: {err}')