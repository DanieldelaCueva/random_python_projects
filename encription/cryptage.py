# import Tkinter for the graphical interface
import datetime, os
from tkinter import Tk
from pathlib import Path

# importat class Interface from module inteface
from modules.interface.interface import Interface

from modules.encription_algorithms.rot13 import *
from modules.encription_algorithms.cesar import *
from modules.encription_algorithms.vigenere import *
from modules.encription_algorithms.polybe import *
 
def encoding():

    """
        Will show the encoded message when button is clicked
    """

    interface.effacer_sortie()

    message = interface.get_entree()
    cle = interface.get_cle()

    try:
        if interface.get_mode() == "1":
            if interface.get_methode() == "ROT13":
                message_code = rot13_c(message)['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CODE DE CÉSAR":
                message_code = cesar_c(message, cle)['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CODE DE VIGENÈRE":
                message_code = vigenere_c(message, cle)['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CARRÉ DE POLYBE":
                message_code = polybe_c(message)['message_code']
                interface.afficher_sortie(message_code)

            else:
                interface.afficher_sortie("")
        else: 
            if interface.get_methode() == "ROT13":
                message_decode = rot13_d(message)['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CODE DE CÉSAR":
                message_decode = cesar_d(message, cle)['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CODE DE VIGENÈRE":
                message_decode = vigenere_d(message, cle)['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CARRÉ DE POLYBE":
                message_decode = polybe_d(message)['message_decode']
                interface.afficher_sortie(message_decode)
    # affiche une erreur si elle se produit
    except ValueError as error:
        interface.afficher_alerte(error)

def sauvegarder():

    """
        Fonction qui crée un fichier texte avec les métadonnées de l'opération
    """

    date = datetime.datetime.now().strftime('%Y-%m-%d-%Hh%Mmin%Ss')
    
    adresse_fichier = f"{Path(__file__).parent}/output/{date}.txt" # le fichier .txt avec les métadonnées sera enregisté dans le directoire "output", avec la date d'enregistrement comme nom de fichier

    # crée un fichier texte, y écrit les différentes métadonnées et données du codage, enfonction de la méthode également
    with open(adresse_fichier, 'x', encoding='utf8') as f:
        f.write('Date: ' + date)
        f.write("\n")
        if interface.get_mode() == "1":
            f.write('Opération: Encodage')
            f.write("\n")
        else:
            f.write('Opération: Décodage')
            f.write("\n")

        f.write("Méthode: " + interface.get_methode())
        f.write("\n")
        if interface.get_methode() == "CODE DE VIGENÈRE":
            f.write('Clé: ' + interface.get_cle())
            f.write("\n")
        if interface.get_methode() == "CODE DE CÉSAR":
            f.write('Décalage: ' + interface.get_cle())
            f.write("\n")
        f.write('Message introduit: ' + interface.get_entree())
        f.write("\n")
        f.write('Message résultant: ' + interface.get_sortie())


# création d'un objet Tk et de l'interface (objet), il sera impossible de changer les dimensions de l'interface
fenetre_principale = Tk()
fenetre_principale.resizable(False, False)
interface = Interface(fenetre_principale, encoding, sauvegarder)

# le script entre dans une boucle infine en attendant qu'un évènement se produise
fenetre_principale.mainloop()