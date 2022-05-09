#Ouverture du fichier et recuperation des lignes
import NosFonctions.Fonctions
ponderation_1 = 25
ponderation_2 = 25
ponderation_3 = 50
fichier=open("note.txt", "r")
lignes_fichier=fichier.readlines()
etudiants=[] #Tableau d'etudiants


 

""""
    -------------DEBUT --------------- 
    Convertion des eléments de [lignes_fichier] en liste
"""
for elements in lignes_fichier:
    etudiants.append(elements.split())
""""
    -------------FIN ---------------  
"""

""""
    -------------DEBUT ---------------
    Initialisation du dictionnaire
"""
dico_etudiant={}
for listes in etudiants:
    index=listes.pop(0)
    int_list = [int(i) for i in listes]
    dico_etudiant[index]= int_list

""""
    -------------FIN ---------------
"""
continuer = True
while  continuer:


    """
        dico_note = { 'E1': 12, 'E2': 12 ......... }
        formule_moy = note1*25 + note2*25 + note3*50
    """
    dico_note_totale ={}
    for cle, valeur in dico_etudiant.items():
        dico_note_totale[cle]= (valeur[0]/20)*ponderation_1 + (valeur[1]/20)*ponderation_2 + (valeur[2]/20)*ponderation_3

    dico_somme={}
    for cle, valeur in dico_etudiant.items():
        dico_somme[cle]= sum(valeur)
    #Minimum
    mini=NosFonctions.Fonctions.Minimum(dico_note_totale)
    #Maximum
    maxi=NosFonctions.Fonctions.Maximum(dico_note_totale)
    # print(mini[0])
    notes_1={}
    notes_2={}
    notes_3={}
    for cle, valeur in dico_etudiant.items():
        notes_1[cle] = valeur[0]
        notes_2[cle] = valeur[1]
        notes_3[cle] = valeur[2]

    somme_notes_1 = 0
    nombre_de_notes_1=0
    for cle in notes_1.keys():
        somme_notes_1 += notes_1[cle]
        nombre_de_notes_1 +=1 

    moyenne_notes_1= somme_notes_1/nombre_de_notes_1


    somme_notes_2 = 0
    nombre_de_notes_2=0
    for cle in notes_2.keys():
        somme_notes_2 += notes_2[cle]
        nombre_de_notes_2 +=1 

    moyenne_notes_2= somme_notes_2/nombre_de_notes_2

    somme_notes_3 = 0
    nombre_de_notes_3=0
    for cle in notes_3.keys():
        somme_notes_3 += notes_3[cle]
        nombre_de_notes_3 +=1 

    moyenne_notes_3= somme_notes_3/nombre_de_notes_3

    somme_moyennes = 0
    nombre_de_moyenne=0
    for cle in dico_note_totale.keys():
        somme_moyennes += dico_note_totale[cle]
        nombre_de_moyenne +=1 
    moyenne_generale_des_evaluations= somme_moyennes/nombre_de_moyenne
    # print(moyenne_generale_des_evaluations)
    menu=NosFonctions.Fonctions.MENU()
    print(menu)
    choix=int(input(":"))
    if choix==1:
        print("L'etudiant {} possede la plus basse note.".format(mini[0]))
        print("Sa note totale est: {}".format(mini[1]))
        print(".....................................................................")
        print("L'etudiant {} possede la plus haute note.".format(maxi[0]))
        print("Sa note totale est: {}".format(maxi[1]))
    elif choix==2:
        moyenneGlobal = (moyenne_notes_1/20)*25 + (moyenne_notes_2/20)*25 + (moyenne_notes_3/20)*50
        print("La moyenne de l'examen 1  est: {}".format(moyenne_notes_1))
        print("La moyenne de l'examen 2  est: {}".format(moyenne_notes_2))
        print("La moyenne de l'examen 3  est: {}".format(moyenne_notes_3))
        print("La moyenne globale est: {}".format(moyenneGlobal))
    elif choix==3:
        print("La variance pour l'examen 1 est: {:.3f}".format(NosFonctions.Fonctions.variance(notes_1)))
        print("La variable pour l'examen 2 est: {:.3f}".format(NosFonctions.Fonctions.variance(notes_2)))
        print("La variance pour l'examen 3 est: {:.3f}".format(NosFonctions.Fonctions.variance(notes_3)))
        print("La variance globale est: {:.3f}".format(NosFonctions.Fonctions.variance(dico_note_totale)))
    elif choix==4:
        ecartType1 = NosFonctions.Fonctions.EcartType(NosFonctions.Fonctions.variance(notes_1))
        print("L'ecart type de l'examen 1 est : {:.3f}".format(ecartType1))

        ecartType2 = NosFonctions.Fonctions.EcartType(NosFonctions.Fonctions.variance(notes_2))
        print("L'ecart type de l'examen 2 est : {:.3f}".format(ecartType2))

        ecartType3 = NosFonctions.Fonctions.EcartType(NosFonctions.Fonctions.variance(notes_3))
        print("L'ecart type de l'examen 3 est : {:.3f}".format(ecartType3))
        ecartGlobal = NosFonctions.Fonctions.EcartType(NosFonctions.Fonctions.variance(dico_note_totale))
        print("L'ecart type global 3 est : {:.3f}".format(ecartGlobal))

    elif choix==5:
        etudiant=input("Vous voulez connaitre les statistiques de quel etudiant ?")
        try:
            classement=NosFonctions.Fonctions.rang(dico_note_totale,dico_note_totale[etudiant])
            print("la moyenne de {} est: {}".format(etudiant, dico_somme[etudiant]/3))
            if classement==1:
                print("Le rang de {} est: {}er/20".format(etudiant, classement))
            else:
                print("Le rang de {} est: {}eme/20".format(etudiant, classement))
        except KeyError:
            print("Le nom de l'etudiant est invalide")
    elif choix==7:
        print("Changement des ponderation")
        ponderation_1 = float(input("Nouvelle ponderation Examen 1:"))
        ponderation_2 = float(input("Nouvelle ponderation Examen 2:"))
        ponderation_3 = float(input("Nouvelle ponderation Examen 3:"))
    elif choix==8:
        echec=NosFonctions.Fonctions.tauxEchec(dico_note_totale)
        print(echec)

    demande = input('Voulez vous continuer? Y-oui N-non: ')
    if demande == "N":
        continuer=False








    


fichier.close()



