
# -*- coding=utf-8 -*-

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
print(CES, COES, COE *4, COES, COE*4, COES, COE *4, COES, COE*4, COES, COE *4, COES, COE*4, CSO, sep="")
print(CNES, " "* 30, CONS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNES, " "* 30, CONS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNES, " "* 30, CSOM, sep="")
print(CNS,  " "* 30, CSOM, sep="")
print(CNS,  " "* 30, CSOM, sep="")
print(CNES, " "* 30, CONS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNES, " "* 30, CONS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNES, " "* 30, CONS, sep="")
print(CNS,  " "* 30, CNS, sep="")
print(CNE, CONE, COE *4, CONE, COE*4, CONE, COE *4, CONE, COE*4, CONE, COE *4, CONE, COE*4, CON, sep="")