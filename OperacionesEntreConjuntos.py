import random

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
from matplotlib.patches import Ellipse



def mostrar_diagrama_venn(conjuntos, nombres=None):
    conjuntos = list(map(set, conjuntos))
    
    # Definir nombres predeterminados si no se proporcionan
    nombres = ['a', 'b', 'c'][:len(conjuntos)] if nombres is None else nombres

    plt.figure(figsize=(8, 8))

    if len(conjuntos) == 1:
        # Dibujar un solo conjunto
        plt.gca().add_patch(Ellipse((0.5, 0.5), 0.4, 0.4, color='blue', alpha=0.5))
        plt.text(0.5, 0.5, '\n'.join(map(str, conjuntos[0])), ha='center', va='center', fontsize=12, color='black')
        plt.title(f'Diagrama de Venn para 1 Conjunto: {nombres[0]}')
        plt.gca().set_aspect('equal')
        plt.axis('off')

    elif len(conjuntos) == 2:
        v = venn2(subsets=conjuntos, set_labels=nombres)
        
        for label_id in ['10', '01', '11']:
                 #'10' representa la región del diagrama que solo pertenece al primer conjunto (excluyendo el segundo conjunto).
            #'01' representa la región del diagrama que solo pertenece al segundo conjunto (excluyendo el primer conjunto).
            #'11' representa la intersección de ambos conjuntos.
            label = v.get_label_by_id(label_id)
            if label:
                label.set_text('\n'.join(map(str, conjuntos[0] - conjuntos[1])) if label_id == '10' else
                               '\n'.join(map(str, conjuntos[1] - conjuntos[0])) if label_id == '01' else
                               '\n'.join(map(str, conjuntos[0] & conjuntos[1])))
        
        plt.title('Diagrama de Venn para 2 Conjuntos')

    elif len(conjuntos) == 3:
        v = venn3(subsets=conjuntos, set_labels=nombres)
        
        for label_id in ['100', '010', '001', '110', '101', '011', '111']:
            label = v.get_label_by_id(label_id)
            if label:
                label.set_text('\n'.join(map(str, conjuntos[0] - conjuntos[1] - conjuntos[2])) if label_id == '100' else
                               '\n'.join(map(str, conjuntos[1] - conjuntos[0] - conjuntos[2])) if label_id == '010' else
                               '\n'.join(map(str, conjuntos[2] - conjuntos[0] - conjuntos[1])) if label_id == '001' else
                               '\n'.join(map(str, conjuntos[0] & conjuntos[1] - conjuntos[2])) if label_id == '110' else
                               '\n'.join(map(str, conjuntos[0] & conjuntos[2] - conjuntos[1])) if label_id == '101' else
                               '\n'.join(map(str, conjuntos[1] & conjuntos[2] - conjuntos[0])) if label_id == '011' else
                               '\n'.join(map(str, conjuntos[0] & conjuntos[1] & conjuntos[2])))
        
        plt.title('Diagrama de Venn para 3 Conjuntos')

    else:
        print("Solo se pueden mostrar diagramas de Venn para 1, 2 o 3 conjuntos.")
        return

    plt.show()





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


