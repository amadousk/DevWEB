import csv
import mysql.connector

link = mysql.connector.connect(
    host='mysql' ,
    database='rna' ,
    user='root' ,
    password=""
)

print('Hello World !')

cur = link. cursor () 
with open('./data/rna_import_20221101_dpt_01.csv', 'r', encoding='ISO-8859-1') as f :
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        print(row[0])
        cur.execute(
            "INSERT INTO data (rna_id, rna_id_ex_id, gestion) VALUES (%s, %s, %s)", (row[0], row[1], row[3])
        )
        link.commit ()
link.close()