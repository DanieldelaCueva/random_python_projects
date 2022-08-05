# importation du module externe Tkinter qui nous aide à contruire une interface graphique
from tkinter import (CENTER, RIGHT, Button, Label, OptionMenu,
                     Radiobutton, StringVar, Text, Entry, messagebox)

import os
from pathlib import Path

class Interface:
    """
        Class in which the appearance and functionnality of the interface are defined. Takes a Tk object in the constructor, as well as an encoding and a save function (saves metadata ina text file).
    """

    def __str__(self):
        return "Tk oject-based interface"
    
    def __init__(self, window, encoding, save):

        # window initialization
        self._window = window
        self._window.title("Encoder - Decoder") 
        self._window.iconbitmap(f'{Path(__file__).parent.parent.parent}\icon.ico')

        ## INTERFACE COMPONENTS

        self._instructions_message = Label(self._window, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Choose encoding methos, mode and key")
        self._instructions_message.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self._mode_selection = StringVar(self._window, "1")

        # dict containing the buttons to generate
        modes = {
            "Encoder": "1",
            "Décoder": "2"
        }

        # loop for button creation
        line = 1
        for (text, value) in modes.items():
            Radiobutton(self._window, text = text, variable = self._mode_selection, value = value, command=self.change_on_mode).grid(row = line, column=0, columnspan=4, padx=10, pady=10)
            line += 1

        # ROT13 is default
        self._method_select = StringVar(self._window, "ROT13")

        methods = ("ROT13", "CESAR'S CODE", "VIGENERE'S CODE", "POLYBE'S SQUARE")
        self._method_list = OptionMenu(self._window, self._method_select, *methods, command=self.change_on_method)
        self._method_list.grid(row = 3, column=0, columnspan=4, padx=10, pady=10)

        self._input_label = Label(self._window,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Enter a message:                                                                           ")
        self._input_label.grid(row = 4, column=0, columnspan=4, pady=5, sticky="W")

        self._input_field = Text(self._window, font=('Helvetica', 12), height=3, padx=10, pady=10)
        self._input_field.grid(row = 5, column=0, columnspan=4, padx=10, pady=2)

        self._key_value = StringVar(self._window, "")

        self._key_label = Label(self._window, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Enter encoding key:")
        self._key_input = Entry(self._window, textvariable=self._key_value)

        self._output_label = Label(self._window,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="The result is:                                                                                ")
        self._output_label.grid(row = 9, column=0, columnspan=4, pady=5, sticky="W")

        self._output_field = Text(self._window, font=('Helvetica', 12), height=3, padx=10, pady=10, state="disabled")
        self._output_field.grid(row = 12, column=0, columnspan=4, padx=10, pady=2)

        
        self._encode_button = Button(self._window, justify=CENTER, text = "Encode", command=encoding)
        self._encode_button.grid(row = 13, column=0, columnspan=4, pady=10)

        self._save_button = Button(self._window, justify=RIGHT, text = "Save", command=save)
        self._save_button.grid(row = 13, column=3, columnspan=4, pady=10)     


    
    # getters for the input, output, mode, methode, and key

    @property
    def input_content(self):
        return self._input_field.get("1.0", "end-1c")

    @property
    def output_content(self):
        return self._ouput_field.get("1.0", "end-1c")

    @property
    def mode(self):
        return self._mode_selection.get()
        
    
    @property
    def method(self):
        return self._method_select.get()

    @property
    def key(self):
        return self._key_value.get()


    # class methods
    def clean_output(self):
        self._output_field.configure(state="normal")
        self._output_field.delete("1.0", "end-1c")
        self._output_field.configure(state="disabled")


    def show_output(self, message):
        self._output_field.configure(state="normal")
        self._output_field.insert("1.0", message)
        self._output_field.configure(state="disabled")

 
    def show_alert(self, alert):
        messagebox.showerror("Error", alert)

    def change_on_mode(self):
        if self.mode == "1":
            self._instructions_message.config(text="Choose a method, mode, and key")
            self._key_label.config(text="Enter key:")
            self._encode_button.config(text="Encode")
        elif self.mode == "2":
            self._instructions_message.config(text="Choose a method, mode, and key")
            self._key_label.config(text="Enter decoding key:")
            self._encode_button.config(text="Decode")

    def change_on_method(self, *args):
        if self.method == "ROT13" or self.method == "POLYBE'S SQUARE":
            self._key_label.grid_forget()
            self._key_input.grid_forget()
        elif self.method == "CESAR'S CODE":
            self._key_label.config(text="Enter a gap number")
            self._key_label.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")
            self._key_input.grid(row = 8, column=1, columnspan=4, pady=5)
        elif self.method == "VIGENERE'S CODE":
            self._key_label.config(text="Entrez a key:")
            self._key_label.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")
            self._key_input.grid(row = 8, column=1, columnspan=4, pady=5)
    
if __name__ == "__main__":
    print("Module Interface, contains class Interface")