import math

#une fonction qui calcule la quantité d'information 

def quantité_information(probablité):
    if probabilité > 0:
        return -math.log2(probabilité)
    else:
        return 0

        
         
            