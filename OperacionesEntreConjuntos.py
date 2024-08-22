import random
import itertools

#OPERACION BASICA UNION DE CONJUNTOS -------------------------------------------------
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





#OPERACION BASICA DIFERENCIA DE CONJUNTOS -------------------------------------------------
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



#OPERACION BASICA SUBCONJUNTO ALEATORIO -------------------------------------------------
def subcojunto_aleatorio(*conjuntos):
    # Seleccionar un conjunto aleatorio de los conjuntos proporcionados
    conjunto_seleccionado = random.choice(conjuntos)
    
    # Obtener un tamaño aleatorio para el subconjunto (entre 0 y el tamaño del conjunto seleccionado)
    tamaño_subconjunto = random.randint(0, len(conjunto_seleccionado))
    
    # Generar un subconjunto aleatorio del tamaño seleccionado
    subconjunto = set(itertools.islice(random.sample(conjunto_seleccionado, tamaño_subconjunto), tamaño_subconjunto))
    
    return conjunto_seleccionado, subconjunto

# Definir varios conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9}
conjunto3 = {10, 11, 12}

# Obtener un conjunto aleatorio y un subconjunto de este
conjunto_aleatorio, subconjunto = subcojunto_aleatorio(conjunto1, conjunto2, conjunto3)

print("Conjunto seleccionado:", conjunto_aleatorio)
print("Subconjunto aleatorio:", subconjunto)