import networkx as nx 
import matplotlib as plt
import requetes 
from tkinter import * 

G = requetes.json_vers_nx("data_100.txt")
 
fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()
