from data_stark import *

def validar_entero(numero:str)-> bool:
    """Esta funcion recibe un string y valida que sea un numero, retorna true o false"""
    if numero.isnumeric():
        return True
    return False

def stark_menu_principal()-> int:
    """Esta funcion valida que el usuario haya ingresado un numero valido, retorna el numero casteado"""
    res = input("""
1 - Listar ordenado por nombre\n2 - Listar masculinos debiles\n3 - Cantidad por color de ojos
4 - Listar por color de pelo\n5 - Listar inteligencia\n6 - Listar promedio\n7 - Asignar IMC\n8 - Salir\n
""")
    
    if validar_entero(res) == False or int(res) > 8:
        return -1
    return int(res)

def normalizar_datos(lista:list) -> bool:
    """Esta funcion recibe una lista y convierte al tipo de dato correcto las keys
    'altura', 'peso'  y 'fuerza', retorna un booleano"""
    normalizar = False
    if not lista or normalizar:
        return False
    for heroes in lista:
        if type(heroes['fuerza']) != int:
            heroes['fuerza'] = int(heroes['fuerza'])
            normalizar = True
        if type(heroes['altura']) != float:
            heroes['altura'] = float(heroes['altura'])
            normalizar = True
        if type(heroes['peso']) != float:
            heroes['peso'] = float(heroes['peso'])
            normalizar = True
    return normalizar
normalizar_datos(lista_personajes)

def ordenar_por_nombre(heroes:list):
    """Esta funcion recibe una lista y ordena de manera ascendente los nombres en las
    keys 'nombre', retorna la lista ordenada"""
    for i in range(len(heroes)-1):
        for j in range(i + 1, len(heroes)):
            if heroes[i]['nombre'] > heroes[j]['nombre']:
                aux = heroes[i]
                heroes[i] = heroes[j]
                heroes[j] = aux
    return heroes

def mostrar_heroes(heroes, nombre=True, identidad=True, empresa=True, altura=True, peso=True, genero=True, color_ojos=True, color_pelo=True,
                    fuerza=True, inteligencia=True, imc=False):
    """Esta funcion recibe una lista y un booleano por cada key en los diccionarios de cada heroe, muestra cada dato de cada heroe
    segun el valor que reciba"""
    if not heroes:
        print("La lista está vacía")
        return

    encabezado = ""
    if nombre: encabezado += "{:<20}|".format("Nombre")
    if identidad: encabezado += "{:<30}|".format("Identidad")
    if empresa: encabezado += "{:<15}|".format("Empresa")
    if altura: encabezado += "{:<10}|".format("Altura")
    if peso: encabezado += "{:<10}|".format("Peso")
    if genero: encabezado += "{:<7}|".format("Género")
    if color_ojos: encabezado += "{:<12}|".format("Color Ojos")
    if color_pelo: encabezado += "{:<12}|".format("Color Pelo")
    if fuerza: encabezado += "{:<10}|".format("Fuerza")
    if inteligencia: encabezado += "{:<12}|".format("Inteligencia")
    if imc: encabezado += "{:<10}|".format("IMC")

    print(encabezado)
    print("-" * len(encabezado))

    for heroe in heroes:
        fila = ""
        if nombre: fila += "{:<20}|".format(heroe.get("nombre", ""))
        if identidad: fila += "{:<30}|".format(heroe.get("identidad", ""))
        if empresa: fila += "{:<15}|".format(heroe.get("empresa", ""))
        if altura: fila += "{:<10}|".format(heroe.get("altura", ""))
        if peso: fila += "{:<10}|".format(heroe.get("peso", ""))
        if genero: fila += "{:<7}|".format(heroe.get("genero", ""))
        if color_ojos: fila += "{:<12}|".format(heroe.get("color_ojos", ""))
        if color_pelo: fila += "{:<12}|".format(heroe.get("color_pelo", ""))
        if fuerza: fila += "{:<10}|".format(heroe.get("fuerza", ""))
        if inteligencia: fila += "{:<12}|".format(heroe.get("inteligencia", ""))
        if imc: fila += "{:<10}|".format(heroe.get("imc", ""))

        print(fila)
        print("-" * len(encabezado))


