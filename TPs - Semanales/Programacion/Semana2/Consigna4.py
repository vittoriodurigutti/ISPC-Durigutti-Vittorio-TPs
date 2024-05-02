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