'''
Ejercicio uno: escribe un programa simple que simule la operación del
comando grep en Unix. Debe pedir al usuario que ingrese una expresión
regular y cuente el número de líneas que coincidan con ésta:
$ python grep.py
Ingresa una expresión regular: ^Author
mbox.txt tiene 1798 líneas que coinciden con ^Author
$ python grep.py
Ingresa una expresión regular: ^X-
mbox.txt tiene 14368 líneas que coinciden con ^X-
$ python grep.py
Ingresa una expresión regular: java$
mbox.txt tiene 4175 líneas que coinciden con java$
'''
import re
archivo = open('mbox.txt')
contador = 0

for linea in archivo:
  linea = linea.rstrip()
  if re.search('^Author', linea):
    contador +=1 

print("tiene %d líneas que coinciden con" %contador)
'''
Ejercicio 2: escribe un programa que busque líneas en la forma:
New Revision: 39772
Extrae el número de cada línea usando una expresión regular y el
método findall(). Registra el promedio de esos números e imprímelo.
Ingresa nombre de archivo: mbox.txt
38444.0323119
Ingresa nombre de archivo: mbox-short.txt
39756.9259259
'''
import re
archivo = open('mbox-short.txt')

contador = 0
suma = 0

for linea in archivo:
  linea = linea.rstrip()
  x = re.findall(r'^New Revision\S*: ([0-9.]+)', linea)
  if len(x) > 0:
    suma+=(float(x[0]))
    contador+=1

print(suma/contador)