from .cesar import cesar_c, cesar_d

def rot13_c(clean_message):
    """
    Encodes a message following rot13 algorithm
    """

    # rot13 is cesar with a gap of 13
    result = cesar_c(clean_message, 13)


    return {
        "algorithm": "ROT13",
        "base_alphabet": result["base_alphabet"],
        "base_numbers": result["base_numbers"],
        "key": None,
        "clean_message": clean_message,
        "encoded_message": result["encoded_message"]
    }

def rot13_d(encoded_message):
    """
    Returns a message decoded following rot13 algorithm
    """

    # rot13 is Cesar with a gap of 13
    result = cesar_d(encoded_message, 13)

    return {
        "algorithm": "ROT13",
        "base_alphabet": result["base_alphabet"],
        "base_numbers": result["base_numbers"],
        "cle": None,
        "encoded_message": encoded_message,
        "clean_message": result["clean_message"]
    }


if __name__ == "__main__":
    print("ROT13 module")