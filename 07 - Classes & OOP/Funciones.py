from math import factorial


class Funciones: 
    def __init__(self,lista):
        self.lista = lista
    
    def lista_primos(self):
        for i in self.lista:
            if (self.numero_primo(i)):
                print(i, 'Si es primo')
            else:
                print(i, 'No es primo')

    def numero_primo(self, n):
        primo = True
        for i in range (2,n):
            if (n%i == 0):
                primo = False
                break
            return primo 

    def conv_grados(self,origen, destino):
        for i in self.lista:
            print(i,'grado',origen,'son', self.conversion_grados(i,origen,destino), destino ) 
    
    def conversion_grados(self, valor, origen, destino):
        num_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                num_destino = valor
            elif (destino == 'farenheit'):
                num_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                num_destino = valor + 273.15
            
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                num_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                num_destino = valor
            elif (destino == 'kelvin'):
                num_destino = ((valor - 32) * 5 / 9) + 273.15

        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                num_destino = valor - 273.15
            elif (destino == 'farenheit'):
                num_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                num_destino = valor

        else:
            print('Parámetro de Origen incorrecto')
        return num_destino

    def num_factorial(self):
        for i in self.lista:
            print('El factorial de',i , 'es',factorial(i))

    def factorial(self,numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser positivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero
