# -*- coding: utf-8 -*-
# ---- GUIA 3. Dinámica de incendios forestales ----

"""  Ejercicio 1
Represente el estado del bosque mediante una lista denominada bosque de n elementos (n = 10 por
ejemplo), donde cada elemento representa una celda. Llamemos bosque vacıo a un bosque que solo
tenga celdas vacıas, bosque limpio a un bosque que solo tenga celdas vac ıas y  arboles vivos, bosque
quemado a un bosque que tenga celdas vacıas,  arboles vivos y  arboles quemados. Genere un bosque
de cada tipo. Implemente la funcion generar_bosque_vacio(n) que devuelva un bosque vacıo de n
posiciones.
"""

VACIO = 0
ARBOL = 1
QUEMADO = -1

import random
import numpy as np

def generar_bosque_vacio(tamanio_n):
    bosque = []
    for posicion in range(tamanio_n):
        bosque.append(0)
    return bosque


def generar_bosque_limpio(tamanio_n):
    bosque = []
    for posicion in range(tamanio_n):
        bosque.append(random.randint(0, 1))
    return bosque


def generar_bosque_quemado(tamanio_n):
    bosque = []
    for posicion in range(tamanio_n):
        bosque.append(random.randint(-1, 1))
    return bosque


print('Ejemplo de bosque vacio con n=10 :', generar_bosque_vacio(10))
print('Ejemplo de bosque limpio con n=10 :', generar_bosque_limpio(10))
print('Ejemplo de bosque quemado con n=10 :', generar_bosque_quemado(10))


"""  Ejercicio 2
Implemente la funcion brotes(bosque, p) que a partir de un bosque y de un valor real p genere un
 arbol en cada celda vacıa de dicho bosque con probabilidad p. Corra la funcion brotes empezando
con un bosque vacıo de n = 10 celdas y probabilidad p = 0,6. ¿Cuantos arboles brotaron en total?
Si corre nuevamente la funcion sobre el mismo bosque inicial, ¿cuantos  ́arboles brotaron? Pruebe
correr la funcion con un bosque limpio y con uno vacıo.
Sugerencia: construir una funcion suceso_aleatorio(prob) que genera un numero al azar y devuelve
True o False con la probabilidad indicada como par ́ametro.
"""


def suceso_aleatorio(prob):
    if random.random() < prob:
        return True
    else:
        return False


# print(suceso_aleatorio(.3)) #test
# print(suceso_aleatorio(.3))
# print(suceso_aleatorio(.3))
# voy a usar como parametro de probabilidad p=0.6
def brotes(bosque, p):
    arbol_nuevo = 0
    for sitio in range(len(bosque)):
        if bosque[sitio] == VACIO and suceso_aleatorio(
                p):  # si una posicion esta vacia y la probabilidad "es verdadera", entonces:
            bosque[sitio] = ARBOL  # "plantar" un arbol en la posicion vacia
            arbol_nuevo = arbol_nuevo + 1
    return bosque, arbol_nuevo


bosque = generar_bosque_vacio(10)
bosque, cant_brotes = brotes(bosque, .6)
print('Arboles que brotaron en el bosque vacio:', cant_brotes, '.Estado del bosque:', bosque, 'Tasa efectividad brotes',
      sum(bosque) / len(bosque))
bosque, cant_brotes = brotes(bosque, .6)
print('Nuevos arboles que brotaron en el mismo bosque, que ya no es vacio, en un nuevo ciclo:', cant_brotes,
      '.Estado del bosque:', bosque, 'Tasa efectividad brotes', sum(bosque) / len(bosque))

print('---Ahora pruebo en un bosque limpio:')
bosque = generar_bosque_limpio(10)
bosque, cant_brotes = brotes(bosque, .6)
print('Arboles que brotaron en el bosque limpio:', cant_brotes, '.Estado del bosque:', bosque,
      'Tasa efectividad brotes', sum(bosque) / len(bosque))
bosque, cant_brotes = brotes(bosque, .6)
print('Nuevos arboles que brotaron en el mismo bosque en un nuevo ciclo:', cant_brotes, '.Estado del bosque:', bosque,
      'Tasa efectividad brotes', sum(bosque) / len(bosque))


"""  Ejercicio 3
3. Construya una funcion cuantos(bosque, tipo_celda) que devuelva la cantidad de celdas que hay en
el bosque de la categorıa tipo_celda. Por ejemplo cuantos(bosque, 1) devuelve la cantidad de arboles
vivos, cuantos(bosque, -1) la cantidad de arboles quemados y cuantos(bosque, 0), la cantidad de
celdas vacıas.
Sugerencia: explore la funcion una_lista.count(0) cuando se aplica a la lista una_lista.
"""


