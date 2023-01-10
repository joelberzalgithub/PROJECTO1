# Programa principal
from Paquetes import datos as d
from Paquetes import funciones as f
import os

flg_0 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
flg_06 = False
flg_end = False

while not flg_end:
    while flg_0:
        opt = f.menu(d.menu_principal, d.menu_principal_opt)
        if opt == '1':
            flg_0 = False
            flg_01 = True
        if opt == '2':
            flg_0 = False
            flg_02 = True
        if opt == '3':
            flg_0 = False
        if opt == '4':
            flg_0 = False
        if opt == '5':
            flg_0 = False
        if opt == '6':
            flg_0 = False
            flg_end = True
    while flg_01:
        opt = f.menu(d.menu_01, d.menu_01_opt)
    while flg_02:
        opt = f.menu(d.menu_02, d.menu_01_opt)



