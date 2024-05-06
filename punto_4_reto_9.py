import time

#Se declara la funcion que va a evaluar el 
def calcular_tiempo (num)->float:
  #Se inicia el tiempo que va a tomar en cada iteracion
  start_time = time.time()
  #Serie de Fibonacci
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= num):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1 
  #Finaliza el tiempo que tarda la iteracion
  end_time = time.time()
  #Se calcula el tiempo total
  timer = end_time - start_time
  #Se retorna los valores que se van a utilizar
  return n2, timer



if __name__ == "__main__":
    #Se declaran e inicializar las variables
    num : int = 0
    serie : int = 0
    #Seutiliza un bucle While para que se detenga cuando el tiempo de la iteracion sea igual o mayor a 0.1 (Se declara ese valor como significativo)
    while serie <= 0.1:
        suma, tiempo = calcular_tiempo (num)
        num +=1
        print (f"En la serie de {num} el tiempo se vuelve significativo ya que tarda {tiempo} y su suma es {suma}")
    

'''
if __name__ == "__main__":
    num : int = 0
    timer : int = 0
    #Se propone otra forma de solucion :)
    while timer <= 0.1:
        start_time = time.time()
        serie = calcular_tiempo (num)
        end_time = time.time()
        timer = end_time - start_time
        num +=1
        print (f"En la serie de {num} el tiempo se vuelve significativo ya que tarda es {timer}")
    


'''