import pandas as pd #Libreria para Excel
import psycopg2 #Libreria para conexion base de datos Postgresql

#Codigo para importar de Excel a Postgresql fila por fila


#Leer el archivo de Excel con su path correspondiente y el nombre de la hoja (son varias hojas de Excel pero descargue y modifique el nombre de la hoja)
dataframe = pd.read_excel(r'C:\Users\*****', sheet_name='*****')

#Columnas a leer del Excel
column_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


#Pandas para leer el excel
datos = dataframe.iloc[:, column_indices].values.tolist()


#Conexión a la base de datos del server
conn = psycopg2.connect(
    user="*****",
    host="*****",
    database="*****",
    password="*****"
)
cursor = conn.cursor()

#Iterar en base de datos poniendo los valores correspondientes(Los valores son los nombres de la base de datos que tiene)
for row in datos:
    consulta_insert = "INSERT INTO dummy_excel (Status, Comment) VALUES (%s, %s)"
    cursor.execute(consulta_insert, row)

conn.commit()
cursor.close()
conn.close()