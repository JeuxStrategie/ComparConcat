# ================================================================================================================
# ce programme a pour but de concatener des fichiers présents dans un répertoire source en un seul fichier
# ================================================================================================================
import os
import time


# -----------------------------------------------------------------------------------------
# la procédure concatener a plusieurs paramètres
# paramètre 1 : repertoireSource = le répertoire qui contient les fichiers à concaténer
# paramètre 2 : repertoireSortie = le répertoire qui contient le fichier concaténé
# paramètre 3 : nomFichierConcatene = le répertoire qui contient le fichier concaténé
# -----------------------------------------------------------------------------------------
def concatener(repertoireSource, repertoireSortie, nomFichierConcatene):

    # on initialise les variables en dehors des boucles
    start_time = time.time()  # on sauvegarde l'heure dans la variable start_time
    compteurFichier = 0  # le nombre de fichiers lus dans le répertoire source

    # on ouvre en écriture (c'est le 'w' pour write) le fichier "nomFichierConcatene" dans le répertoire "repertoireSortie"
    # la fonction os.path.join permet de contruire un nom de chemin à partir de plusieurs noms de chemins partiels
    filewriteConcatener = open(os.path.join(repertoireSortie, nomFichierConcatene), 'w')

    # on boucle avec la boucle for
    # pour tous les fichiers présents dans la liste des fichiers du répertoire repertoireSource
    for filename in os.listdir(repertoireSource):
        with open(os.path.join(repertoireSource, filename), 'r', encoding='UTF-8') as fileread:

            # on augmente le compteur de fichier lu de 1
            compteurFichier = compteurFichier + 1

            # initialisation des variables dans la boucle pour chaque fichier
            # le compteur ligne est le nombre de lignes lues pour CHAQUE fichier
            compteurLigne = 0

            # on lit la première ligne du fichier source et on augmente le compteur de ligne lue de 1
            line = fileread.readline()
            if line != "" : compteurLigne = compteurLigne + 1

            # on lit les lignes du fichier ligne à ligne tant qu'on a pas atteint la fin du fichier
            while line:
                ligneAEcrireConcatener = line

                filewriteConcatener.write(ligneAEcrireConcatener)

                # on lit la ligne suivante du fichier source et on augmente le compteur de ligne lue de 1
                line = fileread.readline()
                if line != "" : compteurLigne = compteurLigne + 1

            # on a lu tous les fichiers source (boucle while avant)
            # on ferme le fichier source pour pouvoir passer au suivant
            print("compteur de lignes : " + str(compteurLigne))
            fileread.close()

    # on a lu tous les fichiers source
    # on ferme le fichier resultat
    filewriteConcatener.close()

    # on écrit dans la console la durée du programme et le nombre de fichiers lus dans le répertoire source
    print("nombre de fichiers lus : " + str(compteurFichier))
    print("--- %s seconds ---" % (time.time() - start_time))


# on appelle la procédure de concatenation concatener avec les 3 paramètres
concatener(os.getcwd() + '/EXEMPLE1/fichiers_source', os.getcwd() + '/EXEMPLE1/fichiers_resultat', 'fichierConcatene.csv')



