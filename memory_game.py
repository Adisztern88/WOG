import random
import time
from colorama import Fore

def difficulty_1():
    secret_number = random.randint(1, 101) #generate_number
    print("Remember the secret number:", secret_number,end="")
    time.sleep(5)
    print("\r ")
    g_number = int(input("Try guessing the number: ")) #get_guess_from_user
    if g_number == secret_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{secret_number}")

def difficulty_2():
    secret_number = random.sample(range(1, 101), 2) #generate_number
    print("Remember the secret number:", secret_number, end="")
    time.sleep(5)
    print("\r ")
    user_guesses =[]
    for i in range(2):
        g_numbers = int(input(f"Try guessing the {i + 1}th number: ")) #get_guess_from_user
        user_guesses.append(g_numbers)

    user_guesses.sort()
    secret_number.sort()

    if user_guesses == secret_number: #compare_results
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong numbers!!!\nThe numbers were:{secret_number}")

def difficulty_3():
    secret_number = random.sample(range(1, 101), 3)
    print("Remember the secret number:", secret_number, end="")
    time.sleep(5)
    print("\r ")
    user_guesses = []
    for i in range(3):
        g_numbers = int(input(f"Try guessing the {i + 1}th number: "))
        user_guesses.append(g_numbers)

    user_guesses.sort()
    secret_number.sort()

    if user_guesses == secret_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong numbers!!!\nThe numbers were:{secret_number}")

def difficulty_4():
    secret_number = random.sample(range(1, 101), 4)
    print("Remember the secret number:", secret_number, end="")
    time.sleep(5)
    print("\r ")
    user_guesses = []
    for i in range(4):
        g_numbers = int(input(f"Try guessing the {i + 1}th number: "))
        user_guesses.append(g_numbers)

    user_guesses.sort()
    secret_number.sort()

    if user_guesses == secret_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong numbers!!!\nThe numbers were:{secret_number}")

def difficulty_5():
    secret_number = random.sample(range(1, 101), 5)
    print("Remember the secret number:", secret_number, end="")
    time.sleep(5)
    print("\r ")
    user_guesses = []
    for i in range(5):
        g_numbers = int(input(f"Try guessing the {i + 1}th number: "))
        user_guesses.append(g_numbers)

    user_guesses.sort()
    secret_number.sort()

    if user_guesses == secret_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong numbers!!!\nThe numbers were:{secret_number}")



