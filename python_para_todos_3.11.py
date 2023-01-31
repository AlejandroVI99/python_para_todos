'''
Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0
'''
print ("Introduzca Horas:")
horas = int(input())
print ("Introduzca Tarifa:")
tarifa = float(input())

if horas > 40:
  horas_extra = horas - 40
  salario = 40 * tarifa + (horas_extra * (tarifa * 1.5))
else:
  salario = horas * tarifa

print("Salario: " + str(salario))

'''
Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
del programa:
Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve
Error, por favor introduzca un número
Introduzca las Horas: cuarenta
Error, por favor introduzca un número
'''
try:
  horas = int(input("Introduzca Horas:"))
  tarifa = float(input("Introduzca Tarifa:"))
  if horas > 40:
    horas_extra = horas - 40
    salario = 40 * tarifa + (horas_extra * (tarifa * 1.5))
  else:
    salario = horas * tarifa
  print("Salario: " + str(salario))

except Exception as e:
  print ("Erro, por favor introduce un numero")

'''
Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:
Puntuación Calificación
>= 0.9 Sobresaliente
>= 0.8 Notable
>= 0.7 Bien
>= 0.6 Suficiente
< 0.6 Insuficiente
Introduzca puntuación: 0.95
Sobresaliente
Introduzca puntuación: perfecto
Puntuación incorrecta
Introduzca puntuación: 10.0
Puntuación incorrecta
Introduzca puntuación: 0.75
Bien
Introduzca puntuación: 0.5
Insuficiente
Ejecuta el programa repetidamente, como se muestra arriba, para probar con varios
valores de entrada diferentes.
'''

while True:
  try:
    calificacion = float(input("Introduce una calificacion:"))

    if calificacion >= 0.9 and calificacion <= 1:
      print("Sobresaliente")
    elif calificacion >= 0.8 and calificacion < 0.9:
      print("Notable")
    elif calificacion >= 0.7 and calificacion < 0.8:
      print("Bien")
    elif calificacion >= 0.6 and calificacion < 0.7:
      print("Suficiente")
    elif calificacion < 0.6:
      print("Insuficiente")
    else:
      print("Puntuacion incorrecta")
  except Exception as e:
    print("Puntuacion incorrecta")