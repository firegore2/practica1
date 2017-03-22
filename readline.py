# -*- coding=utf-8 -*-
import time
fname = 'niveles.txt'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
lvls= int(content[0])
lvl_actual = 0
linea_actual = 1
ncoches = 0
lista_coches=[[] for i in range(lvls)]
#print type(lvls), lvls," tamaño: ",len(content),
#for i in range(len(content)):
#    print("content[",i,"]",content[i],"\n",)
#    time.sleep(2)
while lvl_actual < lvls:
    ncoches = int(content[linea_actual])
    ncoches_actual = 0
    print("content[",linea_actual,"], numero de coches: ",ncoches," nivel: ",lvl_actual,"\n",)
    linea_actual+=1
    while   ncoches_actual < ncoches:
        print("-coche numero ",ncoches_actual,"[",content[linea_actual],"]","\n",)
        lista_coches[lvl_actual].append(content[linea_actual])
        linea_actual+=1
        ncoches_actual+=1
    lvl_actual+=1
print('\n',lista_coches)
    