import numpy as np

#############################################################################################
#  propTransSec: Probabilités de transition avec le dé sécurité                             #
#############################################################################################


def propTranSec(): # Noter que cette fonction est indépendante de circle et layout
    '''
       Calcule les probabilités de transitions d'un état s à un état s'
       pour le dé sécurité uniquement

       pré : elle n'a aucun argument

       post: retoune un tableau de type numpy.ndarray de dimension 15*15 dont les
             valeur sont réelles qui représentent les probabilités de transitions de s
             à s'. NB: la lecture du résultat se fait suivant les lignes
    '''
    transition= np.zeros((15,15))

    
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

    
    return transition


#############################################################################################
#  propTransNoAct: Probabilités de transition avec le dé normal actualisées                 #
#############################################################################################

def propTransNoAct(layout,circle): # probabilité de transitionc avec le
                                   # dé normal  avec pieges (proba de 50% qu'on declanche un piege)
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
    

    return update

#############################################################################################
#  propTransNoAct: Probabilités de transition avec le dé  risque                #
#############################################################################################
def propTransNoRisq(layout,circle): # probabilité de transitionc avec le
                                   # dé risque
    '''
       Calcule les probabilités de transitions de chaque état s aux états éventuelles s' qui
       peuvent etre accessible lorsqu'on utilise uniquement le dé risque

       pré :
           layout: vecteur de type numpy.ndarray de longueurs 15 
           circle : booléen ( True or False)


       post: retoune un tableau de type numpy.ndarray de dimension 15*15 
    '''


    
    

    return risque
#############################################################################################
#  markovDecison: Algorithme d'itération par valeurs                                        #
#############################################################################################

def markovDecision(layout,circle):

    ''' Cette fonction lance l'algorithme du processus de décision de Markov pour
        déterminer la stratégie optimale concernant le choix des dés dans le jeu
        Snakes and Ladders, en utilisant la méthode de "l'itération de valeur".

     pré:
        layout: un vecteur de type numpy.ndarray qui représente la disposition
               du jeu, contenant 15 valeurs représentant les 15 carrés du jeu
               Snakes and Ladders. les valeurs possibles de layout sont 0,1,2,3 ou 4.
               Il est à noter que le premier et dernier élément de layout sont toujours
               0.

        circle: une variable booléenne (True or False), indiquant si le joueur doit
                atterrir exactement sur la case d'arrivée pour gagner (circle = True)
                ou gagne toujours en dépassant le case final (circle = False).

     post: retourne une liste contenant les vecteurs Expec et Dice où
          Expec: un vecteur de type numpy.ndarray contenant le coût attendu
                (= nombre de tours) associé aux 14 cases du jeu, à l'exclusion
                 de celle d'arrivée
          Dice: un vecteur de type numpy.ndarray contenant le choix des dés à
                utiliser pour chacun des 14 cases du jeu (1 pour le dé
                "sécurité", 2 pour le dé "normal"), à l'exclusion du dernier.
    '''

    V=np.zeros(15)
    v=np.zeros(15)
    delta=1      # va nous permettre de calculer les variations de la moyenne du nombre de tour d'une itération à l'autre
    teta=1/10**6 # sera notre condition d'arret pour la convergence
    k=0
    Dice=np.zeros(15,int)
    probaN=propTransNoAct(layout,circle) # nous donne les probabilités de transitions lorsqu'on utilise le dé normal
    probaS=propTranSec()
    probaR=probaTransResq()# nous donne les  probalités de transitions lorsqu'on utilise le dé sécurité

    while delta>teta:
        delta=0
        for i in range(14):     # l'indice i represente la case i+1
             v[i]=V[i]          # on peut remarquer que le case 15 à pour valeur v=0 et V=0 et ne sera jamais mis a jour car c'est la destination finale

                                ## Bellman’s equations of optimality
             
    return [V[:14],Dice[:14]] # ici on retourne les 14 premiers résultats

############################################################################################
# Création d'une classe qui matérialise un joueur qui se déplace sur le circuit de jeu     #                                    #
############################################################################################
class PartieJeu:

    def __init__(self,i,Dice,layout,circle):
        '''
          
         '''
        self.etat=i
        self.decision=Dice
        self.tours=0
        self.piege=layout
        self.circle=circle
        if self.etat==14:   #on marque la fin d'un jeu par cette état, notez que, bien que une partie non circulaire
                            # on peut gagner lorsque on atterit au dela de la case 15, on a tenu compte cela en dans la suite
                            # en ramenant cet état à 14 pour ainsi mettre fin au jeu
            return self.tours


    def lanceDe(self):
        '''
           retoune le résultat du lancé de dé du joueur à l'état i
        '''
        


    def etatSuivant(self):
        '''
          elle met à jour l'état du joueur après le lancé d'un dé, i.e où le joueur atterrit

        '''
        dec=self.lanceDe()

        

    def __str__(self):
        return "pour arriver à la case " + str(self.etat+1) +" l'agent à joué "+ str(self.tours) + " tours "