def cuantos(bosque, tipo_celda):
    contador = bosque.count(tipo_celda)  # uso el metodo sugerido para contar un tipo de celda
    return contador


bosque = generar_bosque_quemado(100)  # bosque de ejemplo para verificar funcion
# Contando con la funcion cuantos(bosque,tipo_celda)
print('Cantidad de arboles quemados:', cuantos(bosque, QUEMADO))
print('Cantidad de arboles vivos:', cuantos(bosque, ARBOL))
print('Cantidad de sitios vacios:', cuantos(bosque, VACIO))

"""Probe la sugerencia y obtuve la misma cantidad para un tipo de celda. Asi que en lugar de escribir esta función:
```
def cuantos(bosque,tipo_celda):
  contador = 0
  for sitio in range(len(bosque)):
    if bosque[sitio] == tipo_celda: contador = contador + 1 #sumo a un contador si tengo ese tipo de celda
  return contador
```
Incorpore el metodo .count()

## Ejercicio 4
Implemente la funcion `rayos(bosque, f)` que realiza la caıda de rayos en un bosque con probabilidad
f. Suponga que en cada celda hay una probabilidad f de que caiga un rayo, si en la celda habıa
un arbol y cayo un rayo, entonces el arbol se quema (la celda pasa del estado 1 al estado -1), si la
celda estaba vacıa y cayo un rayo, no pasa nada (sigue en estado 0). Pruebe correr la funcion con
diferentes bosques con n = 100 celdas (por ejemplo un bosque completamente lleno de  arboles y
un bosque limpio que tenga la mitad de las celdas ocupadas por  ́arboles). ¿Que fraccion de arboles
resultan quemados?
"""


def rayos(bosque, f):
    for sitio in range(len(bosque)):
        if suceso_aleatorio(f) and bosque[sitio] == ARBOL:
            bosque[sitio] = QUEMADO
    return bosque


print('Verano en un bosque de 100 celdas con 100 arboles vivos')
bosque_vivo_100de100 = [1] * 100
print(bosque_vivo_100de100)
print(rayos(bosque_vivo_100de100, .1))
print('Se quemaron', cuantos(bosque_vivo_100de100, QUEMADO), 'arboles de los 100 que estaban vivos', )
print(' ')
print('Verano en un bosque de 100 celdas con 50 arboles vivos y 50 arboles vacios')
bosque_vivo_50de100 = [1] * 50 + [0] * 50
random.shuffle(bosque_vivo_50de100)
print(bosque_vivo_50de100)
print(rayos(bosque_vivo_50de100, .1))
print('Se quemaron', cuantos(bosque_vivo_50de100, QUEMADO), 'arboles de los 50 que estaban vivos', )


"""  Ejercicio 5
Implemente la funcion `propagacion(bosque)` que realiza la fase de propagacion de incendios en un
bosque. Luego de aplicar esta funcion en el bosque no queda ningun arbol vivo que sea vecino de un
arbol quemado. Pruebe correrla para los siguientes bosques:

+ `b_1 = [1, 1, 1, -1, 0, 0, 0, 0, 0, 0, -1, 1, 0]`
+ `b_2 = [-1, 1, 1, -1, 1, 1, 0, 1, 1, 1, 0, -1, 1]`
"""


def paso_propagacion(bosque):
    for sitio in range(len(bosque)):
        if bosque[sitio] == ARBOL:
            # si en el sitio hay un arbol vivo y si su anterior sitio (vecino) esta quemado, entonces la posicion actual se incendia
            if sitio > 0 and bosque[sitio - 1] == QUEMADO:
                bosque[sitio] = QUEMADO
                # si la posicion del sitio es menos a la longitud (check) y el siguiente sitio esta quemado, entonces la posicion actual se incendia (sentido contrario de propag al anterior)
            elif sitio < (len(bosque) - 1) and bosque[sitio + 1] == QUEMADO:
                bosque[sitio] = QUEMADO
    return bosque


def propagacion(bosque):
    bosque_0 = bosque.copy()  # copio la lista bosque que le doy a la funcion
    bosque_1 = paso_propagacion(bosque)  # guardo en otra variable un paso de propagacion
    while bosque_0 != bosque_1:  # Si un_paso no hizo nada, corto el while (es decir while actua mientras los estados del bosque cambien)
        bosque_0 = bosque_1.copy()  # copio el paso o cambio
        bosque_1 = paso_propagacion(bosque_1)  # paso a un nuevo paso
    return bosque_1


