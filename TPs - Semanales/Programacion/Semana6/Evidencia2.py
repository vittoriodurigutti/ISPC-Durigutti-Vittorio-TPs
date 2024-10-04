#Clase cliente. Base de donde se optendran resto de elementos

class paciente:
    def __init__ (self,dni,nombre,apellido,fechaNacimiento,patologia,telefono1,telefono2,email,direccion,analisis_sangre):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__fechaNacimiento=fechaNacimiento
        self.patologia=patologia    

# componenetes correspondientes a la entidad "Contacto"
        self.telefono1=telefono1
        self.telefono2=telefono2
        self.email=email
        self.direccion=direccion

# componente relacionado a la entidad de monitoreo remoto. La idea seria que este valor se actualice cada X lapso de tiempo
# a fin de practicidad funcionara igual que el metodo de analisis, donde se tiene que ingresar el conjunto de valores para cobre escribir el elemento  
        self.__monitoreo_remoto= {
            "ritmo_cardiaco" : "",
            "fecha" : "",
            "hora" : ""
        }

# componenete relacionado a la entidad analisis de sangre
        self.__analisis_sangre = {
            "colesterol Total":"",
            "colesterol HDL":"",
            "colesterol LDL":"",
            "triglicerios":"",
            "BNP":""
        }

# componenete relacioado a la entidad Dispositivo de monitoreo
        self.__dispositivo = {
            "MAC" : "",
            "Marca" : "",
            "Modelo" : "",
            "Fecha de colocacion" : ""            
        }

# Getters para aquellos estados que definidos como privados
    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento

    @property
    def ritmo_cardiaco(self):
        return self.__monitoreo_remoto
    
    @property
    def analisis_sangre(self):
        return self.__analisis_sangre
    
    @property
    def nuevo_dispositivo(self):
        return self.__dispositivo
    
# Metodo con el cual actualizar el analisis de sangre, de forma que no sea posible modificar valores individuales
    def actualizar_analisis(self, nuevo_analisis):
        if isinstance (nuevo_analisis,dict):
            self.__analisis_sangre.update(nuevo_analisis)
        else: 
            print("El indicador comentado no existe dentro de los parametros de este analisis")

# Metodo para actualizar lo relacionado a la entidad Monitoreo remoto 
    def actualizar_monitoreo(self, nuevo_monitoreo):
        if isinstance (nuevo_monitoreo,dict):
            self.__monitoreo_remoto.update(nuevo_monitoreo)
        else: 
            print("El indicador comentado no existe dentro de los parametros de este analisis")

# Metodo necesario para actualizar lo relacionado al dispositivo del paciente. Este es unico, y debe cambarse en conjunto.
    def actualizar_dispositivo(self, nuevo_dispositivo):
        if isinstance (nuevo_dispositivo,dict):
            self.__dispositivo.update(nuevo_dispositivo)
        else: 
            print("Alguno de los valores ingresador no corresponde a las caracteristicas de un dispositivo")


#------------------------------------------------
#------------------------------------------------

# estos serian los objetos, de ejemplo, que nombro como paciente 1,2 y 3 respectivamente para resumir.

paciente1 = paciente(
    dni="12345678",
    nombre="Juan",
    apellido="Pérez",
    fechaNacimiento="01/01/1980",
    patologia="Hipertensión",
    telefono1="1234567890",
    telefono2="0987654321",
    email="juan.perez@example.com",
    direccion="Calle Falsa 123"
)

# Actualizar el análisis de sangre
nuevo_analisis = {
    "colesterol Total": "200",
    "colesterol HDL": "60",
    "colesterol LDL": "130",
    "trigliceridos": "150",
    "BNP": "100"
}
paciente1.actualizar_analisis(nuevo_analisis)

# Actualizar el monitoreo remoto
nuevo_monitoreo = {
    "ritmo_cardiaco": "75",
    "fecha": "17/05/2024",
    "hora": "12.30"
}
paciente1.actualizar_monitoreo(nuevo_monitoreo)

# Actualizar el monitoreo remoto
nuevo_dispositivo = {
    "MAC" : "00:1B:44:11:3A:B7",
    "Marca" : "AMEDTEC Medizintechnik",
    "Modelo" : "HOLTER-RR 24H ABPM",
    "Fecha de colocacion" : "01/01/2023"            
    }

#---------------------------

paciente2 = paciente(
    dni="38491711",
    nombre="Vittorio",
    apellido="Durigutti",
    fechaNacimiento="09/08/1994",
    patologia="Hipotension",
    telefono1="2964479362",
    telefono2="2964479363",
    email="vittodutti@example.com",
    direccion="Nueva Zelanda 105 PA"
)

nuevo_analisis = {
    "colesterol Total": "180",
    "colesterol HDL": "63",
    "colesterol LDL": "123",
    "trigliceridos": "142",
    "BNP": "89"
}
paciente1.actualizar_analisis(nuevo_analisis)

nuevo_monitoreo = {
    "ritmo_cardiaco": "68",
    "fecha": "17/03/2024",
    "hora": "16:00"
}
paciente1.actualizar_monitoreo(nuevo_monitoreo)

nuevo_dispositivo = {
    "MAC" : "00:1F:6B:00:7C:D7",
    "Marca" : "AMEDTEC Medizintechnik",
    "Modelo" : "HOLTER-RECORDER EP830",
    "Fecha de colocacion" : "05/03/2024"            
    }

#---------------------------

