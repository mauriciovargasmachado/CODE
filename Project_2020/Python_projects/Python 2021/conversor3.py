
def conversor (tipo_peso,valor_dolar):
    pesos = input("Cuantos pesos " + tipo_peso + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares =round(dolares,3)
    dolares = str(dolares)
    print(" El valor total de dolares que usted posee es de $" + dolares + " Dolares")


menu = (""" 
Bienvenido al conversor de monedas por favor seleccione su tipo de moneda

1 - Pesos Colombianos
2 - pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
""")

opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos",3875)
    
elif opcion == 2:
    conversor("Argentinos",65)
elif opcion == 3:
    conversor("Mexicanos",24)
else: 
    print("Por favor ingresa una opcion correcta!")