b_1 = [1, 1, 1, -1, 0, 0, 0, 0, 0, 0, -1, 1, 0]
b_2 = [-1, 1, 1, -1, 1, 1, 0, 1, 1, 1, 0, -1, 1]

print(b_1)
print(propagacion(b_1))

print(b_2)
print(propagacion(b_2))


"""  Ejercicio 6
Implemente la funcion `limpieza(bosque)` que reemplaza los arboles quemados por celdas vacıas.
"""

def limpieza(bosque):
    for sitio in range(len(bosque)):
        if bosque[sitio] == QUEMADO:
            bosque[sitio] = VACIO
    return bosque


print(limpieza(b_1))  # ejemplo


"""  Ejercicio 7
Implemente el programa de incendio forestal para un p y f fijos repitiendo varias veces (n rep = 50)
la dinamica anual del bosque, y calcule la cantidad de arboles que sobreviven (la produccion) en
promedio sobre todos los pasos de tiempo. Para ello:

+ Generar un bosque vacio de `n=100` celdas. 
+ En cada paso de tiempo `t` desde 1 hasta `n_rep` implementar la dinámica:
    
    a. **Primavera:** los árboles brotan con probabilidad `p` en un bosque limpio (y el resultado es un bosque limpio)
    
    b. **Rayos:** los rayos caen con probabilidad `f` sobre el bosque limpio. Ahora tenemos (probablemente) un bosque con elementos `QUEMADO`

    c. **Propagación incendio:** el fuego se esparce a *todos* los vecinos de los quemados.

    d. **Limpieza:** los árboles quemados pasan a posiciones vacías.

+ Registrar el número de arboles que hay, y devolver el bosque actualizado. De manera de poder realizar el próximo ciclo


Cuente y registre la cantidad de  ́arboles que sobreviven en el bosque obtenido y vuelva a la primavera con el bosque actual.

Sugerencia: Implemente una funcion que dado un bosque, y las probabilidades p y f, aplique las 4
etapas del anio sobre ese bosque.

Probemosla en un ciclo con `n=100`, `n_rep=50`, `f=0.02` y `p=0.4`.
"""


# implemento la sugerencia
def ciclo_anual(bosque_ciclo, p_brote, f_rayos):
    bosque = brotes(bosque_ciclo, p_brote)  # primavera
    bosque = rayos(bosque_ciclo, f_rayos)  # verano1
    bosque = propagacion(bosque_ciclo)  # verano2
    bosque = limpieza(bosque_ciclo)  # otoño-primavera
    return cuantos(bosque, ARBOL), bosque
    # la funcion me devuelve en el primer argumento cuantos arboles vivos quedan en invierno al cabo de un anio,
    # y en el segundo la lista bosque


# Parametros ciclo anual
n = 100  # cantidad de celdas del bosque
f = 0.02  # probabilidad de que un rayo caiga y proque un incendio
p = 0.4  # probabilidad de brotes viables
n_rep = 50  # cantidad de anios que se repite seguido el ciclo

bosque = generar_bosque_vacio(n)

# Veo que paso al cabo de 50 anios partiendo de un bosque vacio (sin arboles vivos pero con "semillas"=brotes)
arboles_vivos_por_anio = []  # en esta lista guardo en cada elementos la cantidad de arboles que quedaron vivos
for t in range(n_rep):
    cant_arboles_vivos, bosque = ciclo_anual(bosque, p, f)
    arboles_vivos_por_anio.append(cant_arboles_vivos)
print('Como esta el bosque al cabo de 50 anios? Tiene', cant_arboles_vivos, 'arboles vivos', bosque)
print('Listado de arboles que quedaron vivos cada anio:', arboles_vivos_por_anio)
print('En promedio quedaron vivos', np.mean(arboles_vivos_por_anio), 'arboles')

# Adicional: grafico arboles vivos en el tiempo, medido al fin de cada ciclo
import matplotlib.pyplot as plt

plt.style.use('dark_background')  # configuro todos los graficos en modo oscuro

plt.plot(range(n_rep), arboles_vivos_por_anio, color='green', linewidth=2.0)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.title('Conteo de arboles vivos en primavera por 50 anios')
plt.show()


