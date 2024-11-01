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

    source = {} 

    n = int(input("Combien d'événements dans la source ? "))  # Demander combien d'événements

    
    
      

           # Collecter les événements et leurs probabilités
    for i in range(n):
        evenement=input(f"Nom de l'évenemnt {i+1}:")
        probabilité=float(input(f"probabilité de {evenement} :"))
        source[evenement]=probabilité
    
 # Affichage des quantités d'information et calcul de l'entropie

    print("\nQuantité d'information pour chaque événement:")

    for evenement,probabilité in source.items():
       information=quantité_information(probabilité)
       print(f"{evenement}: {information:.4f} bits")

    entropie = calcul_entopie(source)
    print(f"\nEntropie totale de la source: {entropie:.4f} bits")

            # Exécuter le programme
if __name__ == "__main__":
    main()