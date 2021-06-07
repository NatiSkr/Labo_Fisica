# -*- coding: utf-8 -*-
# ---- GUIA 4 ÓRBITAS ----

"""  EJERCICIO 1
Consideramos que la Tierra comienza moviendose en la
direccion del eje y. Definamos las posiciones en x e y como listas donde iremos guardando las posiciones futuras:

*   `x_lista = [-147095000000.0, -147095000000.0]` (atencion que es necesario poner el .0 decimal para que se pueda usar np.sqrt() para la raız cuadrada)
*   `y_lista = [0.0, 2617920000.0]`
*   `dt = 60 * 60 * 24` (para que el paso del tiempo sea un dıa en segundos).
*   `tiempo_total = 400` (para simular un poco mas de un año.)
*   `x_sol = 0, y_sol = 0` (recuerden que consideramos quieto al Sol)


Para realizar la simulacion, primero definamos funciones que devuelvan la aceleracion tomando las posiciones actuales
del Sol y la Tierra, usando las ecuaciones de la figura:

* La funcion `calcula_delta(x sol, x tierra)` que recibe dos posiciones en una dimension (x o y)
y retorna la diferencia entre ambas

* La funcion `calcula_distancia(pos sol,pos tierra)`, que recibe dos listas, una con la posicion [x sol,y sol]
y otra con la posicion [x tierra,y tierra] y retorna la distancia entre ambas.

*La funcion `calcula_aceleracion(pos sol,pos tierra)` que recibe dos listas, una con la posicion [x sol,y sol]
y otra con la posicion [x tierra,y tierra] y usando las dos funciones anteriores, calcula la aceleracion gravitatoria,
retornando una lista con dos valores [aceleracion x,aceleracion y].
"""

#IMPORTO LIBRERIAS / PAQUETES
import numpy as np
# Tambien podria usar Scipy https://docs.scipy.org/doc/scipy/reference/constants.html
# pero no me quiero arriesgar a usar como variable algo que este contenido en esa lib

#DECLARO VARIABLES
G = 6.693*10**-11 # Constante de gravitacion. Unidades N*m^2/kg^2
M = 1.98*10**30 # Masa del Sol, unidades=kg

delta_t = 60 * 60 * 24 #para que el paso del tiempo sea un dıa pero medido en segundos
tiempo_total = 400 #años simuladores (para simular un poco mas de un año.)

#posicion inicial de la tierra en metros. Del tiempo 't= -dt' al tiempo 't=0', la posición cambió pero solo en, no en x
x_lista = [-147095000000.0, -147095000000.0]
y_lista = [0.0, 2617920000.0]

#posicion sol
r_Sol=[0,0] #consideramos quieto al Sol

#Armo las primeras funciones
def calcular_delta(sol_1D, tierra_1D):  #tomo como referencia el sol que en mi sistemas de referencia va a estar fijo
  delta = sol_1D - tierra_1D
  return delta

def calcular_distancia(pos_sol, pos_tierra): #imput: dos listas de dos elementos
  #Formato pos_sol=[x_sol,y_sol]
  #Formato pos_tierra[x_tierra,y_tierra]
  if len(pos_sol)==len(pos_tierra)==2: #chequeo que esten en los mismos espacios vectoriales
    distancia = np.sqrt( (pos_sol[0] - pos_tierra[0])**2 + (pos_sol[1] - pos_tierra[1])**2 )
    return distancia #me devuelve un 'int' o 'float' como coordenadas vectoriales de la diferencia de distancia
  else: return print('Las coordenadas de posicion estan en espacios diferentes')
r_Tierra_0 = [x_lista[1], y_lista[1]]
print(calcular_distancia(r_Sol, r_Tierra_0))

def calcula_aceleracion(pos_sol,pos_tierra): #imput: dos listas de dos elementos. Calcula las aceleraciones instantaneas
#usando las dos funciones anteriores, calcula la aceleracion gravitatoria,
# retornando una lista con dos valores [aceleracion x,aceleracion y].
  aceleracion = []
  d = calcular_distancia(pos_sol,pos_tierra)  #almaceno resultado 'list'
  x = calcular_delta(pos_sol[0], pos_tierra[0]) #almaceno resultado 'int' o 'float'
  y = calcular_delta(pos_sol[1], pos_tierra[1]) #almaceno resultado 'int' o 'float'
  aceleracion_x = ( (G*M) / d**2) * ( x / d) 
  aceleracion_y = ( (G*M) / d**2) * ( y / d)
  aceleracion = [aceleracion_x, aceleracion_y]
  return aceleracion

