Corresponde a la Actividad N°3 'Dinámica de incendios forestales' de la cursada virtual de Mecanica y Termodinamica, DF, FCEyN.

Formato original: Jupyter notebook .ipynb

Generado automaticamente por Colaboratory


Vamos a representar un bosque *unidimensional*, es decir que tenemos una cadena `n` de posiciones,
cada una de las cuales puede estar en uno de los siguientes estados:

+ **0** representa una posición vacia (`VACIO`);
+ **1** representa un árbol (`ARBOL`); y
+ **-1** representa un árbol quemado (`QUEMADO`).

Este bosque lo vamos a representar entonces por una lista de *python* de longitud `n`,
donde cada elemento de ella podrá estar en cada uno de los estados anteriores.
Un *bosque vacio* va a tener todos los elementos en el estado `VACIO`.
Y un *bosque limpio* solo puede tener elementos `ARBOL` o `VACIO` (pero no puede tener posiciones en estado `QUEMADO`)