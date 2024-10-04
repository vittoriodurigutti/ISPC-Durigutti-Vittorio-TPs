import mysql.connector
from database import conectar_db
from datetime import datetime

# En este documento, se encuentran definidas y diferenciadas todas las funciones que interactuaran con la base de datos.

# Funciones para añadir individuos a las respectibas tablas de entidade.

# Funcion para añadir un nuevo paciente a la base de datos
def agregar_paciente(db, cursor, Nombre, Apellido, DNI, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto):
    # uso de la funcion strptime, que viene el modulo datetime para convertir el dato tipo string ingresado en fecha nacimiento, en el formato date requerido por MySQL
    Fecha_Nacimiento = datetime.strptime(Fecha_Nacimiento, '%d-%m-%Y').strftime('%Y-%m-%d')
    try:
        cursor.execute("INSERT INTO pacientes (DNI, Nombre, Apellido, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (DNI, Nombre, Apellido, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto))
        db.commit()
        print("Paciente añadido con exito!")
    except mysql.connector.errors.IntegrityError:
        print("Ya existe un paciente registrado con los mismos datos.")

# Funcion para añadir un nuevo medico a la base de datos
def agregar_medico(db, cursor, Nombre, Apellido, DNI, Especialidad, Email):
    try:
        cursor.execute("INSERT INTO medicos (Nombre, Apellido, DNI, Especialidad, Email) VALUES (%s, %s, %s, %s, %s)", (Nombre, Apellido, DNI, Especialidad, Email))
        db.commit()
        print("Nuevo miembro del personal añadido con exito!")
    except mysql.connector.errors.IntegrityError:
        print("Ya existe un registro de personal bajo los mismos datos.")


#######################################################################

# Funcion para crear un turno. Es extensa por la cantidad de variables involucradas
def crear_turno(conn, cursor, id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta):

    #Misma linea de codigo que en la funcion ingresar _paciente, para corrergir el ingreso de datos de fecha, segun lo lee MySQL
    Fecha = datetime.strptime(Fecha, '%d-%m-%Y').strftime('%Y-%m-%d')

    # Verificar si el paciente existe
    cursor.execute("SELECT * FROM pacientes WHERE DNI=%s", (id_paciente,))
    paciente = cursor.fetchone()
    if paciente is None:
        print()
        print("Paciente no encontrado.")
        print()
        return

    # Verificar si el medico existe
    cursor.execute("SELECT * FROM medicos WHERE DNI=%s", (id_medico,))
    medico = cursor.fetchone()
    if medico is None:
        print()
        print("Medico no encontrado.")
        print()
        return

    # Verificar si ya existe un turno en la misma Fecha y Hora
    cursor.execute("SELECT * FROM turnos WHERE Fecha=%s AND Hora=%s", (Fecha, Hora))
    turno_existente = cursor.fetchone()
    if turno_existente:
        print()
        print("Horario no disponible.")
        print()
        return

    # Verificar si la Fecha de la consulta es anterior a la fecha actual
    data_atual = datetime.today().date()
    data_consulta = datetime.strptime(Fecha, "%Y-%m-%d").date()
    if data_consulta < data_atual:
        print()
        print("No se pudo agendar la cita.")
        print()
        return

    # Insertar el nuevo turno en la tabla turnos
    cursor.execute("INSERT INTO turnos (id_turno, id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
                   (id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta))
    conn.commit()
    print()
    print("Turno creado con exito!")
    print()
    conn.close()

#######################################################################

# funcion para buscar y traer el total de pacientes existentes en la base de datos.
def buscar_pacientes(conn, cursor):
    cursor.execute("SELECT DNI, Nombre, Apellido, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto FROM pacientes")
    pacientes = cursor.fetchall()
    return pacientes

# funcion para buscar y traer un pacienteen base al dato <DNI>, que funciona como su clave primaria
def buscar_paciente_por_dni(conn, cursor, DNI):
    try:
        cursor.execute("SELECT * FROM pacientes WHERE DNI=%s", (DNI,))
        paciente = cursor.fetchone()
        if paciente is None:
            print()
            print("No se encontró un paciente con el DNI proporcionado.")
            print()
        else:
            return paciente
    except mysql.connector.Error as err:
        print()
        print(f"Error: {err}")
        print()

# funcion para buscar y traer todos los turnos registrados
def buscar_turno(conn, cursor):
    cursor.execute("SELECT turnos.id_turno, pacientes.Nombre, turnos.Fecha, turnos.Hora, turnos.Especialidad, turnos.Motivo_consulta FROM turnos INNER JOIN pacientes ON turnos.id_paciente=pacientes.DNI")
    horarios = cursor.fetchall()
    return horarios

# funcion para buscar y traer todos los medicos registrados
def buscar_medicos(conn, cursor):
    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()
    return medicos

# Funcion para traer a todos los medicos correspondiente de una determinada especialidad
def buscar_medicos_por_especialidad(conn, cursor, Especialidad):
    try:
        cursor.execute("SELECT * FROM medicos WHERE Especialidad=%s", (Especialidad,))
        medicos = cursor.fetchall()
        if not medicos:
            print()
            print("No se encontraron médicos con la especialidad proporcionada.")
            print()
        else:
            return medicos
    except mysql.connector.Error as err:
        print()
        print(f"Error: {err}")
        print()

#############################################

#Funciones para borrar datos de las tablas.

# funcion para eliminar/borrar registro de un turno de la respectiva tabla
def cancelar_turno(conn, cursor, id_turno):
    cursor.execute("SELECT * FROM turnos WHERE id_turno=%s", (id_turno,))
    turno = cursor.fetchone()
    if turno is None:
        print()
        print("Turno no disponible/encontrado.")
        print()
        return

    cursor.execute("DELETE FROM turnos WHERE id_turno=%s", (id_turno,))
    conn.commit()
    print("Turno cancelado con exito!")


# funcion para eliminar/borrar paciente del registro
def eliminar_paciente(conn, cursor, DNI):
    cursor.execute("SELECT * FROM pacientes WHERE DNI=%s", (DNI,))
    paciente = cursor.fetchone()
    if paciente is None:
        print()
        print("Paciente no encontrado.")
        print()
        return

    cursor.execute("DELETE FROM pacientes WHERE DNI=%s", (DNI,))
    conn.commit()
    print()
    print("Paciente eliminado con éxito!")
    print()

# funcion para eliminar/borrar medico del registro
def eliminar_medico(conn, cursor, DNI):
    cursor.execute("SELECT * FROM medicos WHERE DNI=%s", (DNI,))
    medico = cursor.fetchone()
    if medico is None:
        print()
        print("Médico no encontrado.")
        print()
        return

    cursor.execute("DELETE FROM medicos WHERE DNI=%s", (DNI,))
    conn.commit()
    print()
    print("Médico eliminado con éxito!")
    print()