import networkx as nx
import json
import matplotlib.pyplot as plt
import matplotlib.animation as m
import random
import jupyter
from pyvis.network import Network

#Q1 6.1 

G = nx.Graph()
def json_vers_nx(chemin):
    """ convertit un fichier json en un graph networkx

    Args:
        chemin (String): le chemin du fichier json

    Returns:
        Graph: retourne un graphe avec l'ensemble des acteurs ayant collaboré avec Kevin Bacon ou les acteurs proches
    """
    try : 
        fic = open(chemin)
        lignes = fic.read().split("\n") # on découpe chacune des lignes et on les place dans une liste
        G.add_node("Kevin Bacon") # ajout du noeud principal
        j = 0 # un compteur pour s'assurer que la boucle while s'arrête
        while j<len(list(G.nodes)) and j<1000:
            acteurPrec = list(G.nodes)[j]
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
                                G.add_edge(acteur, acteurPrec)
            j+=1
        options = {
        'with_labels': True,
        'node_size': 1000,
        'node_color': "skyblue",
        'node_shape': "s", 
        'alpha': 0.5, 
        'linewidths': 10
        } 
        pos = {}
        longueur = len(list(G.nodes))/2
        x = 0
        y = 0
        for noeud in list(G.nodes):
            pos[noeud]=[x,y]
            if y>longueur:
                y = 0
                x += 15
            y += 15
        # des options pour rendre le graphe plus lisible
        plt.clf() # on efface les figures précédentes 
        nx.draw(G, pos, **options)
        plt.show()
        return G
    
    except FileNotFoundError: # si le fichier n'a pas pu s'ouvrir
        print("impossible d'ouvrir le fichier")
        return None


# Q2 6.2
def collaborateurs_communs(G,u,v):
    """ recherche l'ensemble des acteurs qui ont à la fois collaboré avec l'acteur u et l'acteur v

    Args:
        G (Graph): un graphe 
        u (String): un acteur
        v (String): un autre acteur quelconque

    Returns:
        set: une ensemble de l'ensemble des noeuds (acteurs) adjacents à la fois à u et v
    """
    if u not in list(G.nodes) or v not in list(G.nodes):
        return None
    return set(G.adj[u]).intersection(set(G.adj[v]))
        

#Q3 6.3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs




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
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    while distance<=k:
        if distance != k and v in collaborateurs_proches(G,u,distance):
            est_avant = True
        elif not est_avant and v in collaborateurs_proches(G,u,distance):
            return True
        distance += 1
    return False


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
    iteration = 0
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    sont_proches = est_proche(G,u,v,distance)
    while not sont_proches:
        distance += 1
        sont_proches = est_proche(G,u,v,distance)
    return distance



def distance(G,u,v):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
   
    Parametres:
        G: le graphe
        u: un acteur
        v: un second acteur
    """
    if u not in G.nodes or v not in G.nodes:
        print("est un illustre inconnu")
        return None
    pile = [u]
    atteint = {u:0}
    while (len(pile)>0):
        noeud_courant = pile.pop()
        for noeud in G[noeud_courant]:
            if noeud not in atteint:
                pile.append(noeud)
                atteint[noeud]=atteint[noeud_courant]+1
            elif atteint[noeud]>atteint[noeud_courant]+1:
                atteint[noeud]=atteint[noeud_courant]+1
    if v in atteint:
        return atteint[v]
                
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
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    max = 0
    for acteur in G.nodes:
        if acteur != u:
            distanceActeur = distance(G,u,acteur)
            if distanceActeur != None and distanceActeur>max:
                max = distanceActeur
    return distanceActeur

#Q5 6.5
def dicoDistance(G,u):
    """fonction non demandée mais utile, retourne un dictionnaire de distance à partir d'un acteur

    Args:
        G (Graph): un graphe
        u (String): un acteur

    Returns:
        dict: dictionnaire avec pour cle un noeud et valeur la distance avec u
    """
    if u not in G.nodes:
        print("est un illustre inconnu")
        return None
    pile = [u]
    atteint = {u:0}
    while (len(pile)>0):
        noeud_courant = pile.pop()
        for noeud in G[noeud_courant]:
            if noeud != noeud_courant:
                if noeud not in atteint:
                    pile.append(noeud)
                    atteint[noeud]=atteint[noeud_courant]+1
                elif atteint[noeud]>atteint[noeud_courant]+1:
                    atteint[noeud]=atteint[noeud_courant]+1
    return atteint

# Pour ces fonctions, il est possible d'utiliser la fonction networkx closeness_centrality(G)

def centre_hollywood(G):
    """ determine l'acteur le plus central (avec la plus petite distance avec les autres acteurs)

    Args:
        G (Graph): un graphe 

    Returns:
        String: l'acteur le plus central
    """
    min = 15 #6 degré de séparation max
    acteurCentral = ""
    listeDistance=[]
    for u in G.nodes:
        listeDistance.append(dicoDistance(G,u))
    for dico in listeDistance:
        for cle in dico:
            if dico[cle]<min:
                min = dico[cle]
                acteurCentral = cle
    return acteurCentral



def eloignement_max(G:nx.Graph):
    """ determine la plus grande distance entre deux acteurs dans le graphe

    Args:
        G (Graph): un graphe 

    Returns:
        int: la plus grande distance separant deux acteurs dans le graphe
    """
    max = 0
    listeDistance=[]
    for u in G.nodes:
        listeDistance.append(dicoDistance(G,u))
    for dico in listeDistance:
        for cle in dico:
            if dico[cle]>max:
                max = dico[cle]
    return max

#Bonus

def collaborateurs_proches_graphe(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    graphe = nx.Graph()
    graphe.add_node(u)
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    graphe.add_edge(c,voisin)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    plt.clf()
    plt.show()
    return graphe
