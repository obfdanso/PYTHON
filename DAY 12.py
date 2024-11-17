# Guessing game project
    # import random
    # print("Welcome to the Guessing Game\nI am thinking of a number between 1 and 100")
    # numbers = []
    # for i in range(1,101):
    #     numbers.append(i)
    # chosen_number = random.choice(numbers)

    # def easy():
    #       attempts = 10
    #       print(f"You have {attempts} attempts to guess the number")
    #       end_game = False
    #       while not end_game:
    #             guess = int(input("Guess the number "))
    #             if guess < chosen_number:
    #                 attempts -= 1
    #                 print(f"Too low\nYou have {attempts} attempts left")

    #             if guess > chosen_number:
    #                 attempts -=1
    #                 print(f"Too high\nYou have {attempts} attempts left")
                
    #             if guess == chosen_number:
    #                 print(f"You guessed right on your { 10 - attempts}th attempt. You win")
    #                 end_game = True
    #             if attempts == 0:
    #                  print(f"You have {attempts} attempts left. You lose")
    #                  end_game = True

    # def hard():
    #     attempts = 5
    #     print(f"You have {attempts} attempts to guess the number")
    #     end_game = False
    #     while not end_game:
    #             guess = int(input("Guess the number "))
    #             if guess < chosen_number:
    #                 attempts -= 1
    #                 print(f"Too low\nYou have {attempts} attempts left")

    #             if guess > chosen_number:
    #                 attempts -=1
    #                 print(f"Too high\nYou have {attempts} attempts left")
                
    #             if guess == chosen_number:
    #                 print(f"You guessed right on your {10 - attempts}th attempt. You win")
    #                 end_game = True
    #             if attempts == 0:
    #                  print(f"You have {attempts} attempts left. You lose")
    #                  end_game = True

    # difficulty = input("Choose a difficulty. Type 'easy' or 'hard' to choose ")

    # if difficulty == 'easy':
    #      easy()
    # else:
    #      hard()


