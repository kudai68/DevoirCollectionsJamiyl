# Création d'une liste de 10 éléments de type chaîne de caractères
liste = ["Football", "Basketball", "Handball", "Volleyball", "Baseball", "Hockey", "Golf", "Cycling", "Cricket", "F1"]

# Affichage des éléments de la liste
print("----------------------------------Affichage des éléments de la liste----------------------------------------")
print(liste)

# Changer le contenu de l'élément numéro 5
liste[4] = "Nascar"
print("------------------------------Liste après modification de l'élément numéro 5--------------------------------")
print(liste)

# Création d'une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
liste2 = [element for element in liste if "a" in element]
print("--------------------------Nouvelle liste avec les éléments contenant la lettre 'a'-------------------------")
print(liste2)

# Ajout d'un élément à la fin de la liste
liste.append("grenouille")
print("------------------------------Liste après ajout d'un élément à la fin-----------------------------------")
print(liste)

# Ajout d'un élément à l’index numéro 2
liste.insert(1, "Schistosoma")
print("--------------------------Liste après ajout d'un élément à l'index numéro 2------------------------------")
print(liste)

# Suppression de l'élément numéro 3
liste.pop(2)
print("-------------------------------Liste après suppression de l'élément numéro 3-------------------------------")
print(liste)

# Suppression de l'élément à l’index numéro 2
liste.pop(2)
print("--------------------------Liste après suppression de l'élément à l'index numéro 2--------------------------")
print(liste)

# Liste ordonnée
liste.sort()
print("----------------------------------------Liste ordonnée-----------------------------------------------------")

