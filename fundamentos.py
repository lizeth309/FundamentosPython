#Kennia Lizeth Villegas Ascencio          
#210112303                   09/02/2023

def nuevoTema(tema):
    print("\n=======", tema, "=======\n")

print("===== Operadores aritmeticos =====")
print ("Operador division entera (10 // 3:)", 10//3)
print ("Operador potencia (5 ** 3):",  5 ** 3)

print("===== Operadores logicos =====")
print("Operador and (true and false): ", True and False)
#True y False siempre usa mayusculas 

#Actividad: tabla de verdad de los operadores logicos.

print("=====TABLA DE LA VERDAD=====")
print("AND")
print("True and False: ", True and False)
print("False and False: ", False and True)
print("False and False: ", False and False)
print("True and True: ", True and True)
print("OR")
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)
print("True or True: ", True or True )
print("NOT")
print("True: ", not True)
print("False: ", not False)

#Siempre despues de ("") se pone , 

nuevoTema("Operadores de comparacion")
print("2 == 3", 2 == 3)
print("5 != 3", 5 != 3)
print("4 < 6" , 4 < 6)
print("7 <= 4", 7 <= 4)
print("6 > 3", 6 > 3)
print("8 >= 8", 8 >= 8)

nuevoTema("Variables")
variable1 = 10
variable2 = 6.2456
variable3 = "Juancho"
dosPalablas = "Hola"
dos_palabras = "Hello"

print(variable1, variable2, variable3, dos_palabras, dosPalablas)

a, b, c = 10, 5.16, "palabra"
print(a, b, c)

nuevoTema("Enteros")
w = 111
x = 1234567890
y = -460
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotanes")
x = 1297.50
print(x, type(x))
y = 0.5637
print(y, type(y))

nuevoTema("Numeros complejos")
x = -46j
y = 12 + 45j
z= 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = [8]
print(lis, "es", bool(lis))
t = ()
print(t, "es", bool(t))
new = "hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1 + 0j
print(comp, "es", bool(comp))
val = None
print(val, "es", bool(None))

nuevoTema("Listas") #no son arreglos 
a = [10, 20.5, "python list"]
print(a)
print(a[1])
a[0] = "hola"
print(a)

nuevoTema("Tuplas")
t = (25, "Tupla", 1 + 10j, 3.1416)
print(t)
print(t[2])
print('t[1:5]:', t[1:4])
#t[1] = 34   Operacion no valida en tuplas

nuevoTema("conjuntos")
t = {50, 20, 30, 40, 10, 50}
print("conjunto t= ", t, type(t))

nuevoTema("diccionario")
d = {1:"valor1", "valor2":2j}
print(d, type(d))
print("d[valor2]:", d["valor2"])

nuevoTema("Cadenas")
cadena1 = "cadena con comillas dobles"
cadena2 = 'cadena con comillas simples'
print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea = '''Esta es una cadena
de varias  con  tabulares  y
                saltos
de
linea'''

print(cadenaMultilinea)
print("--segmentacion de cadena--")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.capitalize()
print(cadena5)