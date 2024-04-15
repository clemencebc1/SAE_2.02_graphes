import networkx as nx
import json 
import matplotlib as plt

def json_vers_nx(chemin):
    graphe = nx.Graph()
    try : 
        fic = open(chemin)
        dico = dict()
        print('ok')
        lignes = fic.read().split("\n")
        print('ok')
        for ligne in lignes:
            ligneDico = json.loads(ligne)
            if ("[[Kevin Bacon]]" in ligneDico["cast"]):
                for acteur in ligneDico["cast"]:
                    graphe.add_node(acteur)
        print("lignes")
        plt.clf()
        nx.draw(graphe)
    except FileNotFoundError:
        return 0

print(json_vers_nx("/home/iut45/Etudiants/o22301776/SAE_2.02_graphes/data.txt"))