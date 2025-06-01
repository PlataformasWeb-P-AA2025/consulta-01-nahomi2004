'''
*****************
|   Recordar    |
*****************

1. Levantar el servidor de MongoDB
"C:\MongoDB\bin\mongod.exe" --dbpath="C:\data\db"

2. Abrir una nueva terminal normal (no admin) y ejecutar
"C:\MongoDB\bin\mongosh.exe"

3. Crear la base de datos (opcional en realidad)
En MongoDB no necesitas crear explícitamente la base de datos antes de usarla. Se crea automáticamente cuando insertas datos. Pero si quieres prepararla desde la consola para verificar, puedes hacer:
'''

import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB (asegúrate de que el servidor esté corriendo en localhost:27017)
client = MongoClient("mongodb://localhost:27017/")
db = client["torneos_atp"]
coleccion = db["partidos"]

# Leer archivos Excel
df_2022 = pd.read_excel("data/2022.xlsx")
df_2023 = pd.read_excel("data/2023.xlsx")

# Convertir DataFrames a diccionarios (listas de documentos)
documentos_2022 = df_2022.to_dict(orient="records")
documentos_2023 = df_2023.to_dict(orient="records")

# Insertar documentos en la colección
coleccion.insert_many(documentos_2022)
coleccion.insert_many(documentos_2023)

print("Datos insertados correctamente en MongoDB.")

# CONSULTA 1: Mostrar los partidos jugados en 'Adelaide'
print("\nConsulta 1: Partidos jugados en Adelaide")
for partido in coleccion.find({"Location": "Adelaide"}).limit(5):
    print(f"{partido['Date']} - {partido['Winner']} vs {partido['Loser']}")

# CONSULTA 2: Buscar partidos con resultado 'Retired'
print("\nConsulta 2: Partidos terminados como 'Retired'")
for partido in coleccion.find({"Comment": "Retired"}):
    print(f"{partido['Date']} - {partido['Winner']} vs {partido['Loser']} (Retired)")
