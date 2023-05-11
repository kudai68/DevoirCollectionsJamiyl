# Question 1
print("============================================Question 1==========================================================")

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

# Affichage de la liste au sens inverse
liste_inverse = liste[::-1]
print("---------------------------------------------Liste inversée------------------------------------------------")
print(liste_inverse)

# Vider la liste
liste.clear()
print("----------------------------------------------Liste vidée---------------------------------------------------")
print(liste)

# Suppression de la liste
del liste

# Question 2
print("============================================Question 2==========================================================")

# Création d'une tuple de 10 éléments de type entier
laTuple = (6, 10, 2002, 36, 100, 44, 77, 99, 3, 14)

# Affichage des éléments de la tuple
print("---------------------------------------Les éléments de la laTuple sont----------------------------------------------")
print(laTuple)

# Affichage du nombre de fois que la valeur 3 apparait dans la tuple
print("--------------------------Le nombre de fois que la valeur 3 apparait dans la laTuple est--------------------------")
print(laTuple.count(3))

# Affichage du contenu de l'élément numéro 5
print("---------------------------------------Le contenu de l'élément numéro 5 est---------------------------------------")
print(laTuple[4])

# Ordonner la tuple
laTuple = tuple(sorted(laTuple))
print("--------------------------------------------------laTuple ordonnée--------------------------------------------------")
print(laTuple)

# Ajouter un élément à la fin de la tuple
liste_laTuple = list(laTuple)
liste_laTuple.append(11)
laTuple = tuple(liste_laTuple)

# Ajouter un élément à l'index 3
liste_laTuple = list(laTuple)
liste_laTuple.insert(3,786)
laTuple = tuple(liste_laTuple)

# Afficher la nouvelle tuple
print("-----------------------------------------------laTuple après ajout----------------------------------------------")
print(laTuple)

print("============================================Question 3==========================================================")

# Création d'un set de 10 éléments de type chaîne de caractères
uneSet = set(["Football", "Basketball", "Handball", "Volleyball", "Baseball", "Hockey", "Golf", "Cycling", "Cricket", "F1"])

