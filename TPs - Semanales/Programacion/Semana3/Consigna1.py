"""4.1 Crea una clase que representa una estación meteorológica, la cual debe incluir:
* Latitud y longitud donde está instalada la estación (Propiedades de la clase).
* Estado de batería.
* Conversión de Dirección del viento (Métodos)."""

"""4.2 Agregar de acuerdo a nuestro criterio:
* Medición de temperatura.
* Registro de cantidad de lluvia caída.
* Otras características y funcionalidades que consideres relevante."""


class EstacionMeterologica:
    def __init__(self, latitud,longitud,carga_bateria):
        self.latitud = latitud
        self.longitud = longitud
        self.estado_carga_bateria=carga_bateria
        self.TablaConversionDV={
            "0":"Norte",
            "1":"Noreste",
            "2":"Este",
            "3":"Sureste",
            "4":"Sur",
            "5":"Suroeste",
            "6":"Oeste",
            "7":"Noroeste",
            }

    def estadoBateria(self):
        if self.cargaBateria >= 80:
            estado="nivel de carga: alto"
        elif 30<= self.cargaBateria <= 79:
            estado="nivel de carga: medio"
        elif self.cargaBateria <=29:
            estado="nivel de carga bajo"
        else:
            "error en el valor ingresado"
            return estado
    
    def direccionViento(self, valor):
        return self.TablaConversionDV.get(valor, "El dato brindado no corresponde a un valor definido en la tabla")
    
    def actualizarTemperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura

    def actualizarLluvia(self, nueva_lluvia):
        self.lluvia = nueva_lluvia


Estacion1 = EstacionMeterologica(40.7128, -74.0060, 100)


print (Estacion1.direccionViento("4"))