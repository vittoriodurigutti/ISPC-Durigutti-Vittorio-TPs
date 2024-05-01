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