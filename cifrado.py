import string
# El limite de desplazamiento es 11 sin embargo para textos largos aplica hasta 6
desplazamiento =4

def codifica (texto):
    cifrado = ""
    if texto == texto.upper():
        lista = list(string.ascii_uppercase)
    else:
        lista = list(string.ascii_lowercase)

    for car in texto:
        if car in lista:
            cifrado += lista[(lista.index(car)+ desplazamiento%(len(lista)))]
        else:
            cifrado += car

    print(cifrado)
    return cifrado

def decodifica (texto):
    decifrado = ""
    if texto == texto.upper():
        lista = list(string.ascii_uppercase)
    else:
        lista = list(string.ascii_lowercase)

    for car in texto:
        if car in lista:
            decifrado += lista[(lista.index(car) - desplazamiento%(len(lista)))]
        else:
            decifrado += car

    print(decifrado)
    return decifrado

if __name__ == "__main__":
    cifrado = codifica("CUIDADO")
    decifrado = decodifica(cifrado)


   #