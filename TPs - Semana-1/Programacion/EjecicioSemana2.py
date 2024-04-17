# 2.1 Realizar una función que calcule el descuento en la compra de acuerdo a su valor.

Compra=int(input("Buenos dias, ingrese el monto de compra "))

if Compra >= 500:
    pago=Compra*0.90
    print ("Usted debe abonar $ ", pago)

else: 
    pago=Compra*0.95
    print ("Usted debe abonar $ ", pago)

#2.2 Crear una función llamada "calcular_area_circulo" que reciba el radio de un círculo como argumento y calcule y devuelva el área del círculo. Les recuerdo que el área de un círculo se calcula con la fórmula: área = pi * radio^2 y pi tiene un valor aproximado de 3.141592. No olviden pensar los tipos de datos que se utilizarán y escribir el Docstring correspondiente.


radio=int(input("ingrese el valor del radio "))

def calcular_area_circulo(radio):
    pi=3.141592
    area= pi* (radio**2)
    return area
    

area= calcular_area_circulo(radio)
print(f"el area del circulo con un radio de {radio} cm, es de {area} cm")

#Una estación meteorológica, informa la dirección del viento con una codificación numérica del 0 al 7 para representar las diferentes direcciones del viento de la siguiente manera:
#Crear una función que reciba el número de dirección del viento y lo traduzca en una cadena de texto correspondiente a la dirección real. Esta cadena de texto deberá ser impresa en pantalla para que los operadores puedan leerla fácilmente.
#Recuerda utilizar nombres descriptivos para tu función y las variables que utilices

direccionViento={
    "0":"Norte",
	"1":"Noreste",
	"2":"Este",
	"3":"Sureste",
	"4":"Sur",
	"5":"Suroeste",
	"6":"Oeste",
	"7":"Noroeste"
}

def codifNumerica(valor):
    return direccionViento.get(valor, "valor no corresponde con ningun valor de la estacion")

valor = str(input("ingrese uno de los numeros correspondientes a la siguiente codificacion numerica, para optener la direccion del viento")) 
print (f"La direccion del viento es {codifNumerica(valor):}")

#La estación meteorológica, registra la velocidad del viento en diferentes momentos del día. Se desea calcular la velocidad promedio del viento para publicarla en una página web.
#Para esto, crear una función llamada "calcular_velocidad_promedio" que reciba una lista de velocidades del viento y devuelva la velocidad promedio. La velocidad del viento se expresa en metros por segundo.

Ingreso_registro_velocidades = input("Ingrese las velocidades registradas en valores de 3 dígitos, completando los dígitos primeros con 0 de ser menor que 100 Km/h: ")
velocidades_del_viento = [Ingreso_registro_velocidades[i:i+3] for i in range(0, len(Ingreso_registro_velocidades), 3)]
velocidades_del_viento = [int(v) for v in velocidades_del_viento]


print(velocidades_del_viento)

def calcular_velocidad_promedio(velocidades_del_viento):
    velocidad_promedio=(sum(velocidades_del_viento))/(len(velocidades_del_viento))
    return velocidad_promedio

velocidad_promedio=calcular_velocidad_promedio(velocidades_del_viento)
print (f"Le valocidad promedio, en pos de los valores ingresados es de {velocidad_promedio} km/h")

#2.5 La estación también informa el porcentaje de carga de su batería interna. Crear una función llamada "estado_bateria" que reciba un número entero que representa el porcentaje de carga de la batería y devuelva un mensaje indicando el estado actual de la batería.

carga_bateria=int(input("Ingrese el valor de carga de su bateria en este momento: "))

def estado_bateria(carga_bateria):
    if carga_bateria >= 80:
        estado="Cargada" 
    elif 30 <= carga_bateria >= 79:
        estado=("Carga media")
    elif carga_bateria <= 29:
        estado=("Carga baja, REEMPLAZAR") 
    else:
        estado= "Error" 
    return estado

estado_carga_bateria=estado_bateria(carga_bateria)
print(f"actualmente su bateria se encuentra {estado_carga_bateria}")
