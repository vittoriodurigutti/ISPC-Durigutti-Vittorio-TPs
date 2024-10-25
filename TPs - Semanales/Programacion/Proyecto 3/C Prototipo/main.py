# Programa en Python
# Programacion - 
# Proyecto 2

# EJECUCION DEL PROGRAMA: python menu_mysql.py


''' 
El programa consta de 4 partes fundamentales.
- (LINEA 16) Las librerias funcionales para poder conectar con la base de datos. 
-  La funcion conectar con la que establecemos la conecion con la base de datos en el entorno local
    - (LINEA 24) Funciones con las que interactuar con la conexion 
    - (LINEA 47) Función para cerrar la conexión
- Las funciones con las que interacutar con la base de datos
    - Funciones para agregar datos a la base de datos:
        - (LINEA 70) Función para insertar un cliente en la base de datos
        - (LINEA 97) Funcion para insertar dispositivo
        - (LINEA 116) Funcion para insertar sensor_actuador
    - Funciones para modificar datos a la base de datos:
        - (LINEA 143) Función para modificar un cliente
        - (LINEA 165) Función para cambiar el nombre de la habitación de un actuador
    - Funciones para eliminar datos a la base de datos:
        - (LINEA 188) Función para dar de baja un cliente (y eliminar todos sus dispositivos y sensores)
    - Funciones para buscar datos a la base de datos:
        - (LINEA 228) Función para buscar un cliente por DNI y mostrar sus datos
        - (LINEA 246) Función para mostrar todos los controladores de un cliente
        - (LINEA 268) Función para mostrar lecturas de un sensor específico
        - (LINEA 289) Función para buscar por DNI del cliente, sensores, ubicación y habitación
        - (LINEA 317) Función para recibir una alarma y mostrar información del sensor
- (LINEA 366) Menu interactivo, mediante la terminal, con el que realizar las solicitudes, asi como la conexion.

'''

import mysql.connector
from mysql.connector import Error
import serial  # Para leer desde el puerto serial
import time  # Para manejar tiempos de espera

#---------------------------------------------------------------#
# Función para conectar a la base de datos
def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',       
            database='GASDETECTOR',  
            user='root',            
            password='rootpassword'  # Cambia si es necesario
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

#---------------------------------------------------------------#
# Función para registrar la lectura del sensor en la base de datos
def registrar_lectura(connection, id_sensor, nivel_gas):
    cursor = connection.cursor()
    try:
        query = """INSERT INTO Lectura (fecha_hora, nivel_gas, id_sensor_actuador)
                   VALUES (NOW(), %s, %s)"""
        cursor.execute(query, (nivel_gas, id_sensor))
        connection.commit()
        print(f"Lectura registrada: Sensor {id_sensor}, Nivel de Gas: {nivel_gas}")
    except Error as e:
        print(f"Error al registrar la lectura: {e}")
    finally:
        cursor.close()

#---------------------------------------------------------------#
# Función para leer datos del puerto serial y registrar en la base de datos
def leer_datos_serial(connection, puerto='/dev/ttyUSB0', baudrate=9600):
    try:
        ser = serial.Serial(puerto, baudrate, timeout=1)
        print(f"Conectado al puerto {puerto} a {baudrate} baudios")
        time.sleep(2)  # Esperar a que el puerto serial se estabilice

        while True:
            linea = ser.readline().decode().strip()  # Leer y decodificar línea
            if linea:
                print(f"Datos recibidos: {linea}")
                try:
                    # Suponemos que los datos vienen en el formato: "ID_SENSOR:NIVEL_GAS"
                    id_sensor, nivel_gas = linea.split(":")
                    registrar_lectura(connection, id_sensor, float(nivel_gas))
                except ValueError:
                    print(f"Formato incorrecto: {linea}")
    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial: {e}")
    except KeyboardInterrupt:
        print("\nLectura interrumpida por el usuario.")
    finally:
        ser.close()
        print("Puerto serial cerrado.")

#---------------------------------------------------------------#
# Menú interactivo
def menu():
    connection = conectar()
    if connection:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Leer datos del monitor serial y registrar en la base de datos")
            print("2. Salir")
            
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                puerto = input("Introduce el puerto serial (por defecto /dev/ttyUSB0): ") or '/dev/ttyUSB0'
                baudrate = input("Introduce la velocidad de baudios (por defecto 9600): ") or 9600
                leer_datos_serial(connection, puerto, int(baudrate))
            elif opcion == '2':
                connection.close()
                print("Conexión cerrada. Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    else:
        print("No se pudo conectar a la base de datos.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
