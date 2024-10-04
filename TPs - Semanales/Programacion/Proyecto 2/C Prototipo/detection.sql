-- Tabla CLIENTE
CREATE TABLE Cliente (
    dni_cliente VARCHAR(10) PRIMARY KEY,  -- DNI único 
    nombre VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(15),
    direccion_contacto VARCHAR(255)
);

-- Tabla CONTROLADOR
CREATE TABLE Controlador (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,  -- Clave primaria autoincremental
    mac_dispositivo VARCHAR(17) UNIQUE NOT NULL,  -- MAC Address única y no nula
    nombre_dispositivo VARCHAR(100),
    dni_cliente VARCHAR(10),  -- Relación con Cliente (mismo tipo que en Cliente)
    ubicacion_dispositivo VARCHAR(255),  -- Ubicación física del dispositivo
    FOREIGN KEY (dni_cliente) REFERENCES Cliente(dni_cliente) ON DELETE CASCADE -- Relación con Cliente
);

-- Tabla HABITACION
CREATE TABLE Habitacion (
    id_habitacion INT AUTO_INCREMENT PRIMARY KEY,  -- Clave primaria autoincremental
    nombre_habitacion VARCHAR(100) NOT NULL,  -- Nombre no nulo
    id_dispositivo INT,  -- FK hacia Controlador
    FOREIGN KEY (id_dispositivo) REFERENCES Controlador(id_dispositivo) ON DELETE CASCADE  -- Relación con Controlador
);

-- Tabla SENSOR_ACTUADOR
CREATE TABLE Sensor_Actuador (
    id_sensor_actuador INT AUTO_INCREMENT PRIMARY KEY,  -- Clave primaria autoincremental
    estado_sensor_actuador ENUM('activo', 'inactivo', 'en mantenimiento') DEFAULT 'activo',
    id_habitacion INT,  -- FK hacia Habitación
    FOREIGN KEY (id_habitacion) REFERENCES Habitacion(id_habitacion) ON DELETE CASCADE  -- Relación con Habitación
);

-- Tabla LECTURA 
CREATE TABLE Lectura (
    id_lectura INT AUTO_INCREMENT PRIMARY KEY,  -- Clave primaria autoincremental
    fecha_hora DATETIME NOT NULL,  -- Fecha y hora del incidente
    nivel_gas FLOAT NOT NULL,  -- Nivel de gas detectado
    id_sensor_actuador INT,  -- FK hacia Sensor_Actuador
    FOREIGN KEY (id_sensor_actuador) REFERENCES Sensor_Actuador(id_sensor_actuador) ON DELETE CASCADE  -- Relación con Sensor_Actuador
);

-- Carga de datos genericos para poder realizar consulta en las tablas. 
USE GASDETECTOR;

-- Insertar clientes
INSERT INTO Cliente (dni_cliente, nombre, email, telefono, direccion_contacto) VALUES
('20123456', 'Juan Pérez', 'juan.perez@mail.com', '1134567890', 'Calle Falsa 123, Buenos Aires, Argentina'),
('20456789', 'María López', 'maria.lopez@mail.com', '1145678901', 'Avenida Siempre Viva 456, Rosario, Argentina'),
('30123456', 'Carlos Gómez', 'carlos.gomez@mail.com', '1156789012', 'Calle Sol 789, Córdoba, Argentina'),
('30456789', 'Ana Martínez', 'ana.martinez@mail.com', '1167890123', 'Avenida Libertad 321, Mendoza, Argentina'),
('40123456', 'Luis Fernández', 'luis.fernandez@mail.com', '1178901234', 'Calle Luna 654, Mar del Plata, Argentina');

-- Insertar controladores (dispositivos)
INSERT INTO Controlador (mac_dispositivo, nombre_dispositivo, dni_cliente, ubicacion_dispositivo) VALUES
('00:1A:2B:3C:4D:5E', 'Controlador Juan', '20123456', 'Calle Falsa 123, Buenos Aires'),
('00:1A:2B:3C:4D:5F', 'Controlador María', '20456789', 'Avenida Siempre Viva 456, Rosario'),
('00:1A:2B:3C:4D:60', 'Controlador Carlos', '30123456', 'Calle Sol 789, Córdoba'),
('00:1A:2B:3C:4D:61', 'Controlador Ana', '30456789', 'Avenida Libertad 321, Mendoza'),
('00:1A:2B:3C:4D:62', 'Controlador Luis', '40123456', 'Calle Luna 654, Mar del Plata'),
('00:1A:2B:3C:4D:63', 'Controlador Juan 2', '20123456', 'Oficina Central, Buenos Aires'),
('00:1A:2B:3C:4D:64', 'Controlador María 2', '20456789', 'Sucursal Norte, Rosario'),
('00:1A:2B:3C:4D:65', 'Controlador Carlos 2', '30123456', 'Sucursal Centro, Córdoba');

-- Insertar habitaciones
INSERT INTO Habitacion (nombre_habitacion, id_dispositivo) VALUES
('Sala de Estar', 1),
('Cocina', 1),
('Comedor', 2),
('Baño', 2),
('Dormitorio Principal', 3),
('Sala de Estar', 3),
('Cocina', 4),
('Comedor', 5),
('Cocina', 6),
('Oficina', 7),
('Comedor', 8);

-- Insertar sensores/actuadores
INSERT INTO Sensor_Actuador (estado_sensor_actuador, id_habitacion) VALUES
('activo', 1),
('activo', 2),
('activo', 3),
('activo', 4),
('activo', 5),
('activo', 6),
('activo', 7),
('activo', 8),
('activo', 9),
('activo', 10),
('activo', 11);

-- Insertar lecturas de ejemplo
INSERT INTO Lectura (fecha_hora, nivel_gas, id_sensor_actuador) VALUES
(NOW(), 45.6, 1),
(NOW(), 20.4, 2),
(NOW(), 18.9, 3),
(NOW(), 100.2, 4),
(NOW(), 80.6, 5),
(NOW(), 95.1, 6),
(NOW(), 70.4, 7),
(NOW(), 110.9, 8),
(NOW(), 90.3, 9),
(NOW(), 65.2, 10),
(NOW(), 40.7, 11);

-- Verificacion de datos en las tablas, a fin de convalidad que ingresaron correctamente
SELECT * FROM Cliente;
SELECT * FROM Controlador;
SELECT * FROM Habitacion;
SELECT * FROM Sensor_Actuador;
SELECT * FROM Lectura;
