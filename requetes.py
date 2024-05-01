import networkx as nx
import json
import matplotlib.pyplot as plt
import random

#Q1 6.1 
def json_vers_nx(chemin):
    """ convertit un fichier json en un graph networkx

    Args:
        chemin (String): le chemin du fichier json

    Returns:
        Graph: retourne un graphe avec l'ensemble des acteurs ayant collaboré avec Kevin Bacon ou les acteurs proches
    """
    graphe = nx.Graph()
    try : 
        fic = open(chemin)
        print('ok')
        lignes = fic.read().split("\n") # on découpe chacune des lignes et on les place dans une liste
        print('ok')
        graphe.add_node("Kevin Bacon") # ajout du noeud principal
        j = 0 # un compteur pour s'assurer que la boucle while s'arrête
        while j<len(list(graphe.nodes)) and j<1000:
            acteurPrec = list(graphe.nodes)[j]
            acteurPrecL = "[["+acteurPrec+"]]"
            acteurPrec = acteurPrec.replace('[[', '') # on efface la double liste dans la chaine de caracteres
            acteurPrec = acteurPrec.replace(']]', '')
            for i in range(len(lignes)-1):
                ligneDico = json.loads(lignes[i]) # on convertit la ligne str en dictionnaire
                if (acteurPrec in ligneDico["cast"]) or (acteurPrecL in ligneDico["cast"]): # si l'acteur precedent de la liste de noeud se trouve dans le casting d'un film
                        for acteur in ligneDico["cast"]: # alors on ajoute une arete entre lui et l'acteur qu'il a cotoyé
                            acteur = acteur.replace('[[', '')
                            acteur = acteur.replace(']]', '')
                            if (acteur != acteurPrec): # si ce n'est pas lui même (pas de boucle)
                                graphe.add_edge(acteur, acteurPrec)
                            
            j+=1
        options = {
        'with_labels': True,
        'node_size': 1000,
        'node_color': "skyblue",
        'node_shape': "s", 
        'alpha': 0.5, 
        'linewidths': 10
        } # des options pour rendre le graphe plus lisible
        plt.clf() # on efface les figures précédentes 
        nx.draw(graphe, pos = nx.random_layout(graphe), **options)
        plt.show()
        return graphe
    except FileNotFoundError: # si le fichier n'a pas pu s'ouvrir
        print("impossible d'ouvrir le fichier")

G = json_vers_nx("data2.txt")


# Q2 6.2
def collaborateurs_communs(G,u,v):
    """ recherche l'ensemble des acteurs qui ont à la fois collaboré avec l'acteur u et l'acteur v

    Args:
        G (Graph): un graphe 
        u (String): un acteur
        v (String): un autre acteur quelconque

    Returns:
        list: une liste de l'ensemble des noeuds (acteurs) adjacents à la fois à u et v
    """
    collab2Acteurs = []
    for arete1 in G.adj[u]:
        for arete2 in G.adj[v]:
            if (arete1 == arete2):
                collab2Acteurs.append(arete1)
    return collab2Acteurs
        
    
print(collaborateurs_communs('Kevin Bacon', 'Dev Anand', G))

#Q3 6.3
def collaborateurs_proches(G,u,k):
    """ recherche l'ensemble des acteurs qui ont collaboré à une distance k de l'acteur u

    Args:
        G (Graph): un graphe 
        u (String): un acteur
        k (int): une distance à parcourir

    Returns:
        list: une liste de l'ensemble des noeuds (acteurs) se trouvant à une distance au plus k de l’acteur
    """
    pile = [u] # l'ensemble des noeuds à parcourir
    atteint = [u] # ceux deja parcouru
    indiceP = 0
    cptK = 0
    while (len(pile)>0) and cptK<k:
        if indiceP == 0: # si l'indice du parcours à 0, on met le nombre de noeud pour une distance k dans une variable
            nbNoeudK = len(pile)
        noeud_courant = pile.pop()
        indiceP += 1
        for noeud in G[noeud_courant]:
            if noeud not in atteint: # si l'acteur n'est pas deja proche
                pile.append(noeud)
                atteint.append(noeud)
        if indiceP>nbNoeudK: # si indice superieur au nb de noeud pour k distance, cela veut dire que l'ensemble des noeuds est deja parcouru
            cptK += 1 # on augmente le compteur de distance k, pour passer à la distance suivante
            indiceP = 0
    return atteint

print(collaborateurs_proches(G, 'Dev Anand', 2))
print(G.adj['Dev Anand'])


def est_proche(G,u,v,k=1):
    """ verifie si l'acteur v est à une distance k de l'acteur u

    Args:
        G (Graph): un graphe 
        u (String): un acteur
        v (String): un autre acteur
        k (int): une distance à parcourir

    Returns:
        boolean: True si l'acteur v est bien à distance k de l'acteur u sinon False
    """
    distance = 0
    est_avant = False
    while distance<=k:
        if distance != k and v in collaborateurs_proches(G,u,distance):
            est_avant = True
        elif not est_avant and v in collaborateurs_proches(G,u,distance):
            return True
        distance += 1
    return False

print(est_proche(G, 'Dev Anand', 'Neeru Bajwa',  1))
print(est_proche(G, 'Dev Anand', 'Neeru Bajwa',  4))
print(est_proche(G, 'Dev Anand', 'Alok Nath', 1))

def distance_naive(G,u,v):
    """ determine la distance entre deux acteurs

    Args:
        G (Graph): un graphe 
        u (String): un acteur
        v (String): un autre acteur

    Returns:
        int: la distance separant deux acteurs
    """
    distance = 1
    sont_proches = est_proche(G,u,v,distance)
    while not sont_proches:
        distance += 1
        sont_proches = est_proche(G,u,v,distance)
    return distance

print(distance_naive(G, 'Dev Anand', 'Neeru Bajwa'))
print(distance_naive(G, 'Dev Anand', 'Alok Nath'))


def distance(G,u,v):
    return None

# Q4 6.4
def centralite(G,u):
    """ determine la plus grande distance que possède un acteur u avec un autre

    Args:
        G (Graph): un graphe 
        u (String): un acteur

    Returns:
        int: la plus grande distance separant l'acteur u d'un autre acteur
    """
    return None

#Q5 6.5
def centre_hollywood(G):
    """ determine la plus grande distance entre deux acteurs dans le graphe

    Args:
        G (Graph): un graphe 

    Returns:
        int: la plus grande distance separant deux acteurs dans le graphe
    """
    return None

