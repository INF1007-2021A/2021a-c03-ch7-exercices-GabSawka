#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle
from typing import Sequence
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

def draw(thick,orientation=90):
    turtle.pendown()
    turtle.width(thick*5)
    turtle.color(0,1,0)
    turtle.setheading(orientation)
    turtle.forward(20*thick)
    posi=turtle.pos()
    for i in range(2):
        turtle.penup()
        turtle.setpos(posi[0],posi[1])
        head=orientation+30*(-1)**i
        if thick !=0:
            draw(thick-1,head)

def saisie():
    c_not_valid=True
    while(c_not_valid):
        chaine=str(input("chaine adn: "))
        c_not_valid=(not valide(chaine))
    return chaine
        
def valide(chaine):
    car_valide=['a','c','t','g']
    if(len(chaine)==0):
        return False
    for letter in chaine:
        if letter not in car_valide:
            return False
    return True  

def proportion(chaine, seq):
    nb_tot=len(chaine)-len(seq)+1
    nb_pres=0
    
    for l in range(len(chaine)-len(seq)+1):
        l_precedant = seq[0]==chaine[l]
        for s in range(0,len(seq)):
            if seq[s]!=chaine[l+s] and l_precedant:
                l_precedant=False 
        if l_precedant:
            nb_pres+=1
    print(nb_tot)
    print(nb_pres)
    return nb_pres/nb_tot

def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(massevolumiqueelipsoide(1,2,3,5))
    #print(get_most_use_letter("aaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbb eeee"))
    #draw(4)
    #chaine = saisie()
    #sequence = saisie()
    #ratio=proportion(chaine,sequence)
    #print(chaine)
    #print(sequence)
    #print(ratio)
    print(facto(4))


