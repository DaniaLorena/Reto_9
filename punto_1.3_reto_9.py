'''
Punto_2, Taller_1 Realice un programa que lea un número enteros y determine si es par o impar.
'''

if __name__ == "__main__":
    #Se solicitan la variable a utilizar
    num_1 = float (input("Ingrese un  numero: "))
    #Se ejecuta lambda
    num_par = (lambda num_1: num_1 %2 == 0)(num_1)
    #Se imprime el resultado
    print (f"El numero es {num_par}")

