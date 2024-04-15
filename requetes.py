import networkx as nx
import json
import matplotlib.pyplot as plt


def json_vers_nx(chemin):
    graphe = nx.Graph()
    try : 
        fic = open(chemin)
        print('ok')
        lignes = fic.read().split("\n")
        print('ok')
        acteurPrec = "[[Kevin Bacon]]"
        graphe.add_node('[[Kevin Bacon]]')
        grapheListe = ["[[Kevin Bacon]]"]
        for i in range(0, len(lignes)-1):
            ligneDico = json.loads(lignes[i])
            for acteur in ligneDico["cast"]:
                grapheListe.append(acteur)
        j = 0
        while j<len(grapheListe):
            acteurPrec = grapheListe[j]
            for i in range(0, len(lignes)-1):
                ligneDico = json.loads(lignes[i])
                if (acteurPrec in ligneDico["cast"]):
                        for acteur in ligneDico["cast"]:
                            graphe.add_edge(acteur, acteurPrec)
                
        print("lignes")
        #graphe.remove_edge('[[Kevin Bacon]]', '[[Kevin Bacon]]')
        plt.clf()
        nx.draw(graphe)
        plt.show()
    except FileNotFoundError:
        return 0

print(json_vers_nx("data.txt"))