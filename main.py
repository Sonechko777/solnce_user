import csv

name_u='A'
with open('bank.csv') as csvfile:
    found = False
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        if name_u in row['name']:
            print('есть такое имя')
