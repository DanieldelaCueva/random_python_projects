# importation du module externe Tkinter qui nous aide à contruire une interface graphique
from tkinter import (CENTER, RIGHT, Button, Label, OptionMenu,
                     Radiobutton, StringVar, Text, Entry, messagebox)

import os
from pathlib import Path

class Interface:
    """
        Classe qui définit l'aspect et la fonctionnalité de l'interface. Elle prend un objet de type Tk en argument, ainsi qu'une fonction de codage/décodage et une fonction pour savegarder les métadonnées dans un fichier texte.
        Certains attributs de la classe commençent par "_". Ils sont supposés être privés et ne doivent pas être accédés en dehors de la classe, or le concept de règles de visibilité n'existe pas en Python. 
    """

    def __str__(self):
        return "Interface basée sur un objet Tk"
    
    def __init__(self, fenetre, codage, sauvegarder):

        """
            Contructeur de la classe, exécuté lorsque une instance est crée. Initialise les composants de l'interface.
        """

        # initialisation de la fenêtre
        self._fenetre = fenetre
        self._fenetre.title("Encodeur - Décodeur") 
        self._fenetre.iconbitmap(f'{Path(__file__).parent.parent.parent}\icone.ico') # l'icone, lors de d'installation, se trouve dans le même directoire 'cryptage' que le fichier exécutable

        ## COMPOSANTS DE L'INTERFACE

        # crée une étiquette conteant les instructions
        self._mesage_instructions = Label(self._fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Choisissez la méthode, le mode et la clé de codage")

        # place le texte à un endroit précis de la fenêtre avec la méthode grid()
        self._mesage_instructions.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # variable qui va contenir le mode de codage selectionnée, 1 (Encoder) est la valeur par défaut
        self._selection_mode = StringVar(self._fenetre, "1")

        # dicionaire contenant le texte et le numéro des boutons à générer pour les différents modes disponibles
        modes = {
            "Encoder": "1",
            "Décoder": "2"
        }

        # boucle créant les boutons indiqués dans le dictionnaire
        ligne = 1
        for (texte, valeur) in modes.items():
            Radiobutton(self._fenetre, text = texte, variable = self._selection_mode, value = valeur, command=self.changer_selon_mode).grid(row = ligne, column=0, columnspan=4, padx=10, pady=10)
            ligne += 1

        # variable qui va contenir la méthode de codage selectionnée, ROT13 est la valeur par défaut
        self._selection_methode = StringVar(self._fenetre, "ROT13")

        # tuple contenant les différentes méthodes disponibles et liste affichée, de type OptionMenu
        methodes = ("ROT13", "CODE DE CÉSAR", "CODE DE VIGENÈRE", "CARRÉ DE POLYBE")
        self._liste_de_methodes = OptionMenu(self._fenetre, self._selection_methode, *methodes, command=self.changer_selon_methode)
        
        # affiche l'outil de sélection de la méthode de codage
        self._liste_de_methodes.grid(row = 3, column=0, columnspan=4, padx=10, pady=10)

        # étiquette et champ de texte pour entrer le message à encoder/décoder
        self._label_entree = Label(self._fenetre,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Entrez le message:                                                                         ")
        self._label_entree.grid(row = 4, column=0, columnspan=4, pady=5, sticky="W")

        self._champ_entree = Text(self._fenetre, font=('Helvetica', 12), height=3, padx=10, pady=10)
        self._champ_entree.grid(row = 5, column=0, columnspan=4, padx=10, pady=2)

        # variable qui contiendra la valeur de la clé
        self._v_cle = StringVar(self._fenetre, "")

        # étiquette et champ de texte pour entrer la clé de codage
        # elles ne sont pas montrées par défaut car la méthode par défaut, rot13, ne nécessite pas de clé de codage
        self._label_cle = Label(self._fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Entrez la clé de codage:")

        self._entree_cle = Entry(self._fenetre, textvariable=self._v_cle)

        # étiquette et champ de texte où le message encodé/décodé sera affiché
        self._label_sortie = Label(self._fenetre,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Le résultat est:                                                                                ")
        self._label_sortie.grid(row = 9, column=0, columnspan=4, pady=5, sticky="W")

        self._champ_sortie = Text(self._fenetre, font=('Helvetica', 12), height=3, padx=10, pady=10, state="disabled")
        self._champ_sortie.grid(row = 12, column=0, columnspan=4, padx=10, pady=2)

        # bouton qui, actionné, appelera la fonction de codage
        self._bouton_coder = Button(self._fenetre, justify=CENTER, text = "Coder", command=codage)
        self._bouton_coder.grid(row = 13, column=0, columnspan=4, pady=10)

        # bouton qui, actionné, sauvegardera le message introduit et le résultat de son encodage/décodage
        self._bouton_sauvegarder = Button(self._fenetre, justify=RIGHT, text = "Sauvegarder", command=sauvegarder)
        self._bouton_sauvegarder.grid(row = 13, column=3, columnspan=4, pady=10)     


    
    # getters pour le message entré, la sortie, le mode, la méthode, et la clé
    def get_entree(self):
        """
            Retourne le message entré
        """
        return self._champ_entree.get("1.0", "end-1c")

    def get_sortie(self):
        """
            Retourne le message à la sortie
        """
        return self._champ_sortie.get("1.0", "end-1c")

    def get_mode(self):
        """
            Retourne le mode de codage
        """
        return self._selection_mode.get()
    
    def get_methode(self):
        """
            Retourne la méthode codage
        """
        return self._selection_methode.get()

    def get_cle(self):
        """
            Retourne la clé de codage
        """
        return self._v_cle.get()


    # méthodes de la classe
    def effacer_sortie(self):
        """
            Fonction qui efface le champ de sortie
        """
        self._champ_sortie.configure(state="normal")
        self._champ_sortie.delete("1.0", "end-1c")
        self._champ_sortie.configure(state="disabled")


    def afficher_sortie(self, message):
        """
            Fonction qui affiche le message à la sortie
        """
        self._champ_sortie.configure(state="normal")
        self._champ_sortie.insert("1.0", message)
        self._champ_sortie.configure(state="disabled")

 
    def afficher_alerte(self, alerte):
        """
            Fonction qui affiche une alerte avec un message de texte donné
        """
        messagebox.showerror("Erreur", alerte)

    def changer_selon_mode(self):
        """
            Fonction qui change l'interface en fonction du mode de codage sélectionné
        """
        if self.get_mode() == "1":
            self._mesage_instructions.config(text="Choisissez la méthode, le mode et la clé de codage")
            self._label_cle.config(text="Entrez la clé de codage:")
            self._bouton_coder.config(text="Coder")
        elif self.get_mode() == "2":
            self._mesage_instructions.config(text="Choisissez la méthode, le mode et la clé de décodage")
            self._label_cle.config(text="Entrez la clé de décodage:")
            self._bouton_coder.config(text="Décoder")

    def changer_selon_methode(self, *args):
        """
            Fonction qui change l'interface en fonction de la méthode de codage sélectionnée
        """
        if self.get_methode() == "ROT13" or self.get_methode() == "CARRÉ DE POLYBE":
            self._label_cle.grid_forget()
            self._entree_cle.grid_forget()
        elif self.get_methode() == "CODE DE CÉSAR":
            self._label_cle.config(text="Entrez le décalage:")
            self._label_cle.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")
            self._entree_cle.grid(row = 8, column=1, columnspan=4, pady=5)
        elif self.get_methode() == "CODE DE VIGENÈRE":
            self._label_cle.config(text="Entrez la clé de codage:")
            self._label_cle.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")
            self._entree_cle.grid(row = 8, column=1, columnspan=4, pady=5)
    
# si le module n'est pas importé, mais exécuté
if __name__ == "__main__":
    print("Vous avez exécuté le module Interface, qui contient la classe Interface")