def vigenere_c(clean_message, original_key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Encodes a message following Vigenere's algorithm
    """

    try:
        clean_message = str(clean_message)
    except ValueError:
        raise ValueError("Invalid message")

    for char in original_key.upper():
        if not char in alphabet:
            raise ValueError("Some character in the key isn't included in the alphabet")

    encoded_message = ""

    key = original_key.replace(" ", "")

    while len(key) < len(clean_message):
        key += key

    k = 0

    for char in clean_message.upper():
        if char in alphabet:
            i = ( alphabet.index(char) + alphabet.index(key.upper()[k]) ) % len(alphabet)
            k += 1

            encoded_message += alphabet[i]
        else:
            encoded_message += char
    
    return {
        "algorithm": "Vigenère",
        "base_alphabet": alphabet,
        "base_numbers": None,
        "key": original_key,
        "clean_message": clean_message,
        "encoded_message": encoded_message
    }

def vigenere_d(encoded_message, original_key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Decodes a message following Vigenere's algorithm
    """

    try:
        encoded_message = str(encoded_message)
    except ValueError:
        raise ValueError("Invalid message")

    for char in original_key.upper():
        if not char in alphabet:
            raise ValueError("Some character in the key isn't included in the alphabet")

    clean_message = ""

    key = original_key.replace(" ", "")

    while len(key) < len(encoded_message):
        key += key

    k = 0

    for char in encoded_message.upper():
        if char in alphabet:
            i = ( alphabet.index(char) - alphabet.index(key.upper()[k]) )
            if i < 0:
                i += len(alphabet)
            k += 1

            clean_message += alphabet[i]
        else:
            clean_message += char
    
    return {
        "algorithm": "Vigenère",
        "base_alphabet": alphabet,
        "base_numbers": None,
        "key": original_key,
        "encoded_message": encoded_message,
        "clean_message": clean_message
    }

# si le module n'est pas importé, mais exécuté
if __name__ == "__main__":
    print("Vigeneres's module")