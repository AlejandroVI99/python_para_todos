'''
7.11 Ejercicios
Ejercicio 1: Escribe un programa que lea un archivo e imprima su con-
tenido (línea por línea), todo en mayúsculas. Al ejecutar el programa,
debería parecerse a esto:
python shout.py
Ingresa un nombre de archivo: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
Puedes descargar el archivo desde www.py4e.com/code3/mbox-short.txt
'''
manejador_archivo = open('mbox-short.txt')
inp = manejador_archivo.read().upper()
print(inp)

'''
Ejercicio 2: Escribe un programa que solicite un nombre de archivo
y después lea ese archivo buscando las líneas que tengan la siguiente
forma:
X-DSPAM-Confidence: 0.8475
**Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla
aparte para extraer el número decimal de la línea. Cuenta esas líneas y después
calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al
final del archivo, imprime el valor medio de “spam confidence”.
Ingresa un nombre de archivo: mbox.txt
Promedio spam confidence: 0.894128046745
Ingresa un nombre de archivo: mbox-short.txt
Promedio spam confidence: 0.750718518519
Prueba tu programa con los archivos mbox.txt y mbox-short.txt.
'''
nombre_archivo = input('Ingresa un nombre de archivo: ')

archivo = open(nombre_archivo)
contador = 0
promedio = 0
for linea in archivo:
  if linea.startswith('X-DSPAM-Confidence: '):
    dos_puntos = linea.find(':')
    numero = linea[dos_puntos + 1:]
    resultado = float(numero.strip())
    promedio += resultado
    contador += 1

print(promedio/contador)

'''
Ejercicio 3: Algunas veces cuando los programadores se aburren o
quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
a su programa. Modifica el programa que pregunta al usuario por el
nombre de archivo para que imprima un mensaje divertido cuando el
usuario escriba “na na boo boo” como nombre de archivo. El programa
debería funcionar normalmente para cualquier archivo que exista o no
exista. Aquí está un ejemplo de la ejecución del programa:

python huevo.py
Ingresa un nombre de archivo: mbox.txt
Hay 1797 líneas subject en mbox.txt
python huevo.py
Ingresa un nombre de archivo: inexistente.tyxt
El archivo no puede ser abierto: inexistente.tyxt
python huevo.py
Ingresa un nombre de archivo: na na boo boo
NA NA BOO BOO PARA TI - Te he atrapado!
No te estamos aconsejando poner Huevos de Pascua en tus programas;
es sólo un ejercicio.
'''
try:
  nombre_archivo = input("Ingresa un nombre de archivo: ")
  if nombre_archivo == "na na boo boo":
    print("NA NA BOO BOO PARA TI - Te he atrapado!")
    exit()

  archivo = open(nombre_archivo)
  contador = 0
  promedio = 0

  for linea in archivo:
    if linea.startswith('X-DSPAM-Confidence: '):
      dos_puntos = linea.find(':')
      numero = linea[dos_puntos + 1:]
      resultado = float(numero.strip())
      promedio += resultado
      contador += 1

  print(promedio/contador)
except Exception as e:
  print("No existe el archivo")