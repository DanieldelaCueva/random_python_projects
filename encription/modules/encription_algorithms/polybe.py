chiffres="0123456789"

def creer_grille(alphabet):
    # vérifie que l'alphabet introduit a bien une longeur de 25, arrete l'exécution sdu programme et affiche une erreur sinon
    if len(alphabet) != 25:
        raise ValueError("L'alphabet doit comporter 25 lettres")

    # construit la grille de codage (matrice) a partir de l'alphabet de 25 lettres donné
    grille = list()
    for i in range(1, 6):
        ligne = alphabet[5*(i-1) : (5*i)]
        grille.append(list(ligne))
    return grille

def polybe_c(message_clair, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXY"):

    """
        Code un message selon le chiffrement de Polybe
    """

    # convertit le message en texte, affiche une erreur s'il échoue
    try:
        message_clair = str(message_clair)
    except ValueError:
        raise ValueError("Message invalide")

    grille = creer_grille(alphabet)

    message_code = ""

    for caractere in message_clair.upper():
        if caractere in alphabet:
            codage = ""
            # cherche dans quelle ligne de la matrice de codage se trouve le caractère à coder, joint sa ligne et colonne au message
            for ligne in grille:
                if caractere in ligne:
                    codage += str(grille.index(ligne) + 1)
                    codage += str(ligne.index(caractere) + 1)
                    message_code += codage
        elif caractere in chiffres:
            # affiche une erreur si le caractère à coder est un chiffre
            raise ValueError("Les chiffres ne peuvent pas être encodés avec Polybe")
        else:
            message_code += caractere

    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Polybe",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "cle": None,
        "message_clair": message_clair,
        "message_code": message_code
    }

def polybe_d(message_code, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXY"):

    """
        Décode un message selon le chiffrement de Polybe
    """

    # convertit le message en texte, affiche une erreur s'il échoue
    try:
        message_code = str(message_code)
    except ValueError:
        raise ValueError("Message invalide")

    for caractere in message_code.upper():
        print(caractere)
        if caractere in alphabet:
            raise ValueError("Les lettres ne peuvent pas être décodées avec Polybe")

    grille = creer_grille(alphabet)
    message_decode = ""

    # la variable i sera incrémentée de 2 si sa position dans le message contient un chiffre 
    # (message_code[i]-1 et message_code[i+1]-1 seront les indices sur la matrice d'une lettre)
    # et sera incrémentée de 1 si le caractère trouvé est diférent (espace, ponctuation)
    i = 0
    
    while i < len(message_code):
        if message_code[i] in chiffres:
            # ajoute au message décodé le cactère trouvé sur la grille en fonction de ses coordonnées (indiquées sur le message codé)
            x = int(message_code[i])-1
            y = int(message_code[i+1])-1
            message_decode += str(grille[x][y])
            i+=2
        else:
            message_decode += message_code[i]
            i+=1
    
        
    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Polybe",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "cle": None,
        "message_code": message_code,
        "message_decode": message_decode
    }

# si le module n'est pas importé, mais exécuté
if __name__ == "__main__":
    print("Vous avez éxécuté le module Polybe, qui contient les fonctions d'encodage et de décodage selon le carré de polybe")