def union_conjuntos(*conjuntos):
    # Crear una lista vacía para almacenar la unión de los elementos
    lista_union = []
    
    # Crear un conjunto para rastrear los elementos ya agregados
    elementos_agregados = set()
    
    # Iterar sobre cada conjunto
    for conjunto in conjuntos:
        # Iterar sobre cada elemento del conjunto
        for elemento in conjunto:
            # Si el elemento no ha sido agregado previamente, se agrega a la lista y al conjunto de seguimiento
            if elemento not in elementos_agregados:
                lista_union.append(elemento)
                elementos_agregados.add(elemento)
    
    return lista_union


def calcularInterseccion(conjuntos):
    repetidos = []
    for element in conjuntos[0]:
        if all(element in conjunto for conjunto in conjuntos) and element not in repetidos:
            repetidos.append(element)

    return repetidos


def calcularDS(conjuntos):
    resultado = []
    if len(conjuntos) < 2:

        resultado = conjuntos

    else:
        repetidos = []
        union = conjuntos[0]+conjuntos[1]
        
        for element in conjuntos[0]:
            if element in conjuntos[1] and element not in repetidos:
                repetidos.append(element)
        # Nueva lista excluyendo los números a eliminar
        conjuntos[1] = [element for element in union if element not in repetidos]
        del conjuntos[0]
        resultado = calcularDS(conjuntos)

    return resultado

def calcularDiferenciaSimetrica(conjuntos):
    interseccion = calcularInterseccion(conjuntos)
    nuevo_conjuntos = []
    print(interseccion)

    # Iterar sobre cada conjunto en el array de conjuntos
    for conjunto in conjuntos:
        # Crear una lista temporal para almacenar los elementos que no están en interseccion
        nuevo_conjunto = []
        
        # Iterar sobre cada elemento en el conjunto
        for element in conjunto:
            # Si el elemento no está en interseccion, agregarlo al nuevo_conjunto
            if element not in interseccion:
                nuevo_conjunto.append(element)
        
        # Agregar el nuevo_conjunto al resultado
        nuevo_conjuntos.append(nuevo_conjunto)
    
    resultado = calcularDS(nuevo_conjuntos)
    return resultado

