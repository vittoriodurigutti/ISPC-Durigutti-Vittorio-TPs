"""4.1 Crea una clase que representa una estación meteorológica, la cual debe incluir:
* Latitud y longitud donde está instalada la estación (Propiedades de la clase).
* Estado de batería.
* Conversión de Dirección del viento (Métodos)."""



class EstacionMeterologica:
    Latitud = 
    Longitud = 

    def EstadoBateria(cargaBateria):
        if cargaBateria >= 80:
            estado="nivel de carga: alto"
        elif 30<= cargaBateria <= 79:
            estado="nivel de carga: medio"
        elif cargaBateria <=29:
            estado="nivel de carga bajo"
        else:
            "error en el valor ingresado"
            return estado
    
    estado_carga_bateria=EstadoBateria(cargaBateria)
    print(f"{estado_carga_bateria}")


    TablaConversionDV={
    "0":"Norte",
	"1":"Noreste",
	"2":"Este",
	"3":"Sureste",
	"4":"Sur",
	"5":"Suroeste",
	"6":"Oeste",
	"7":"Noroeste",
    }

    def direccionViento(valor):
        return TablaConversionDV.get(valor, "El dato brindado no corresponde a un valor definido en la tabla")
    





