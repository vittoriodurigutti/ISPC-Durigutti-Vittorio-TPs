#2.2 Crear una función llamada "calcular_area_circulo" que reciba el radio de un círculo como argumento y calcule y devuelva el área del círculo. Les recuerdo que el área de un círculo se calcula con la fórmula: área = pi * radio^2 y pi tiene un valor aproximado de 3.141592. No olviden pensar los tipos de datos que se utilizarán y escribir el Docstring correspondiente.


radio=int(input("ingrese el valor del radio "))

def calcular_area_circulo(radio):
    pi=3.141592
    area= pi* (radio**2)
    return area
    

area= calcular_area_circulo(radio)
print(f"el area del circulo con un radio de {radio} cm, es de {area} cm")