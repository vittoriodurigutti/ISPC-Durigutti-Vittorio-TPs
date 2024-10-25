/*
Proyecto final correspondiente al modulo de programacion, base de datos y, etica y deaontologia profesional
-------------------------------------------
Integrantes:
Luciano Lujan | GitHub: https://github.com/lucianoilujan
Durigutti, Vittorio | GitHub: https://github.com/vittoriodurigutti
Joaquin Zalazar | GitHub: https://github.com/breaakerr
Lisandro Juncos | GitHub: https://github.com/Lisandro-05
-------------------------------------------

En el documento a contiunacion se crea la base de datos bajo el nombre PROYECTO_ISPC, 
y a continuacion las 3 tablas correspondientes a las entidades principales.

Y en ultima instancia se crean a modo de ejemplo 2 objetos de cada entidad, para poder realizar consultas.
*/

-- Comando para creacion de la base de datos, con el aditivo "IF NOT EXIST" para que no genere errores al ejecutar el script repetidas veces
CREATE DATABASE IF NOT EXISTS PROYECTO_ISPC;
-- Este comando indica cual es la base de datos, que queremos dar inicio.
USE PROYECTO_ISPC;

-- El script crea la tabla "pacientes". Mas extensa y en escencia la base de esta base de datos.
-- Se compone de 3 de las entidades indicadas en el esquema entidad relacion, siendo esta paciente, contacto y direccion que son una extension de la otra.alter
-- En la definicion de la clase paciente dentro del codigo python, se plantearon estas ultimas dos como diccionarios, dentro de la ya indica clase paciente.
 -- El apartado DNI funcionanara como id_paciente en la tabla turnos
CREATE TABLE IF NOT EXISTS pacientes (
    DNI VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    Telefono1 VARCHAR(20) NOT NULL,
    Telefono2 VARCHAR(20),
    Email VARCHAR(100),
    Provincia VARCHAR(50),
    Ciudad VARCHAR(50),
    Calle VARCHAR(100),
    CP VARCHAR(10),
    Numero VARCHAR(10),
    Depto VARCHAR(10)
);
 
 -- Similar a la tabla de paciente, constituida por menor cantidad de atributos.
 -- El apartado DNI funcionanara como id_medico en la tabla turnos
CREATE TABLE IF NOT EXISTS medicos (
    DNI VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Especialidad VARCHAR(50) NOT NULL,
    Email VARCHAR(100)
);
 
 -- Tabla en la que se registran los turnos, y que servira tambien como principal tabla para interconsultas. 
 -- Como mencionado previamente, contiene 2 claves foraneas correspondientes a id_medico e id_paciente
CREATE TABLE IF NOT EXISTS turnos (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente VARCHAR(20) NOT NULL,
    id_medico VARCHAR(20) NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Especialidad VARCHAR(50) NOT NULL,
    Motivo_consulta TEXT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(DNI),
    FOREIGN KEY (id_medico) REFERENCES medicos(DNI)
);


-- Aqui desarrollamos los scripts para introducir dos objetos de ejemplo en cada tabla, a fin de poder hacer consultas de ejemplo y prueba.
	INSERT INTO pacientes (DNI, Nombre, Apellido, Fecha_Nacimiento, Telefono1, Telefono2, Email, Provincia, Ciudad, Calle, CP, Numero, Depto) VALUES 
	('12345678', 'Juan', 'Pérez', '1980-01-01', '1234567890', '0987654321', 'juan.perez@example.com', 'Córdoba', 'Córdoba', 'Calle Falsa', '5000', '123', 'A'),
	('87654321', 'María', 'González', '1990-01-01', '0987654321', '1234567890', 'maria.gonzalez@example.com', 'Córdoba', 'Córdoba', 'Calle Verdadera', '5000', '321', 'B');

	INSERT INTO medicos (DNI, Nombre, Apellido, Especialidad, Email) VALUES 
	('11223344', 'Carlos', 'Rodríguez', 'Cardiología', 'carlos.rodriguez@example.com'),
	('44332211', 'Ana', 'Martínez', 'Neurología', 'ana.martinez@example.com');

	INSERT INTO turnos (id_paciente, id_medico, Fecha, Hora, Especialidad, Motivo_consulta) VALUES 
	('12345678', '11223344', '2024-06-10', '10:00:00', 'Cardiología', 'Control rutinario'),
	('87654321', '44332211', '2024-06-11', '11:00:00', 'Neurología', 'Dolor de cabeza persistente');