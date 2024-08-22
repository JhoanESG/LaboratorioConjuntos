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

# Definir tres conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto3 = {5, 6, 7}

# Obtener la unión como una lista
resultado = union_conjuntos(conjunto1, conjunto2, conjunto3)

print("Unión de los conjuntos en una lista:", resultado)



def diferencia_conjuntos(conjunto_base, *conjuntos):
    # Realizar la diferencia de conjuntos
    diferencia = conjunto_base.difference(*conjuntos)
    
    # Convertir el resultado a una lista
    lista_diferencia = list(diferencia)
    
    return lista_diferencia


# Definir conjuntos
conjunto_base = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6}
conjunto3 = {5, 7}

# Obtener la diferencia como una lista
resultado = diferencia_conjuntos(conjunto_base, conjunto2, conjunto3)

print("Diferencia de los conjuntos en una lista:", resultado)