""" Ejercicio 8 

Cuál es el valor óptimo de `p` (el que da lugar a una producción máxima de árboles) cuando `f=0.02`. Hacer un barrido de los distintos valores de `p` de `0` a  `1`, y hacer el gráfico correspondiente. 

**Sugerencia:** armar una función `evolucion(bosque, d, f, n_rep)` que realize el ciclo completo de `n_rep` anios, partiendo del estado inicial `bosque`. Esta función devuelve la lista de número de árboles al final de cada ciclo (y adicionalmente el estado final del bosque, que podría servir para nuevas simulaciones)
"""


def conteo_anual(bosque_ciclo, p_rep, f_rep,
                 n_rep):  # a esta altura tengo que tener mucho cuidado con los nombres de las variables
    lista_arboles = []
    for anio in range(n_rep):
        cant_arboles, bosque_rep = ciclo_anual(bosque_ciclo, p_rep, f_rep)
        lista_arboles.append(cant_arboles)
    return lista_arboles, bosque_rep  # cada vez que llamo la funcion me devuelve los arboles vivos al cabo de 'n_rep' anios


# NUEVOS PARAMETROS
n = 100
n_rep = 50
f = 0.02
lista_probabilidad = np.arange(0, 1, 0.01)  # el tercer argumento es el "paso" enter 0 y 1

barrido_p = []
for p in lista_probabilidad:
    bosque_bucle = generar_bosque_vacio(n)
    cant_vivos, bosque_50Y = conteo_anual(bosque_bucle, p, f, n_rep)
    barrido_p.append(np.mean(cant_vivos))
# Cada vez que chequeo un numero de la lista_probabilidad lo hago repitiendo un nuevo ciclo de 50 anios
plt.plot(lista_probabilidad, barrido_p, '.', color='red')  # x,y,color
plt.xlabel('valores de p')
plt.ylabel('arboles vivos. n_rep=50 anios')
plt.title('Rendimiento de produccion de arboles en 0<p<1')
plt.axhline(y=int(np.mean(barrido_p)), color='black', linestyle='-')
plt.show()
print('Promedio arboles vivos=', int(np.mean(barrido_p)))

"""Al ejecutar varias veces y analizar el grafico, se observa que los valores que serian optimos de p estan por arriba del promedio simple, y que este es desbalanceado por los extremos, asi que descarto eso valores y solo tomo los superiores al promedio de arboles vivos, aproximadamente entre 0.2 y 0.8

## Ejercicio 9 

(optativo*) Dinamica evolutiva. En esta version del modelo se permite que haya una heterogeneidad en el bosque: no todas las celdas tienen la misma probabilidad de hacer brotar arboles. Cada celda usa su propio valor de p para hacer brotar  ́arboles y en cada paso de tiempo t, despues de la
propagacion del incendio y antes de la epoca de limpieza, cada celda en la que habıa un arbol en la epoca de primavera modifica su valor de p:

*  si el arbol sobrevivio entonces p de la celda aumenta en 0,05.
*  si el arbol no sobrevivio, entonces p de la celda disminuye en 0,05. 

Las celdas donde no habıa arbol mantienen su valor de p. En un bosque de n = 100 celdas, inicialice un valor de p para cada celda; por ejemplo, p = 0,5 para cada celda, o un n ́umero al azar entre 0 y 1 para cada celda. Guarde la informacion en una lista `pes`. Simule la dinamica de propagacion de
incendios evolutiva con una probabilidad de caıda de rayos fija de f = 0,1. Compare los resultados obtenidos con la dinamica simple. Por ejemplo, evalue la distribucion final de p para la grilla de celdas. Grafique la cantidad de arboles que sobrevive en cada anio en funcion del tiempo. ¿Cual es
la produccion promedio en cada caso?
"""


# defino una nueva funcion brotes que tome cada valor p de una lista
# podria haberlo resuelto directamente en funcion_periodo pero preferi esta opcion
def brotes_p_var(bosque, p):  # bosque lista de arboles, p lista de probabilidades
    arbol_nuevo = 0
    for e in range(len(bosque)):
        if bosque[e] == VACIO and suceso_aleatorio(
                p[e]):  # si una posicion esta vacia y la probabilidad "es verdadera" para ese sitio, entonces:
            bosque[e] = ARBOL  # "plantar" un arbol en la posicion vacia
            arbol_nuevo = arbol_nuevo + 1
    return bosque


