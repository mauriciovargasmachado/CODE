import random 


from types import resolve_bases


def adivina_el_numero_computadora(x):

    print("===============================================================")
    print("==================Bienvenido al Juego==========================")
    print("===============================================================")
    print(f"=====Escoje un numero entre 1 y {x} y yo lo adivinare!!!=====")
    print("===============================================================")

    limite_inferior = 1
    limiter_superior = x

    respuesta_usuario = ""
    while respuesta_usuario != " c":
        if limite_inferior != limiter_superior:
            prediccion = random.randint(limite_inferior,limiter_superior)
        else:
            prediccion + limite_inferior
        
        respuesta_usuario = input(f"Mi prediccion es: {prediccion}, si es muy alta ingresa (A), si es muy pequena ingresa (B) y si es correcta incresa (C)").lower()
        
        if respuesta_usuario == " a":
            limiter_superior = prediccion - 1
        
        elif respuesta_usuario == " b":
            limite_inferior == prediccion +1

    print (f"he adivinado tu numero!!!")

adivina_el_numero_computadora(100)