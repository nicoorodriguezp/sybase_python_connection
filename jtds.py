import jaydebeapi

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

# Crear un cursor
cursor = conn.cursor()

# Ejecutar consultas SQL
sql_query = "SELECT top 10 * FROM database.scheme.table"

cursor.execute(sql_query)
results = cursor.fetchall()

# Hacer algo con los resultados
for row in results:
    print(row)

# Cerrar cursor y conexión
cursor.close()
conn.close()
