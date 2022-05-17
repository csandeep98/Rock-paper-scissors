import random
from words import words
import string


def get_valid_words(words):
    # randomly selects a word from the list of words
    word = random.choice(words)

    while '-' or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  # gives individual letters
    alphabets = set(string.ascii_uppercase())
    used_letters = set()

    while len(word_letters) > 0:

        print('these are the words that are used till now : ',
              ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]

        print('current word : ', ''.join(word_list))
        user_word = input('enter any word : ').upper()

        if user_word in alphabets - used_letters:
            used_letters.add(user_word)
            if user_word in word_letters:
                word_letters.remove(user_word)

        elif user_word in used_letters:
            print("you have already guessed this word,pls try again letter")

        else:
            print("Invalid pls try again")


hangman()
