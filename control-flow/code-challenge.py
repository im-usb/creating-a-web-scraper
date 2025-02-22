import random

print("Welcome to the Python Casino!")
pc_choice = random.randint(1, 50)

play = True
user_choice = 0

while play:
    user_choice = int(input("Enter a number between 1 and 50: "))
    if user_choice == pc_choice:
        print("You win!")
        play = False
    elif user_choice < pc_choice:
        if pc_choice - user_choice <= 5:
            print("Low but you are close!")
        else:
            print("Too low!")
    elif user_choice > pc_choice:
        if user_choice - pc_choice <= 5:
            print("High but you are close!")
        else:
            print("Too high!")
