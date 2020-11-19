'''
A draft python script for importing csv data related to the django application. It hasn't been tested properly.
'''
from example.models import Database
import csv

count = 0

CSV_PATH = "example.tsv"

# Ouvertur du fichier tsv
with open(CSV_PATH, newline ="") as csvfile:

    reader = csv.reader(csvfile, delimiter= "\t", quotechar = "'")
    print("Loading database...")
    next(reader,None)

    for row in reader:
        # print(row)

        if(row[9] == 'X'):
            row[9] = row[9].replace('X', '55') # conversion du chromosome X par 55
        if(row[15] == ''):
            row[15] = row[15].replace('' , '-9999') # -9999 for empty data
        if(row[13] == ''):
            row[13] = row[13].replace('', '-9999') # -9999 for empty data
        if(row[14] == ''):
            row[14] = row[14].replace('', 'Empty_Data')
        if(row[8] == ''):
            row[8] = row[8].replace('', '-9999')  # -9999 for empty data
        if(row[9] == ''):
            row[9] = row[9].replace('', '-9999') # -9999 for empty data
        if(row[10] == ''):
            row[10] = row[10].replace('', '-9999') # -9999 for empty data
        Database.objects.create(x= int(row[0]), y= row[1], z= row[2], x= row[3], y=row[4], z=row[5], x= row[6],
        y= row[7], z= row[8], x= int(row[9]), y= int(row[10]), z= row[11], x = row[12], y= int(row[13]) , z= row[14], x= float(row[15]),
        y=float(row[16]),  z=float(row[17]) )
