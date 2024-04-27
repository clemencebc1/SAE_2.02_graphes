import networkx as nx
import json
import matplotlib.pyplot as plt
import random

#6.1 
def json_vers_nx(chemin):
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


# 6.2
def collaborateurs_communs(acteur1, acteur2, G):
    collab2Acteurs = []
    for arete1 in G.adj[acteur1]:
        for arete2 in G.adj[acteur2]:
            if (arete1 == arete2):
                collab2Acteurs.append(arete1)
    return collab2Acteurs
        
    
print(collaborateurs_communs('Kevin Bacon', 'Dev Anand', G))

#6.3
def collaborateurs_proches(G,u,k):
    pile = [u]
    atteint = [u]
    i = 0
    while (len(pile)>0) and i<k+1:
        i += 1
        noeud_courant = pile.pop()
        print(noeud_courant)
        for noeud in G[noeud_courant]:
            if noeud not in atteint:
                pile.append(noeud)
                atteint.append(noeud)
    return atteint

print(collaborateurs_proches(G, 'Dev Anand', 2))
print(G.adj['Dev Anand'])


def est_proche(G,u,v,k=1):
    return None
def distance_naive(G,u,v):
    return None
def distance(G,u,v):
    return None
