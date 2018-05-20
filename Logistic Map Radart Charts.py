#Le code ci-dessous permet le tracé de toutes courbes et de visualiser la suite un+1 = f(un) sous forme d'un diagramme en toile d'araignée. Il prend trois arguments obligatoires, la fonction sous forme de chaîne de caractères, un terme initial et un coefficient c qui doit aussi se trouver dans la fonction passée en argument. Tous les autres arguments sont optionnels. Les deux premiers définissent la plage sur laquelle f(x) existe, les deux suivants définissent le niveau de zoom sur l'abscisse et l'ordonnée, les deux suivants, les coordonnées de l'abscisse et de l'ordonnée et enfin les deux derniers définissent la taille de la fenêtre. Ce code permet aussi de correctement représenter des fonctions non-continues en certains points du domaine de définition ou avec des domaines de définition plus réduit que celui passé en argument.

from Tkinter import *
from math import *
from decimal import Decimal #pour ne pas avoir des erreurs de floating point

def courbeDiagramme(fonction, u0, c, x1 = -1000, x2 = 1000, zoomx = 40, zoomy = 30, x0 = 375, y0 = 250, W = 750, H = 500) : 
    T = Tk() #Appelle le master widget
    T.title('Courbe de f(x) et diagramme en toile d\'araignée')
    coeffC = 'Decimal('+ "'" + str(c)+ "'" + ')'    #mettre le nombre décimal sous forme de chaîne
    fonction = [x for x in fonction]    #transforme la chaîne en liste
    fonction = [coeffC if x=='c' else x for x in fonction]  #remplace c par la chaîne
    fonction = ''.join(fonction)    #reforme une chaîne
    f = lambda x : eval(fonction) #permet de transformer la chaîne de caractère en fonction
    F = Canvas(T, width=W, height=H, bg='light yellow') #crée le window widget
    F.pack()
    fonctionValide = False #pour savoir s'il faut écrire un message d'erreur
    F.create_line(0, y0, W, y0, fill='black')   #crée axe des abscisses
    F.create_line(x0, 0, x0, H, fill='black')   #crée axe des ordonnées
    x = Decimal(str(x1))    #un float sans les problèmes de float
    xe = x0 + zoomx*x
    yc = y0 - zoomy*x #nécessaire pour la gradation de l'axe des ordonnées
    try : #essaie f(x)
        y = f(x)
        ye = y0 - zoomy*y #coordonnée de y en fonction de l'axe des ordonnées et du facteur de zoom
    except : pass #si c'est pas possible, on continue sans
    compteur = 100   #nécessaire afin de graduer les axes
    while x <= x2 :  #for loop ne permettait pas un pas moins grand que 1
        if compteur == 100 : #graduation des axes
            if int(x) == 0 : #à chaque fois que x est un entier alors on gradue pour ordonnées et abscisses
                F.create_text(x0 - 15, y0 - 15, text=int(x))
            else :
                F.create_line(int(xe), y0 - 5, int(xe), y0 + 5, fill='black')
                F.create_text(int(xe), y0 - 15, text=int(x))
                F.create_line(x0 - 5, int(yc), x0 + 5, int(yc), fill='black')
                F.create_text(x0 - 15, int(yc), text=int(x))
            compteur = 0 #et on remet le compteur à zéro
        x += Decimal('0.01') #pour avoir un pas de 1/10eme
        compteur += 1
        oldxe = xe #ancien repère xe
        xe = x0 + zoomx*x #nouveau repère xe
        yc = y0 - zoomy*x #nouveau repère yc
        try :
            y = f(x) #condition problématique
            fonctionValide = True #la fonction est valide
            if switch is False : #si une fonction n'existait pas sur la valeur précédente (x-1)
                ye = y0 - zoomy*y #On recharge la valeur ye et à la prochaine itération on la mettra dans oldye
                switch = True
            else : 
                oldye = ye #sinon on procède normalement
                ye = y0 - zoomy*y 
                F.create_line(oldxe, oldye, xe, ye, fill='red') #crée une ligne entre oldxe, oldye et xe,ye
        except : 
            switch = False #la fonction n'existe pas pour x
            continue #on recommence avec prochain x
    diagramme_aux (f, u0, x0, y0, x1, x2, zoomx, zoomy, F)
    if fonctionValide is not True : print 'Impossible de traiter la fonction ' + str(fonction) + ', veuillez vous assurer qu\'elle est correcte.'
    T.mainloop()

def diagramme_aux (f, u0, x0, y0, x1, x2, zoomx, zoomy, F) :
    F.create_line(x0 + zoomx*x1, y0 -zoomy*Decimal(str(x1)), x0 + zoomx*Decimal(str(x2)), y0 -zoomy*Decimal(str(x2)), fill='black', width = 2) #crée la bissectrice
    ux1 = Decimal(str(u0)) #pour être certain que la fonction sorte un nombre décimal si nécessaire
    try : uy1 = f(ux1)  #si le nombre fait parti du domaine de définition
    except : 
        print "Le terme initial ne fait pas parti du domaine de définition" #sinon on sort
        return
    F.create_line(x0 + zoomx*ux1, y0, x0 + zoomx*ux1, y0 - zoomy*uy1, fill='blue', width = 2) #crée le premier trait vertical
    for x in xrange(x2) :   #Limite le nombre d'itérations au nombre de la plage positif de x, suffisant pour le tracer, trop pour les polynômes
        ux2 = uy1 #Nouvelles valeurs pour permettre la récursion   
        uy2 = uy1
        F.create_line(x0 + zoomx*ux1, y0 - zoomy*uy1, x0 + zoomx*ux2, y0 - zoomy*uy2, fill='blue', width = 2)  #crée les traits horizontaux
        ux1 = ux2
        uy1 = f(ux2)    #récursion
        F.create_line(x0 + zoomx*ux2, y0 - zoomy*uy2, x0 + zoomx*ux1, y0 - zoomy*uy1, fill='blue', width = 2)  #crée les traits verticaux

        
    

courbeDiagramme('c*x*(1-x)', .3, 2.9, -50, 50, 250, 250, 250, 240, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 2.9, -50, 50, 650, 600, 250, 590, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.3, -50, 50, 250, 250, 250, 240, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.3, -50, 50, 650, 600, 250, 590, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.5, -50, 50, 250, 250, 250, 240, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.5, -50, 50, 650, 600, 250, 590, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.564, -50, 50, 250, 250, 250, 240, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.564, -50, 50, 650, 600, 250, 590, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.84, -50, 50, 250, 250, 250, 240, 1000, 500)

courbeDiagramme('c*x*(1-x)', .3, 3.84, -50, 50, 650, 600, 250, 590, 1000, 500)