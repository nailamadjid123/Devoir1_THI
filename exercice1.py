import math

#une fonction qui calcule la quantité d'information 

def quantité_information(probabilité):
    if probabilité > 0:
        return -math.log2(probabilité)
    else:
        return 0
                                 #***********************************************************************#

# Fonction pour calculer l'entropie d'une source

def calcul_entopie(source):
    entropie=0
    for evenement,probabilité in source.items():  # Cette méthode retourne une liste de paires clé-valeur (c'est-à-dire les événements et leurs probabilités
             
      if probabilité >0: #pas de probabilité nulles
          info=quantité_information(probabilité) 
          entropie +=probabilité *info
    return entropie


                                 #***********************************************************************#

# Fonction principale pour collecter les événements et probabilités

def main():
    source={}
    n=int(input("Combien d'événements dans la source ???"))
 # Collecter les événements et leurs probabilités
for i in range(n):
    evenement=input(f"Nom de l'évenemnt {i+1}:")

            