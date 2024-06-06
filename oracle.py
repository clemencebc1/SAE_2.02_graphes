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
    try:
        distance=input("Entrez une distance (un nombre)\n")
        return int(distance)
    except:
        tour=0
        dis=demandeDistance()
        while tour<4 and type(dis)!=int:
            if tour==4:
                print("les caractères entrés ne sont pas des chiffres")
                return None
            tour+=1
            dis=demandeDistance()
        return int(dis)
        
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
                    print("un des acteurs n'est pas connu")
                    return None
                res = ""
                for acteur in collabCommun:
                    res += acteur + ", "
                return res
            case "2":
                distance = demandeDistance()
                if distance == None:
                    return None

                collabProche = requetes.collaborateurs_proches(json_vers_nx, acteurU, distance)
                res = ""
                print(type(collabProche))
                if collabProche != None:
                    for acteur in collabProche:
                        res += acteur + ","
                print(res)
                return True
            case "3":
                acteurV=input("entrez un acteur différent de "+acteurU+" afin de savoir si celui-ci est à une distance k de l'acteur saisi\n")
                distance = demandeDistance()
                if distance == None:
                    return None
                res = requetes.est_proche(json_vers_nx,acteurU,acteurV,int(distance))
                if res:
                    print(acteurU + " est bien à une distance "+str(distance)+" de "+acteurV+"\n")
                else:
                    print(acteurU + " n'est pas à une distance "+str(distance)+" de "+acteurV+"\n")
                    
                return True
            case "4":
                acteurV=input("entrez un acteur différent de "+acteurU+" pour calculer leur distance\n")
                res = requetes.distance(json_vers_nx,acteurU,acteurV)
                if res!=None:
                    print("La distance entre "+ acteurU + " et " + acteurV+ " est de "+ str(res))
                else:
                    return None
                return True
            case "5":
                res = requetes.centralite(json_vers_nx,acteurU)
                if res == None:
                    print(acteurU+ " est incconu")
                    return None
                print("Le plus grand éloignement de "+acteurU+ " avec un autre acteur est "+str(res))
                return True
            case "6":
                print("L'acteur de plus central d'hollywood, c'est-à-dire le moins éloigné, est "+ requetes.centre_hollywood(json_vers_nx))
                return True
            case "7":
                print("La distance de l'acteur le moins central, c'est-à-dire le plus éloigné, est "+str(requetes.eloignement_max(json_vers_nx)))
                return True
            case _:
                print("Votre proposition n'est pas dans les choix")
                
                return None

def explication():
    explication= input("Dans le cadre de notre SAé 2.02, nous vous proposons de réaliser divers calculs autour du jeu des six degrés de Bacon ! Voulez-vous plus d'explication ?(Oui/Non) \n");
    if explication.lower() == "oui":
        print("Très bien, le jeu a pour but est de relier un acteur quelconque à Kevin Bacon par six partenaires de cinéma au maximum. \n Le degré de séparation d'un acteur est caractérisé par un Bacon number, Kevin Bacon "+
                        "a un Bacon de number de lui-même de 0.  \n Le Bacon number d'un acteur A ayant tourné directement avec Kevin Bacon est 1. \n "+
                        "Puis l'acteur B direct à l'acteur A a un Bacon number de 2 etc. \n Nous vous proposons donc de réaliser divers calculs de distance, d'acteurs communs etc.\n")
    return 1


# programme principal permettant de lancer l'application
def programme_principal():
    """le programme principal lançant l'application
    """
    try:
        explication()
        
    
        json_vers_nx=chemin()
        if json_vers_nx == None:
            return "Veuillez relancer le programme, le nom du fichier génère une erreur"
        acteurU=input("Donnez le nom d'un acteur\n")
        continuer=True
        tour = 0
        while continuer and tour<100:
            choix_programme(json_vers_nx,acteurU)
            tour += 1
            continuerCalculs = input("Voulez-vous continuer le calculs ? Oui/Non\n")
            if continuerCalculs.lower() == "non" or continuerCalculs.lower() != "oui":
                return "À bientôt !"
            chgmntActeur = chgmntActeurU(acteurU)
            if chgmntActeur != None:
                acteurU = chgmntActeur

        if  tour == 100:
            return "Vous avez effectué beaucoup de calculs ! Redémarrez le programme pour en refaire de nouveau."
        return "À bientôt !"
    except ValueError:
        return "une erreur est survenue, veuillez relancer le programme"


print(programme_principal())