# Importamos la clase Database, y las funciones definidas en la carpeta funciones. A fin de no alargar por demas el archivo del menu.
from funciones import *

# Clase menu, que se representa mediante la consola para que podamos interactuar.
class Menu:
    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
# Este sera el menu principal, con el que accedemosa submenues segun la categoria de las entidades definidas en la base de datos
    def menuPrincipal(self):    
        while True: 
            print("Bienvenido al menu principal")  
            print("1 - Consulta sobre Pacientes")
            print("2 - Consulta sobre Medicos")
            print("3 - Consulta sobre Turnos")
            print("4 - Salir")
            print()
            
            opcion = input("Elija una opcion: ")
            
            if opcion == '1':
                self.menuPaciente()
            elif opcion == '2':
                self.menuMedico()
            elif opcion == '3':
                self.menuTurno()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

###########################################################
    
    # Sub Menu relacionado a las opciones de paciente.                
    def menuPaciente(self):
        while True:    
            print("1 - Adicionar paciente")
            print("2 - Buscar un paciente")
            print("3 - Eliminar paciente")
            print("4 - Exhibir pacientes registrados")
            print("9 - Salir")
            
            opcion = input("Elija una opcion: ")
            
            # Se solicita ingresar todos los valores necesarios para crear un paciente. Tener en cuenta que uno de los valores es una fecha.
            if opcion == "1":
                Nombre = input("Digite Nombre del paciente: ")
                Apellido = input("Digite Apellido del paciente: ")
                DNI = input("Digite DNI del paciente: ")
                Fecha_Nacimiento = input("Digite Fecha de Nacimiento del paciente (DD-MM-AAAA): ")
                Telefono1 = input("Digite Telefono1 del paciente: ")
                Telefono2 = input("Digite Telefono2 del paciente, en caso de no poseer coloque un guion: ")
                Email = input("Digite Email del paciente: ")
                Provincia = input("Ingrese provincia: ")
                Ciudad = input("Ingrese ciudad/localidad: ")
                CP = input("Ingrese el codigo postal: ")
                Calle = input("Ingrese la calle: ")
                Numero = input("Digite altura de la direccion: ")
                Depto = input("Digite piso/departamento/lote: ")
                agregar_paciente(self.db, self.cursor, Nombre, Apellido, DNI, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto)
                print("-------------------------------------------")

            # Esta opcion llama a la fucion para buscar un paciente, mediante su DNI   
            elif opcion == "2":
                DNI = input("Digite DNI del paciente a buscar: ")
                paciente = buscar_paciente_por_dni(self.db, self.cursor, DNI)
                if paciente:
                    print(f"Paciente encontrado: DNI: {paciente[0]}, Nombre: {paciente[1]}, Apellido: {paciente[2]}, Fecha de Nacimiento: {paciente[3]}")
                else:
                    print("No se encontró un paciente con ese DNI.")
                print("-------------------------------------------")
            
            # Y esta funcion permite eliminarlos
            elif opcion == "3":
                DNI = input("Digite DNI del paciente a eliminar: ")
                eliminar_paciente(self.db, self.cursor, DNI)
                print("-------------------------------------------")

                        # Trae la funcion para buscar pacientes en la base.
            elif opcion == "4":
                pacientes = buscar_pacientes(self.db, self.cursor)
                print("Pacientes registrados:")
                for paciente in pacientes:
                    print(f"DNI: {paciente[0]}, Nombre: {paciente[1]}, Apellido: {paciente[2]}, Fecha de Nacimiento: {paciente[3]}")
                print("-------------------------------------------")

            # Similar a los munues telefonicos, usamos el 9 para salir y terminar el programa
            elif opcion == "9":
                print("Saliendo del programa.")
                break

            else:
                print("Opción invalida, intente nuevamente.")

