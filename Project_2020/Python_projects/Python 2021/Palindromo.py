
# def palindromo(palabra):
#     invertida=0
#     palabra = palabra.strip()
#     palabra = palabra.lower()
#     invertida == palabra[::-1]
#     if palabra == invertida:
#         return True
#     else:
#         return False



# def run():
#     es_palindromo=0
#     palabra = input("Escribe una palabra para verificar: ")
#     es_palindromo == palindromo(palabra)
#     if es_palindromo == True:
#         print("Tu palabra es un Palindromo!!!")
#     else:
#         print("Hemos verificado y tu palabra NO es un palindromo")




# run()

def es_palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ')
    if es_palindromo(palabra):
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()      