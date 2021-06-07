# ---- GUIA 2. Parte 2 FIGURITAS ----


# Punto 2
# el metodo random.randint(_,_) en la funcion comprar_una_figu me devuelve un numero aleatorio
# dentro de un rango entre el primer y segundo argumento
import random
import numpy as np
import matplotlib.pyplot as plt  # importo para graficar


def comprar_una_figu(figus_total):
    return random.randint(1, figus_total)


print(comprar_una_figu(6))


# Punto 3
def cuantas_figus(figus_total):
    album = []
    for i in range(figus_total):
        album.append(0)
    figus_compradas = 0
    while sum(album) < figus_total:
        figu = comprar_una_figu(figus_total)
        figus_compradas = figus_compradas + 1
        if album[figu - 1] == 0: album[figu - 1] = 1
    return album, figus_compradas


album, fig_que_compre = cuantas_figus(6)
print('se lleno el album! (estado', album, 'donde 1 significa espacio lleno) con la compra de',
      fig_que_compre, 'figuras.')


# Punto 4
# HAGO UNA FUNCION QUE ME DEVUELVA UNA LISTA 'n'
# DONDE SUS ELEMENTOS SON LA CANTIDAD DE FIGURAS QUE COMPRE PARA LLENAR CADA ALBUM
def cantidad_promedio(n_repeticiones, figus_total):
    n = []
    for i in range(0, n_repeticiones):  # Para una cierta cantidad de repeticiones 'n_repeticiones':
        album, cant = cuantas_figus(
            figus_total)  # agregar la cant de figuras compradas por llenado de album a una lista 'n'
        n.append(cant)  # hasta que se terminen las repeticiones
    return n


cant_albums_llenados = 1000
cant_figuras = 6
n = cantidad_promedio(cant_albums_llenados, cant_figuras)
print('Para llenar', cant_albums_llenados,
      'albums de', cant_figuras,
      'figuras, se compraron en promedio', np.mean(n),
      'figuras para llenar cada album, o  redondeado para abajo', int(np.mean(n)), 'fig.')

# Punto 5

cant_albums_llenados = 100
cant_figuras = 669
n = cantidad_promedio(cant_albums_llenados, cant_figuras)
print('Para llenar', cant_albums_llenados,
      'albums de', cant_figuras,
      'figuras, se compraron en promedio', np.mean(n),
      'figuras para llenar cada album, o  redondeado para abajo', int(np.mean(n)), 'fig.')


# ----------------------------------------------------------------------------------------


# ---- GUIA 2. Parte 2 PAQUETES ----

# Punto 1
# aprovecho la logica de una funcion anterior

def agarrar_figu(tamanio):
    return random.randint(1, tamanio)


def gen_paquete(fig):
    paquete_generado = []
    for i in range(fig):
        figu = agarrar_figu(669)
        paquete_generado.append(figu)
    return paquete_generado


print('se armo un paquete! (estado', gen_paquete(5), ').')


# Punto 2
# Implementar una funcion 'generar_paquetes(figus_total,figus_paquete)' donde se genera un paquete de figuritas al azar.
# Utilizo: 'figus_total' tamanio del album y 'figus_paquete' la cantidad de figuritas por paquete.

def generar_paquete(figus_total, figus_paquete):
    paq_generado = []
    for i in range(figus_paquete):
        figu = agarrar_figu(figus_total)
        paq_generado.append(figu)
    return paq_generado


print('se armo un paquete! (paq cerrado', generar_paquete(669, 5), ').')


# Punto 3
# Implementar una funcion 'cuantos_paquetes(figus_total,figus_paquete)'
# que dado el tamanio del album simule su llenado y devuelva cuantos paquetes se debieron adquirir para completarlo

def cuantos_paquetes(figus_total, figus_paquete):
    llenado_album = []
    for i in range(figus_total):
        llenado_album.append(0)
    paq_comprados = 0
    while sum(llenado_album) < figus_total:
        paquete = generar_paquete(figus_total, figus_paquete)
        paq_comprados = paq_comprados + 1
        for figura in paquete:
            if llenado_album[figura - 1] == 0:
                llenado_album[figura - 1] = 1
    return paq_comprados


print('Para llenar el album se debio comprar', cuantos_paquetes(669, 5), 'paquetes')


# Punto 4
# Calcular n_repeticiones=100 veces la funcion cuantos paquetes
# Utilizar figus_total=669, figus_paquete=5 y guardar resultados obtenidos en una lista. Calcular su promedio.

def cantidad_promedio(n_repeticiones, figus_total, figus_paquete):
    # HAGO UNA FUNCION QUE ME DEVUELVA UNA LISTA 'n'
    # DONDE SUS ELEMENTOS SON LA CANTIDAD DE PAQUETES QUE COMPRE PARA LLENAR CADA ALBUM
    n = []
    for i in range(0, n_repeticiones):
        cant = cuantos_paquetes(figus_total, figus_paquete)
        n.append(cant)
    return n


# Para una cierta cantidad de repeticiones 'n_repeticiones':
# agregar la cantidad de paquetes comprados por llenado de album a una lista 'n' hasta que se terminen las repeticiones
promedio_compras = cantidad_promedio(100, 669, 5)
print('Se compraron en promedio', np.mean(promedio_compras), 'paquetes para llenar cada album')


# ----------------------------------------------------------------------------------------


# ---- GUIA 2. Parte 3 HISTOGRAMAS ----

# Retomo las ultimas funciones de la guia de Figuritas:
# n_paquetes=cuantos_paquetes(figus_total,figus_paquete)
# Ahora armo una nueva función que ejecute un 'experimento', cuyo resultado almaceno en una variable tipo lista donde
# cada elemento es la cantidad de paquetes comprados:
def experimento(figus_total, figus_paquete, n_repeticiones):
    # En realidad es la misma funcion que cantidad_promedio pero con otro nombre (se pedia armar una nueva función)
    lista_exp = []
    for i in range(0, n_repeticiones):
        cant = cuantos_paquetes(figus_total, figus_paquete)
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
def repetir_experimento(figus_total, figus_paquete, n_repeticiones, n_rep_exp):
    promedios_n_experimentos = []
    for n in range(n_rep_exp):
        lista_promedio_exp_individual = experimento(figus_total, figus_paquete, n_repeticiones)
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
