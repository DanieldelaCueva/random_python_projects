alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"

def cesar_c(clean_message, gap=3):

    """
    Encodes following cesar's algorithm
    """

    try:
        clean_message = str(clean_message)
    except ValueError:
        raise ValueError("Invalid message")

    try:
        gap = int(gap)
    except ValueError:
        raise ValueError("In Cesar's algorithm, key must be an integer gap")

    encoded_message = ""

    for char in clean_message.upper():
        if char in alphabet: 
            i = alphabet.index(char) 
            encoded_i = (i+gap)%26
            
            encoded_message += alphabet[encoded_i]

        elif char in numbers:
            i = numbers.index(char)
            encoded_i = (i+gap)%10
            
            encoded_message += numbers[encoded_i]
        else:
            encoded_message += char

    return {
        "algorithm": "César",
        "base_alphabet": alphabet,
        "base_numbers": numbers,
        "key": gap,
        "clean_message": clean_message,
        "encoded_message": encoded_message
    }

def cesar_d(encoded_message, gap=3):
    """
    Decodes follwoing cesar's algorithm
    """

    try:
        encoded_message = str(encoded_message)
    except ValueError:
        raise ValueError("Invalid message")

    try:
        gap = int(gap)
    except ValueError:
        raise ValueError("In Cesar's algorithm, key must be an integer gap")

    clean_message = ""

    for char in encoded_message.upper():
        if char in alphabet:
            i = alphabet.index(char)
            decoding_i = i - gap

            if decoding_i < 0:
                decoding_i += 26

            clean_message += alphabet[decoding_i]

        elif char in numbers:
            i = numbers.index(char)
            decoding_i = i-gap

            if decoding_i < 0:
                decoding_i += 10
                
            clean_message += numbers[decoding_i]
        else:
            clean_message += char

    
    return {
        "algorithm": "Cesar",
        "base_alphabet": alphabet,
        "base_numbers": numbers,
        "key": gap,
        "encoded_message": encoded_message,
        "clean_message": clean_message
    }

if __name__ == "__main__":
    print("Cesar module")
