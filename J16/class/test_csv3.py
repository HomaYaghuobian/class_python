import csv

with open ('J16\class\class.csv','r') as csv_file:
    csv_readerr = csv.reader(csv_file)    # اشاره گر 

    fields = next(csv_file)
    rows = []
    for row in csv_file:
        rows.append(row)

for field in fields:
    print(field , '|' , end='')
print()

for rwo in rows :
    for data in row:
        print(data,'   ',end='')
    print()
    print('-'*30)

# print(fields)
# print(rows) 