tierra0=[-147095000000.0,0]
tierra1 = [-147095000000.0, 2617920000.0]
print(calcula_aceleracion(r_Sol,tierra0))
print(calcula_aceleracion(r_Sol,tierra1))

"""## EJERCICIO 2
Definan las variables y funciones a utilizar y, usando las funciones, calculen las dos primeras aceleraciones correspondientes a las dos primeras posiciones dadas.

Nota: esto ya lo empece en el punto anterior, en la siguiente celda solo hago el calculo usando las dos primeras posiciones

"""

#Listas donde almaceno las dos primeras aceleraciones para usar con verlet
lista_aceleracion_x =[]
lista_aceleracion_y =[]

r_Tierra_ant = [x_lista[0], y_lista[0]] #posicion de la tierra antes del instante cero
aceleraciones = calcula_aceleracion ( r_Sol , r_Tierra_ant )
lista_aceleracion_x.append ( aceleraciones[0] )
lista_aceleracion_y.append ( aceleraciones[1] )

r_Tierra_0 = [x_lista[1], y_lista[1]] #posicion de la tierra en t=0
aceleraciones = calcula_aceleracion ( r_Sol , r_Tierra_0 )
lista_aceleracion_x.append ( aceleraciones[0] )
lista_aceleracion_y.append ( aceleraciones[1] )

print('aceleraciones en x (m/s^2)',lista_aceleracion_x)
print('aceleraciones en y (m/s^2)',lista_aceleracion_y)
print('Dias de medicion [0,1]')

"""## EJERCICIO 3
Defina la funcion `realizar_verlet(pos anterior,pos actual,aceleracion actual,dt)`, que recibe dos posiciones en forma de listas, `pos_anterior= [x anterior,y anterior]`, `pos_actual=[x actual,y actual]`, y la `aceleracion_actual=[aceleracion x,aceleracion y]`, y usando las ecuaciones de la figura devuelva `pos_posterior = [x posterior,y posterior]`.
"""

def realizar_verlet(pos_anterior,pos_actual,aceleracion_actual,dt):
  pos_posterior = []
  pos_x = 2*pos_actual[0] - pos_anterior[0] + aceleracion_actual[0]*dt**2  # me da la nueva posicion en x (indice 0)
  pos_y = 2*pos_actual[1] - pos_anterior[1] + aceleracion_actual[1]*dt**2  # me da la nueva posicion en y (indice 1)
  pos_posterior = [pos_x, pos_y]
  return pos_posterior # devuelve lista [x posterior,y posterior] con las nuevas posiciones de la Tierra

#test

anterior = (x_lista[0],y_lista[0])
actual = (x_lista[1],y_lista[1])
aceleracion = calcula_aceleracion(r_Sol,actual)
realizar_verlet(anterior,actual,aceleracion,delta_t)

"""## EJERCICIO 4
Realice un ciclo que utilizando la funcion realiza verlet vaya calculando y guardando la trayectoria terrestre, los dıas correspondientes y las aceleraciones en las listas definidas.



"""

tiempo = 400
r_previo = r_Tierra_ant #= [x_lista[0], y_lista[0]] posicion de la tierra antes del instante cero
r_inicial = r_Tierra_0 #[x_lista[1], y_lista[1]] posicion de la tierra en t=0
a_inicial = [ lista_aceleracion_x[1] , lista_aceleracion_y[1]]
#ARMO UNA FUNCION PORQUE PUEDE RESULTAR UTIL PARA CALCULAR OTRAS ORBITAS
def calcular_orbita (pos_tierra_dia , pos_tierra_ant , pos_sol , A_actual , dias ):
  tiempo_total = dias #en dias
  #Inicializo con las primeras 2 posiciones iniciales
  r_anterior = pos_tierra_ant #= [x_lista[0], y_lista[0]] posicion de la tierra antes del instante cero
  r_actual = pos_tierra_dia  #[x_lista[1], y_lista[1]] posicion de la tierra en t=0
  # Tomo los datos de 'actual' como las posiciones y aceleraciones del dia 1
  dias_lista = [1]
  Rx_lista = [r_actual[0]]
  Ry_lista = [r_actual[1]]
  Ax_lista = [A_actual[0]]
  Ay_lista = [A_actual[1]]
  for i in range (2 , tiempo_total+1) :
    # Guardo el dia
    dias_lista.append(i)
    # Calculo la aceleracion
    A_xy = calcula_aceleracion(r_Sol, r_actual)
    # Calculo la posicion futura
    r_posterior = realizar_verlet(r_anterior, r_actual, A_xy, delta_t)
    # Guardo posiciones nuevas del dia
    Rx_lista.append(r_posterior[0])
    Ry_lista.append(r_posterior[1])
    # Guardo nuevas aceleraciones
    A_xy = calcula_aceleracion(r_Sol, r_posterior)
    Ax_lista.append(A_xy[0])
    Ay_lista.append(A_xy[1])
    # Actualizo listas con las posiciones
    r_anterior = r_actual
    r_actual = r_posterior
  return Rx_lista , Ry_lista , Ax_lista , Ay_lista , dias_lista

