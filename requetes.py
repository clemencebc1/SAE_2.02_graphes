def json_vers_nx(chemin):
    graphe = nx.Graph()
    try : 
        fic = open(chemin)
        print('ok')
        lignes = fic.read().split("\n")
        print('ok')
        graphe.add_node("Kevin Bacon")
        j = 0
        while j<len(list(graphe.nodes)) and j<500:
            acteurPrec = list(graphe.nodes)[j]
            acteurPrecL = "[["+acteurPrec+"]]"
            acteurPrec = acteurPrec.replace('[[', '')
            acteurPrec = acteurPrec.replace(']]', '')
            for i in range(len(lignes)):
                ligneDico = json.loads(lignes[i])
                if (acteurPrec in ligneDico["cast"]) or (acteurPrecL in ligneDico["cast"]):
                        for acteur in ligneDico["cast"]:
                            acteur = acteur.replace('[[', '')
                            acteur = acteur.replace(']]', '')
                            if (acteur != acteurPrec):
                                graphe.add_edge(acteur, acteurPrec)
            j+=1
        options = {'with_labels': True,'node_size': 1000,'node_color': "skyblue",'node_shape': "s", 'alpha': 0.5, 
        'linewidths': 10}
        plt.clf()
        nx.draw(graphe, pos = nx.random_layout(graphe), **options)
        plt.show()
    except FileNotFoundError:
        print("impossible d'ouvrir le fichier")

print(json_vers_nx("data.txt"))
