import math

# Fonction qui calcule la quantité d'information
def quantité_information(probabilité):
    if probabilité > 0:
        return -math.log2(probabilité)
    else:
        return 0

# Fonction pour calculer l'entropie d'une source
def calcul_entropie(source):
    entropie = 0
    for evenement, probabilité in source.items():
        if probabilité > 0:  # Pas de probabilité nulles
            info = quantité_information(probabilité)
            entropie += probabilité * info
    return entropie

# Fonction pour calculer l'entropie conjointe
def calcul_entropie_conjointe(source1, source2, joint_probabilities):
    entropie_conjointe = 0
    for (ev1, ev2), prob in joint_probabilities.items():
        if prob > 0:
            info = quantité_information(prob)
            entropie_conjointe += prob * info
    return entropie_conjointe

# Fonction pour calculer l'entropie conditionnelle moyenne
def calcul_entropie_conditionnelle(entropie_conjointe, entropie_source):
    return entropie_conjointe - entropie_source

# Fonction pour calculer la quantité d'information mutuelle
def calcul_information_mutuelle(entropie_source1, entropie_source2, entropie_conjointe):
    return entropie_source1 + entropie_source2 - entropie_conjointe

# Fonction principale pour collecter les événements et probabilités
def main():
    # Collecte des événements et probabilités pour la première source
    source1 = {}
    somme_probabilites1 = 0.0

    n1 = int(input("Combien d'événements dans la première source ? "))
    for i in range(n1):
        evenement = input(f"Nom de l'événement {i + 1} (source 1): ")
        while True:
            probabilite = float(input(f"Probabilité de {evenement} (entre 0 et 1) : "))
            if 0 <= probabilite <= 1:
                break
            else:
                print("Erreur: La probabilité doit être comprise entre 0 et 1.")
        source1[evenement] = probabilite
        somme_probabilites1 += probabilite

    if abs(somme_probabilites1 - 1.0) > 1e-6:
        print("Erreur: La somme des probabilités de la première source doit être égale à 1.")
        return

    # Collecte des événements et probabilités pour la deuxième source
    source2 = {}
    somme_probabilites2 = 0.0

    n2 = int(input("Combien d'événements dans la deuxième source ? "))
    for i in range(n2):
        evenement = input(f"Nom de l'événement {i + 1} (source 2): ")
        while True:
            probabilite = float(input(f"Probabilité de {evenement} (entre 0 et 1) : "))
            if 0 <= probabilite <= 1:
                break
            else:
                print("Erreur: La probabilité doit être comprise entre 0 et 1.")
        source2[evenement] = probabilite
        somme_probabilites2 += probabilite

    if abs(somme_probabilites2 - 1.0) > 1e-6:
        print("Erreur: La somme des probabilités de la deuxième source doit être égale à 1.")
        return

    # Collecte des probabilités conjointes
    joint_probabilities = {}
    for ev1 in source1:
        for ev2 in source2:
            while True:
                prob = float(input(f"Probabilité conjointe P({ev1}, {ev2}) : "))
                if 0 <= prob <= 1:
                    joint_probabilities[(ev1, ev2)] = prob
                    break
                else:
                    print("Erreur: La probabilité doit être comprise entre 0 et 1.")

    # Calcul des entropies
    entropie1 = calcul_entropie(source1)
    entropie2 = calcul_entropie(source2)
    entropie_conjointe = calcul_entropie_conjointe(source1, source2, joint_probabilities)

    # Affichage des résultats
    print(f"\nEntropie de la première source: {entropie1:.4f} bits")
    print(f"Entropie de la deuxième source: {entropie2:.4f} bits")
    print(f"Entropie conjointe des deux sources: {entropie_conjointe:.4f} bits")

    entropie_conditionnelle = calcul_entropie_conditionnelle(entropie_conjointe, entropie1)
    print(f"Entropie conditionnelle de la deuxième source sachant la première: {entropie_conditionnelle:.4f} bits")

    information_mutuelle = calcul_information_mutuelle(entropie1, entropie2, entropie_conjointe)
    print(f"Quantité d'information mutuelle: {information_mutuelle:.4f} bits")

# Exécuter le programme
if __name__ == "__main__":
    main()
