import random

def run():

    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido <= numero_aleatorio:
            print("Elige un numero mas grande")
        else:
            print("Elige un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero: "))
    print ("haz adivinado mi numero!!!! Ganaste!!!")
        
            
if __name__ =="__main__":
    run()