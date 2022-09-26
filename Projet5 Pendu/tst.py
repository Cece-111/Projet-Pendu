from random import*

def dessinPendu(nb):
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
    return tab[nb]

def pendu():
    jouer="OUI"
    partie=0
    reussite=0
    while jouer=="OUI":
        partie+=1
        fichier=open ("dico.txt","r",encoding="utf-8")  # Ouvre le fichier txt
        listMot=fichier.readlines()                     # Met les mots dans une liste

        motAlea=randint(0,len(listMot))                 # Choisi un nombre entre 0 et le nb de mots
        motChoisi=listMot[motAlea]                      # Transcrit le nombre par le mot correspondant
        print("Partie n°", partie)                      # Affiche le numéro de la partie
        listMotAffiche=[]
        motAffiche=''                                   # Initialisation du mot caché
        compteurRaté=0
        for etoiles in range(len(motChoisi)-1):         # Boucle pour remplacer les lettres du mot par des étoiles
            motAffiche+="_ "                            # Remplace les lettres par des étoiles
            listMotAffiche.append('_ ')                 # Creer une liste avec les etoiles séparées

        fin=0
        listLettreDeja=[]
        listeCaractèresAdmis=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        while '_ ' in motAffiche and fin==0:
            lettreCorrect=0
            while lettreCorrect==0:
                lettreEntree=str(input("Ecrivez une lettre.")).upper()  # Demande une lettre a l'utilisateur

                if lettreEntree in listLettreDeja:          # Vérifie que la lettre n'a pas déja été saisie.
                    print('Vous avez deja saisi la lettre',lettreEntree,"Merci d'en entrer une autre.")

                elif len(lettreEntree)!=1:                  # Vérifie qu'il n'y a qu'un seul caratère de saisie.
                    print("Merci de n'écrire qu'une lettre à la fois.")

                elif lettreEntree not in listeCaractèresAdmis:  # Vérifie que le caractère entrée est admis.
                    print("Votre caractère n'est pas admis. Voici la lite des caractères admis:",listeCaractèresAdmis)

                else:
                    listLettreDeja.append(lettreEntree)
                    lettreCorrect=1



            if lettreEntree in motChoisi:
                indice=0
                print('Bravo! Une lettre en plus de trouvée!\n')
                for etoilesARemplacer in listMotAffiche:

                    if etoilesARemplacer=='_ ' and motChoisi[indice]==lettreEntree:
                        listMotAffiche[indice]=lettreEntree+" "

                    indice+=1


            else:
                compteurRaté+=1
                print("domage... , il n'y a pas la lettre",lettreEntree,"dans le mot à trouver.\n")


            print(dessinPendu(compteurRaté))

            motAffiche=''
            for i in listMotAffiche:
                motAffiche+=i

            if compteurRaté>=10:
                fin=1
                print("Domage! Vous avez perdu... \nPeut etre la prochaine fois \^-^/ .")

            if fin==0:
                print("Lettres trouvées: [",motAffiche,"]")

        if fin==0:
            print("Félicitation! Tu as réussit!")
            reussite+=1

        jouer=str(input("Voulez-vous rejouer? si oui écrivez OUI")).upper()

    if partie>1:
        print("Vous avez réussit à trouver",reusite,"mots sur",partie,"parties")


    fichier.close



pendu()