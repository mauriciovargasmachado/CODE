# def imprimir_mensaje():
#   print = ("mensaje especial: ")
#   print = ("Estoy aprendiendo a usar funciones: ")
# imprimir_mensaje()


# def suma (a,b):
#     print("Se sumaran dos numeros!")
#     resultados = a + b
#     return resultados
# sumatoria = suma (1,4)
# print (sumatoria)


def conversacion(mensaje):
    print("Hola")
    print("Como estas?")
    print(mensaje)
    print("Adios")


opcion = int(input("elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
       conversacion("Elegiste la opcion 2")
elif opcion == 3:
        conversacion("Elegiste la opcion 3")
else:
    print("La opcion elegida no es validad, por favor vuelva a intentar!")