Posiciones_x , Posiciones_y , Aceleraciones_x , Aceleraciones_y , Dias = calcular_orbita( r_inicial , r_previo , r_Sol , a_inicial , tiempo)

print('Longitud Posiciones_x ',len(Posiciones_x),Posiciones_x)
print('Longitud Posiciones_y ',len(Posiciones_y),Posiciones_y)
print('Longitud Ax_lista ',len(Aceleraciones_x),Aceleraciones_x)
print('Longitud Ay_lista ',len(Aceleraciones_y),Aceleraciones_y)
print('Longitud lista Dias ',len(Dias),Dias)

"""## EJERCICIO 5
Importar la biblioteca necesaria y graficar la trayectoria en el plano (x, y).



"""

import matplotlib.pyplot as plt
plt.style.use('dark_background') #configuro todos los graficos en modo oscuro
if len(Posiciones_x)==len(Posiciones_y):  #chequeo que las listas sean del mismo tamaño para graficar
  plt.plot ( Posiciones_x , Posiciones_y , color='grey')
  plt.title('Trayectoria de la Tierra')
  plt.xlabel('Posicion en x')
  plt.ylabel('Posicion en y')
  plt.show()

"""## EJERCICIO 6
Grafique ahora la aceleracion x o y en funcion de los dıas.
Vamos a hacer un video animado del movimiento. Para eso necesitamos ir guardando una sucesion de fotos de cada dıa.
"""

if len(Dias)==len(Aceleraciones_x):  #chequeo que las listas sean del mismo tamaño para graficar
  plt.plot ( Dias , Aceleraciones_x , color='cyan')
  plt.title('Desplazamiento en x de la Tierra')
  plt.xlabel('Dias')
  plt.ylabel('Posicion en x')
  plt.show()
else: print('Error: Hay una discrepancia entre los datos de aceleracion en el eje x y el tiempo de medicion')

if len(Dias)==len(Aceleraciones_y): 
  plt.plot ( Dias , Aceleraciones_y , color='cyan')
  plt.title('Desplazamiento en y de la Tierra')
  plt.xlabel('Dias')
  plt.ylabel('Posicion en y')
  plt.show()
else: print('Error: Hay una discrepancia entre los datos de aceleracion en el eje y y el tiempo de medicion')

"""## EJERCICIO 7
Arme una funcion hacer foto(lista x,lista y,pos sol,dia) que reciba las posiciones de la Tierra y el Sol y un dıa, y haga un grafico que muestre la trayectoria en el plano (x, y) de la Tierra, el Sol como un punto amarillo y la Tierra como un punto azul en el dıa elegido.

"""

def hacer_foto_orbita ( lista_x , lista_y , pos_sol , dia ) :
  # borra lo que hubiera antes en la figura
  plt.clf ()
  # grafico trayectoria (x,y)
  plt.plot ( lista_x , lista_y , 'grey')
  plt.title('Trayectoria de la Tierra alrededor del Sol. Dia:'+str(dia))
  # grafico al Sol
  #’yo ’ es para hacer un punto amarillo ( ’y’ de yellow y ’o’ de punto )
  #ms elige el tamanio del punto
  plt.plot ( pos_sol[0], pos_sol[1],'yo', ms =20)
  # grafico a la Tierra mas chiquita
  #’b’ es por blue
  plt.plot( lista_x[dia+1] , lista_y[dia+1] ,'bo', ms =10)
  plt.show
  return

hacer_foto_orbita( Posiciones_x , Posiciones_y , r_Sol , 60)

