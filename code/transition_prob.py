import numpy as np


#############################################################################################
#  propTransSec: Probabilités de transition avec le dé sécurité                             #
#############################################################################################


def propTranSec(): 
    '''
       Calcule les probabilités de transitions d'un état s à un état s'
       pour le dé sécurité uniquement

       pré : elle n'a aucun argument

       post: retoune un tableau de type numpy.ndarray de dimension 15*15 dont les
             valeur sont réelles qui représentent les probabilités de transitions de s
             à s'. NB: la lecture du résultat se fait suivant les lignes
    '''
    transition= np.zeros((15,15))
    for i in range(15):
     if i not in [2,9,13,14]:
        for j in range(i,i+2):
            transition[i,j]=0.5
     else:
        if i==2:
            transition[i,i]=1/2
            transition[i,i+1]=1/4
            transition[i,i+8]=1/4
        if i==9:
            transition[i,i]=0.5
            transition[i,i+5]=0.5
        if i==13:
            transition[i,i]=0.5
            transition[i,i+1]=0.5
        if i==14:
            transition[i,i]=1

    return transition

#############################################################################################
#  propTransNo: Probabilités de transition avec le dé normal                                #
#############################################################################################


def propTransNo(circle): # probabilité de transition avec le dé normal
    '''
       Calcule les probabilités de transitions de chaque état s aux états éventuelles s' qui
       peuvent etre accessible lorsqu'on utilise uniquement le dé normal et qu'il n'existe
       aucun piège sur les cases

       pré : circle est un booléen ( True or False)

       post: retoune un tableau de type numpy.ndarray de dimension 15*15 dont les
             valeur sont réelles qui représentent les probabilités de transitions de s
             à s'. NB: la lecture du résultat se fait suivant les lignes
    '''


    transition= np.zeros((15,15)) # on crée un tableau 15*15 rempli de zéros
    for i in range(15):
     if i not in [2,8,9,13,14]: # ces points sont des points particulier à traiter séparément
        for j in range(i,i+3):
            transition[i,j]=1/3
     else:
        if i==2:
            transition[i,i]=1/3
            transition[i,i+1]=1/6
            transition[i,i+2]=1/6
            transition[i,i+9]=1/6
            transition[i,i+8]=1/6
        if i==8:
            transition[i,i]=1/3
            transition[i,i+1]=1/3
            transition[i,i+6]=1/3

        if i==9:                     # la différence entre circle=False et
                                     #se trouve unique quand on se
                                      #trouve sur les cases 10 et 14
            if circle==False:
                transition[i,i]=1/3
                transition[i,i+5]=2/3
            else:
                transition[i,i]=1/3
                transition[i,i+5]=1/3
                transition[i,0]=1/3

        if i==13:
            if circle==False:
                transition[i,i]=1/3
                transition[i,i+1]=2/3
            else:
                transition[i,i]=1/3
                transition[i,i+1]=1/3
                transition[i,0]=1/3

        if i==14:
            transition[i,i]=1
    
    return transition


#############################################################################################
#  propTransNoAct: Probabilités de transition avec le dé normal actualisées                 #
#############################################################################################

