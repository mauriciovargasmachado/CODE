
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % 1 == 0:
            contador = contador + 1
    if contador == 0:
        return True
    else:
        return False 


def run():

    numero = int(input("Por favor escribe un numero: "))
    if es_primo(numero) == True:
        print (" El " + str(numero) + " que ha seleccionado es primo")
    else:
            print ("El " + str(numero) + " que ha seleccionado NO es primo")


if __name__ =="__main__":
    run()