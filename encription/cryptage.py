# import Tkinter for the graphical interface
import datetime, os
from tkinter import Tk
from pathlib import Path

# import class Interface from module inteface
from modules.interface.interface import Interface

from modules.encription_algorithms.rot13 import *
from modules.encription_algorithms.cesar import *
from modules.encription_algorithms.vigenere import *
from modules.encription_algorithms.polybe import *
 
def encoding():

    """
        Will show the encoded message when button is clicked
    """

    interface.clean_output()

    message = interface.input_content
    cle = interface.key

    try:
        if interface.mode == "1":
            if interface.algorithm == "ROT13":
                encoded_message = rot13_c(message)['encoded_message']
                interface.show_output(encoded_message)

            elif interface.algorithm == "CESAR'S CODE":
                encoded_message = cesar_c(message, cle)['encoded_message']
                interface.show_output(encoded_message)

            elif interface.algorithm == "VIGENERE'S CODE":
                encoded_message = vigenere_c(message, cle)['encoded_message']
                interface.show_output(encoded_message)

            elif interface.algorithm == "POLYBE'S SQUARE":
                encoded_message = polybe_c(message)['encoded_message']
                interface.show_output(encoded_message)

            else:
                interface.show_output("")
        else: 
            if interface.algorithm == "ROT13":
                decoded_message = rot13_d(message)['clean_message']
                interface.show_output(decoded_message)

            elif interface.algorithm == "CESAR'S CODE":
                decoded_message = cesar_d(message, cle)['clean_message']
                interface.show_output(decoded_message)

            elif interface.algorithm == "VIGENERE'S CODE":
                decoded_message = vigenere_d(message, cle)['clean_message']
                interface.show_output(decoded_message)

            elif interface.algorithm == "POLYBE'S SQUARE":
                decoded_message = polybe_d(message)['clean_message']
                interface.show_output(decoded_message)
    except ValueError as error:
        interface.show_alert(error)

def save():

    """
        Creates a text file with operation's metadata
    """

    date = datetime.datetime.now().strftime('%Y-%m-%d-%Hh%Mmin%Ss')
    
    file_location = f"{Path(__file__).parent}/output/{date}.txt"

    with open(file_location, 'x', encoding='utf8') as f:
        f.write('Date: ' + date)
        f.write("\n")
        if interface.mode == "1":
            f.write('Operation: Encoding')
            f.write("\n")
        else:
            f.write('Operation: Decoding')
            f.write("\n")

        f.write("algorithm: " + interface.algorithm)
        f.write("\n")
        if interface.algorithm == "VIGENERE'S CODE":
            f.write('Key: ' + interface.key)
            f.write("\n")
        if interface.algorithm == "CESAR'S CODE":
            f.write('Gap: ' + interface.key)
            f.write("\n")
        f.write('Introduced message: ' + interface.input_content)
        f.write("\n")
        f.write('Resulting message: ' + interface.output_content)


main_window = Tk()
main_window.resizable(False, False)
interface = Interface(main_window, encoding, save)

main_window.mainloop()