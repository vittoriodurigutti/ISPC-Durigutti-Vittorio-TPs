from menu import Menu
from database import conectar_db


print("-------------------------------------------- ")
print(" ACTIVIVIDAD: PROYECTO FINAL ")
print("-------------------------------------------- ")
print("PROYECTO: GESTOR DE CITAS MEDICAS CON DB INCLUIDA ")
print("-------------------------------------------- ")
print("Integrantes:" )
print("Luciano Lujan | GitHub: https://github.com/lucianoilujan" )
print("Durigutti, Vittorio | GitHub: https://github.com/vittoriodurigutti" )
print("Joaquin Zalazar | GitHub: https://github.com/breaakerr" )
print("Lisandro Juncos | GitHub: https://github.com/Lisandro-05" )
print("-------------------------------------------- ")
print()



#######################################################################

def main():
    # Crear una instancia de la base de datos
    db, cursor = conectar_db()
    if db:
        print("Conexión establecida exitosamente")
        menu = Menu(db, cursor)
        menu.menuPrincipal()
        db.close()
    else:
        print("No se pudo establecer la conexión a la base de datos")

if __name__ == "__main__":
    main()

#######################################################################

# En la primera etapa, pensamos en desarrollar una clase, correspondiente a cada entidad principal.
# Al pasar segun lo indicado en clase, a MySQL, estas quedan sin funcion, puesto que cada tabla de entidad se crea directamente sobre MySQL 

"""# Clases correspondientes a las entidades fundamentales de la base de datos. Cada entidad tendra una serie de valores no moficables segun se requiera

# Clase paciente, los valores de contacto y direccion los ponemos en formato de diccionario, y debajo los respectivos getters
class Paciente:
    def __init__(self, Nombre, Apellido,DNI,Fecha_Nacimiento,Telefono1,Telefono2,Email,Provincia,Ciudad,Calle,CP,Numero,Depto,):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DNI = DNI
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Contacto = {
            'Telefono1': Telefono1,
            'Telefono2': Telefono2,
            'Email': Email
        }
        self.Direccion = {
            'Provincia': Provincia,
            'Ciudad': Ciudad,
            'Calle': Calle,
            'CP': CP,
            'Numero': Numero,
            'Depto': Depto
        }

# Clase Turno, con definicion de los valores que no se deben poder cambiar.
class Turno:
    def __init__(self, id_turno, id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta):
        self.id_turno = id_turno
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.Fecha = Fecha
        self.Hora = Hora
        self.Especialidad = Especialidad
        self.Motivo_consulta = Motivo_consulta



# Clase Medico, con los valores fundamentales para un medico relacionado a la consulta, considerand que puede haber mas de un profesional por especialidad.
class Medico:
    def __init__(self, Nombre, Apellido, DNI, Especialidad, Email):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DNI = DNI
        self.Especialidad = Especialidad
        self.Email = Email
"""

#######################################################################

# En primera instancia, habiamos definido un bloque de codigo para crear las tablas, si estas aun no existian.
# Estabamos haciendo uso de sqlite que permitia crear un archivo .sql dentro del programa sin requerimiento de acceso a mysql


"""# Funcion para crear una tabla de pacientes
def crear_tabla_pacientes():
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            DNI INT PRIMARY KEY,
            Nombre VARCHAR(30) NOT NULL,
            Apellido VARCHAR(30) NOT NULL,
            Fecha_Nacimiento DATE NOT NULL,
            Telefono1 VARCHAR(12) NOT NULL,
            Telefono2 VARCHAR(12),
            Email VARCHAR(60) NOT NULL,
            Provincia VARCHAR(30) NOT NULL,
            Ciudad VARCHAR(30) NOT NULL,
            Calle VARCHAR(30) NOT NULL,
            CP VARCHAR(4) NOT NULL,
            Numero INT NOT NULL,
            Depto VARCHAR(10)
        )'''
    )
    conn.commit()
    conn.close()

# Funcion para crear una tabla de turnos
def crear_tabla_turnos():
    conn = sqlite3.connect('turno.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turnos (
            id_turno INT AUTO_INCREMENT PRIMARY KEY,
            id_paciente INT NOT NULL,
            id_medico INT NOT NULL,
            Fecha DATE NOT NULL,
            Hora TIME NOT NULL,
            Especialidad VARCHAR(30) NOT NULL,
            Motivo_consulta VARCHAR(255) NOT NULL,
            FOREIGN KEY (id_paciente) REFERENCES pacientes (DNI),
            FOREIGN KEY (id_medico) REFERENCES medicos (DNI)
        )
    ''')
    conn.commit()
    conn.close()

# Funcion para crear una tabla de medicos
def crear_tabla_medicos():
    conn = sqlite3.connect('medicos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
            DNI INT PRIMARY KEY,
            Nombre VARCHAR(30) NOT NULL,
            Apellido VARCHAR(30) NOT NULL,
            Especialidad VARCHAR(30) NOT NULL,
            Email VARCHAR(60) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()"""

#######################################################################