def propTransNoAct(layout,circle): # probabilité de transitionc avec le
                                   # dé normal  avec pieges
    '''
       Calcule les probabilités de transitions de chaque état s aux états éventuelles s' qui
       peuvent etre accessible lorsqu'on utilise uniquement le dé normal

       pré :
           layout: vecteur de type numpy.ndarray de longueurs 15 
           circle : booléen ( True or False)


       post: retoune un tableau de type numpy.ndarray de dimension 15*15 dont les
             valeur sont réelles qui représentent les probabilités de transitions de s
             à s'. NB: la lecture du résultat se fait suivant les lignes
    '''


    update=propTransNo(circle) # on récupère le résultat de la situation sans piège
                                # qu'on va mettre à jour suivant les pièges
    index=layout.nonzero() # nous renvoie un tuple dont le premier élément est
                            #un vecteur numpy.array dont les
                            # éléments sont les index des cases non nuls de layout (ie où on a des pièges)
    k=index[0].tolist() # on convertit en une liste
    for i in range(15): # on va parcourrir chaque case et traiter suivant la situation
                        # l'idée fondamentale est de se servir du fait que quand on est sur une case il faut à la fois
                        #traiter ce qui peut se produire si on a ou pas un piège sur la dite case et par la meme
                        #occasion regarder les pièges qui se trouve sur les deux cases qui la suivent
                        # et à chaque fois faire attention au case qui peuvent poser problème tels que les cases 3,10,11,12 et 13

        if i in k or (layout[i]==0 and i!=14):


            if i==2:   # on part de la case 3 en passant par le chemin rapide
                 if i==2 and 10 in k: # on traite le cas i=2 ie partant de la cas 3 et passant par les case 11 (alors le résultat du dé est 1)
                    if layout[10]==1:
                        update[i,10]=0
                        update[i,0]= update[i,0]+1/6
                    elif layout[10]==2:
                        update[i,10]=0
                        update[i,0]= update[i,0]+1/6
                    elif layout[10]==4: #layout[i]==4: piège aléatoire
                        update[i,10]=1/18
                        update[i,0]=update[i,0]+2/18 # rentrer de 3 case + rentré à la case départ
                 if i==2 and 11:      # on traite le cas i=2 ie partant de la cas 3 et passant par les case 11 (alors le résultat du dé est 2)
                     if layout[11]==1:
                        update[i,11]=0
                        update[i,0]= update[i,0]+1/6
                     elif layout[11]==2: # rentrer de 3 cases
                        update[i,11]=0
                        update[i,1]=update[i,1]+ 1/6 
                     elif layout[11]==4: #layout[i]==4: piège aléatoire
                        update[i,11]=1/18 # prison dans la case 12
                        update[i,1]=update[i,1] + 1/18 # rentrer de 3 case 
                        update[i,0]=update[i,0]+1/18 # rentré à la case départ


            if layout[i]==3 or layout[i]==0:
                 pass                 # ici on ne met pas à jour car le  piège 3 se comporte comme si on avait pas de piège
            elif layout[i]==1:
                 update[i,i]=0
                 update[i,0]=update[i,0]+1/3

            elif layout[i]==2:
                 update[i,i]=0

                 if i-3<=0:  # on peut inclure le cas de la case 11 ( qui correspond à i=10) car en rentrant de 3 case on tombe à la
                              # prmière case
                    update[i,0]= update[i,0]+1/3

                 elif i==11 or i==12 or i==10:
                    update[i,i-10]=1/3 # on fait i-10 pour pouvoir traiter les 3 cas ensembles
                 else:
                    update[i,i-3]=1/3

            else:               #layout[i]==4: piège aléatoire
                update[i,i]=1/9 # prison


                if i-3 <= 0:   # rentrer de 3 cases ( on peut inclure la case 10)
                    update[i,0]=update[i,0]+ 1/9

                elif i==11 or i==12 or i==10:
                    update[i,i-10]=1/9 # rentrer de 3 cases :on fait i-10 pour pouvoir traiter les 2 cas ensembles
                else:
                    update[i,i-3]=1/9 # rentrer de 3 cases
                update[i,0]= update[i,0]+1/9 # traite rentré à la case départ et c'est valable pour toute les cases

