'''
Ejercicio 4: Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
Escribir un programa para abrir el archivo romeo.txt y leerlo línea
por línea. Para cada línea, dividir la línea en una lista de palabras
utilizando la función split. Para cada palabra, revisar si la palabra ya
se encuentra previamente en la lista. Si la palabra no está en la lista,
agregarla a la lista. Cuando el programa termine, ordenar e imprimir
las palabras resultantes en orden alfabético.
Ingresar nombre de archivo: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
'''
nombre_archivo = input('Ingresa un nombre de archivo: ')

archivo = open(nombre_archivo)
lista = []

for linea in nombre_archivo:
  linea = linea.split()
  lista.append(linea)

lista_de_palabras = sum(lista,[])
lista_de_palabras_unicas = list(set(lista_de_palabras))
print(sorted(lista_de_palabras_unicas))

'''
Ejercicio 5: Escribir un programa para leer a través de datos de una ban-
deja de entrada de correo y cuando encuentres una línea que comience
con “From”, dividir la línea en palabras utilizando la función split.
Estamos interesados en quién envió el mensaje, lo cual es la segunda
palabra en las líneas que comienzan con From.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Tendrás que analizar la línea From e imprimir la segunda palabra de
cada línea From, después tendrás que contar el número de líneas From
(no incluir From:) e imprimir el total al final. Este es un buen ejemplo
de salida con algunas líneas de salida removidas:
python fromcuenta.py
Ingresa un nombre de archivo: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
[...líneas de salida removidas...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
Hay 27 lineas en el archivo con la palabra From al inicio
'''
archivo = open('mbox-short.txt')
contador = 0
for line in archivo:
    renglon = line.split()
    if len(renglon) > 0 and renglon[0] == 'From':
      print(renglon[1])
      contador += 1
print('hay %d lineas en el archivo con la palabra From al inicio' % contador)

'''
Ejercicio 6: Reescribe el programa que pide al usuario una lista de
números e imprime el máximo y el mínimo de los números al final cuando
el usuario ingresa “hecho”. Escribe el programa para almacenar los
números que el usuario ingrese en una lista, y utiliza las funciones max()
y min() para calcular el máximo y el mínimo después de que el bucle
termine.

Ingresa un número: 6
Ingresa un número: 2
Ingresa un número: 9
Ingresa un número: 3
Ingresa un número: 5
Ingresa un número: hecho
Máximo: 9.0
Minimo: 2.0
'''
lista = []
while True:
  try:
    numero = input("Introduce un numero: ")
    if numero == 'hecho':
      break
    else:
      lista.append(int(numero))

  except Exception as e:
    print("Entrada invalida")

if len(lista) > 0:
  print("Maximo " + str(max(lista)))
  print("Minimo " + str(min(lista)))