def evolucion_periodo(bosque_periodo, p_inicial, f_rayos, n_rep):
    p_list = []
    for n in range(len(bosque_periodo)):
        p_list.append(p_inicial)
    #  print(p_list)
    lista_vivos = []
    for anio in range(n_rep):
        bosque_periodo = brotes_p_var(bosque_periodo, p_list)  # primavera
        bosque_periodo = rayos(bosque_periodo, f_rayos)  # verano1
        bosque_periodo = propagacion(bosque_periodo)  # verano2
        # NUEVO comportamiento de la probabilidad ahora depende del estado del arbol
        for a in range(len(bosque_periodo)):
            if bosque_periodo[a] == ARBOL:
                p_list[a] = p_list[a] + 0.05
            elif bosque_periodo[a] == QUEMADO:
                p_list[a] = p_list[a] - 0.05
            round(p_list[a], 2)
        # otoño-primavera
        bosque_periodo = limpieza(bosque_periodo)
        cant_arboles = cuantos(bosque_periodo, ARBOL)
        lista_vivos.append(cant_arboles)
    p_list = [round(x, 2) for x in p_list]  # redondeo a dos decimales la probabilidad
    return lista_vivos, bosque_periodo, p_list


tamanio_bosque = 100
ej_vivos, ej_bosque, ej_p = evolucion_periodo(generar_bosque_vacio(tamanio_bosque), 0.5, 0.1, n_rep)
print(len(ej_vivos), len(ej_p))

plt.plot(range(n_rep), ej_vivos, color='green', linewidth=2.0)  # x,y,color
plt.xlabel('anios')
plt.ylabel('Conteo de arboles')
plt.title('Comportamiento del bosque en un periodo de 50 anios')
plt.show()

variacion_vivos = arboles_vivos_por_anio.copy()  # copio lista original de evolucion sin variacion de probabilidad
for n in range(len(variacion_vivos)):
    variacion_vivos[n] = variacion_vivos[n] - ej_vivos[n]
print(len(variacion_vivos), variacion_vivos)
plt.bar(range(n_rep), variacion_vivos, color='cyan')
plt.xlabel('anios')
plt.ylabel('diferencia de arboles con y sin var de p')
plt.show()


# En general se obtiene que crecen mas arboles con el modelo donde no varia p que con el modelo en el que si lo hace.


"""**Transformaciones y ajustes**
---------------------------------
Al finalizar la guía de Incendios se obtiene una función que simula el crecimiento de un
bosque en el tiempo.
1. Generar un bosque con los siguientes parámetros
(aproximados, pueden jugar un poco hasta encontrar algo que les guste más)
y graficar el número de arboles en función del número de ciclos.
```
Número máximo de árboles ~ 10000
Cantidad de ciclos (anios) ~ 50
p ~ 0.025
f ~ 0.025
```
"""

# VALORES FIJOS
bosque = generar_bosque_vacio(10000)
anios = 200  # valores que me resultaron interesantes:50,100,200,300,1000
p = 0.025
f = 0.025
cant_vivos, bosque_n_rep = conteo_anual(bosque, p, f,
                                        anios)  # aprovecho una funcion anterior donde p permanece constante
media_vivos = int(np.mean(cant_vivos))

anio_cambio = 20  # a ojo, valor fijo (lo elijo yo)
arboles_anio_cambio = cant_vivos[
    anio_cambio]  # guardo en una variable los arboles vivos en ese anio, me va a resultar util

# ---GRAFICO---#
plt.plot(range(anios), cant_vivos, color='lightgreen', linewidth=2.0)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.title('Conteo de arboles vivos en primavera por 50 anios. Promedio=' + str(media_vivos))
# Incorporo dos rectas como guia
# linea horizonntal dada por el promedio de arboles vivos en todo el periodo
plt.axhline(y=media_vivos, color='lightgray', linestyle='dashed')
# linea vertical incorporada a ojo en un valor alrededor del cual se comienza a estabilizar la poblacion de arboles (cambia comportamiento)
plt.axvline(x=anio_cambio, color='lightgray', linestyle='dashed')
plt.show()
print('Cantidad exacta de arboles a los', anio_cambio, 'anios (cambio comportamiento):', arboles_anio_cambio)

"""Observo que la cantidad anual de arboles se estabiliza a partir de los 20 anios aproximadamente y que sus valores se encuentran por encima de la media total de los 200 anios.

2. ¿Cuál es el valor en el que se estabiliza? Calcularlo con las herramientas que aprendieron hasta ahora.
"""

# Primero genero funciones que voy a necesitar para el analisis
from scipy.optimize import curve_fit


# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

# Esta función es necesaria para calcular el R^2
def rquared(y, y_fit):
    ss_res = np.sum((y - y_fit) ** 2)  # Suma de los residuos al cuadrado
    ss_tot = np.sum((y - np.mean(y)) ** 2)  # Suma Total de los cuadrados
    return 1 - (ss_res / ss_tot)  # R^2


