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
	"7":"Noroeste",
}

def codifNumerica(valor):
    return direccionViento.get(valor, "valor no corresponde con ningun valor de la estacion")

valor = str(input("ingrese uno de los numeros correspondientes a la siguiente codificacion numerica, para optener la direccion del viento ")) 
print (f"La direccion del viento es {codifNumerica(valor):}")