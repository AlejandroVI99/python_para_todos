'''
Ejercicio 2: Escribe un programa que use input para pedirle al usuario
su nombre y luego darle la bienvenida.
Introduzca tu nombre: Chuck
Hola, Chuck
'''
print ("Introduzca tu nombre:")
nombre = input()

print("Hola " + nombre)

'''
Ejercicio 3: Escribe un programa para pedirle al usuario el número de
horas y la tarifa por hora para calcular el salario bruto.
Introduzca Horas: 35
Introduzca Tarifa: 2.75
Salario: 96.25
Por ahora no es necesario preocuparse de que nuestro salario tenga exactamente
dos dígitos después del punto decimal. Si quieres, puedes probar la función interna
de Python round para redondear de forma adecuada el salario resultante a dos
dígitos decimales.
'''
print ("Introduzca Horas:")
horas = int(input())
print ("Introduzca Tarifa:")
tarifa = float(input())

salario = horas * tarifa

print("Salario: " + str(salario))

'''
Ejercicio 4: Asume que ejecutamos las siguientes sentencias de asig-
nación:
ancho = 17
alto = 12.0
Para cada una de las expresiones siguientes, escribe el valor de la expresión y el
tipo (del valor de la expresión).
1. ancho/2
2. ancho/2.0
3. alto/3
4. 1 + 2 * 5
Usa el intérprete de Python para comprobar tus respuestas.

  1. ancho/2 float
  2. ancho/2.0 float
  3. alto/3 float 
  4. 1 + 2 * 5 int
'''

'''
Ejercicio 5: Escribe un programa que le pida al usuario una temper-
atura en grados Celsius, la convierta a grados Fahrenheit e imprima
por pantalla la temperatura convertida.
'''
print ("Introduzca la temperatura en Celsius:")
temperatura_c = int(input())
temperatura_f = (temperatura_c * 1.8) + 32

print ("La temperatura en Fahrenheit es:" + str(temperatura_f))