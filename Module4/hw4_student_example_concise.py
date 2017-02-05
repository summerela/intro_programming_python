import csv

f = open('airports.dat', encoding='utf8')

reader = csv.reader(f, delimiter=',')

for row in reader:
    airport = row[3]
    if airport == 'Russia' or airport == 'Australia':
        print('Row #' + str(reader.line_num) + ' ' + str(row))


