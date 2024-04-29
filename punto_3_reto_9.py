
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