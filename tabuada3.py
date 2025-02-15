tabuada = 1
contador = 1

while tabuada <=10:
    while contador <=10:
        resultado = tabuada * contador
        print (tabuada, "*", contador, "=", resultado)
        contador  += 1
    print("")
    tabuada +=1
    contador = 1