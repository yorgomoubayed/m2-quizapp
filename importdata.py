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
        if(row[15] == 'NR'):
            row[15] = row[15].replace('NR', '-1') # Conversion de NR (fréquence non renseigné) par rien (1)
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
        Database.objects.create(pumedid= int(row[0]), first_author= row[1], date= row[2], journal = row[3], link= row[4], study = row[5], disease= row[6],
        initial_sample_size= row[7], region= row[8], chr_id= int(row[9]), chr_pos= int(row[10]), strongest_snp_id_risks= row[11], snps = row[12], snp_id_current= int(row[13]) , context= row[14], risk_allele_frequency= float(row[15]),
        p_value = float(row[16]),  p_valueLog = float(row[17]) )
        # print(row)
        # accumulateur_data += [row[9]]
#     print(f"{str(count)} succès d'insertion")
        # print(row[0])
# print(len(accumulateur_data))
# print(row[0])
