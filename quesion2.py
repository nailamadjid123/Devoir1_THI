import math

# Fonction pour calculer l'entropie d'une source
def calcul_entropie(prob_source):
    return sum(p * math.log2(1/p) for p in prob_source if p > 0)

# Fonction pour calculer l'entropie conjointe entre deux sources
def calcul_entropie_conjointe(Px, P_j_sachent_i):
    entropie_conjointe = 0
    for i in range(len(Px)):
        for j in range(len(P_j_sachent_i)):
            Pxy = P_j_sachent_i[j][i] * Px[i]  # P(Xi, Yj) = P(Yj | Xi) * P(Xi)
            if Pxy > 0:  # Éviter les log(0)
                entropie_conjointe += Pxy * math.log2(1/Pxy)
    return entropie_conjointe

# Fonction pour calculer l'entropie conditionnelle moyenne H(Y|X)
def calcul_entropie_conditionnelle(Px, P_j_sachent_i):
    entropie_conditionnelle = 0
    for i in range(len(Px)):
        S = 0
        for j in range(len(P_j_sachent_i)):
            if P_j_sachent_i[j][i] > 0:  # Éviter log(0)
                S += P_j_sachent_i[j][i] * math.log2(1/P_j_sachent_i[j][i])
        entropie_conditionnelle += Px[i] * S
    return entropie_conditionnelle

# Fonction pour calculer la quantité d'information mutuelle
def calcul_information_mutuelle(Px, Py, Hxy):
    Hx = calcul_entropie(Px)
    Hy = calcul_entropie(Py)
    return Hx + Hy - Hxy

# Fonction pour vérifier que la somme des probabilités est égale à 1
def verifie_probabilites(prob_source):
    somme = sum(prob_source)
    if abs(somme - 1.0) > 1e-6:  # Tolérance pour éviter les erreurs de précision
        print(f"Erreur : La somme des probabilités est {somme}, elle doit être égale à 1.")
        return False
    return True

# Fonction principale pour recueillir les probabilités des deux sources
def main():
    # Recueil des probabilités pour la première source X
    Px = []
    while True:
        n_x = int(input("Combien d'événements dans la source X ? "))
        Px = []
        for i in range(n_x):
            prob = float(input(f"Probabilité de l'événement X{i+1} : "))
            Px.append(prob)
        if verifie_probabilites(Px):
            break
    
    # Recueil des probabilités pour la source Y
    Py = []
    while True:
        n_y = int(input("Combien d'événements dans la source Y ? "))
        Py = []
        for j in range(n_y):
            prob = float(input(f"Probabilité de l'événement Y{j+1} : "))
            Py.append(prob)
        if verifie_probabilites(Py):
            break

    # Recueil des probabilités conditionnelles P(Yj|Xi)
    P_j_sachent_i = []
    while True:
        print("Entrez les probabilités conditionnelles P(Y|X):")
        P_j_sachent_i = []
        for j in range(n_y):
            P_j = []
            print(f"Probabilités P(Y{j+1}|X) :")
            for i in range(n_x):
                prob = float(input(f"Probabilité P(Y{j+1}|X{i+1}) : "))
                P_j.append(prob)
            P_j_sachent_i.append(P_j)
        
        # Vérification que la somme des probabilités conditionnelles pour chaque Yj est égale à 1
        if all(verifie_probabilites(P_j_sachent_i[j]) for j in range(n_y)):
            break

    # Calcul de l'entropie conjointe
    Hxy = calcul_entropie_conjointe(Px, P_j_sachent_i)
    print(f"Entropie conjointe H(X,Y) = {Hxy:.4f} bits")

    # Calcul de l'entropie conditionnelle moyenne H(Y|X)
    H_y_given_x = calcul_entropie_conditionnelle(Px, P_j_sachent_i)
    print(f"Entropie conditionnelle moyenne H(Y|X) = {H_y_given_x:.4f} bits")

    # Calcul de la quantité d'information mutuelle I(X;Y)
    Ixy = calcul_information_mutuelle(Px, Py, Hxy)
    print(f"Quantité d'information mutuelle I(X;Y) = {Ixy:.4f} bits")

# Exécuter le programme
if __name__ == "__main__":
    main()
