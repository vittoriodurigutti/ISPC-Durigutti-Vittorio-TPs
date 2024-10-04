meses= ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "dicimebre"]

estaciones = ["verano", "otoño", "invierno", "primavera"]


dia= int(input ("favor ingrese el dia "))
mes= input("favor ingrese el mes " ).lower()
indiceMes=meses.index(mes)

if  indiceMes in [0,1]  or (indiceMes==11 and dia >= 21) or (indiceMes==2 and dia<21):
    estacion = estaciones[0]
elif indiceMes in [3, 4]  or (indiceMes==2 and dia >= 21) or (indiceMes==5 and dia<21):
    estacion = estaciones[1]
elif indiceMes in [6, 7]  or (indiceMes==5 and dia >= 21) or (indiceMes==8 and dia<21):
    estacion = estaciones[2]
elif indiceMes in [9, 10]  or (indiceMes==8 and dia >= 21) or (indiceMes==11 and dia<21):
    estacion = estaciones[3]
else:
    estacion = "ERROR"

print ("la estacion del año es " + estacion)