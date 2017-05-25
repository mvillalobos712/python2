#descripcion:ejecutar un programa que le pregunte al usuario si el numero es par o impar
#entrada: ingresar numero par o impar n = int(input("ingrese un numero /n:"))
#salida: numero par o impar con str 
#autor: mvillalobos712
#fecha: 25-05-2017
#version: 1.0
#plataforma: v2.1 python
n = int(input("ingrese un numero /n:"))
if (n%2 == 0):
 print(str(n)+"par")
else:
 impresion(str(n)+"impar")
