'''
Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo
dependiendo del día de la semana en que se recibió. Para hacer esto
busca las líneas que comienzan con “From”, después busca por la tercer
palabra y mantén un contador para cada uno de los días de la semana.
Al final del programa imprime los contenidos de tu diccionario (el orden
no importa).
Línea de ejemplo:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Ejemplo de ejecución:
python dow.py
Ingresa un nombre de archivo: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''
archivo = open('mbox-short.txt')
dias = dict()

for line in archivo:
    renglon = line.split()
    if len(renglon) > 0 and renglon[0] == 'From':
      if renglon[2] not in dias:
        dias[renglon[2]] = 1
      else:
        dias[renglon[2]] += 1

print(dias)
'''
Ejercicio 3: Escribe un programa para leer a través de un historial de
correos, construye un histograma utilizando un diccionario para contar
cuántos mensajes han llegado de cada dirección de correo electrónico, e
imprime el diccionario.
Ingresa un nombre de archivo: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
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

print(correos)
'''
Ejercicio 4: Agrega código al programa anterior para determinar quién
tiene la mayoría de mensajes en el archivo. Después de que todos los
datos hayan sido leídos y el diccionario haya sido creado, mira a través
del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máx-
imos y mínimos) para encontrar quién tiene la mayoría de mensajes e
imprimir cuántos mensajes tiene esa persona.
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

max_correos = max(correos, key = correos.get)

print(max_correos, correos[max_correos])
'''
Ejercicio 5: Este programa almacena el nombre del dominio (en vez de
la dirección) desde donde fue enviado el mensaje en vez de quién envió
el mensaje (es decir, la dirección de correo electrónica completa). Al
final del programa, imprime el contenido de tu diccionario.
python schoolcount.py
Ingresa un nombre de archivo: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''
archivo = open('mbox-short.txt')
dominios = dict()

for line in archivo:
    renglon = line.split()
    if len(renglon) > 0 and renglon[0] == 'From':
      arroba = renglon[1].find('@')
      dominio = renglon[1][arroba + 1:]
      if dominio not in dominios:
        dominios[dominio] = 1
      else:
        dominios[dominio] += 1

print(dominios)