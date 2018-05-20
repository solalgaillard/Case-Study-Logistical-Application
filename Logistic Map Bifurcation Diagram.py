#Le code ci-dessous permet de visualiser le diagramme de bifurcation. Il ne prend aucun argument obligatoire. Tous les autres arguments sont optionnels. Ils permettent de décider de la marge entre le bord de la fenêtre et les axes ainsi que la taille de la fenêtre.

from Tkinter import *
from math import *
from decimal import Decimal #pour ne pas avoir des erreurs de floating point

def AppLog(x0 = 20, y0 = 20, W = 900, H = 600) : 
    T = Tk() #Appelle le master widget
    T.title('Application Logistique')
    F = Canvas(T, width=W, height=H, bg='light yellow') #crée le window widget
    F.pack()
    zoomx = (W- 2*x0)/Decimal('1.2') #garde le ratio pour qu'il soit toujours bon même en changeant la taille de la fenêtre
    zoomy = H - y0*2
    F.create_line(x0, y0, W-x0, y0, fill='Slate Blue', width = 3)   #crée axe des abscisses-haut
    F.create_text(x0 - 10, y0 + 5, text='1', fill='Slate Blue')   #repère 1
    F.create_line(x0, H - y0,  W-x0, H - y0, fill='Slate Blue', width = 3)   #crée axe des abscisses-bas
    F.create_text(x0 - 10, H - y0 - 5, text='0', fill='Slate Blue')   #repère 0
    F.create_line(x0, y0, x0, H - y0, fill='Slate Blue', width = 3)   #crée axe des ordonnées-gauche
    F.create_text(x0 + 10, H - 10, text='2.8', fill='Slate Blue')   #repère 2.8
    F.create_line(W - x0, y0, W - x0, H - y0, fill='Slate Blue', width = 3)   #crée axe des ordonnées-droite
    F.create_text(W - x0 - 5, H - 10, text='4', fill='Slate Blue')   #repère 4
    u0 = Decimal('0.3')   #terme initial
    c = Decimal('2.8')  #c initial
    while c <= Decimal('4') :
        yRec = (c*u0*(1-u0))    #terme un initial
        for i in range(2000) :
            x = x0 + zoomx*(c - Decimal('2.8')) #placement de c sur l'abscisse
            yRec = c*yRec*(1-yRec)  #terme récursif
            y = H - y0 - zoomy*yRec #placement de un sur l'ordonnée
            if i >= 1500 : F.create_rectangle(x, y, x, y, outline='red') #création du point après les 1500 premières itérations
        c += Decimal('0.005')    #itération
    T.mainloop()


AppLog() 
    
