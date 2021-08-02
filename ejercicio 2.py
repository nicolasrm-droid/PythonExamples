def Numero_primo():
    numero = 2
    yield numero #generador de numeros

    #ciclo while donde se comprueba si es primo o no
    while True:
        temp = numero #variable temporal
        while True:
          temp += 1
          contador = 1
          divisores = 0
          while contador <= temp: #contador va a empezar a contar desde 1 hasta donde este el numero de la varible temp
               if  temp % contador == 0: #el residuo es igual a 0
                     divisores += 1
               if divisores > 2:
                     break
               contador += 1

          if divisores == 2:
           yield  temp

NP = Numero_primo()
primos = [next(NP) for _ in range(2)]
print(primos)
