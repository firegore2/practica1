# -*- coding=utf-8 -*-
import  random, csv, operator
def readFile(fn):
    with open(fn) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def isEmptyFile(fn):
    if len(readFile(fn))==0:
        print("fichero vacio")
        return True
    else:
        print("fichero no vacio")
        return False


def readCSVint(csvf):
    e=[]
    with open(csvf) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            #print(reg)  # Cada línea se muestra como una lista de campos
            reg =list(map(int,reg))
            e.append(reg)
    return e

