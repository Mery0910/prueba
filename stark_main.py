from data_stark import *
from funciones2024 import *

while True:
    opcion = stark_menu_principal()
    print("")
    match opcion:
        case 1:
            mostrar_heroes(ordenar_por_nombre(lista_personajes))
        case 2:
            heroes_m = obtener_superheroes_por_genero(lista_personajes, "M")
            fuerza_minima = obtener_minimo(heroes_m, "fuerza")
            los_mas_debiles = obtener_dato_cantidad(heroes_m, fuerza_minima, "fuerza")
            mostrar_heroes(los_mas_debiles)
        case 3:
            contar_listar_por_caracteristica(lista_personajes, 'color_ojos', 'contar')
        case 4:
            contar_listar_por_caracteristica(lista_personajes, 'color_pelo', 'listar')
        case 5:
            contar_listar_por_caracteristica(lista_personajes, 'inteligencia', 'listar')
        case 6:
            heroes_f = obtener_superheroes_por_genero(lista_personajes, "F")
            promedio_f = calcular_promedio(heroes_f,'fuerza')
            print(f"El promedio de fuerza de las superheroes de genero femenino es: {promedio_f}\n")
            mostrar_heroes(obtener_dato_mayor(lista_personajes, promedio_f,'fuerza'),True,False,False,False,True,False,False,False,False,False)
        case 7:
            agregar_imc(lista_personajes, 'peso', 'altura')
            mostrar_heroes(lista_personajes,True,False,False,False,False,False,False,False,False,False,True)
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opcion invalida")