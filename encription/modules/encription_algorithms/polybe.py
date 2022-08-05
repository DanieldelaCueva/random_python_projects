numbers="0123456789"

def create_grid(alphabet):
    if len(alphabet) != 25:
        raise ValueError("The alphabet must me 25 letters long")

    grid = list()
    for i in range(1, 6):
        line = alphabet[5*(i-1) : (5*i)]
        grid.append(list(line))
    return grid

def polybe_c(clean_message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXY"):

    """
        Encodes following polybe's algorithm
    """

    try:
        clean_message = str(clean_message)
    except ValueError:
        raise ValueError("Invalid message")

    grid = create_grid(alphabet)

    encoded_message = ""

    for char in clean_message.upper():
        if char in alphabet:
            encoding = ""
            for line in grid:
                if char in line:
                    encoding += str(grid.index(line) + 1)
                    encoding += str(line.index(char) + 1)
                    encoded_message += encoding
        elif char in numbers:
            raise ValueError("Numbers can't be encoded with Polybe")
        else:
            encoded_message += char

    return {
        "algorithm": "Polybe",
        "base_alphabet": alphabet,
        "base_numbers": numbers,
        "key": None,
        "clean_message": clean_message,
        "encoded_message": encoded_message
    }

def polybe_d(encoded_message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXY"):

    """
        Decodes a message following Polybe's algorithm
    """

    try:
        encoded_message = str(encoded_message)
    except ValueError:
        raise ValueError("Invalid message")

    for char in encoded_message.upper():
        if char in alphabet:
            raise ValueError("Characters can't be decoded with Polybe")

    grid = create_grid(alphabet)
    clean_message = ""

    i = 0
    
    while i < len(encoded_message):
        if encoded_message[i] in numbers:
            x = int(encoded_message[i])-1
            y = int(encoded_message[i+1])-1
            clean_message += str(grid[x][y])
            i+=2
        else:
            clean_message += encoded_message[i]
            i+=1
    
    return {
        "algorithm": "Polybe",
        "base_alphabet": alphabet,
        "base_numbers": numbers,
        "cle": None,
        "encoded_message": encoded_message,
        "clean_message": clean_message
    }

if __name__ == "__main__":
    print("Polybe module")