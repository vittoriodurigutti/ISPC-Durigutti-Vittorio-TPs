## Proyecto Integrador

### Objetivo
La empresa "Dispositivos Inteligentes SRL" nos ha encomendado la tarea de
diseñar y desarrollar un nodo IoT (Internet de las Cosas) capaz de registrar al menos
una variable importante en una base de datos. Este proyecto tiene como objetivo
aplicar tus conocimientos en electrónica y programación de microcontroladores para
crear un dispositivo inteligente que sea capaz de recopilar y almacenar datos
relevantes.
El esquema general del sistema a desarrollar se muestra en la siguiente
imagen:
1. Se dispondrá de sensores que midan al menos una variable de interés.
2. Este sensor será conectado a un microcontrolador (ESP32 o similar), el cual
enviará datos por algún protocolo de comunicación a una PC. Adicional a esto, cuando
la variable medida supere cierto umbral, se accionará un actuador.
3. En esta PC correrá un programa, a desarrollar, en Python que recibirá la
información enviada por el sistema embebido, y enviará datos a un Sistema Gestor de
Base de Datos local.
4
4. Por último, nuestro SGDB, almacenará los datos recibidos desde el
programa Python cliente.

--- 

## Esquema de trabajo

### Entrega 1
**Fecha de entrega (13/09/24)**

- Elegir una variable de interés que sea relevante, podría ser la temperatura ambiente, la humedad, la luminosidad, la presión atmosférica, o cualquier otro parámetro.
- Seleccionar un sensor adecuado para medir la variable elegida. Asegúrate de que el sensor sea compatible con el microcontrolador que utilizarás y que proporcione lecturas precisas.
- El dispositivo que estamos diseñando debe relevar la información producida por el Sensor, el nivel de batería del dispositivo y en base a un úmbral elegido, accionar un Actuador.
- Diseñar el esquema eléctrico considerando el sensor, la medición de nivel de batería y el actuador al microcontrolador.
- Documentar la elección y justificación de la variable y el sensor en un informe técnico. Explicar en base a que criterio se accionará el actuador.
- Incluir un resumen de la hoja de datos del sensor en el reporte que se entregará.

**Nota:** Si surgen dudas sobre la utilización de los elementos electrónicos, consultar con el docente sobre cómo se interconecta.
**Aclaración:** No es necesario adquirir el sensor, sólo hacer la selección y luego será simulado.

--- 

### Entrega 2

**Fecha de entrega (04/10/24)**
Creación de la base de datos en MySQL y el Programa en Python para almacenar la información que generará nuestro dispositivo.
Para esto:
- Diseñar la estructura y crear tablas necesarias.
- Proporcionar el esquema y el código de creación de la base de datos y
las tablas.
- Conectarse desde Python a la base de datos y escribir la información
recibida por el puerto de comunicación elegido, por ej: serie. Se deberá
leer el puerto con python y luego ingresar datos (INSERT INTO) a la BD.

**Nota:** Aún no tenemos corriendo el dispositivo, por lo que se puede utilizar
la función input() para generar información que ingrese al programa.

--- 

### Entrega 3

**Fecha de entrega (25/10/24)**
Escribir un programa que permita al microcontrolador recopilar datos del sensor
y prepararlos para su envío. Para esto, debe considerar la capacidad de comunicación
del Sistema embebido elegido.
- Realizar la programación del comportamiento del actuador.
- Probar la comunicación completa entre el dispositivo IoT y la PC. Realizar las correcciones necesarias y la optimización del sistema que consideres.
- Proporcionar el código fuente y documentación de los programas que se han escrito.
- Documentar las pruebas realizadas, las correcciones y cambios realizados a lo largo del proyecto.

---

### Defensa del proyecto

**Fecha de entrega: 04/11/24**
- Se deberán recuperar las entregas desaprobadas y se realizará una defensa oral del proyecto.
- Cada grupo deberá presentar su proyecto ante los docentes del módulo. La defensa oral tendrá una duración de 15 minutos por grupo y se evaluará la capacidad de los integrantes para explicar y defender su trabajo de manera clara y concisa. 
- Los integrantes del grupo deberán exponer de manera conjunta, distribuyendo el tiempo de manera equitativa.

**Pautas de grupo y entregable**
El presente trabajo práctico final integrador, se plantea para realizarse en grupo
de hasta 4 alumnos. Una vez confeccionado se debe entregar un archivo en PDF que
contenga lo siguiente:
- Desarrollo del prototipo:
- Identificación de los componentes y conexionado físico
- Programa embebido
- Código fuente en Python que incluya la temática seleccionada a
desarrollar, con las respectivas consultas a la base de datos
- Almacenamiento de información en Base de Datos

**Formato de entrega**
Cada entrega debe incluir un informe claro y completo que explique los detalles
técnicos y las decisiones tomadas en cada etapa del proyecto.
Este informe debe ser subido a la plataforma del instituto antes de la fecha
límite.
Se deberá entregar una ficha informativa que incluya:
- Título del proyecto
- Nombres completos de los integrantes del grupo
- Fecha de entrega
- Relato de problemática planteada (máximo 200 palabras)

**Extensión:** El informe final deberá tener una extensión de entre 10 y 20 páginas, escritas en letra Arial 12, a doble espacio, con márgenes de 2,5 cm.
**Formato:** El proyecto deberá presentarse en formato digital (PDF).
**Criterios de evaluación**
- Se evaluará la presentación y funcionamiento del proyecto, la capacidad de respuesta a las preguntas y la defensa general del trabajo.
- Cumplimentar TODAS las consignas.
- Entregas parciales en tiempo y forma.
- Proyecto completo al fin del 2° cuatrimestre
- Se podrán recuperar las entregas que no sean subidas a tiempo, con una penalidad sobre la nota final.