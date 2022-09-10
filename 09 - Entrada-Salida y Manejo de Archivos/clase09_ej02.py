import sys

if (len(sys.argv)== 2):
    import datetime
    import os
    tiempo = datetime.datetime.now()
    tiempo = int(datetime.datetime.timestamp(tiempo))

    lluvia = sys.argv[1]
    temperatura = input('Ingrese la temperatura en grados centígrados')
    humedad = input('Ingrese el porcentaje de humedad')
    linea = str(tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    logs_lluvia = open('clase09_ej02.csv', 'a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()

else:
    print("ERROR: Debe ingresar 3 valores (3)")
    print('Ejemplo: <temperatura> <humedad> <True o False>')