# Funcion de ajuste lineal
def ajuste_lineal(x, y):
    f = lambda x, a, b: a * x + b  # la función modelo, con la que ajustamos
    popt, pcov = curve_fit(f, x, y)  # ajusto sin incertezas en y
    sigmas = np.sqrt([pcov[0, 0], pcov[
        1, 1]])  # las incertezas de los parametros son la raiz de la diagonal de la matriz de covarianza
    a = popt[0]  # pendiente
    b = popt[1]  # ordenada al origen
    ea = sigmas[0]  # desv std error pendiente
    eb = sigmas[1]  # desv std ordenda al origen
    R = rquared(y, a * x + b)  # R^2
    print('INFORMACION SOBRE EL AJUSTE LINEAL')
    print('R^2 = %0.2f' % R)
    print('Pendiente: %f ± %f' % (a, ea))
    print('Ordenada al origen: %f ± %f' % (b, eb))
    return a, b, ea, eb, R


# cambio de lista a array por un error que me da python, al tomar los elementos como float no puedo realizar la proximas operaciones, a menos que el objeto sea un array!
x_array = np.array(range(anios)[anio_cambio:anios])
y_array = np.array(cant_vivos[anio_cambio:anios])
a1, b1, ea1, eb1, R1 = ajuste_lineal(x_array, y_array)
print('')
print('Cantidad exacta de arboles a los', anio_cambio, 'anios:', arboles_anio_cambio)
# Defino recta del ajuste por ecuacion:
arboles_estable_ajuste1 = int(
    a1 * anio_cambio + b1)  # clase int, redondeo para abajo. Considero que no puedo tener por ej 2.37 arboles, tiene que ser un numero entero!
x_ajuste1 = range(anio_cambio, anios)
y_ajuste1 = [arboles_estable_ajuste1] * (anios - anio_cambio)
# ---GRAFICO---#
plt.figure(figsize=(10, 5))
plt.plot(range(anios), cant_vivos, color='lightgreen', linewidth=2.0)  # grafico de crecimiento
plt.plot(x_ajuste1, y_ajuste1, color='orange', linewidth=2.0)  # ajuste horizontal de etapa estable
plt.title('Conteo de arboles vivos en primavera por 50 anios. Promedio total=' + str(media_vivos), fontsize=16)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.axvline(x=anio_cambio, color='gray', linestyle='dashed')  # marco anio de cambio
plt.grid('on')
plt.show()

print('ESTIMACIONES DE ESTABILIZACION DE LA POBLACION DE ARBOLES A PARTIR DE LOS', anio_cambio, 'anioS')
print(' Por ajuste lineal:', arboles_estable_ajuste1)
arboles_estable_promedio = int(np.mean(cant_vivos[
                                       anio_cambio:anios]))  # promedio de lista de conteo anual de arboles desde que se estabilizo la poblacion, redondeado hacia abajo y convertido en tipo integer
print(' Por promedio:', arboles_estable_promedio)

"""En un principio pense un ajuste lineal con una pendiente poco pronunciada, pero esto no seria correcto conceptualmente si pienso que se estabilizada alrededor de un valor. Por otra parte R^2 me indica que de esta forma solo puedo explicar un 35% de los resultados, pero tengo que tener en cuenta que la poblacion varia en toda la fase creciendo y decreciendo ciclicamente, y de todas formas hasta los 200 anios varia entre cierto rango relativamente pequeño (aprox diferencia de 2 ordenes de magnitud)

3. ¿Cómo es el crecimiento? Seleccionar la fase inicial (transitoria) y graficarla con dis-
tintas transformaciones de los ejes.
```
Lineal ( y vs x ): y = a · x + b
Semilogy ( ln(y) vs x ) : y = b · exp(a · x)
ln(y) = ln(b · exp(a · x)) = ln(b) + ln(exp(a · x)) = a · x + ln(b)
Loglog ( ln(y) vs ln(x) ) : y = b · x^a
ln(y) = ln(b · x^a) = ln(b) + ln(x^a) = a · ln(x) + ln(b)
```
"""

# puntos de fase de crecimiento
x_crec = np.array(range(anios)[0:anio_cambio])
y_crec = np.array(cant_vivos[0:anio_cambio])

# ESCALAS
x_lin = x_crec + 1  # elimino punto cero
y_lin = y_crec
y_exp = np.exp(x_lin)
x_log = np.log(x_lin)
y_log = np.log(y_lin)

