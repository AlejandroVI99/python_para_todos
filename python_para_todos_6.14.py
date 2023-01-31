'''
Ejercicio 5: Toma el siguiente código en Python que almacena una ca-
dena:
str = 'X-DSPAM-Confidence:0.8475'
Utiliza find y una parte de la cadena para extraer la porción de la cadena
después del carácter dos puntos y después utiliza la función float para
convertir la cadena extraída en un número de punto flotante.
'''
str = 'X-DSPAM-Confidence:0.8475'
dos_puntos = str.find(':')
numero = str[dos_puntos + 1:]
resultado = float(numero)
print(resultado)
'''
Ejercicio 6: Lee la documentación de los métodos de cadenas en
https://docs.python.org/library/stdtypes.html#string-methods Quizá
quieras experimentar con algunos de ellos para asegurarte de entender
como funcionan. strip y replace son particularmente útiles.
La documentación usa una sintaxis que puede ser confusa. Por ejem-
plo, en find(sub[, start[, end]]), los corchetes indican argumentos op-
cionales. De modo que sub es requerido, pero start es opcional, y si se
incluye start, entonces end es opcional.
'''