"""## EJERCICIO 8
Copie la funcion `hacer_video(lista x,lista y,pos sol,dia, nombre video)` que reciba las posiciones de la Tierra y el Sol, y guarde un video con la animacion del movimiento, con `nombre_video` como nombre del archivo. Necesitara tener instalada la biblioteca imageio e importarla

```
import imageio

def hacer_video ( lista_x , lista_y , pos_sol , nombre_video ) :
  lista_fotos =[] # aca voy a ir guardando las fotos
  for i in range (len ( lista_x ) ) :
    if i %2==0: # esto es para guardar 1 de cada 2 fotos y tarde menos
      hacer_foto ( lista_x , lista_y , pos_sol , i )
      plt . savefig ( nombre_video +’.png ’)
      lista_fotos . append ( imageio . imread ( nombre_video +’. png ’) )
    print (str( i ) +’ de ’+str(len( lista_x ) ) +’ fotos guardadas ’)
  imageio . mimsave ( nombre_video +’.mp4 ’, lista_fotos ) # funcion que crea el video
  print (’Video Guardado ’)
```


"""

import imageio
 
def hacer_video_orbita ( lista_x , lista_y , pos_sol , nombre_video ) :
  lista_fotos =[] # aca voy a ir guardando las fotos
  for i in range (len ( lista_x ) ) :
    if i %2==0: # esto es para guardar 1 de cada 2 fotos y tarde menos
      hacer_foto_orbita ( lista_x , lista_y , pos_sol , i )
      plt.savefig ( nombre_video +'.png' )
      lista_fotos.append ( imageio.imread ( nombre_video +'.png') )
    #print (str(i) + 'de' +str(len( lista_x ) ) + 'fotos guardadas') #test, quitar # al inicio para verificar que se guardan las fotos
  imageio.mimsave ( nombre_video +'.mp4', lista_fotos ) # funcion que crea el video
  print ('Video Guardado')

hacer_video_orbita ( Posiciones_x , Posiciones_y , r_Sol , 'Movimiento_traslacion' )

"""## EJERCICIO 9
¿Como cambia la forma de la trayectoria si la Tierra de pronto fuera al doble de velocidad?
(Ayuda: para esto deber ́ıamos multiplicar `lista_y[1]` por 2, ¿Por que?)

Al principio del movimiento pareciera que toma una orbita circular, pero luego sigue una trayectoria recta

Multiplicamos por 2 el algoritmo de Verlet duplica la velocidad al hacer el producto de la posicion por un escalar
"""

#Para esto me resultaba util el punto 4 en forma de función. En este codigo lista_y[1] = r_inicial[1] = r_Tierra_0[1]
r_inicial2 = [ x_lista[1] , y_lista[1]*2 ] #[x_lista[1], y_lista[1]] posicion de la tierra en t=0
#Tengo que volver a calcular la aceleracion del primer dia
a_inicial2 = calcula_aceleracion ( r_Sol , r_inicial )  # aceleracion en x , aceleracion en y en el primer dia

Posiciones2_x , Posiciones2_y , Aceleraciones2_x , Aceleraciones2_y , Dias2 = calcular_orbita( r_inicial2 , r_previo , r_Sol , a_inicial2 , tiempo)

print('Longitud Posiciones2_x ',len(Posiciones2_x),Posiciones2_x)
print('Longitud Posiciones2_y ',len(Posiciones2_y),Posiciones2_y)
print('Longitud Aceleraciones2_x ',len(Aceleraciones2_x),Aceleraciones2_x)
print('Longitud Aceleraciones2_y ',len(Aceleraciones2_y),Aceleraciones2_y)
print('Longitud lista Dias ',len(Dias),Dias2)

if len(Posiciones2_x)==len(Posiciones2_y):  #chequeo que las listas sean del mismo tamaño para graficar
  plt.plot ( Posiciones2_x , Posiciones2_y , color='grey')
  plt.title('Trayectoria de la Tierra')
  plt.xlabel('Posicion en x')
  plt.ylabel('Posicion en y')
  plt.show()

hacer_foto_orbita( Posiciones2_x , Posiciones2_y , r_Sol , 60)

"""## EJERCICIO 10
¿Y si la velocidad fuera la mitad? ¿Es suficientemente chiquito el dt?

Ahora resulta que en cierto rango de tiempo el sol se acerca o se aleja mucho al sol
"""

r_inicial3 = [ x_lista[1] , y_lista[1]*0.5 ] #[x_lista[1], y_lista[1]] posicion de la tierra en t=0
a_inicial3 = calcula_aceleracion ( r_Sol , r_inicial )  # aceleracion en x , aceleracion en y en el primer dia
Posiciones3_x , Posiciones3_y , Aceleraciones3_x , Aceleraciones3_y , Dias3 = calcular_orbita( r_inicial3 , r_previo , r_Sol , a_inicial3 , tiempo)

