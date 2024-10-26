# Programa en Python
# Programacion - 
# Proyecto 2

# EJECUCION DEL PROGRAMA: python menu_mysql.py | 
# Lectura de los datos enviamos por el monitor serial 



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
            password='Contrasena09081994'  # Cambia si es necesario
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
        print(f"[INFO] Lectura registrada en la BD: Sensor {id_sensor}, Nivel de Gas: {nivel_gas}")
    except Error as e:
        print(f"[ERROR] Error al registrar la lectura: {e}")
    finally:
        cursor.close()

#---------------------------------------------------------------#
# Función para leer datos del puerto serial y registrar en la base de datos
def leer_datos_serial(connection, puerto='COM5', baudrate=9600):
    ser = None
    try:
        ser = serial.Serial(puerto, baudrate, timeout=3)
        ser.reset_input_buffer()  # Limpia el buffer al iniciar
        print(f"[INFO] Conectado al puerto {puerto} a {baudrate} baudios")
        time.sleep(2)

        while True:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if linea:
                print(f"[DEBUG] Datos recibidos del ESP32: '{linea}'")
                try:
                    id_sensor, nivel_gas = linea.split(":")
                    print(f"[INFO] Sensor: {id_sensor}, Nivel de Gas: {nivel_gas}")
                    registrar_lectura(connection, id_sensor, float(nivel_gas))
                except ValueError as e:
                    print(f"[ERROR] Formato incorrecto: '{linea}' - {e}")

            time.sleep(2)  # Esperar 2 segundos entre lecturas

    except serial.SerialException as e:
        print(f"[ERROR] Error al abrir el puerto serial: {e}")
    except KeyboardInterrupt:
        print("\n[INFO] Lectura interrumpida por el usuario.")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("[INFO] Puerto serial cerrado.")


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
                puerto = input("Introduce el puerto serial (por defecto COM5): ") or 'COM5'
                baudrate = input("Introduce la velocidad de baudios (por defecto 9600): ") or 9600
                leer_datos_serial(connection, puerto, int(baudrate))
            elif opcion == '2':
                connection.close()
                print("[INFO] Conexión cerrada. Saliendo...")
                break
            else:
                print("[ERROR] Opción no válida. Inténtalo de nuevo.")
    else:
        print("[ERROR] No se pudo conectar a la base de datos.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
