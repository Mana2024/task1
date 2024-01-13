import random
import hangman_diagram
word_list = ["beautiful", "apple", "potato"]
lives = 6
print("welcome to Hangman Game")
chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("guess a letter:")  # p
    for position in range(len(chosen_word)):  # 0 1 2
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("you lose")
    if '_' not in display:
        game_over = True
        print("you win")
    print(hangman_diagram.stages[lives])