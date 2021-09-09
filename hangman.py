import random
from words_list import words
import string

correct_word = random.choice(words)
lives = 10
incorrect_letters = set()
correct_letters = set(correct_word)
used_correct_letters = set()
l=""
all_letters = set(string.ascii_lowercase)

while lives > 0 and len(correct_letters) > 0:
    lives = lives - 1
    user_letter = input('Enter a letter: ')

    if user_letter in correct_letters:
        correct_letters.remove(user_letter)
        used_correct_letters.add(user_letter)
        l = [letter if letter in used_correct_letters else '_' for letter in correct_word]

    else:
        incorrect_letters.add(user_letter)

    print(f"The letters you have guessed correctly so far: ", ' '.join(l))
    print(f"Incorrect letters you have used:", ','.join(incorrect_letters))
    print(f'You have {lives} lives left')

print(f"You lose. The word is {correct_word}" if lives == 0 else f'Congratulations! You have guessed the word {correct_word}')











