peso_colombiano = float(input("Por favor ingrese el valor de pesos colombianos: "))
valor_dolar = 4000
conversor = peso_colombiano / valor_dolar
conversor = round(conversor,3)
conversor = str(conversor)
print("El valor de sus pesos colombianos en dolares es de: "+ conversor)