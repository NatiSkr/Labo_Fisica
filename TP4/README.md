Corresponde a la Actividad N°4 'Órbitas' de la cursada virtual de Mecanica y Termodinamica, DF, FCEyN.

Formato original: Jupyter notebook .ipynb

Generado automaticamente por Colaboratory


Para utilizar el algoritmo de Verlet, necesitamos dos posiciones iniciales, es decir un
par `(x[i-1], x[i])` y otro `(y[i-1],y[i])`.

Tomamos estas de un momento en particular de la orbita terrestre, sacadas de la pagina de la NASA https://ssd.jpl.nasa.gov/horizons.cgi


ERRORES CONOCIDOS
- generación de listas de planeta
- escala de video incorrecta --> ajustar tamaño de graficos a ancho y alto fijo. El cambio de magnitud del vector aceleracion reescala todo