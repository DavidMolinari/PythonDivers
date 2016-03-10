''' TP Cryoptographie
Meh
'''

# A. Occurence d'une lettre dans un message :

'''
a. Lister les variables utilisées ainsi que leur type.
message = variable de type chaine de caractere
n = variable de type entier
i et cpt = variables de type entier

b. Il manque l'incrépentation du compteur i pour permettre de boucler
jusqu'à la longueur de message, donc l'instruction : i = i + 1

c. Cet algorithme permet de compter le nombre de fois où la lettre 'a'
est dans le mesage.

e. pour prendre e compte le A en majusculre, on ajoute une condition
    de plus : if (message[i] == 'a' or message[i] == 'A') '''



# Fontion qui retourne le nombre d'occurence de la lettre a/A
def occurence_lettre(message):
    n = len(message)
    i = 0
    cpt = 0
    while (i < n):
        if (message[i] == 'a' or message[i] == 'A') :
            cpt = cpt + 1
        i = i + 1
    print(cpt)
# Fonction qui retourne sous forme d'un tableau, le nombre d'occurencs
# de toutes les lettres de l'alphabet


''' Programme principal '''
print("Occurences de la lettre a dans J'aime les ananas :")
occ1 = occurence_lettre("J'aime les ananas !")
print("Occurences de la lettre a Avez vous appris votre cours ?  :")
occ2 = occurence_lettre('Avez vous appris votre cours ? ')




