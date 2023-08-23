import os
import jaydebeapi
import pandas as pd

SERVER = "IP_DEL_SERVIDOR"
PORT = "4100"
UID = "USUARIO"
PWD = "PASSWORD"
DATABASE = 'BASE_DE_DATOS' # No es necesario usarlo, pero se puede agregar si se quiere crear una conexion especifica a una BD

# Configuración de la conexión
jtds_path = 'jtds_1.3.1/jtds-1.3.1.jar'  # Ruta al archivo jtds.jar 
url = f'jdbc:jtds:sybase://{SERVER}:{PORT}'
driver = 'net.sourceforge.jtds.jdbc.Driver'

# Establecer la conexión
conn = jaydebeapi.connect(driver, url, [UID, PWD], jtds_path)

# Ejecutar consultas SQL
sql_query = "SELECT top 10 * FROM database.scheme.table"

with conn:
    df = pd.read_sql(sql_query, conn)

# Guardar en un archivo parquet
parquet_file_path = 'output/parquet/resultados.parquet'
directory = os.path.dirname(parquet_file_path)
if not os.path.exists(directory):
    # Crear directorio si no existe
    os.makedirs(directory)


df.to_parquet(parquet_file_path, index=False)

print(df)