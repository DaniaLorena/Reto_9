'''
Reto 8_ punto6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se
 han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
'''
# Se declara la funcion principal "Main"
if __name__ == "__main__":
    #Se solicitan las variables
    num_contagiados = int (input("Ingrese el numero de contagiados actuales: "))
    num_dias = int (input("Ingrese numero de dias: "))
    #Se utiliza lambda 
    cantidad_total = (lambda x, y : y*2**x)(num_dias, num_contagiados)
    print (f"La cantidad de carne entre gallinas, gallos y pollitos es de : {cantidad_total} de contagiados")

