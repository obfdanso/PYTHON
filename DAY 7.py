import random
logo = '''                                         
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''                          
print(logo)

word_list = ['Hypnosis','Baguette','Pterodactyl','Archaeology', 'Fibonacci', 'Labyrinth','Xenotransplantation','Pseudopseudohypoparathyroidism','Pickle','Python']

chosen_word = random.choice(word_list)
display = []
hint = random.choice(chosen_word).lower()

for d in chosen_word:
    display += "_"
print(f"This is your hint {hint}, {display}")
lives = len(chosen_word)
endgame = False

while not endgame:
     while lives > 0:
        guess = input("Guess a letter in the chosen word\n").lower()
        letter = chosen_word[0]

        for letter in chosen_word:
            if letter == guess:
                print("Right")
            else:
                print("Wrong")

       
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(display)
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, which is wrong. You lose a life")
        if lives == 0:
            print(f"You lose. The word was {chosen_word}")
        if "_" not in display:
            endgame = True
            print("You win")