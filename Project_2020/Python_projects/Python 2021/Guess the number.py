import random


def adivina_el_numero(x):

    print("===============================================================")
    print("==================Bienvenido al Juego==========================")
    print("===============================================================")
    print("===Tu meta es adivinar el numero generado por la computadora===")
    print("===============================================================")

    numero_aleatorio = random.randint(1,x) #numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int (input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print ("Intenta otra vez, el numero es mayor que esto")
        
        elif prediccion > numero_aleatorio:
            print ("Intenta nuevamente, el numero es menor que esto")

    print (f"Felicitaciones adivinaste el numero {numero_aleatorio} correctamente!!! Gracias por participar!!!")


adivina_el_numero (100)