# GRAFICOS  CON DISTINTAS ESCALAS
fig_fase_inicial, (ax1, ax2, ax3) = plt.subplots(nrows=1,
                                                 ncols=3)  # incorporamos figuras como subplots ax1, ax2, ax3 del grafico 'fig_fase_inicial'
ax1.plot(x_lin, y_lin, '.')  # eje x:lineal /// eje y:lineal
ax2.plot(x_lin, y_log, '.')  # eje x:lineal /// eje y:log
ax3.plot(x_log, y_log, '.')  # eje x:log /// eje y:log
ax1.set(title='lineal')  # titulo primer graf, segundo, etc..
ax2.set(title='semilog')
ax3.set(title='loglog')
fig_fase_inicial.suptitle('Fase Inicial', fontsize=16)
fig_fase_inicial.show()

"""4. Ajustar una función lineal sólo en el caso que consideren apropiado. Luego reportar los valores obtenidos para los parámetros del ajuste, y los valores en la función original (sin transformar).

La escala log-log me resulta apropiada para realizar un ajuste lineal, aunque tengo concentrada una gran cantidad puntos en una region del grafico que no siguen un compartamiento muy lineal. Podria realizar dos ajustes, uno lineal hasta ln(2) y otro con alguna escala apropiada diferente, pero para simplificar realizo un solo ajuste.
"""

# Elijo la escala log-log y realizo un ajuste sobre esta
# ajuste lineal
a2, b2, ea2, eb2, R2 = ajuste_lineal(x_log, y_log)
# Con los parametros a,b
x_ajustelin = x_log  # clase lista
y_ajustelin = a2 * x_ajustelin + b2  # clase lista
# ---GRAFICO---#
plt.plot(x_ajustelin, y_ajustelin, color='red', linewidth=2)  # ajuste
plt.plot(x_log, y_log, '.')  # eje x:log /// eje y:log
plt.title('Ajuste lineal fase crecimiento. Log-Log', fontsize=16)
plt.grid('on')
plt.show()

# PARAMETROS
b = np.exp(b2)
a = a2
x_ajuste2 = range(0, anio_cambio)
y_ajuste2 = b * (x_ajuste2 ** a)
print('FUNCION:  y=', round(b, 2), '. x^(', round(a, 2), ').  Parametros de funcion potencial b=', b, ' , a=', a)
# ---GRAFICO---#
plt.figure(figsize=(10, 5))
plt.plot(range(anios), cant_vivos, color='lightgreen', linewidth=2.0)  # grafico de arboles por anio
plt.axvline(x=anio_cambio, color='gray', linestyle='dashed')  # marco anio de cambio

plt.plot(x_ajuste1, y_ajuste1, color='red')  # ajuste horizontal de etapa estable
plt.plot(x_ajuste2, y_ajuste2, color='red')  # ajuste exp etapa de crecimiento

plt.title('Comportamiento de poblacion de bosque', fontsize=16)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.grid('on')
plt.show()

"""5. ¿Cómo varía la curva para distintos valores de p? Graficar con la transformación que corresponda y ajustar.
Repetirlo para distintos valores de p y graficar el valor de los parámetros del ajuste en función del valor de p. ¿Cómo varía el R2?"""

anios = 200

plt.figure(figsize=(15, 5))
valores_prob_brotes = [0.005, 0.015, 0.025, 0.035, 0.045]  # lista distintos valores de p
# En un ciclo finito de repeticion hago que corra y dibuje los dintintos valores de p
leyenda = []
l = 0
for p in valores_prob_brotes:
    bosque = generar_bosque_vacio(10000)
    cant_vivos, estado_bosque = conteo_anual(bosque, p, 0.025, anios)
    plt.plot(range(anios), cant_vivos, linewidth=2.0)
    leyenda.append('p={}'.format(valores_prob_brotes[l]))
    l = l + 1
plt.legend(leyenda)
plt.title('Crecimiento del bosque con distintos rendimientos de brotes', fontsize=18)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.grid('on')
plt.xticks(np.arange(0, 200, 10))
plt.show()

"""A mayor p, mas se retrasa el cambio de comportamiento del crecimiento a una fase estable.
Tambien aumenta la variacion de la poblacion una vez que alcanzo la fase estable"""

lista_a = []
lista_b = []
lista_R2 = []
lista_cambio = [40, 30, 20, 15,
                10]  # en orden segun cada p, elegidos a ojo donde aprox esta el cambio de comportamiento
