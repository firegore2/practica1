# -*- coding=utf-8 -*-
import time
fname = 'niveles.txt'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
lvls= int(content[0])
#print type(lvls), lvls," tamaño: ",len(content),
for i in range(len(content)):
    print "content[",i,"]",content[i],"\n",
    time.sleep(2)