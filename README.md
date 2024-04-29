# Reto_9
### Primer punto
De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
##### 1.1
Punto_6, Reto 8
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```
# Se declara la funcion principal "Main"
if __name__ == "__main__":
    #Se solicitan las variables
    num_contagiados = int (input("Ingrese el numero de contagiados actuales: "))
    num_dias = int (input("Ingrese numero de dias: "))
    #Se utiliza lambda 
    cantidad_total = (lambda x, y : y*2**x)(num_dias, num_contagiados)
    print (f"La cantidad de carne entre gallinas, gallos y pollitos es de : {cantidad_total} de contagiados")
```
##### 1.2
Punto_2, Taller_1 
Realice un programa que lea un número enteros y determine si es par o impar.
```
if __name__ == "__main__":
    #Se solicitan la variable a utilizar
    num_1 = float (input("Ingrese un  numero: "))
    #Se ejecuta lambda
    num_par = (lambda num_1: num_1 %2 == 0)(num_1)
    #Se imprime el resultado
    print (f"El numero es {num_par}")
```
##### 1.3
Punto 5, Reto_8
Calcular el valor de 2 elevado a la potencia n.
```
if __name__ == "__main__":
    #Se ingresa datos por consola
    numero = int (input("Ingrese que potencia desea elevar el numero 2 : "))
    #Se utiliza  la funcion lambda
    potecia: float = (lambda x : 2**x)(numero)
    print (f" 2 elevado a {numero} da como resultado: {potecia} ")
```

### Segundo punto
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

##### 2.1
Punto 1, Rerto_6

Una función matemática para calcular el volumen y el área superficial.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
Revise como utilizar el valor de pi usando import math y math.pi
```
#Se importa la liobreria Math que se utilizara en el desarrollo
from math import *

#Se defina las funciones 
def volumen_total (*args) ->float:
    #Se desarrollan las operaciones para calcular un determinado valor
    volumen_esfera = (4*pi*radio_uno**3)/3
    volumen_cono = (pi*altura*radio_dos)/3
    volumen_total = volumen_cono + volumen_esfera
    #Ya terminada las operaciones se retorna la variables finales 
    return volumen_total

def area_total (*args) ->float:
    area_cono : float= pi*radio_dos*(radio_dos + sqrt(radio_dos**2+altura**2))
    area_esfera = 4*pi*radio_uno**2
    area_total = area_cono + area_esfera
    return area_total


#Funcion principal Main
if __name__ == "__main__":
    #Se introducen por consola los valores a utilizar
    radio_uno = float (input("Ingrese el radio de la esfera: "))
    radio_dos = float (input("Ingrese el radio del cono: "))
    altura = float (input ("Ingrese la altura del cono: "))
    opcion = int (input("Ingrese el numero de la opcion que desea saber , [1]Volumen, [2]Area Superficial: "))
    #Se utiliza un if para saber que tipo de magnitud desea conocer
    if (opcion == 1):
        #Se crea una variable la cual va a contener el retorno de las funciones declaradas anteriormente
        volumen_total = volumen_total (radio_uno, radio_dos, altura)
        print (f"El volumento total de las figuras es: {volumen_total} [m^3]")
    if (opcion == 2):
        area_total = area_total (radio_uno, radio_dos, altura)
        print (f"El volumento total de las figuras es: {area_total} [m^2]")
else: 
    print ("Esa opcion no es adecuada")
```
##### 2.2
Punto 5, Taller_1
Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
```
# Se realizar la funcion que va operar los valores
def determinar_suma (*args) ->float:
    #Se declara e inicializa la variable suma
    suma : float = (num_uno + num_dos)
    #Con el conocional if se analiza si la condicion se cumple o no 
    if suma > num_tres:
        print ("La suma de "+str(num_uno)+ " + "+ str(num_dos) + " = "+ str(suma)+" es mayor que "+str(num_tres))
    else :
        if (suma < num_tres):
            #De acuerdo al caso que se cumpla se muestra el mensaje por consola
            print ("La suma de "+str(num_uno)+ " + "+str(num_dos) + " = "+ str(suma)+" es menor que "+str(num_tres))
        else:
            print ("La suma de "+str(num_uno)+ " + "+str(num_dos) + " = "+ str(suma)+" es igual que "+str(num_tres))

if __name__ == "__main__":
    #Se piden los valores por consola
    num_uno = float (input("Introduzca el primer numero: "))
    num_dos  = float (input("Introduzca el segundo numero: "))
    num_tres  = float( input("Introduzca el tercer numero: "))
    #Se llama a la funcion que va a evaluar los valores introducidos por consola
    respuesta  = determinar_suma (num_uno, num_dos, num_tres)
```
##### 2.3
Punto 9, Taller_1
Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.
```
#Se declara la funcion que va a evaluar el argumento
def verificar_pais (*Cualqui) ->float:
    #Se utiliza match case para comparar el argumento y si cumple con la condicion devuelva el texto
    match pais:
        case "colombia":
            print ("La capital de {} es Bogota".format(pais))
        case "venezuela":
            print ("La capital de {} es Caracas".format(pais))
        case "ecuador":
            print ("La capital de {} es Quito".format(pais))
        case "peru":
            print ("La capital de {} es Lima".format(pais))
        case "argentina":
            print ("La capital de {} es Buenos Aires".format(pais))
        case "chile":
            print ("La capital de {} es Santiago de Chile".format(pais))
        case "surinam":
            print ("La capital de {} es La Parabarimo".format(pais))
        case "brasil":
            print ("La capital de {} es Brasilia".format(pais))
        case "uruguay":
            print ("La capital de {} es Montevideo".format(pais))
        case "paraguay":
            print ("La capital de {} es Santiago de Chile".format(pais))
        case "bolivia":
            print ("La capital de {} es Sucre".format(pais))
        case "trinidad y tobago":
            print ("La capital de {} es Puerto España".format(pais))
        case _:
            print ("Pais NO IDENTIFICADO")

#Se declara la funcion principal
if __name__ == "__main__":
    #Se solicita por consola el dato
    pais = input ("Ingrese el nombre del país latinoamericano del cual quiere conocer su capital: ")
    pais = verificar_pais (pais)

```

### Tercer punto
Escriba una función recursiva para calcular la operación de la potencia

```
def potencia(base: int, exponente: int )-> int:
  # Caso base 
  if exponente == 1: 
    return base
  else:
    # Condicion de la funcion recursiva
    return base*potencia(base, exponente-1)

if __name__ == "__main__":
  #Ingreso de datos
  num_base = int(input("Ingrese la base: "))
  num_potencia = int(input("Ingrese la potencia: "))
  #Se llama a la funcion
  Num_potencia = potencia (num_base, num_potencia)
  print(f"El numero {num_base} elevado a {num_potencia} es: {Num_potencia}")

```
### Cuarto punto
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.
```
  
```
### Perfil de  stackoverflow
[Captura-de-pantalla-2024-04-29-164934.png](https://postimg.cc/PCyq7ySp)
- https://stackoverflow.com/users/24786586/dania-lorena-perez-moreno?tab=profile
### Perfil de Linkedin
[Captura-de-pantalla-2024-04-29-170536.png](https://postimg.cc/jLVCnLW5)
- www.linkedin.com/in/dania-perez


