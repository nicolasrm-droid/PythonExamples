# para correr el programa es con la tecla F5
# ejercicio 1
Number = int(input("Introduce un número entero: "))
sum = Number + Number
mult = Number * Number

if Number % 2 == 0:
    print("El número " + str(Number) + " es par")
    print(str(Number) + "+" + str(Number) )
    print(sum)
else:
    print("El número " + str(Number) + " es impar")
    print(str(Number) + "+" + str(Number) )
    print(mult)
# **********************************************************
