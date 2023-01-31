#4.14 Ejercicios

'''
Ejercicio 4: ¿Cuál es la utilidad de la palabra clave “def” en Python?
b) Indica el comienzo de una función
'''

'''
Ejercicio 5: ¿Qué mostrará en pantalla el siguiente programa Python?
def fred():
print("Zap")
def jane():
print("ABC")
jane()
fred()
jane()

d) ABC Zap ABC
'''

'''
Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-y-
media para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa).
Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0
'''
def calculo_salario(horas, tarifa):
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
  print ("Error, por favor introduce un numero")

horas = int(input("Introduzca Horas:"))
tarifa = float(input("Introduzca Tarifa:"))

calculo_salario(horas, tarifa)

'''
Ejercicio 7: Reescribe el programa de calificaciones del capítulo ante-
rior usando una función llamada calcula_calificacion, que reciba una
puntuación como parámetro y devuelva una calificación como cadena.
Puntuación Calificación
> 0.9 Sobresaliente
> 0.8 Notable
> 0.7 Bien
> 0.6 Suficiente
<= 0.6 Insuficiente
'''
def calcula_calificacion(calificacion):
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

try:
  calificacion = float(input("Introduce una calificacion:"))
  calcula_calificacion(calificacion)
except Exception as e:
  print("Puntuacion incorrecta")