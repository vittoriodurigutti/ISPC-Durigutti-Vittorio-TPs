-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS MiBaseDeDatos;

-- Usar la base de datos
USE MiBaseDeDatos;

-- Tabla Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    DNI INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellidos VARCHAR(100),
    Direccion VARCHAR(200),
    Email VARCHAR(100),
    Telefono VARCHAR(15)
);

-- Tabla Contratos
CREATE TABLE IF NOT EXISTS Contratos (
    Num_Contato INT PRIMARY KEY,
    DNI_cliente INT,
    Cod_plan INT,
    Fecha_inicio DATE,
    FOREIGN KEY (DNI_cliente) REFERENCES Clientes(DNI),
    FOREIGN KEY (Cod_plan) REFERENCES Planes(Cod_plan)
);

-- Tabla Planes
CREATE TABLE IF NOT EXISTS Planes (
    Cod_plan INT PRIMARY KEY,
    Descripcion VARCHAR(255),
    Precio DECIMAL(20, 2)
);

-- Tabla Equipos
CREATE TABLE IF NOT EXISTS Equipos (
    Num_serie INT PRIMARY KEY,
    modelo VARCHAR(100),
    Num_Contato INT,
    FOREIGN KEY (Num_Contato) REFERENCES Contratos(Num_Contato)
);
