# ---- GUIA 2. Parte 1 FIGURITAS ----

import random
import numpy as np
import matplotlib.pyplot as plt  # importo para graficar
album_size = int(input('Escriba la cantidad de espacios disponibles para completar en el album: '))
pack_size = int(input('Escriba la cantidad de figuras contenidas en un pack: '))
repeat_n_times = int(input('Escriba la cantidad de albums a completar secuencialmente: '))
print('\n')

# Punto 2 - Establecer un máximo puntaje de las figuras y devolver un valor entre [1:maximo
def generate_random_card(max_figuras=6):  # antes llamada comprar_una_figu
    # aleatoriamente sacar un numero entre 1 :max_figus
    return random.randint(1, max_figuras)

# Test funcion generate_random_card
""" dar un valor maximo de figura (min=1)
figu = generate_random_card(int(input('Escriba puntaje máximo de figurita: ')))
print('1 Abrí el paquete y salio la figura ', figu)

# dejar valor por defecto de figuras (6)
figu = generate_random_card()
print('2 Abrí el paquete y salio la figura ', figu)
"""


# Punto 3 ¿Cuantas figuras tengo que completar la serie 1 : ls limite superior?
def complete_single_album(max_figuras):
    # Establecer tamaño de lista 'album' con 'max_figuras' y llenarla con ceros
    album = []
    for i in range(max_figuras):
        album.append(0)
    figuras_compradas = 0  # contador. Cantidad de figuras que compro hasta completar lista 'album'
    # Si el numero de figura se corresponde con un lugar vacio de la lista 'album'
    # colocar un 1 en dicho lugar de la lista
    # sacar una figura aleatoriamente y actualizar contador hasta que cada elemento del album tenga un 1
    while sum(album) < max_figuras:
        figu = generate_random_card(max_figuras)
        figuras_compradas = figuras_compradas + 1
        if album[figu - 1] == 0:
            album[figu - 1] = 1
    return figuras_compradas
    # devuelvo cantidad de compras para completar album (integer)


# Test funcion cuantas_completar
"""
cant_comprada = complete_single_album(album_size)
print('Se lleno el album de', album_size, 'espacios '+
    'con la compra de', cant_comprada, 'figuras.')
"""


# Punto 4  -  Si lleno varios albums secuencialmente, no al mismo tiempo compartiendo figuras
# ¿Cuantas figuras compre hasta completar cada album?
def complete_all_albums(n_repeticiones, max_cards):
    cant_por_album = []
    # Ejecutar complete_single_album hasta completar las repeticiones
    for i in range(0, n_repeticiones):
        cant = complete_single_album(max_cards)  # agregar la cant de figuras compradas por llenado de album a una lista 'n'
        cant_por_album.append(cant)  # hasta que se terminen las repeticiones
    return cant_por_album


# Punto 5 Chequear funcionamiento de las funciones anteriores
"""
secuencia1 = complete_all_albums(repeat_n_times, album_size)
print('Para llenar', repeat_n_times, 'albums de', album_size, 'espacios,',
        'se compraron en promedio', round(np.mean(secuencia1),2), 'figuras por album')
print('Detalle: ', secuencia1)
"""


# ---- GUIA 2. Parte 2 PAQUETES ----------------------------------------------------------


# Punto 1: ya esta realizado en la parte 1, punto 2 con la funcion 'generate_random_card'
# Ahora genero paquetes con figuras aleatorias

# Punto 2
# Implementar una funcion donde se genera un paquete 'pack_list' de figuritas al azar.
# La cantidad de figuras en un paquete debe ser independiente de la cantidad de espacios que se pueden llenar en album

def generate_card_pack(contents_per_pack, max_cards):
    pack_list = []
    for i in range(0, contents_per_pack):
        figu_pack = generate_random_card(max_cards)
        pack_list.append(figu_pack)
    return pack_list

# Test generate_card_pack
# print('se armo un paquete ',generate_card_pack(pack_size, album_size))


# Punto 3
# Implementar una funcion 'complete_album_withPacks(max_cards,cards_per_pack)'
# que dado el tamanio del album simule su llenado y devuelva cuantos paquetes se debieron adquirir para completarlo

def complete_album_withPacks(cards_per_pack, max_cards):
    complete_album = []
    for i in range(max_cards):
        complete_album.append(0)
    paq_comprados = 0
    while sum(complete_album) < max_cards:
        paquete = generate_card_pack(max_cards, cards_per_pack)
        paq_comprados = paq_comprados + 1
        for figura in paquete:
            if complete_album[figura - 1] == 0:
                complete_album[figura - 1] = 1
    return paq_comprados


