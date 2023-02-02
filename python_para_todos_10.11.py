'''
Ejercicio 1: Revisa el programa anterior de este modo: Lee y analiza
las líneas “From” y extrae las direcciones de correo. Cuenta el número
de mensajes de cada persona utilizando un diccionario.
Después de que todos los datos hayan sido leídos, imprime la persona con
más envíos, creando una lista de tuplas (contador, email) del diccionario.
Después ordena la lista en orden inverso e imprime la persona que tiene
más envíos.
Línea de ejemplo:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Ingresa un nombre de archivo: mbox-short.txt
cwen@iupui.edu 5
Ingresa un nombre de archivo: mbox.txt
zqian@umich.edu 195
'''
archivo = open('mbox-short.txt')
correos = dict()

for line in archivo:
    renglon = line.split()
    if len(renglon) > 0 and renglon[0] == 'From':
      if renglon[1] not in correos:
        correos[renglon[1]] = 1
      else:
        correos[renglon[1]] += 1

lista = list()
for clave, valor in list(correos.items()):
  lista.append((valor, clave))

lista.sort(reverse=True)

for clave, valor in lista[:1]:
  print(valor, clave)
'''
Ejercicio 2: Este programa cuenta la distribución de la hora del día
para cada uno de los mensajes. Puedes extraer la hora de la línea
“From” buscando la cadena horaria y luego dividiendo la cadena en
partes utilizando el carácter colon. Una vez que hayas acumulado las
cuentas para cada hora, imprime las cuentas, una por línea, ordenadas
por hora tal como se muestra debajo.
python timeofday.py
Ingresa un nombre de archivo: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
archivo = open('mbox-short.txt')
horas = dict()

for line in archivo:
    renglon = line.split()
    if len(renglon) > 0 and renglon[0] == 'From':
      hora = renglon[5][:2]
      if hora not in horas:
        horas[hora] = 1
      else:
        horas[hora] += 1

lista = list()
for clave, valor in list(horas.items()):
  lista.append((clave, valor))

lista.sort(reverse=False)

for clave, valor in lista:
  print(clave, valor)
'''
Ejercicio 3: Escribe un programa que lee un archivo e imprime las
letras en order decreciente de frecuencia. El programa debe convertir
todas las entradas a minúsculas y contar solamente las letras a-z.
El programa no debe contar espacios, dígitos, signos de puntuación,
o cualquier cosa que no sean las letras a-z. Encuentra ejemplos de
texto en idiomas diferentes, y observa cómo la frecuencia de letras es
diferente en cada idioma. Compara tus resultados con las tablas en
https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras.
'''
import string
manejador_archivo = open('mbox-short.txt')
archivo = manejador_archivo.read().lower()

letras = dict()
alfabeto = list(string.ascii_lowercase)
contador = 0

for linea in archivo:
  if linea in alfabeto and linea[contador] not in letras:
    letras[linea] = 1
  elif linea[contador] in letras:
    letras[linea] += 1

lista = list()
for clave, valor in list(letras.items()):
  lista.append((clave, valor))

lista.sort(reverse=False)

for clave, valor in lista:
  print(clave, valor)