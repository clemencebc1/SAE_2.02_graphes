import networkx as nx 
import matplotlib as plt
import requetes 
from tkinter import * 

G = requetes.json_vers_nx("data_100.txt")
 
fenetre = Tk()

label = Label(fenetre, text="Oracle de Bacon")
label.pack()

value = StringVar()
value.set("Kevin Bacon")
acteur1 = Entry(fenetre, textvariable=value, width=20)
acteur1.pack()

acteur2 = Entry(fenetre, width=20)
acteur2.pack()
# acteur1.get() pour obtenir l'input



fenetre.mainloop()