print('Para llenar el album se debio comprar', complete_album_withPacks(pack_size, album_size), 'paquetes')


# Punto 4
# Calcular n_repeticiones=100 veces la funcion cuantos paquetes
# Utilizar max_cards=669, cards_per_pack=5 y guardar resultados obtenidos en una lista. Calcular su promedio.

def cantidad_promedio(n_repeticiones, max_cards, cards_per_pack):
    # HAGO UNA FUNCION QUE ME DEVUELVA UNA LISTA 'n'
    # DONDE SUS ELEMENTOS SON LA CANTIDAD DE PAQUETES QUE COMPRE PARA LLENAR CADA ALBUM
    lista_cant_por_album = []
    for i in range(0, n_repeticiones):
        cant = complete_album_withPacks(max_cards, cards_per_pack)
        lista_cant_por_album.append(cant)
    return lista_cant_por_album


# Para una cierta cantidad de repeticiones 'n_repeticiones':
# agregar la cantidad de paquetes comprados por llenado de album a una lista 'n' hasta que se terminen las repeticiones
promedio_compras = cantidad_promedio(100, 669, 5)
print('Se compraron en promedio', np.mean(promedio_compras), 'paquetes para llenar cada album')


# ----------------------------------------------------------------------------------------


# ---- GUIA 2. Parte 3 HISTOGRAMAS ----

# Retomo las ultimas funciones de la guia de Figuritas:
# n_paquetes=complete_album_withPacks(max_cards,cards_per_pack)
# Ahora armo una nueva función que ejecute un 'experimento', cuyo resultado almaceno en una variable tipo lista donde
# cada elemento es la cantidad de paquetes comprados:
def experimento(max_cards, cards_per_pack, n_repeticiones):
    # En realidad es la misma funcion que cantidad_promedio pero con otro nombre (se pedia armar una nueva función)
    lista_exp = []
    for i in range(0, n_repeticiones):
        cant = complete_album_withPacks(max_cards, cards_per_pack)
        lista_exp.append(cant)
    return lista_exp


print(experimento(669, 5, 10))

# Consigna 1: Calcular para 5, 20, 50, 100, 200, y 1000 repeticiones:
# el promedio, el desvío estándar y el error estándar de la media.
lista_cant_rep = [5, 20, 50, 100, 200, 1000]
# Hago un ciclo con 'for' que tome los elementos de 'lista_cant_rep' como los valores de 'n_repeticiones'
# cuando uso la funcion 'experimento' y le pido que imprima la media, el desvio estandar y el error estandar.
# Recordatorio: n_repeticiones es la cantidad de veces que llene un album
for cant_rep in lista_cant_rep:
    res = experimento(669, 5, cant_rep)
    media = np.mean(res)  # promedio aritmetico
    desvio_std = np.std(res, ddof=1)  # desviacion estandar muestral (,ddof=1)
    error_std = desvio_std / np.sqrt(cant_rep)  # dispersion estandar del promedio
    print('Con', cant_rep, 'repeticiones, obtengo media=', media,
          ';desvio estandar=', round(desvio_std, 2),
          ';error estandar=', round(error_std, 2))

# Consigna 2: Para valor de repetición (excepto 5) hacer el histograma.
# Es importante detallar los ejes y el valor de N en el título.
# En las notas de texto detallar el valor del tamanio del *bin* o factor de clase.
# Hacer los histogramas para cada valor de repeticiones excepto 5. Es decir, la distribucion de compra de paquetes.
print('Numeros de repeticiones N sobre las que hago los histogramas:', lista_cant_rep[1:])
# ignora primer elemento de la lista, considero que su valor es muy bajo para analizarlo estadisticamente

plt.style.use('seaborn-white')  # determino estilo de grafico
# Uso un diccionario para cambiar el formato del titulo porque no me gusta el original
fuente_titulo = {'family': 'serif',
                 'color': 'darkslategray',
                 'weight': 'normal',
                 'size': 14
                 }
# fin diccionario
for cant_rep in lista_cant_rep[1:]:  # ignoro el primer N de repeticion por ser muy chico
    random.seed(0)  # "fijo" los numeros pseudo-aletorios para garantizar reproducibilidad
    datos = experimento(669, 5, cant_rep)
    N_bines = int(np.sqrt(cant_rep))
    plt.hist(datos, bins=N_bines, edgecolor='darkgray', color='lightgreen')
    plt.xlabel('Cantidad de paquetes')
    plt.ylabel('Repeticiones observadas')
    plt.title('Distribucion de frecuencia para N=' + str(cant_rep), fontdict=fuente_titulo)
    plt.show()

