import random

lista = []
opcion = ""


def crearEntrenador(tupla):
    nombreEntrenador = input("Ingrese el nombre del entrenador: ")
    nombrePokemon = input("Ingrese el nombre del pokemon: ")
    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)
    tupla.append((nombreEntrenador, nombrePokemon, ataque, vida))
    print("Entrenador y Pokemon creados.")


def listaEntrenador(tupla):
    n = len(tupla)
    for i in range(1, n):
        for j in range(n - 1):
            if tupla[j][2] < tupla[j + 1][2]:
                tupla[j], tupla[j + 1] = tupla[j + 1], tupla[j]

    print("--------------------------------------------")
    print("Entrenadores ordenados por ataque de su Pokemon:")
    correlativo = 1
    for item in tupla:
        print(f"{correlativo}. Entrenador: {item[0]} | Pokemon: {item[1]} | Ataque: {item[2]} | Vida: {item[3]}")
        correlativo += 1
    print("--------------------------------------------")


def ordenSeleccionVida(lis):
    n = len(lis)
    for manoIzq in range(n):
        ind_min_val = manoIzq
        for vista in range(manoIzq + 1, n):
            if lis[vista][3] < lis[ind_min_val][3]:
                ind_min_val = vista
        lis[manoIzq], lis[ind_min_val] = lis[ind_min_val], lis[manoIzq]
    return lis


def busquedaBinariaVida(array, numero):
    menor = 0
    mayor = len(array) - 1
    for data in range(len(array)):
        medio = (menor + mayor) // 2
        if array[medio][3] == numero:
            return medio
        elif array[medio][3] < numero:
            menor = medio
        else:
            mayor = medio
        if mayor - menor <= 1:
            break
    if array[menor][3] == numero:
        return menor
    elif array[mayor][3] == numero:
        return mayor
    return -1


def borraPorPokemon(tupla):
    if len(tupla) == 0:
        print("No hay entrenadores registrados.")
        return
    vidaBuscada = int(input("Ingrese el valor de vida a buscar: "))
    ordenSeleccionVida(tupla)
    posicion = busquedaBinariaVida(tupla, vidaBuscada)
    if posicion == -1:
        print(f"No se encontró ningún Pokemon con vida {vidaBuscada}.")
    else:
        print(f"Se eliminó a {tupla[posicion][0]} y su Pokemon {tupla[posicion][1]}.")
        tupla.pop(posicion)


def peleaPokemon(lista):
    if len(lista) < 2:
        print("Se necesitan al menos 2 entrenadores para pelear.")
        return
    listaEntrenador(lista)
    numero1 = int(input("Ingrese el número correlativo del primer Pokemon: "))
    numero2 = int(input("Ingrese el número correlativo del segundo Pokemon: "))
    pokemon1 = lista[numero1 - 1]
    pokemon2 = lista[numero2 - 1]

    multiplicador1 = random.randint(0, 5)
    multiplicador2 = random.randint(0, 5)
    danoAPokemon2 = pokemon1[2] * multiplicador1
    danoAPokemon1 = pokemon2[2] * multiplicador2

    vidaFinal1 = pokemon1[3] - danoAPokemon1
    vidaFinal2 = pokemon2[3] - danoAPokemon2

    print(f"{pokemon1[1]} ataca con {danoAPokemon1} de daño a {pokemon2[1]}.")
    print(f"{pokemon2[1]} ataca con {danoAPokemon2} de daño a {pokemon1[1]}.")

    if vidaFinal1 <= 0 and vidaFinal2 <= 0:
        print("¡Ambos Pokemon quedaron sin vida! Ambos entrenadores pierden.")
        lista.remove(pokemon1)
        lista.remove(pokemon2)
    elif vidaFinal1 == vidaFinal2:
        print("¡Empate! Ambos entrenadores pierden.")
        lista.remove(pokemon1)
        lista.remove(pokemon2)
    elif vidaFinal1 > vidaFinal2:
        print(f"¡Ganó el entrenador {pokemon1[0]} con su Pokemon {pokemon1[1]}!")
        lista.remove(pokemon2)
    else:
        print(f"¡Ganó el entrenador {pokemon2[0]} con su Pokemon {pokemon2[1]}!")
        lista.remove(pokemon1)


while opcion != "5":
    print("================================")
    print("MENÚ POKEMON")
    print("================================")
    print("1. Crear Entrenador, 2. Listar Entrenadores, 3. Borrar por Pokemon, 4. Pelea Pokemon, 5. Fin")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        crearEntrenador(lista)
    elif opcion == "2":
        listaEntrenador(lista)
    elif opcion == "3":
        borraPorPokemon(lista)
    elif opcion == "4":
        peleaPokemon(lista)
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opción inválida")