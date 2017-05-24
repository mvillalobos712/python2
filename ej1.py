# Descripcion: Este programa permite saber el ano en el cual la persona cumple cien anos
# Entrada: Nombre y edad del usuario
# Salida:  Ano en el cual la persona cumple cien anos
# Autor:   MARIANELA VILLALLOBOS
# Fecha:  24.05.2017
# Version: 1.0
#Plataforma: Python v2.7
nombre = raw_input("por favor escriba su nombre: ")
edad = int(input("por favor escriba su edad: "))
ano = ((2017 - edad) + 100)
print("Hola, " + nombre + "en el ano " + str(ano) + "cumple cien anos")
