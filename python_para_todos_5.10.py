'''
Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.
Introduzca un número: 4
Introduzca un número: 5
Introduzca un número: dato erróneo
Entrada inválida
Introduzca un número: 7
Introduzca un número: fin
16 3 5.33333333333
'''
lista = []
while True:
  try:
    numero = input("Introduce un numero: ")

    if numero == 'fin':
      break
    else:
      lista.append(int(numero))

  except Exception as e:
    print("Entrada invalida")

if len(lista) > 0:
  print(sum(lista), len(lista), sum(lista)/len(lista))
'''
Ejercicio 2: Escribe otro programa que pida una lista de números como
la anterior y al final muestre por pantalla el máximo y mínimo de los
números, en vez de la media.
'''
lista = []
while True:
  try:
    numero = input("Introduce un numero: ")

    if numero == 'fin':
      break
    else:
      lista.append(int(numero))

  except Exception as e:
    print("Entrada invalida")

if len(lista) > 0:
  print(max(lista), min(lista))