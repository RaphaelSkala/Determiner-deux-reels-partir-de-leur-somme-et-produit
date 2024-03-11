import math

#input de la somme et du produit
somme = float(input("Entrez la somme des deux réels : "))
produit = float(input("Entrez le produit des deux réels : "))

#calcul du discriminant
discriminant = somme**2 - 4 * produit

#print du résultat
if discriminant < 0:
    print("Pas de solutions réelles.")
elif discriminant == 0:
    x = y = somme / 2
    print(f"Les deux réels sont égaux à {x}.")
else:
    x = (somme + math.sqrt(discriminant)) / 2
    y = (somme - math.sqrt(discriminant)) / 2
    print(f"Les deux réels sont : x = {x}, y = {y}")
