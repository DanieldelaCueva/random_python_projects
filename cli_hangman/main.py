import random
import os

def setup():
    words = []
    with open("./files/data.txt", 'r', encoding="utf-8") as f:
        for line in f:
            words.append(line.replace("\n", ""))
    chosen_word = words[random.randint(0, len(words)-1)].upper()
    
    return {
        "word": chosen_word,
        "word_length": len(chosen_word),
        "word_prompt": ["_" for i in range(len(chosen_word))]
    }

def main():
    game_data = setup()

    while list(game_data["word"]) != game_data["word_prompt"]:
        os.system("clear")
        print("Guess the word!")
        for char in game_data["word_prompt"]:
            print(char, end=" ")
        print("\n")
        
        new_letter = str(input("Enter a new letter! ")).upper()

        char_list=list(game_data["word"])
        acc = 0

        while new_letter in char_list:
            nl_index = char_list.index(new_letter)
            game_data["word_prompt"][nl_index+acc] = new_letter
            char_list = char_list[nl_index+1::]
            acc+=(nl_index+1)

    os.system("clear")
    for char in game_data["word_prompt"]:
        print(char, end=" ")
    print("\n")

    print("You won")





if __name__ == "__main__":
    main()