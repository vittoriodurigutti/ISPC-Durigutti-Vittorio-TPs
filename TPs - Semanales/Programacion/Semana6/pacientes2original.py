import sqlite3
import datetime

print("-------------------------------------------- ")
print(" ACTIVIVIDAD: PROYECTO FINAL ")
print("-------------------------------------------- ")
print("PROYECTO: GESTOR DE CITAS MEDICAS CON DB INCLUIDA ")
print("-------------------------------------------- ")
print("INTEGRANTES: Zalazar, GUSTAVO. Durigurri, Vitorrio. ")
print("-------------------------------------------- ")
print()
class Paciente:
    def __init__(self, Nombre, Telefono):
        self.Nombre = Nombre
        self.Telefono = Telefono

class horario:
    def __init__(self, paciente, dia, hora, Especialidad):
        self.paciente = paciente
        self.dia = dia
        self.hora = hora
        self.Especialidad = Especialidad

# Funcion para crear una tabla de pacientes en la base de datos
def crear_tabla_pacientes():
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      Nombre TEXT NOT NULL,
                      Telefono TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

# Funcion para añadir un nuevo paciente a la base de datos
def adicionar_paciente(Nombre, Telefono):
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO pacientes (Nombre, Telefono) VALUES (?, ?)", (Nombre, Telefono))
        conn.commit()
        print("Paciente añadido con exito!")
    except sqlite3.IntegrityError:
        print("Paciente registrado!")
    conn.close()

# Funcion para buscar todos los pacientes anotados
def buscar_pacientes():
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    conn.close()
    return pacientes

# Funcion para realizar un horario de consulta
def marcar_consulta(paciente_id, dia, hora, Especialidad):
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id=?", (paciente_id,))
    paciente = cursor.fetchone()
    if paciente is None:
        print("Paciente no encontrado.")
        conn.close()
        return

    cursor.execute("SELECT * FROM horarios WHERE dia=? AND hora=?", (dia, hora))
    horario_existente = cursor.fetchone()
    if horario_existente:
        print("Horario no disponible.")
        conn.close()
        return

    data_atual = datetime.date.today()
    data_consulta = datetime.datetime.strptime(dia, "%d/%m/%Y").date()
    if data_consulta < data_atual:
        print("No se pudo agendar la cita.")
        conn.close()
        return

    cursor.execute("INSERT INTO horarios (paciente_id, dia, hora, Especialidad) VALUES (?, ?, ?, ?)",
                   (paciente_id, dia, hora, Especialidad))
    conn.commit()
    print("Consulta registrada con exito!")
    conn.close()

    # Funcion para crear la tabla horaria en la base de datos
def crear_tabla_horarios():
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS horarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      paciente_id INTEGER NOT NULL,
                      dia TEXT NOT NULL,
                      hora TEXT NOT NULL,
                      Especialidad TEXT NOT NULL,
                      FOREIGN KEY (paciente_id) REFERENCES pacientes (id))''')
    conn.commit()
    conn.close()

# crear base de datos de pacientes (si no existe)
crear_tabla_horarios()


# Funcion para buscar todos los horarios de consulta
def buscar_horarios():
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT horarios.id, pacientes.Nombre, horarios.dia, horarios.hora, horarios.Especialidad FROM horarios INNER JOIN pacientes ON horarios.paciente_id=pacientes.id")
    horarios = cursor.fetchall()
    conn.close()
    return horarios

# Funcion para cancelar un horario de consulta
def cancelar_consulta(horario_id):
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM horarios WHERE id=?", (horario_id,))
    horario = cursor.fetchone()
    if horario is None:
        print("Horario no disponible/encontrado.")
        conn.close()
        return

    cursor.execute("DELETE FROM horarios WHERE id=?", (horario_id,))
    conn.commit()
    print("Consulta cancelada con exito!")
    conn.close()

# Crear base de datos de los pacientes (si no existe)
crear_tabla_pacientes()

# Loop principal del programa
while True:
    print("1 - Adicionar paciente")
    print("2 - Exhibir pacientes registrados")
    print("3 - Agendar consulta")
    print("4 - Exhibir horarios de consulta")
    print("5 - Cancelar consulta")
    print("6 - Salir")
    opcion = input("Elija una opcion: ")

    print("------------------------------------------")

    if opcion == "1":
        Nombre = input("Digite Nombre del paciente: ")
        Telefono = input("Digite Telefono del paciente: ")
        adicionar_paciente(Nombre, Telefono)
        print("-------------------------------------------")

    elif opcion == "2":
        pacientes = buscar_pacientes()
        print("Pacientes registrados:")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Telefono: {paciente[2]}")
        print("-------------------------------------------")

    elif opcion == "3":
        pacientes = buscar_pacientes()
        print("Pacientes registrados:")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Telefono: {paciente[2]}")
        paciente_id = int(input("Marque el id del paciente para la consulta: "))
        dia = input("Marque el día de la consulta consulta (DD/MM/AAAA): ")
        hora = input("Marque la hora de la consulta (HH:MM): ")
        Especialidad = input("Marque la especialidad deseada para la consulta: ")
        marcar_consulta(paciente_id, dia, hora, Especialidad)
        print("---------------------------------------------")

    elif opcion == "4":
        horarios = buscar_horarios()
        
        
        print("horarios de consulta:")
        for horario in horarios:
            print(f"ID: {horario[0]}, Paciente: {horario[1]}, Dia: {horario[2]}, Hora: {horario[3]}, Especialidad: {horario[4]}")
        print("-------------------------------------------------")
    elif opcion == "5":
        horarios = buscar_horarios()
        print("horarios de consulta:")
        for horario in horarios:
            print(f"ID: {horario[0]}, Paciente: {horario[1]}, Dia: {horario[2]}, Hora: {horario[3]}, Especialidad: {horario[4]}")
        horario_id = int(input("Elija la fecha de la agenda para cancelar: "))
        cancelar_consulta(horario_id)
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción invalida, intente nuevamente.")




