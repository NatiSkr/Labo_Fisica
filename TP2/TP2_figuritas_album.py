# ---- GUIA 2. Parte 1 Llenar albums con figuras individuales ----

import random
import numpy as np
import matplotlib.pyplot as plt
album_size = int(input('Escriba la cantidad de espacios disponibles para completar en el album: '))
pack_size = int(input('Escriba la cantidad de figuras contenidas en un pack: '))
repeat_n_times = int(input('Escriba la cantidad de albums a completar secuencialmente: '))
print('\n')

# Punto 2 - Establecer un máximo puntaje de las figuras y devolver un valor entre [1:maximo
def generate_random_card(max_cards=6):  # antes llamada generate_random_card
    # aleatoriamente sacar un numero entre 1 :max_figus
    return random.randint(1, max_cards)
    # devuelvo un int con el numero de figura / card


# Test funcion generate_random_card
""" dar un valor maximo de figura (min=1)
figu = generate_random_card(int(input('Escriba puntaje máximo de figurita: ')))
print('1 Abrí el paquete y salio la figura ', figu)

# dejar valor por defecto de figuras (6)
figu = generate_random_card()
print('2 Abrí el paquete y salio la figura ', figu)
"""


# Punto 3 ¿Con cuantas figuras aleatorias completo el album?
def complete_single_album(max_cards):
    # Establecer tamaño de lista 'album' con 'max_figuras' y llenarla con ceros
    album = []
    for i in range(max_cards):
        album.append(0)
    figuras_compradas = 0  # contador. Cantidad de figuras que compro hasta completar lista 'album'
    # Si el numero de figura se corresponde con un lugar vacio de la lista 'album'
    # colocar un 1 en dicho lugar de la lista
    # sacar una figura aleatoriamente y actualizar contador hasta que cada elemento del album tenga un 1
    while sum(album) < max_cards:
        figu = generate_random_card(max_cards)
        figuras_compradas = figuras_compradas + 1
        if album[figu - 1] == 0:
            album[figu - 1] = 1
    return figuras_compradas
    # devuelvo cantidad de compras para completar album (int)


# Test funcion cuantas_completar
"""
cant_comprada = complete_single_album(album_size)
print('Se lleno el album de', album_size, 'espacios '+
    'con la compra de', cant_comprada, 'figuras.')
"""


# Punto 4  -  Si lleno varios albums secuencialmente, no al mismo tiempo compartiendo figuras
# ¿Cuantas figuras compre hasta completar cada album?
def complete_all_albums(max_cards, n_repeticiones):
    cant_por_album = []
    # Ejecutar complete_single_album hasta completar las repeticiones
    for i in range(0, n_repeticiones):
        cant = complete_single_album(max_cards)
        cant_por_album.append(cant)
    return cant_por_album
    # devuelve una lista con la cantidad de figuras "compradas" hasta completar cada album.


# Punto 5 Chequear funcionamiento de las funciones anteriores
"""
secuencia1 = complete_all_albums(album_size, repeat_n_times)
print('Para llenar', repeat_n_times, 'albums de', album_size, 'espacios,',
        'se compraron en promedio', round(np.mean(secuencia1),2), 'figuras por album')
print('Detalle: ', secuencia1)
"""


# ---- GUIA 2. Parte 2 Llenar albums con paquetes de figuras ----------------------------------------------------------

# Punto 1: ya esta realizado en la parte 1, punto 2 con la funcion 'generate_random_card'
# Ahora genero paquetes con figuras aleatorias

# Punto 2 genero paquetes con figuras aleatorias
# La cantidad de figuras en un paquete debe ser independiente de la cantidad de espacios que se pueden llenar en album

def generate_card_pack(max_cards, contents_per_pack):
    pack_list = []
    for i in range(0, contents_per_pack):
        figu_pack = generate_random_card(max_cards)
        pack_list.append(figu_pack)
    return pack_list

# Test generate_card_pack
# print('se armo un paquete ',generate_card_pack(album_size, pack_size))


# Punto 3
# Implementar una funcion que simule completar 1 album y devuelva cuantos paquetes se debieron adquirir para completarlo

def fill_album_withPacks(max_cards, cards_per_pack):
    album_status = []
    for i in range(max_cards):
        album_status.append(0)
    generated_packs = 0
    while sum(album_status) < max_cards:
        pack = generate_card_pack(max_cards, cards_per_pack)
        generated_packs = generated_packs + 1
        for card in pack:
            if album_status[card - 1] == 0:
                album_status[card - 1] = 1
    return generated_packs

# Test
# print('Para llenar el album se debio comprar', fill_album_withPacks(album_size, pack_size), 'paquetes')


# Punto 4 Completar con paquetes todos los albums
def fill_all_withPacks(max_cards, cards_per_pack, n_repeats):
    cantPacks_perAlbum = []
    for i in range(0, n_repeats):
        cant = fill_album_withPacks(max_cards, cards_per_pack)
        cantPacks_perAlbum.append(cant)
    return cantPacks_perAlbum
    "devuelve lista donde cada elemento es un int que representa la cantidad de paquetes adquiridos" \
    "por cada album que se completo"


