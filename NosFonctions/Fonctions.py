from math import sqrt
def MENU():
    print("Selectionner un choix...")
    CHOIX="""
        1. Note la plus basse ainsi que la note la plus elevee
        2. Moyenne
        3. Variance
        4. Ecart-Type
        5. Rang et moyenne pour un etudiant
        6. Affichage d'histogramme
        7. Modification de ponderation
        8. Taux d'echec
    """
    return CHOIX
    
def Minimum(dico):
    mini = dico['E1']
    etudiant_min =""
    for cle, valeur in dico.items():
        if valeur<mini:
            mini= valeur
            etudiant_min = cle
    return (etudiant_min, mini)


def Maximum(dico):
    maxi = dico['E1']
    etudiant_max =""
    for cle, valeur in dico.items():
        if valeur>maxi:
            maxi= valeur
            etudiant_max = cle
    return (etudiant_max, maxi)

def GlobaleMoyenne(dico):
    somme=0
    c=0
    for elements in dico.values():
        somme+=elements
        c+=1
    return(somme/c)
def variance(dico):
    listes=[]
    for elements in dico.values():
        listes.append(elements)
    m = sum(listes) / len(listes)
    # calculate variance using a list comprehension
    var_res = sum((xi - m) ** 2 for xi in listes) / len(listes)
    return var_res
def EcartType(variance):
    return sqrt(variance)


def rang(dico, moyenneEtudiant):
    listesNotes=[]
    for note in dico.values():
        listesNotes.append(note)
    listesNotes.sort()
    listesNotes.reverse()
    return listesNotes.index(moyenneEtudiant)+1


def tauxEchec(dico):
    liste=[]
    for note in dico.values():
        liste.append(note)
    i=0
    for note in liste:
        if note<60:
            i+=1
    if i==1:
        return ("Il y'a {} etudiant en echec soit {}%".format(i, (i*100)/len(liste)))
    else:
        return ("Il y'a {} etudiants en echec soit {:.2f}%".format(i, (i*100)/len(liste)))
