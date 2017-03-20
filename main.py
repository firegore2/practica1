# -*- coding=utf-8 -*-

#Muestra el numero de niveles (escribe la primera linea del archivo, el numero 20)
archivo = open('niveles.txt', 'r')
linea1 = archivo.readline(2)
print "existen", linea1, "niveles, seleccione uno:"

print type(linea1)
#seleccion de nivel 
nivelElegido = input()
print "usted ha elegido el nivel", nivelElegido, ", comienza el juego:" 

#cierra el archivo
archivo.close()