# Test fill_all_withPacks
"""
secuencia2 = fill_all_withPacks(album_size, pack_size, repeat_n_times)
print('Se compraron en promedio', round(np.mean(secuencia2),2), 'paquetes para llenar cada album')
"""


# ----------------------------------------------------------------------------------------


# ---- GUIA 2. Parte 3 HISTOGRAMAS ----

# Retomo las ultimas funciones de la guia de Figuritas:

# Consigna 1: Calcular para 5, 20, 50, 100, 200, y 1000 repeticiones:
# el promedio, el desvío estándar y el error estándar de la media.

lista_cant_rep = [5, 20, 50, 100, 200, 1000]

# Hago un ciclo con 'for' que tome los elementos de 'lista_cant_rep' como los valores de 'n_repeticiones'
# cuando uso la funcion 'fill_all_withPacks' y le pido que imprima la media, el desvio estandar y el error estandar.
# Recordatorio: n_repeticiones es la cantidad de veces que llene un album

def stadistics_fill_all_withPacks(max_cards, contents_per_pack, n_repeats_list):
    media = []
    desvio_std = []
    error_std = []
    indice = 0
    for cant_rep in n_repeats_list:
        # Llenar una serie de albums y conseguir la lista de paquetes necesarios para llebarlos
        filled_albums = fill_all_withPacks(max_cards, contents_per_pack, cant_rep)
        # Promedio aritmetico
        media.append(np.mean(filled_albums))
        # Desviacion estandar muestral (ddof = delta degrees of freedom)
        desvio_std.append(round(np.std(filled_albums, ddof = 1), 4))
        # Dispersión estandar del promedio
        error_std.append(round(desvio_std[indice] / np.sqrt(cant_rep), 4))
        # Actualizo indice para recorrer lista de serie de repeticiones
        indice = indice + 1
    return media, desvio_std, error_std
    # devuelve listas con estadisticos


promedio, d_std, e_std = stadistics_fill_all_withPacks(album_size, pack_size, lista_cant_rep)
print(promedio)
print(d_std)
print(e_std)

# Consigna 2: Para valor de repetición (excepto 5) hacer el histograma. Es decir, la distribucion de compra de paquetes.
print('\n Numeros de repeticiones N sobre las que hago los histogramas:', lista_cant_rep[1:], '\n')
# ignora primer elemento de la lista, considero que su valor es muy bajo para analizarlo estadisticamente

plt.style.use('seaborn-white')  # determino estilo de grafico

# Implemento un diccionario para cambiar el formato del titulo
fuente_titulo = {'family': 'serif',
                 'color': 'darkslategray',
                 'weight': 'normal',
                 'size': 14
                 }


"""
for cant_rep in lista_cant_rep[1:]:  # ignoro el primer N de la lista de repeticion por ser muy bajo
    random.seed(0)  # "fijo" los numeros pseudo-aletorios para garantizar reproducibilidad
    datos = fill_all_withPacks(album_size, pack_size, cant_rep)
    plt.hist(datos,
             bins = int(np.sqrt(cant_rep)),
             edgecolor = 'darkgray',
             color = 'lightgreen')
    plt.xlabel('Paquetes adquiridos para completar un album')
    plt.ylabel('Frecuencia absoluta')
    plt.title('Distribucion de frecuencia \n de compra de paquetes. N=' + str(cant_rep), fontdict=fuente_titulo)
    plt.show()
"""


# Consigna 3 Llenar 50 veces 50 albums
# y graficar el histograma con la distribución de los promedios (resultado de cada experimento)

lista_promedios = []
random.seed(0)  # decido "fijar" los numeros aleatorios para que el experimento sea reproducible
for i in range(50):
    promedio, d_std, e_std = stadistics_fill_all_withPacks(album_size, pack_size, [50])
    promedio_i = np.mean(promedio[0])
    lista_promedios.append(promedio_i)


print(promedio[0])
print(d_std[0])
print(e_std[0])

print(lista_promedios)

# Defino mi funcion gaussiana
# x son los datos.mu es la media. sigma es la std. N es el numero de datos. bines son los bin_edges del histograma.
def gaussiana(x, mu, sigma, N, bines):
    deltax = bines[1] - bines[0]
    y = deltax * N * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return y


# defino calculos de media, mediana, desviacion estandar
media = np.mean(lista_promedios)
dest = np.std(lista_promedios, ddof=1)
error_std = dest / np.sqrt(50)
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
        lista_promedio_exp_individual = fill_all_withPacks(max_cards, cards_per_pack, n_repeticiones)
        promedio_exp_individual = np.mean(lista_promedio_exp_individual)
        promedios_n_experimentos.append(promedio_exp_individual)
    return promedios_n_experimentos


realizar_n_exp = repetir_experimento(669, 5, 50, 50)
media = np.mean(realizar_n_exp)
dest = np.std(realizar_n_exp, ddof=1)
error_std = dest / np.sqrt(50)
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
        figu = generate_random_card(669)  # sigo pensando en un album con un tamanio de 669 espacios
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