p_count = 0
leyenda = []
l = 0
for anio_cambio in lista_cambio:
    print('anio PROPUESTO DE CAMBIO DE COMPORTAMIENTO=', anio_cambio)
    P = valores_prob_brotes[0 + p_count]
    print('Probabilidad de brotes=', P)
    bosque = generar_bosque_vacio(10000)
    cant_vivos, estado_bosque = conteo_anual(bosque, P, 0.025, anios)
    # ESCALAS
    x_lin_crec = np.array(range(anios)[0:anio_cambio]) + 1  # elimino punto cero
    y_lin_crec = np.array(cant_vivos[0:anio_cambio])
    x_log_crec = np.log(x_lin_crec)
    y_log_crec = np.log(y_lin_crec)
    A, B, EA, EB, R2 = ajuste_lineal(x_log_crec, y_log_crec)
    # agregos los parametros a,b,R a listas para su posterior recuperacion.
    lista_a.append(A)
    lista_b.append(B)
    lista_R2.append(R2)
    # Con los parametros A,b
    x_ajustelin = x_log_crec  # clase lista
    y_ajustelin = A * x_ajustelin + B  # clase lista
    # ---GRAFICO DE PRUEBA:RECTAS DE AJUSTE---#
    plt.plot(x_ajustelin, y_ajustelin, linewidth=2.0)  # ajuste
    # plt.plot(x_log_crec,y_log_crec,'.') #eje x:log /// eje y:log de puntos de crecimiento
    plt.title('Ajuste lineal fase crecimiento. Log-Log', fontsize=16)
    leyenda.append('p={}'.format(valores_prob_brotes[p_count]))
    p_count = p_count + 1
    print('')
    print('')
plt.legend(leyenda)
plt.grid('on')
plt.show()
print('Prob de brote', valores_prob_brotes)
print('Parametros a', lista_a, 'de regresion lineal')
print('Parametros b', lista_b, 'de regresion lineal')
print('Parametros R2', lista_R2, 'de regresion lineal')

# SUBPLOTS DE PARAMETROS SEGUN VALOR DE P
fig_fase_inicial, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(16, 4))
ax1.scatter(valores_prob_brotes, lista_a, s=50, color='red')
ax2.scatter(valores_prob_brotes, lista_b, s=50, color='red')
ax3.scatter(valores_prob_brotes, lista_R2, s=50, color='red')
ax1.set(title='Parametro a', xlabel='Probabilidad brote', ylabel='Valor a')
ax2.set(title='Parametro b', xlabel='Probabilidad brote', ylabel='Valor b')
ax3.set(title='Bondad de ajuste', xlabel='Probabilidad brote', ylabel='Valor R^2')
ax1.grid('on')
ax2.grid('on')
ax3.grid('on')
fig_fase_inicial.suptitle('Distribucion de parametros de regresion en escalo log-log segun probabilidad de brotes',
                          fontsize=16)
fig_fase_inicial.show()

"""Lo que varia significativamente es el valor de la ordenada al origen 'b' en la escala logaritmica, que en una
escala normal lineal es el coeficiente no exponencial de una funcion potencial y cambia la rapidez de crecimiento.
A mayor b, mas 'inclinada' estara la curva.

El parametro 'a' varia mucho menos pero no sigue un comportamiento y su valor es siempre menor a 1.
R^2 es cercano a 1 en cualquier caso y deberian tener valores similares,
en la medida que haya elegido bien el anio de cambio y realice un correcto ajuste lineal,
ya que le puedo estar agregando puntos a la regresion que no siguen el comportamiento planteado.

6. ¿Cómo varía la curva para distintos valores de f?
"""

anios = 200
p = 0.025

plt.figure(figsize=(15, 5))
valores_prob_rayos = [0.005, 0.015, 0.025, 0.035, 0.045]  # lista distintos valores de f
# En un ciclo finito de repeticion hago que corra y dibuje los dintintos valores de f
leyenda = []
i = 0
for f in valores_prob_rayos:
    bosque = generar_bosque_vacio(10000)
    cant_vivos, estado_bosque = conteo_anual(bosque, p, f, anios)
    plt.plot(range(anios), cant_vivos, linewidth=2.0)
    leyenda.append('f={}'.format(valores_prob_brotes[i]))
    i = i + 1
plt.legend(leyenda)
plt.grid('on')
plt.xticks(np.arange(0, 200, 10))
plt.title('Crecimiento del bosque con distinta probabilidad de tormenta electrica', fontsize=18)
plt.xlabel('anios')
plt.ylabel('Arboles vivos')
plt.show()

"""Cuanto menor sea f, mayor sera el valor de cantidad de arboles en el que se estabiliza la poblacion,
pero tambien aumenta el tiempo que tarda en alcanzar el valor estable
"""