###########################################################

    # Submenu relacionado a las opciones con la entidad medicos
    def menuMedico(self):
        while True:    
            print("1 - Adicionar medico")
            print("2 - Exhibir medicos registrados")
            print("3 - Indique una especialidad, y le brindaremos todos los profesionales disponibles.")
            print("4 - Eliminar medico del registro")
            print("9 - Salir")

            opcion = input("Elija una opcion: ")

            # Opcion que llama a la funcion para agregar un medico a la base de datos
            if opcion == "1":
                Nombre = input("Ingrese el nombre del profesional: ")
                Apellido = input("Ingrese el apellido: ")
                DNI = input("Ingrese el DNI: ")
                Especialidad = input("Identifique la especialidad del profesional: ")
                Email = input("Coloque la casilla de correo a forma de contacto: ")
                agregar_medico(self.db, self.cursor, Nombre, Apellido, DNI, Especialidad, Email)
                print("-------------------------------------------")

            # Opcion que llama a la funcion para agregar un medico a la base de datos
            elif opcion == "2":
                medicos = buscar_medicos(self.db, self.cursor)
                print("Profesionales registrados:")
                for medico in medicos :
                    print(f"DNI: {medico[0]}, Nombre: {medico[1]}, Apellido: {medico[2]}, Especialidad {medico[3]}, Direccion de correo electronico {medico[4]}")
                print("-------------------------------------------")

            elif opcion == "3":
                medicos = buscar_medicos_por_especialidad(self.db, self.cursor, Especialidad)
                print("Pacientes registrados:")
                for medico in medicos:
                    print(f"DNI: {medico[0]}, Nombre: {medico[1]}, Apellido: {medico[2]}, Especialidad {medico[3]}, Direccion de correo electronico {medico[4]}")
                print("-------------------------------------------")

            # Opcion que llama a la funcion para eliminar un medico a la base de datos segun su DNI
            elif opcion == "4":
                DNI = input("Digite DNI del paciente a eliminar: ")
                eliminar_medico(self.db, self.cursor, DNI)
                print("-------------------------------------------")

            # Similar a los munues telefonicos, usamos el 9 para salir y terminar el programa
            elif opcion == "9":
                print("Saliendo del programa.")
                break

            else:
                print("Opción invalida, intente nuevamente.")

###########################################################

    # Aqui definimos las opciones que ejecutan cambios sobre la tabla turnos
    def menuTurno(self):
        while True:    
            print("1 - Crear un turno")
            print("2 - Exhibir turno registrados")
            print("3 - Eliminar turno")
            print("9 - Salir")
            print()
            opcion = input("Elija una opcion: ")
            print("------------------------------------------")
            # Llama a la funcion crear turno, que genera un registro en la base de datos.
            if opcion == "1":
                id_paciente = input("Ingrese el DNI del paciente: ")
                Fecha = input("Ingrese la fecha en la que se agendara el turno, favor utice el formato (DD-MM-AAAA): ")
                Hora = input("Ingrese el horario de la consulta, favor utilice el formato (HH:MM): ")
                Especialidad = input("Indique la especialidad indicada: ")
                id_medico = input("Ingrese el DNI del medico con quien realizara la consulta: ")
                Motivo_consulta = input("Marque el motivo de la consulta: ")
                crear_turno(self.db, self.cursor, id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta)
                print("---------------------------------------------")

            # llama a la opcion buscar turno, trayendo TODOS los registros de la tabla.
            elif opcion == "2":
                horarios = buscar_turno(self.db, self.cursor)
                print("Horarios de consulta:")
                for horario in horarios:
                    print(f"ID Turno: {horario[0]}, Nombre Paciente: {horario[1]}, Fecha: {horario[2]}, Hora: {horario[3]}, Especialidad: {horario[4]}")
                print("-------------------------------------------------")

            # Llama a la funcion para borrar los registros de turno definido. Requiere conocimiento el id_turno a eliminar 
            elif opcion == "3":
                id_turno = int(input("Ingrese el ID del Turno que desea cancelar: "))
                cancelar_turno(self.db, self.cursor, id_turno)
                print("-------------------------------------------------")

            # Similar a los munues telefonicos, usamos el 9 para salir y terminar el programa
            elif opcion == "9":
                print("Saliendo del programa.")
                break

            else:
                print("Opción invalida, intente nuevamente.")
