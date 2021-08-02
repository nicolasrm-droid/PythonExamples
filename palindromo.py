def palindromo(frase):

    frase = frase.lower()
    frase = frase.replace(' ','')
    longitud = len(frase)

    if longitud % 2 == 0:
        izquierda = frase [: longitud // 2]
        derecha = frase[longitud //2:]
    else:
        izquierda = frase [: longitud // 2 ]
        derecha = frase[longitud //2 + 1:]
    if not frase :
        print("escriba una frase")



    print(izquierda)
    print(derecha)

    return izquierda == derecha [::-1] #expresion de slicing lectura de derecha a izquierda

print(palindromo(input("Escriba para verificar si es un palindromo: ")))
