def run():
    mi_diccionario = {
        "llave 1" :1,
        "Llave 2" :2,
        "llave 3" : 3,

    }

    # print(mi_diccionario)

poblacion_paises = {

    "Argentina": 44938712,
    "Brazil" : 210147125,
    "Colombia" : 50372424,
}

# print (poblacion_paises["Argentina"])
# print (poblacion_paises["Argentina"])
# print (poblacion_paises["Argentina"])


# for pais in poblacion_paises.keys():
#     print(pais)

# for pais in poblacion_paises.values():
#     print(pais)    

for pais, poblacion in poblacion_paises.items():
    print(pais + " Tiene " + str(poblacion) + " Habitantes" )  


if __name__=="__main__":
    run()