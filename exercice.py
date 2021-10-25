#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle
#import sys
#sys.path.append("../c03-ch6-1-exercices-GabSawka")
#from c03-ch6-1-exercices-GabSawka.exercice import frequence
#d.classes.Session1-A2021.INF1007.INF1007_cours.
#import exercice
from exercice1 import frequence

# TODO: Définissez vos fonction ici
def massevolumiqueelipsoide(a,b,c,M):
    vol=4/3*pi*a*b*c
    return(vol, M*vol)

def get_most_use_letter(phrase :str):
    dict_arg = frequence(phrase)
    print(dict_arg)
    return list(dict_arg.keys())[0]

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(massevolumiqueelipsoide(1,2,3,5))
    print(get_most_use_letter("aaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbb eeee"))
