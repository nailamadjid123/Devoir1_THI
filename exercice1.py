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
    somme_probabilites = 0.0

    n = int(input("Combien d'événements dans la source ? "))  # Demander combien d'événements

    # Collecter les événements et leurs probabilités
    for i in range(n):
        evenement = input(f"Nom de l'événement {i + 1}: ")

        # Validation de la probabilité
        while True:
            probabilite = float(input(f"Probabilité de {evenement} (entre 0 et 1) : "))
            if 0 <= probabilite <= 1:
                break  # Probabilité valide
            else:
                print("Erreur: La probabilité doit être comprise entre 0 et 1.")

        source[evenement] = probabilite
        somme_probabilites += probabilite  # Ajouter à la somme des probabilités

    # Vérification que la somme des probabilités est bien égale à 1
    if abs(somme_probabilites - 1.0) > 1e-6:  # Tolérance pour éviter les erreurs de précision
        print("Erreur: La somme des probabilités doit être égale à 1. Veuillez vérifier vos entrées.")
        return  # Sortir du programme si la somme n'est pas égale à 1
    
      

        
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
