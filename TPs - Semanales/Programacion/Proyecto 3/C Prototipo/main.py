# Programa en Python
# Proyecto 2
# EJECUCION DEL PROGRAMA: python menu_mysql.py
# Este programa se encarga de leer datos enviados por un ESP32 a través del puerto serial
# y registrar los datos en una base de datos MySQL.

#---------------------------------------------------------------#
# Librerías 

import mysql.connector  # Para manejar la conexión con la base de datos MySQL
from mysql.connector import Error  # Para gestionar errores de MySQL
import serial  # Para leer desde el puerto serial
import time  # Para manejar tiempos de espera

#---------------------------------------------------------------#
# Función para conectar a la base de datos
def conectar():
    try:
        # Crear conexión con la base de datos MySQL usando las credenciales especificadas
        connection = mysql.connector.connect(
            host='localhost',  # Servidor de la base de datos
            database='GASDETECTOR',  # Nombre de la base de datos
            user='root',  # Usuario de la base de datos
            password='Contrasena09081994'  # Contraseña del usuario (cambiar si es necesario)
        )
        # Verifica si la conexión fue exitosa
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection  # Devuelve la conexión para su uso posterior
    except Error as e:
        # Muestra un mensaje de error si la conexión falla
        print(f"Error al conectar a la base de datos: {e}")
        return None

#---------------------------------------------------------------#
# Función para registrar la lectura del sensor en la base de datos
def registrar_lectura(connection, id_sensor, nivel_gas):
    # Crear cursor para ejecutar la consulta SQL
    cursor = connection.cursor()
    try:
        # Consulta SQL para insertar la lectura en la tabla `Lectura`
        query = """INSERT INTO Lectura (fecha_hora, nivel_gas, id_sensor_actuador)
                   VALUES (NOW(), %s, %s)"""
        # Ejecuta la consulta con el valor de nivel de gas e ID del sensor
        cursor.execute(query, (nivel_gas, id_sensor))
        # Confirma los cambios en la base de datos
        connection.commit()
        print(f"[INFO] Lectura registrada en la BD: Sensor {id_sensor}, Nivel de Gas: {nivel_gas}")
    except Error as e:
        # Muestra un mensaje de error si ocurre un problema al ejecutar la consulta
        print(f"[ERROR] Error al registrar la lectura: {e}")
    finally:
        # Cierra el cursor después de realizar la operación
        cursor.close()

#---------------------------------------------------------------#
# Función para leer datos del puerto serial y registrar en la base de datos
def leer_datos_serial(connection, puerto='COM5', baudrate=9600):
    # Inicializa variable para la conexión serial
    ser = None
    try:
        # Configura la conexión serial con el puerto y la velocidad de baudios especificados
        ser = serial.Serial(puerto, baudrate, timeout=3)
        ser.reset_input_buffer()  # Limpia el buffer al iniciar para evitar lecturas residuales
        print(f"[INFO] Conectado al puerto {puerto} a {baudrate} baudios")
        time.sleep(2)  # Espera breve para estabilizar la conexión

        while True:
            # Lee una línea desde el puerto serial, decodifica y elimina caracteres de espacio
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if linea:  # Si hay datos disponibles en la línea
                print(f"[DEBUG] Datos recibidos del ESP32: '{linea}'")
                try:
                    # Divide los datos recibidos en ID del sensor y nivel de gas
                    id_sensor, nivel_gas = linea.split(":")
                    print(f"[INFO] Sensor: {id_sensor}, Nivel de Gas: {nivel_gas}")
                    # Registra la lectura en la base de datos
                    registrar_lectura(connection, id_sensor, float(nivel_gas))
                except ValueError as e:
                    # Muestra un mensaje si el formato de los datos es incorrecto
                    print(f"[ERROR] Formato incorrecto: '{linea}' - {e}")

            time.sleep(2)  # Espera 2 segundos entre lecturas para evitar saturación

    except serial.SerialException as e:
        # Muestra un mensaje si ocurre un error al abrir el puerto serial
        print(f"[ERROR] Error al abrir el puerto serial: {e}")
    except KeyboardInterrupt:
        # Interrumpe la lectura en caso de que el usuario presione Ctrl+C
        print("\n[INFO] Lectura interrumpida por el usuario.")
    finally:
        # Cierra el puerto serial si está abierto
        if ser and ser.is_open:
            ser.close()
            print("[INFO] Puerto serial cerrado.")

#---------------------------------------------------------------#
# Menú interactivo
def menu():
    # Conectar a la base de datos MySQL
    connection = conectar()
    if connection:  # Verifica si la conexión fue exitosa
        while True:
            # Muestra opciones del menú
            print("\n--- Menú de Opciones ---")
            print("1. Leer datos del monitor serial y registrar en la base de datos")
            print("2. Salir")

            # Pide al usuario que seleccione una opción
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                # Solicita el puerto serial (predeterminado COM5) y usa una tasa de 9600 baudios
                puerto = input("Introduce el puerto serial (por defecto COM5): ") or 'COM5'
                baudrate = 9600
                # Inicia la lectura de datos desde el puerto serial
                leer_datos_serial(connection, puerto, int(baudrate))
            elif opcion == '2':
                # Cierra la conexión a la base de datos y termina el programa
                connection.close()
                print("[INFO] Conexión cerrada. Saliendo...")
                break
            else:
                # Mensaje de error si la opción ingresada no es válida
                print("[ERROR] Opción no válida. Inténtalo de nuevo.")
    else:
        # Muestra un mensaje si no se puede conectar a la base de datos
        print("[ERROR] No se pudo conectar a la base de datos.")

# Ejecuta el menú principal al iniciar el programa
if __name__ == "__main__":
    menu()