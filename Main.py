import OperacionesEntreConjuntos

def main():
    print("Hola")
    lista= [
        [1, 3, 4, 7, 8, 10],    # Posición 0
        [2, 4, 5, 6, 8],        # Posición 1
        [1, 3, 5, 8, 9]         # Posición 2
    ]
    res = OperacionesEntreConjuntos.calcularDiferenciaSimetrica(lista)
    print(res)

main()