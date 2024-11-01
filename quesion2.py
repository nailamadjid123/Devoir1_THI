import math

# Fonction pour calculer la quantité d'information pour un événement
def quantite_information(prob):
    if prob > 0:
        return -math.log2(prob)
    else:
        return 0

# Fonction pour calculer l'entropie d'une source
def calcul_entropie(source):
    entropie = 0
    for evenement, prob in source.items():
        if prob > 0:
            entropie += prob * quantite_information(prob)
    return entropie

# Fonction pour calculer l'entropie conjointe de deux sources
def calcul_entropie_conjointe(source_conjointe):
    entropie_conjointe = 0
    for (evenement1, evenement2), prob in source_conjointe.items():
        if prob > 0:
            entropie_conjointe += prob * quantite_information(prob)
    return entropie_conjointe

# Fonction pour calculer l'entropie conditionnelle H(X|Y)
def calcul_entropie_conditionnelle(entropie_conjointe, entropie_y):
    return entropie_conjointe - entropie_y

# Fonction pour calculer la quantité d'information mutuelle I(X;Y)
def calcul_information_mutuelle(entropie_x, entropie_y, entropie_conjointe):
    return entropie_x + entropie_y - entropie_conjointe

# Fonction principale pour collecter les événements et probabilités
def main():
    # Définir les sources X et Y séparément
    source_x = {}
    source_y = {}
    source_conjointe = {}

    # Saisie des événements pour la source X
    n_x = int(input("Combien d'événements dans la source X ? "))
    for i in range(n_x):
        evenement_x = input(f"Nom de l'événement {i + 1} dans X : ")
        prob_x = float(input(f"Probabilité de {evenement_x} dans X : "))
        source_x[evenement_x] = prob_x

    # Saisie des événements pour la source Y
    n_y = int(input("Combien d'événements dans la source Y ? "))
    for i in range(n_y):
        evenement_y = input(f"Nom de l'événement {i + 1} dans Y : ")
        prob_y = float(input(f"Probabilité de {evenement_y} dans Y : "))
        source_y[evenement_y] = prob_y

    # Saisie des probabilités conjointes pour X et Y
    print("\nEntrez les probabilités conjointes pour les paires (X, Y) :")
    for evenement_x in source_x:
        for evenement_y in source_y:
            prob_conjointe = float(input(f"Probabilité de ({evenement_x}, {evenement_y}) : "))
            source_conjointe[(evenement_x, evenement_y)] = prob_conjointe

    # Calcul des entropies
    entropie_x = calcul_entropie(source_x)
    entropie_y = calcul_entropie(source_y)
    entropie_conjointe = calcul_entropie_conjointe(source_conjointe)

    # Calcul de l'entropie conditionnelle H(X|Y)
    entropie_conditionnelle_moyenne = calcul_entropie_conditionnelle(entropie_conjointe, entropie_y)

    # Calcul de l'information mutuelle I(X; Y)
    information_mutuelle = calcul_information_mutuelle(entropie_x, entropie_y, entropie_conjointe)

    # Affichage des résultats
    print(f"\nEntropie de la source X: {entropie_x:.4f} bits")
    print(f"Entropie de la source Y: {entropie_y:.4f} bits")
    print(f"Entropie conjointe H(X, Y): {entropie_conjointe:.4f} bits")
    print(f"Entropie conditionnelle H(X|Y): {entropie_conditionnelle_moyenne:.4f} bits")
    print(f"Quantité d'information mutuelle I(X; Y): {information_mutuelle:.4f} bits")

# Exécuter le programme
if __name__ == "__main__":
    main()
