#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys

def main():
    sensor_call = os.popen("sensors")
    texto = ""
    # conservo la línea que tiene la temperatura
    linea = sensor_call.readlines()[2]
    linea = linea.replace(" ", "")
    pos_inicial = linea.find("+") + 1
    pos_final = linea.find("\xc2")
    sys.stdout.write(unicode(str(int(float(linea[pos_inicial:pos_final]))),encoding='utf-8'))
    sys.stdout.flush()

    # encuentro donde comienza el valor de la temp.
    # pos_inicial = texto.find("+")
    # pos_final = texto.find("º")
    # texto = texto[pos_inicial:pos_final]
    # print texto


if __name__ == '__main__':
    main()
