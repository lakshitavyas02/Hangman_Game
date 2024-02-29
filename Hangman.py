import random 
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
print(logo)
ans_list = []
for char in chosen_word:
    ans_list += "_"
end_game = False
while not end_game:
    guess = input("guess a letter: ").lower()
    if guess in ans_list:
        print(f"You have already guessed the letter {guess}.")
    for pos in range(len(chosen_word)):
        char = chosen_word[pos]
        if char == guess:
            ans_list[pos] = char
    if guess not in chosen_word:
        print(f"You guessed {guess},that is not in the word. You lose a life")
        lives -= 1
        if lives==0:
            end_game = True
            print("you lose!")
    print(f"{' '.join(ans_list)}")    
    if "_" not in ans_list:
        end_game = True
        print("you win!")
    print(stages[lives])