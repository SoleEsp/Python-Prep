import sys

# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

if (len(sys.argv) == 4):
    print("Primer parametro: ",sys.argv[1])
    print("Segundo parametro: ",sys.argv[2])
    print("Tercer parametro: ",sys.argv[3])
else:
    print("ERROR: Debe ingresar 3 parametros")
    print('Ejemplo: 1 2 3')

print("El argumento 0 es el nombre del archivo:", sys.argv[0])