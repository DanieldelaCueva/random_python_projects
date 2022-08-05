def vigenere_c(message_clair, cle_orig, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Code un message selon le chiffrement de Vigenère
    """

    # convertit le message en texte, affiche une erreur s'il échoue
    try:
        message_clair = str(message_clair)
    except ValueError:
        raise ValueError("Message invalide")

    # vérifie que la clé ne contient que des lettres
    for caractere in cle_orig.upper():
        if not caractere in alphabet:
            raise ValueError("Un caractère de la clé n'appartient pas à l'alphabet. Rappel: la clé ne peut contenir que des lettres non accentuées avec Vigenère. Exceptions: ñ - non admise")

    message_code = ""

    cle = cle_orig.replace(" ", "") # supprime les espaces dans la clé

    # s'assure que la clé est assez longue pour coder le message en la répétant autat de fois que nécéssaire
    while len(cle) < len(message_clair):
        cle += cle

    k = 0 # ariable qui va contenir l'indice du caractère travaillé de la clé

    for caractere in message_clair.upper():
        if caractere in alphabet:
            # somme des indices du caractère obtenu dans l'alphabet et du caractère de la clé correspondant, modulo len(alphabet) pour obtenir son indice dans l'alphabet
            i = ( alphabet.index(caractere) + alphabet.index(cle.upper()[k]) ) % len(alphabet)
            k += 1

            message_code += alphabet[i]
        # code uniquement les caractères présents dans l'alphabet indiqué en paramètre
        else:
            message_code += caractere
    
    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Vigenère",
        "alphabet_base": alphabet,
        "chiffres_base": None,
        "cle": cle_orig,
        "message_clair": message_clair,
        "message_code": message_code
    }

def vigenere_d(message_code, cle_orig, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Décode un message selon le chiffrement de Vigenère
    """

    # convertit le message en texte, affiche une erreur s'il échoue
    try:
        message_code = str(message_code)
    except ValueError:
        raise ValueError("Message invalide")

    # vérifie que la clé ne contient que des lettres
    for caractere in cle_orig.upper():
        if not caractere in alphabet:
            raise ValueError("Un caractère de la clé n'appartient pas à l'alphabet. Rappel: la clé ne peut contenir que des lettres non accentuées avec Vigenère. Exceptions: ñ - non admise")

    message_decode = ""

    cle = cle_orig.replace(" ", "") # supprime les espaces dans la clé

    # s'assure que la clé est assez longue pour décoder le message en la répétant autat de fois que nécéssaire
    while len(cle) < len(message_code):
        cle += cle

    k = 0

    for caractere in message_code.upper():
        if caractere in alphabet:
            # différence des indices du caractère obtenu dans l'alphabet et du caractère de la clé correspondant
            i = ( alphabet.index(caractere) - alphabet.index(cle.upper()[k]) )
            # vérification: l'indice obtenu correspond à une position dans l'alphabet de len(alphabet) lettres
            if i < 0:
                i += len(alphabet)
            k += 1

            message_decode += alphabet[i]
        # décode uniquement les caractères présents dans l'alphabet indiqué en paramètre
        else:
            message_decode += caractere
    
    # retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Vigenère",
        "alphabet_base": alphabet,
        "chiffres_base": None,
        "cle": cle_orig,
        "message_code": message_code,
        "message_decode": message_decode
    }

# si le module n'est pas importé, mais exécuté
if __name__ == "__main__":
    print("Vous avez éxécuté le module Vigenère, qui contient les fonctions d'encodage et de décodage selon le code de vignère")