# Consigna 3 Repetir 50 veces el experimento con 50 repeticiones y graficar el histograma conla distribución
# de los promedios (resultado de cada experimento). Responder en un cuadro de texto las preguntas
lista_promedios = []
random.seed()  # decido "fijar" los numeros aleatorios para que el experimento sea reproducible
for i in range(50):
    rep = experimento(669, 5, 50)
    promedio = np.mean(rep)
    lista_promedios.append(promedio)


# print(lista_promedios)

# Defino mi funcion gaussiana
# x son los datos.mu es la media. sigma es la std. N es el numero de datos. bines son los bin_edges del histograma.
def gaussiana(x, mu, sigma, N, bines):
    deltax = bines[1] - bines[0]
    y = deltax * N * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return y


# defino calculos de media, mediana, desviacion estandar
media = np.mean(lista_promedios)
dest = np.std(lista_promedios, ddof=1)
error_std = desvio_std / np.sqrt(50)
N_rep = 50  # N numero de datos, es decir la cantidad de repeticiones
N_bines = 10  # cant bines
counts, bin_edges = np.histogram(lista_promedios, bins=N_bines)
plt.hist(lista_promedios, bins=N_bines, edgecolor='white', color='deepskyblue', density=True)
plt.xlabel('Cantidad de paquetes')
plt.ylabel('Frecuencia relativa')
plt.title('Distribucion de las medias. N=' + str(N_rep), fontdict=fuente_titulo)
plt.xticks(bin_edges)
plt.show()
print('--Información adicional de 1 experimento con 50 repeticiones-- Promedio=', round(media, 1), ';Desvío estándar=',
      round(dest, 1), ';Error estándar=', round(error_std, 1))  # redondeo cifras


# Hasta aca es lo mismo que la consigna 2 con N=50 repeticiones, es decir con un solo experimento.
# Lo dejo para comparr y responder las preguntas.


# Ahora hago un nuevo histograma: repito 50 veces el experimento
def repetir_experimento(max_cards, cards_per_pack, n_repeticiones, n_rep_exp):
    promedios_n_experimentos = []
    for n in range(n_rep_exp):
        lista_promedio_exp_individual = experimento(max_cards, cards_per_pack, n_repeticiones)
        promedio_exp_individual = np.mean(lista_promedio_exp_individual)
        promedios_n_experimentos.append(promedio_exp_individual)
    return promedios_n_experimentos


realizar_n_exp = repetir_experimento(669, 5, 50, 50)
media = np.mean(realizar_n_exp)
dest = np.std(realizar_n_exp, ddof=1)
error_std = desvio_std / np.sqrt(50)
# print(len(realizar_n_exp),realizar_n_exp)
# chequeo que vuelque en la lista los 50 elementos (promedios de cada experimento individual)
plt.hist(realizar_n_exp, bins=N_bines, edgecolor='darkgray', color='purple', density=True)
plt.xlabel('Promedio de paquetes por experimento')
plt.ylabel('Frecuencia relativa')
plt.title('Distribucion de los promedios por experimento. N=' + str(N_rep), fontdict=fuente_titulo)
# ahora si hago la distribucion gaussiana
counts, bin_edges = np.histogram(realizar_n_exp, bins=N_bines)
datos_gauss = np.sort(realizar_n_exp)  # ordeno los datos de menor a mayor
dist_gauss_hist = gaussiana(datos_gauss, media, dest, N_rep, bin_edges)
plt.plot(datos_gauss, dist_gauss_hist)
plt.hist(datos_gauss, bins=N_bines, edgecolor='black', color='lightgray')
plt.xticks(bin_edges)
plt.show()
print('--Información adicional de 50 experimentos con 50 repeticiones-- Promedio=', round(media, 1),
      ';Desvío estándar=', round(dest), 1, ';Error estándar=', round(error_std, 1))  # redondeo cifras


# Consigna 4. Graficar la distribución generada por la función que utilizaron para ver que figurita tocaba
def compro_varias_figuras(cant_compras):
    stock_figus = []
    for c in range(cant_compras):
        figu = comprar_una_figu(669)  # sigo pensando en un album con un tamanio de 669 espacios
        stock_figus.append(figu)
    return stock_figus


compra_figus4 = compro_varias_figuras(
    6690)  # supongo que compro 10 veces la cantidad de figuras que puede tener un album

N_bines4 = 10  # cant bines
counts4, bin_edges4 = np.histogram(compra_figus4, bins=N_bines4)
plt.hist(compra_figus4, bins=N_bines4, edgecolor='black', color='yellow', density=True)
plt.xlabel('Figuras')
plt.ylabel('Frecuencia relativa')
plt.title('Distribucion', fontdict=fuente_titulo)
plt.xticks(bin_edges4)
plt.show()
