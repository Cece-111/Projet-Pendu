#edit by Célian VIGNAUD, Florien MEUNIER, Candys
from random import*

def dessinPendu(nb):
    """
    Fonction qui permet de dessiner le pendu.
    """


    tab=[
    """






    ═══════════════
    """
    ,
    """
    .║
    .║
    .║
    .║
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔═════════
    .║
    .║
    .║
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦════════
    .╠╝
    .║
    .║
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║
    .║
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║       |
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║      ~|
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║      ~|~
    .║
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║      ~|~
    .║      /
    .║
    ═╩═════════════
    """
    ,
    """
    .╔╦══════╦═
    .╠╝      ║
    .║       ☺
    .║      ~|~
    .║      / |
    .║
    ═╩═════════════
    """
    ]
    return tab[nb]                                      # Renvoie le pendu numéro 'nb'

def pendu():
    """
    Fonction qui permet de jouer au pendu.
    """

    jouer="OUI"
    partie=0
    reussite=0

    while jouer=="OUI":

        fichier=open ("dico.txt","r",encoding="utf-8")  # Ouvre le fichier .txt contenant les mots
        listMot=fichier.readlines()                     # Met les mots dans une liste
        print(len(listMot))

        partie+=1
        phrase="Partie n°"+ str(partie)
        print(phrase)
        motAlea=randint(0,len(listMot))                 # Choisit un nombre entre 0 et le nb de mots
        motChoisi=listMot[motAlea]                      # Transcrit le nombre par le mot correspondant
        listMotAffiche=[]
        motAffiche=''                                   # Initialisation du mot caché
        compteurRaté=0
        for etoiles in range(len(motChoisi)-1):         # Boucle pour remplacer les lettres du mot par des "_"
            motAffiche+="_ "                            # Remplace les lettres par des "_"
            listMotAffiche.append('_ ')                 # Creer une liste avec les "_" séparées

        fin=0
        listLettreDeja=[]                               # Initialise la liste des lettre déjà proposées
        listeCaractèresAdmis=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  # Liste des caractères autorisés
        while '_ ' in motAffiche and fin==0:            # Tourne tant qu'il reste des lettres à trouver ou qu'il a eu moins 11 essait faux.
            lettreCorrect=0
            while lettreCorrect==0:                     # Vérifie que la lettre soit valide
                lettreEntree=str(input("Ecrivez une lettre.")).upper()  # Demande une lettre a l'utilisateur

                if lettreEntree in listLettreDeja:      # Vérifie que la lettre n'a pas déja été saisie.
                    print('Vous avez déjà saisi la lettre',lettreEntree,"\nMerci de saisir une autre lettre.")

                elif len(lettreEntree)!=1:              # Vérifie qu'il n'y a qu'un seul caratère de saisie.
                    print("Merci d'écrire une seule lettre.\n")

                elif lettreEntree not in listeCaractèresAdmis:  # Vérifie que le caractère entrée est admis.
                    print(lettreEntree,"n'est pas admis. Voici la lite des caractères admis:\n\t",listeCaractèresAdmis)

                else:
                    listLettreDeja.append(lettreEntree) # Ajout de la lettre dans la liste des lettre déjà proposées
                    lettreCorrect=1

                if lettreCorrect==0:
                    print(dessinPendu(compteurRaté),"\nLettres trouvées: [",motAffiche,"]") # Affiche l'état du pendu et du mot à trouver


            if lettreEntree in motChoisi:               # Regarde si la lettre saisie est présente dans le mot à trouver
                indice=0
                print('Bravo! Une lettre en plus de trouvée!\n')
                for etoilesARemplacer in listMotAffiche:

                    if etoilesARemplacer=='_ ' and motChoisi[indice]==lettreEntree:
                        listMotAffiche[indice]=lettreEntree+" " # Remplace l'enplacement marqué par un underscore de la lettre trouvées par la lettre

                    indice+=1


            else:
                compteurRaté+=1                         # Compte le nombre de raté
                print("dommage... , il n'y a pas la lettre",lettreEntree,"dans le mot à trouver.\n")


            print(dessinPendu(compteurRaté))            # Affiche l'état du pendu

            motAffiche=''
            for i in listMotAffiche:
                motAffiche+=i

            print("Lettres trouvées: [",motAffiche,"]") # Affiche l'état du mot à trouver
            if compteurRaté>=10:                        # Tourne si il y a eu 10 ratés
                fin=1
                print("Dommage! Vous avez perdu... \nPeut-être la prochaine fois \^-^/ .")



        if fin==0:                                      #Tourne si le joueuer a trouvé toutes les lettres
            print("Félicitations! Tu as réussi!")
            reussite+=1

        jouer=str(input("Voulez-vous rejouer? si oui écrivez OUI")).upper()

    if partie>1:
        print("Vous avez réussit à trouver",reussite,"mots sur",partie,"parties")

    fichier.close                                       # Ferme le fichier contenant les differents mots

pendu()                                                 # Execute le programme du pendu