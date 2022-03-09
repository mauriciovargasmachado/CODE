menu = (""" 
Bienvenido al conversor de monedas por favor seleccione su tipo de moneda

1 - Pesos Colombianos
2 - pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
""")

opcion = int(input(menu))
if opcion == 1:
    pesos = input("Cuantos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4000
    dolares = pesos / valor_dolar
    dolares =round(dolares,3)
    dolares = str(dolares)
    print(" El valor total de dolares que usted posee es de $" + dolares + " Dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares =round(dolares,3)
    dolares = str(dolares)
    print(" El valor total de dolares que usted posee es de $" + dolares + " Dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares =round(dolares,3)
    dolares = str(dolares)
    print(" El valor total de dolares que usted posee es de $" + dolares +  "Dolares")
else: 
    print("Por favor ingresa una opcion correcta!")
