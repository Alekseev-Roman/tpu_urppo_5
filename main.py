import random
from datetime import datetime


class Hangman:
    def __init__(self, words, mistakes=6):
        self.words = words
        self.mistakes = mistakes

    def add_word(self, words):
        if type(words) is str:
            self.words.append(words)
        elif type(words) is list:
            self.words += words
        else:
            raise 'Incorrect type of words: ' + type(words) 

    def play(self):
        inputed_letters = []
        random.seed()
        word = random.choice(self.words)
        mistakes_counter = 0

        print('The game start')
        print(f'Guess the {len(word)} letter word')
        
        while mistakes_counter <= self.mistakes:
            for char in word:
                if char in inputed_letters:
                    print(char, end='')
                else:
                    print('_', end='')
            print()


            letter = input('Input a letter: ')
            if letter not in word:
                mistakes_counter += 1
                print('You made a mistake')
            else:
                print('You are right!')
            inputed_letters.append(letter)

            if set(word) <= set(inputed_letters):
                print('You win!')
                print(f'Word: {word}')
                break

        else:
            print('You lose')
            print(f'Correct word: {word}')


if __name__ == '__main__':
    words = ['orange', 'apple', 'pear', 'cherry']
    mistakes = 4
    hangman = Hangman(words, mistakes)
    hangman.play()
