# -*- coding=utf-8 -*-
from machine import Machine
#Piezas del tablero

COE=u'\u2500' # -
CNS=u'\u2502' # │
CES=u'\u250C' # ┌
CSO=u'\u2510' # ┐
CNE=u'\u2514' # └
CON=u'\u2518' # ┘
COES=u'\u252C' # ┬
CNES=u'\u251C' # ├
CONS=u'\u2524' # ┤
CONE=u'\u2534' # ┴
CSOM=u'\u2593' # ▒

#Parking vacío (print linea a linea)

#print(CNES, " "* 30, CONS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNES, " "* 30, CONS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNES, " "* 30, CSOM, sep="")
#print(CNS,  " "* 30, CSOM, sep="")
#print(CNS,  " "* 30, CSOM, sep="")
#print(CNES, " "* 30, CONS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNES, " "* 30, CONS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNS,  " "* 30, CNS, sep="")
#print(CNES, " "* 30, CONS, sep="")
#print(CNS,  " "* 30, CNS, sep="")


matriz = [[000 for x in range(8)] for y in range(8)]

#Primera fila del parking dentro de una matriz
matriz [0][0] = CES + COES + COE *2
matriz [0][1] = COE*2 + COES + COE
matriz [0][2] = COE*3 + COES
matriz [0][3] = COE*4
matriz [0][4] = COES + COE*3
matriz [0][5] = COE + COES + COE*2
matriz [0][6] = COE*2 + COES + COE
matriz [0][7] = COE*3 + CSO
    
#Segunda fila del parking dentro de una matriz
matriz [1][0] = CNES
matriz [1][7] = CONS

#Tercera fila del parking dentro de una matriz
matriz [2][0] = CNES
matriz [2][7] = CONS

#Cuarta fila del parking dentro de una matriz
matriz [3][0] = CNES
matriz [3][7] = CSOM

#Quinta fila del parking dentro de una matriz
matriz [4][0] = CNES
matriz [4][7] = CONS

#Sexta fila del parking dentro de una matriz
matriz [5][0] = CNES
matriz [5][7] = CONS

#Septima fila del parking dentro de una matriz
matriz [6][0] = CNS
matriz [6][7] = CNS

#Octava fila del parking dentro de una matriz
matriz [7][0] = CNE + CONE + COE *2
matriz [7][1] = COE*2 + CONE + COE
matriz [7][2] = COE*3 + CONE
matriz [7][3] = COE*4
matriz [7][4] = CONE + COE*3
matriz [7][5] = COE + CONE + COE*2
matriz [7][6] = COE*2 + CONE + COE
matriz [7][7] = COE*3 + CON


for i in range(len(matriz)): 
    print (matriz[i])


maquina=Machine()
maquina.start("pene.txt")