if len(Posiciones3_x)==len(Posiciones3_y):  #chequeo que las listas sean del mismo tamaño para graficar
  plt.plot ( Posiciones3_x , Posiciones3_y , color='grey')
  plt.title('Trayectoria de la Tierra')
  plt.xlabel('Posicion en x')
  plt.ylabel('Posicion en y')
  plt.show()

hacer_foto_orbita( Posiciones3_x , Posiciones3_y , r_Sol , 60)

"""## EJERCICIO 11
Modifique las funciones `hacer_foto` y `hacer_video` para que reciban tambien las listas de aceleracion y la agreguen al grafico. Para esto puede utilizar la funcion arrow(x1,y1,x2,y2) de matplotlib, la cual grafica una flecha que nace (x1,y1) y apunta en la direccion (x2,y2).

Modifique la siguiente lınea para que la flecha nazca en la posicion de la Tierra del dıa correspondiente, y añadala a la funcion `hacer_foto`.


```
plt . arrow ( ___COMPLETAR___ , ___COMPLETAR___ , aceleracion_x [ dia ]*10**12.5 , aceleracion_y [ dia ]*10**12.5 , width =10**9.5 , Color =’g’)
```


"""

def hacer_foto_movimiento ( lista_x , lista_y , pos_sol , aceleracion_x , aceleracion_y , dia ) :
  # borra lo que hubiera antes en la figura
  plt.clf ()
  # grafico trayectoria (x,y)
  plt.plot ( lista_x , lista_y , 'grey')
  plt.title('Trayectoria de la Tierra alrededor del Sol. Dia:'+str(dia))
  # grafico al Sol
  #’yo ’ es para hacer un punto amarillo ( ’y’ de yellow y ’o’ de punto )
  #ms elige el tamanio del punto
  plt.plot ( pos_sol[0], pos_sol[1],'yo', ms =20)
  # grafico a la Tierra mas chiquita
  #’b’ es por blue
  plt.plot( lista_x[dia+1] , lista_y[dia+1] ,'bo', ms =10)
  # grafico la flecha
  plt.arrow( lista_x[dia], lista_y[dia], aceleracion_x[dia]*10**12.5, aceleracion_y[dia]*10**12.5, width = 10**9.5 , color ='green')
  #plt.show
  return

hacer_foto_movimiento( Posiciones3_x , Posiciones3_y , r_Sol , Aceleraciones3_x , Aceleraciones3_y , 300 )

def hacer_video_movimiento ( lista_x , lista_y , pos_sol , aceleracion_x , aceleracion_y , nombre_video ) :
  lista_fotos =[] # aca voy a ir guardando las fotos
  for i in range (len ( lista_x ) ) :
    if i %2==0: # esto es para guardar 1 de cada 2 fotos y tarde menos
      hacer_foto_movimiento ( lista_x , lista_y , pos_sol , aceleracion_x , aceleracion_y, i )
      plt.savefig ( nombre_video +'.png' )
      lista_fotos.append ( imageio.imread ( nombre_video +'.png') )
    #print (str(i) + 'de' +str(len( lista_x ) ) + 'fotos guardadas') #test, quitar # al inicio para verificar que se guardan las fotos
  imageio.mimsave ( nombre_video +'.mp4', lista_fotos ) # funcion que crea elvideo
  print ('Video Guardado')

hacer_video_movimiento( Posiciones3_x , Posiciones3_y , r_Sol , Aceleraciones3_x , Aceleraciones3_y , 'Movimiento_orbita_+_aceleracion' )

"""## EJERCICIO 12
 (opcional) ¿Como calcular ́ıa la velocidad punto a punto? Grafıquela en funcion de los dıas.

13. (opcional) Explorar en la pagina de la NASA para obtener las posiciones y masas de distintos planetas y agregarlos a la animacion. (note que estan en unidades astronomicas y debe pasarlos a
metros)
https://ssd.jpl.nasa.gov/horizons.cgi#results

14. (opcional) Busc ́a en la p ́agina de la NASA la posici ́on de la Tierra el dıa de tu nacimiento y fijate si podes determinar que dıa ocurrio el primer perihelio o afelio de tu vida (las distancia ́ḿınima y maxima de la Tierra al Sol). Te puede ser  ́util el siguiente link: https://www.timeanddate.com/
date/dateadd.html
"""