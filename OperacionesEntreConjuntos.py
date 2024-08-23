
import random
from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

# Función para leer conjuntos desde la entrada del usuario
def leer_conjuntos():
    conjuntos = []
    while True:
        entrada = input("Ingrese un conjunto (o presione Enter para finalizar): ")
        if not entrada:
            break
        # Convertir la cadena de entrada en un conjunto
        try:
            conjunto = set(map(int, entrada.split()))
            conjuntos.append(conjunto)
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números separados por espacios.")
    return conjuntos

# OPERACION BASICA UNION DE CONJUNTOS -------------------------------------------------
#OPERACION BASICA SUPER CONJUNTO ------------------------------------------------------
def union_conjuntos(*conjuntos):
    lista_union = []
    elementos_agregados = set()
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in elementos_agregados:
                lista_union.append(elemento)
                elementos_agregados.add(elemento)
    return lista_union

# OPERACION BASICA DIFERENCIA DE CONJUNTOS -------------------------------------------------
def diferencia_conjuntos(conjunto_base, *conjuntos):
    diferencia = conjunto_base.difference(*conjuntos)
    lista_diferencia = list(diferencia)
    return lista_diferencia

# OPERACION BASICA SUBCONJUNTO ALEATORIO -------------------------------------------------
def subcojunto_aleatorio(*conjuntos):
    if not conjuntos:
        raise ValueError("Debe proporcionar al menos un conjunto.")

    conjunto_seleccionado = random.choice(conjuntos)
    
    if len(conjunto_seleccionado) > 0:
        tamaño_subconjunto = random.randint(1, len(conjunto_seleccionado))
    else:
        tamaño_subconjunto = 0
    
    # Convertir el conjunto en una lista para usar random.sample()
    lista_conjunto = list(conjunto_seleccionado)
    # Generar un subconjunto aleatorio del tamaño seleccionado
    subconjunto = set(random.sample(lista_conjunto, tamaño_subconjunto))
    
    return conjunto_seleccionado, subconjunto
# Función para mostrar el diagrama de Venn
def mostrar_diagrama_venn(conjuntos):
    if len(conjuntos) == 2:
        venn2(conjuntos)
        plt.show()
    elif len(conjuntos) == 3:
        venn3(conjuntos)
        plt.show()
    else:
        print("Solo se pueden mostrar diagramas de Venn para 2 o 3 conjuntos.")


# Leer conjuntos desde la entrada del usuario
conjuntos = leer_conjuntos()
 # Mostrar diagrama de Venn


if conjuntos:
    # Usar los conjuntos en las funciones
    print("Unión de los conjuntos en una lista y el superconjunto:", union_conjuntos(*conjuntos))

    if len(conjuntos) > 1:
        conjunto_base = conjuntos[0]
        otros_conjuntos = conjuntos[1:]
        print("Diferencia de los conjuntos en una lista:", diferencia_conjuntos(conjunto_base, *otros_conjuntos))
    
    if len(conjuntos) > 1:
        conjunto_aleatorio, subconjunto = subcojunto_aleatorio(*conjuntos)
        print("Conjunto seleccionado:", conjunto_aleatorio)
        print("Subconjunto aleatorio:", subconjunto)

    
        mostrar_diagrama_venn(conjuntos)
   
else:
    print("No se han ingresado conjuntos.")

