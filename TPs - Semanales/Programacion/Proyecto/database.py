import mysql.connector

# a diferencia del ejemplo, ya teniamos creadas los bloques de codigo con los comandos para ejecutar sobre la BD. Por lo que solo 
# establecemos una funcion para evitar el ingreso de datos al conectar con la base de datos.
def conectar_db():
    host = '127.0.0.1'
    port = '3306'
    user = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    database = 'PROYECTO_ISPC'

    conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    return conn, cursor