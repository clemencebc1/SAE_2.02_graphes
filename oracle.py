import networkx as nx 
import matplotlib as plt
import requetes 

# fonctions élémentaires utiles au fonctionnement du programme princpal
def chemin():
    """dessine un graphe à partir d'un fichier texte donnée 

    Returns:
        Graph/str: renvoie le graphe du fichier donné, sinon une chaine de caractères
    """
    chemin=input("Donnez le chemin vers un fichier txt contenant des dictionnaires de films avec leurs acteurs\n")
    tour=0
    json_vers_nx=None
    while json_vers_nx==None and tour<4:
        json_vers_nx=requetes.json_vers_nx(chemin)
        if json_vers_nx != None:
            return json_vers_nx
        else:
            chemin=input("Veuillez redonner le chemin vers un fichier txt contenant des dictionnaires de films avec leurs acteurs\n"+ "il vous reste "+ str(4-tour)+ " tentatives avant de devoir relancer le programme\n")
            tour +=1
    print("impossible d'ouvrir les fichiers, veuillez relancer le programme\n")
    return None

def demandeDistance():
    distance=input("Entrez une distance (un nombre)\n")
    tour=0
    while int(distance)==ValueError and tour<4:
        distance=input("ce n'est pas un nombre, veuillez entrer un chiffre ou un nombre (sans espace), "+"il vous reste"+ str(4-tour)+"tentatives \n")
        if tour==4:
            print("les caractères entrés ne sont pas des chiffres")
            return None
    return int(distance)
        
def chgmntActeurU(acteurU):
    """change l'acteur principal 

    Args:
        acteurU (str): une chaine de caracteres reprensentant l'acteur principal 

    Returns:
        retourne soit le nom du nouvel acteur ou None si aucun changement
    """
    chgmntActeurU = input("Voulez-vous changer d'acteur principal ? "+acteurU+" est actuellement l'acteur principal (Oui/Non)\n")
    if chgmntActeurU.lower() == "oui":
        acteur = input("Entrez le nom complet de l'acteur\n")
        return acteur
    return None

def choix_programme(json_vers_nx, acteurU):
    """effectue les calculs en fonction de l'entrée de l'utilisateur

    Args:
        json_vers_nx (Graph): un graphe networkx
        acteurU (str): une chaine de caracteres definissant un acteur sur lequel les calculs vont être effectués
    """
    choix_fonction = input("que voulez-vous savoir à propos de "+acteurU+ " ?\n"+"1. Les collaborateurs communs entre "+ acteurU+" un autre acteur \n"+"2. Les collaborateurs proches de "+acteurU+" à une distance k\n"+"3. Savoir si "+acteurU+" est proche d'un autre acteur (à une distance donnée)\n"+
    "4. Calculer la distance entre deux acteurs\n"+"5. Calculer la plus grande distance que possède "+acteurU+" avec un autre\n"+"6. Chercher l'acteur le plus central d'hollywood\n"+"7. Chercher l'acteur le moins central d'hollywood\nVeuillez choisir un chiffre selon les calculs souhaités, si aucun n'est souhaité, vous pouvez simplement saisir entrée\n")
    match choix_fonction:
            case "1":
                acteurV=input("Donnez le nom complet d'un acteur différent de "+acteurU+" afin de déterminer leurs collaborateurs communs\n")
                collabCommun = requetes.collaborateurs_communs(json_vers_nx, acteurU, acteurV)
                if collabCommun==None:
                    return "un des deux acteurs n'est pas connu"
                for acteur in collabCommun:
                    res = acteur + ", "
                return res
            case "2":
                distance = demandeDistance()
                if distance == None:
                    return None

                collabProche = requetes.collaborateurs_proches(json_vers_nx, acteurU, distance)
                res = ""
                if collabProche != None:
                    for acteur in collabProche:
                        res += acteur + ","
                    return res
                return None
            case "3":
                acteurV=input("entrez un acteur différent de "+acteurU+" afin de savoir si celui-ci est à une distance k de l'acteur saisi\n")
                distance = demandeDistance()
                if distance == None:
                    return None
                return requetes.est_proche(json_vers_nx,acteurU,acteurV,int(distance))
            case "4":
                acteurV=input("entrez un acteur différent de "+acteurU+" pour calculer leur distance\n")
                return requetes.distance(json_vers_nx,acteurU,acteurV)
            case "5":
                return requetes.centralite(json_vers_nx,acteurU)
            case "6":
                return requetes.centre_hollywood(json_vers_nx)
            case "7":
                return requetes.eloignement_max(json_vers_nx)
            case _:
                return "Votre proposition n'est pas dans les choix"

# programme principal permettant de lancer l'application
def programme_principal():
    """le programme principal lançant l'application
    """
    try:
        explication= input("Dans le cadre de notre SAé 2.02, nous vous proposons")
        if explication:
            print()
    
        json_vers_nx=chemin()
        if json_vers_nx == None:
            return "Veuillez relancer le programme, le nom du fichier génère une erreur"
        acteurU=input("Donnez le nom d'un acteur\n")
        continuer=True
        tour = 0
        while continuer and tour<100:
            choix_programme(json_vers_nx,acteurU)
            tour += 1
            continuerCalculs = input("Voulez-vous continuer le calculs ? Oui/Non")
            if continuerCalculs.lower() == "non":
                continuer = False
            chgmntActeur = chgmntActeurU(acteurU)
            if chgmntActeur != None:
                acteurU = chgmntActeur

        if  tour == 100:
            return "Vous avez effectué beaucoup de calculs ! Redémarrez le programme pour en refaire de nouveau."
        return "À bientôt !"
    except:
        return "une erreur est survenue, veuillez relancer le programme"


print(programme_principal())