# contador = 0
# print (str(contador) + " elevado a la 2 es igual a " + str(2**contador))

def run():
    LIMITE = 10000000

    contador = 0
    numero = int(input("Por favor ingrese un numero para verificar la operacion: "))
    potencia = numero**contador
    while potencia < LIMITE:
        print ("El valor "+ str(numero) +" elevado a la " + str(contador) + " es igual a " + str(numero**contador))
        contador = contador + 1
        potencia = numero**contador


if __name__ =="__main__":
    run()