paciente3 = paciente(
    dni="42425656",
    nombre="Guadalupe",
    apellido="Saravia",
    fechaNacimiento="27/01/2002",
    patologia="Hipertension",
    telefono1="3515965522",
    telefono2="3516363222",
    email="guadalupesaravia@example.com",
    direccion="Nueva Zelanda 105 PA"
)

nuevo_analisis = {
    "colesterol Total": "210",
    "colesterol HDL": "40",
    "colesterol LDL": "130",
    "trigliceridos": "160",
    "BNP": "120"
}
paciente1.actualizar_analisis(nuevo_analisis)

nuevo_monitoreo = {
    "ritmo_cardiaco": "112",
    "fecha": "15/03/2024",
    "hora": "18:30"
}
paciente1.actualizar_monitoreo(nuevo_monitoreo)

nuevo_dispositivo = {
    "MAC" : "00:1F:6F:2D:C6:18",
    "Marca" : "AMEDTEC Medizintechnik",
    "Modelo" : "HOLTER-RECORDER EP830-12",
    "Fecha de colocacion" : "11/01/2024"            
    }

#------------------------------------------------
#------------------------------------------------

# Aqui esta el diccionario, con el listado de los pacientes. Y donde se ingresarian los nuevos pacientes
pacientes = {
    paciente1.dni: paciente1,
    paciente2.dni: paciente2,
    paciente3.dni: paciente3
}

#------------------------------------------------
#------------------------------------------------

# Menu para ingreso de opciones de carga, actualizacion o traer valores de pacientes.
# Cada opcion remite a los metodos correspondientes para el ingreso o actualizacion correspondientes.

while True:
    print("\n=== Menú ===")
    print("1. Mostrar datos del paciente")
    print("2. Actualizar análisis de sangre")
    print("3. Actualizar monitoreo remoto")
    print("4. Actualizar dispositivo")
    print("5. Crear nuevo paciente")
    print("6. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == "1":
        dni = input("Ingrese el DNI del paciente: ")
        if dni in pacientes:
            paciente = pacientes[dni]
            print("Datos del paciente:")
            print("DNI:", paciente.dni)
            print("Nombre:", paciente.nombre)
            print("Apellido:", paciente.apellido)
            print("Fecha de nacimiento:", paciente.fechaNacimiento)
            print("Ritmo cardíaco:", paciente.ritmo_cardiaco)
            print("Análisis de sangre:", paciente.analisis_sangre)
            print("Dispositivo:", paciente.nuevo_dispositivo)
        else:
            print("El paciente no existe.")
    
    elif opcion == "2":
        nuevo_analisis = {
            "colesterol Total":input("favor ingrese el valor de colesterol indicado en su analisis"),
            "colesterol HDL":input("favor ingrese el valor de colesterol indicado en su analisis"),
            "colesterol LDL":input("favor ingrese el valor de colesterol indicado en su analisis"),
            "triglicerios":input("favor ingrese el valor de colesterol indicado en su analisis"),
            "BNP":input("favor ingrese el valor de colesterol indicado en su analisis")            
        }

        dni=input("Ingrese el DNI del paciente: ")
        if dni in pacientes:
            paciente = pacientes[dni]
            paciente.actualizar_analisis(nuevo_analisis)
        else:
            print ("El paciente no existe en nuestra base de datos. Por favor intetne nuevamente.")

    elif opcion == "3":
        nuevo_monitoreo = {
            "ritmo_cardiaco" : input ("Favor ingrese el valor indicado en su dispositivo de monitoreo"),
            "fecha" : input ("Favor ingrese el valor indicado en su dispositivo de monitoreo"),
            "hora" : input ("Favor ingrese el valor indicado en su dispositivo de monitoreo")            
        }

        dni=input ("ingrese el DNI del paciente: ")
        if dni in pacientes:
            paciente = pacientes[dni]
            paciente.actualizar_monitoreo(nuevo_monitoreo)
        else:
            print("El paciente no existe en nuestra base de datos. Por favor intetne nuevamente.")

    elif opcion == "4":
        nuevo_dispositivo = {
            "MAC" : input("Favor ingrese la MAC correspondiente ubicada en la etiqueta del dorso del dispositivo"),
            "Marca" : input("Favor ingrese la marca correspondiente ubicada en la etiqueta del dorso del dispositivo"),
            "Modelo" : input("Favor ingrese el modelo correspondiente ubicado en la etiqueta del dorso del dispositivo"),
            "Fecha de colocacion" : input("Favor ingrese la fecha en formato dd/mm/yyyy en que adquiro el equipo")     
        }

        dni = input ("ingrese el DNI del paciente: ")
        if dni in pacientes:
            paciente = pacientes[dni]
            paciente.actualizar_dispositivo(nuevo_dispositivo)
        else:
            print("El paciente no existe en nuestra base de datos. Por favor intetne nuevamente.")

    elif opcion == "5":
        print ("Ingrese los siguientes datos sobre el nuevo paciente para poder crear su perfil")

        dni = input ("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fechaNacimiento = input ("Fecha de Nacimiento: ")
        patologia = input ("Patologia: ")
        telefono1= input ("Telefono de contacto: ")
        telefono2= input ("Otro telefono de contacto: ")
        email = input("E-mail: ")
        direccion = input("Direccion: ")

        nuevo_paciente = paciente (dni,nombre,apellido,fechaNacimiento,patologia,telefono1,telefono2,email,direccion)
        paciente[dni] = nuevo_paciente

        print ("El paciente a sido creado con exito. Recuerde que los campos de analisis de sandre, monitoreo remoto y dispositivo aun no se encentran cargados en el sistema.")

    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")