#on vient de finir de traiter la position où l'agent se trouve
# maintenant on commence à traiter le cas où il y'a un piège éventuelle sur la case suivante (d'index i+1), comme si on jouait 1
# en quelque sorte on recommence ce qui a été fait précédement en tenant compte de ce qui peut se produire

            if i==9: # ici on est à la case 10 qui est un cas limite, donc la seul issu en jouant 1 c'est d'atterir sur la case 15
                pass # ici on veut gerer le cas particulier de la case 10, car en obtenant 1 avec le dé normal on avance
                     # d'une case et on tombe à la case 15 (et non à 11)

            else:
                if i+1 in k: # ici on traite ensemble les autres cases d'attérissage (lorsqu'on obtient 1)

                    if layout[i+1]==3:
                         pass       # ici on ne met pas à jour car ce piège se comporte coe si on avait zéro


                    elif layout[i+1]==1:
                        update[i,i+1]=0 # on met à jour vu qu'on ne peut pas rester sur cette case
                        if i+1==3: # on traite le cas i=2 ie partant de la cas 3 donc se retrouver à la case 4 
                            update[i,0]= update[i,0]+1/6 # ce que l'on fait si on  joue  à partir de la case 3

                        else:
                            update[i,0]=update[i,0]+1/3 # ce que l'on fait si on ne joue pas à partir de la case 3

                    elif layout[i+1]==2:
                        update[i,i+1]=0 # on met à jour vu qu'on ne peut pas rester sur cette case
                        if i+1-3 < 0 :    # cette condition veut dire qu'on ne peut pas etre quitté de 3 et donc les probas sont 1/3
                            update[i,0]= update[i,0]+1/3
                        elif i+1==3: # on traite le cas i=2 ie partant de la case 3 donc se retrouver à la case 4 sachant qu'on a le piège 2 sur la case 4
                            update[i,0]= update[i,0]+1/6 # i+1-3=0 , donc on repart à la case départ


                        elif i+1==11 or i+1==12: 
                            update[i, i+1-10]=1/3
                        else:
                            update[i,i+1-3]=1/3
                    else:          # layout[i+1]==4: piège aléatoire
                        update[i,i+1]=1/9   # prison : tous le monde subit ceci avec proba 1/9 sauf les cases 4,5,11 et 12 où les probas valent 1/18
                        update[i,0]=update[i,0]+1/9 # proba de rentrer à la case depart de manière aléatoire , aussi lorsque i=2, alors à i+1=3 (case4) on a le piege 4

                        if i+1-3<0:
                            update[i,0]= update[i,0]+1/9 # proba de rentrer de 3 case lorsque on est avant la case 3

                        elif i+1==3: # seulement possible lorsque on a un piège sur la case 3

                            update[i,i+1]=1/18  # ici on ecrase la valeur  update[i,i+1]=1/9 par défaut du piège prison
                            update[i,0]=update[i,0]+ 2/18 -1/9 # le moins 1/9 permet d'annuler le 1/9 de rentrer de 3 cases du cas par défaut des autres cases
                                                               # et la proba de rentrer à la case départ ou rentrer de 3 case est 1/18+1/18=2/18ce
                                                               #qui nous ramène à la case départ

                        elif i+1==11 or i+1==12: # il faut etre quité de la case 11 (pour vouloir atterrir à 12) ou 12 ((pour vouloir atterrir à 13)
                            update[i,i+1-10]=1/9 # rentrer de 3 cases
                        else:
                            update[i,i+1-3]=1/9

# on reprend le meme principe, maintenat on fait comme si le résultat du dé était 2

                if i+2 in k:
                   if i+2==10: # ie i=8,  donc on part de la case 9 et on avance de 2 pour tomber directement à la case 15
                      pass     # d'où on ne modifie rien
                   else:
                    if layout[i+2]==3:
                         pass  # ici on ne met pas à jour car ce piège se comporte coe si on avait zéro

                    elif layout[i+2]==1:
                        update[i,i+2]=0 # on met à jour vu qu'on ne peut pas rester sur cette case
                        if i+2==4:    # on traite le cas i=2 ie partant de la cas 3 et en obtenant 2 du dé
                            update[i,0]= update[i,0]+1/6  # rentrer à la case départ si on ne peut pas attérir sur la case 5 vu le piège 1 qui s'y trouve

                        else:
                            update[i,0]= update[i,0]+1/3 # comportement par défaut pour le reste

                    elif layout[i+2]==2: # rentrer de 3 cases
                        update[i,i+2]=0 # on met à jour vu qu'on ne peut pas rester sur cette case

                        if i+2-3<=0:
                            update[i,0]=update[i,0]+1/3
                        elif i+2==4:     # on traite le cas i=2 ie partant de la cas 3 on se retrouver à la case 5 puis on retourne de 3 cases
                            update[i,i+2-3]= update[i,i+2-3]+1/6 # rentrer de 3 cases
                                                           

                        elif i+2==12:
                            update[i,i+2-10]=1/3
                        else:
                            update[i,i+2-3]=1/3
                    else:                # layout[i+2]==4: piege aléatoire
                        update[i,i+2]=1/9 # prison : tous le monde subit ceci avec proba 1/9 sauf les cases 4,5,11 et 12 où les probas valent 1/18
                        update[i,0]= update[i,0]+1/9 # proba de rentrer à la case depart de manière aléatoire , aussi lorsque i=2, alors à i+1=3 (case4) on a le piege 4
                        if i+2-3<=0:
                            update[i,0]=update[i,0]+1/9 # rentrer de 3 case
                        elif i+2==4: # seulement possible lorsque est sur la case 3

                            update[i,i+2]=1/18  # ici on ecrase la valeur  update[i,i+1]=1/9 par défaut
                            update[i,i+2-3]=update[i,i+2-3]+1/18 # rentrer de 3 cases 
                            update[i,0]=update[i,0]+1/18 -1/9 # retour case départ en annulant le -1/9 par défaut des autres cas

                        elif i+2==12:
                            update[i,i+2-10]=1/9
                        else:
                            update[i,i+2-3]=1/9


    return update