def obtener_superheroes_por_genero(heroes:list, genero_value:str):
    """Esta funcion recibe una lista y una key de genero, crea una nueva lista con los heores del genero indicado,
    retorna la nueva lista"""
    lista = []
    for heroe in heroes:
        if heroe["genero"] == genero_value:
            lista.append(heroe)
    return lista

def obtener_minimo(heroes:list, atributo_key:str)-> bool:
    """Esta funcion recibe una lista y una key, busca un minimo entre los value y, de existir, retorna
    un float con el value minimo"""
    if len(heroes) == 0:
        return False
    res = heroes[0]
    for heroe in heroes:
        if type(heroe[atributo_key]) != float and type(heroe[atributo_key]) != int or atributo_key not in heroe:
            return False
        if heroe[atributo_key] < res[atributo_key]:
            res = heroe

    return res[atributo_key]

def obtener_dato_cantidad(heroes:list, valor:float, atributo_key:str)-> list:
    """Esta funcion recibe una lista, un valor y una key, retorna una lista con los elementos cuyos value
     eran iguales al valor"""
    lista = []

    if len(heroes) == 0:
        return False
    
    for heroe in heroes:
        if heroe[atributo_key] == valor:
            lista.append(heroe)

    return lista

def obtener_dato_mayor(heroes:list, valor:float, atributo_key:str)-> list:
    """Esta funcion recibe una lista y una key, busca un maximo entre los value y ,de existir, los guarda en una nueva lista,
    retorna la nueva lista"""
    lista = []

    if len(heroes) == 0:
        return False
    
    for heroe in heroes:
        if heroe[atributo_key] > valor:
            lista.append(heroe)

    return lista

def contar_listar_por_caracteristica(heroes:list, atributo_key:str, contar_listar:str)->dict: 
    """Esta funcion recibe una lista, un key y una opcion de contar o listar, realiza una 
    operación de contar o listar los héroes según un atributo específico"""

    dic_atributos = {}
    
    for heroe in heroes:
        atributo = heroe[atributo_key].lower()
        if atributo in dic_atributos:
            dic_atributos[atributo].append(heroe["nombre"])
        else:
            dic_atributos[atributo]= [heroe["nombre"]]

    for atributo, nombres in dic_atributos.items():
        if contar_listar == "listar":
            cadena = ", "
            mensaje = cadena.join(nombres)
        elif contar_listar == "contar":
            mensaje = len(nombres)
            
        print(f"\n{atributo_key} {atributo}: {mensaje}")

def sumar_dato_heroe(heroes:list, atributo:str)-> float:
    """Esta funcion recibe una lista y un value, retorna un float con la suma de los value"""
    suma = 0
    for heroe in heroes:
        if type(heroe) != dict or len(heroe) == 0:
            return False
        suma += heroe[atributo]
    return suma

def dividir(dividendo:float, divisor:float)-> float:
    """Esta funcion recibe dos float y, de existir, retorna un float con el resultado de la division"""
    if divisor == 0:
        return False
    res = dividendo / divisor
    return res

def calcular_promedio(heroes:list, atributo:str)-> float:
    """Esta funcion recibe una lista y un value, retorna un float con el promedio"""
    if sumar_dato_heroe(heroes, atributo) == False:
        return False
    return dividir(sumar_dato_heroe(heroes, atributo), len(heroes))


def mostrar_promedio_dato(heroes:list, atributo:str)-> float:
    """Esta funcion recibe una lista y value, retorna un float con el promedio de los value"""
    if atributo == "altura" or atributo == "peso" or atributo == "fuerza" and len(heroes) > 0:
        return print(calcular_promedio(heroes, atributo))
    return False

def agregar_imc(heroes:list, peso_key:str, altura_key:str):
    """Esta funcion recibe una lista, una key de peso y una key de altura, calcula el IMC
    y lo guarda en un nuevo campo del heroe, retorna la lista de heroes"""
    calcular_imc = lambda peso, altura: peso / (altura * altura)

    for heroe in heroes:
        heroe['imc'] = str(calcular_imc(float(heroe[peso_key]),float(heroe[altura_key]) / 100))

    return heroes