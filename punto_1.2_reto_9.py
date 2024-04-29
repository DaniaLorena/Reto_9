'''
Punto 5, Reto_8
Calcular el valor de 2 elevado a la potencia n.
'''

if __name__ == "__main__":
    #Se ingresa datos por consola
    numero = int (input("Ingrese que potencia desea elevar el numero 2 : "))
    #Se utiliza  la funcion lambda
    potecia: float = (lambda x : 2**x)(numero)
    print (f" 2 elevado a {numero} da como resultado: {potecia} ")

