import random
from word import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("Good job", guess, "is in the word!")
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You already guessed the word!", guess)
            elif guess!= word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word


        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats you guessed the word! You Win!")
    else:
        print("You just killed the hangman. The word was "+word+ ". Try Again! ")

def display_hangman(tries):
    stages = ["""
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |      / \\
                -
             """,
             """
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |      /
                -
             """,
             """
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |      
                -
             """,
             """
                ---------
                |       |
                |       O
                |      \\|
                |       |
                |      
                -
             """,
             """
                ---------
                |       |
                |       O
                |       |
                |       |
                |      
                -
             """,
             """
                ---------
                |       |
                |       O
                |      
                |       
                |      
                -
             """,
             """
                ---------
                |       |
                |       
                |      a
                |       
                |      
                -
             """

             ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()

