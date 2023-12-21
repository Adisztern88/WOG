import random
from colorama import Fore

def difficulty_1():
    computer_number = random.randint(1, 10)  # generate_number
    g_number = int(input("Try guessing the number: "))  # get_guess_from_user
    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")

def difficulty_2():
    computer_number = random.randint(10, 100)  # generate_number
    g_number = int(input("Try guessing the number: "))  # get_guess_from_user
    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")

def difficulty_3():
    computer_number = random.randint(100, 1000)  # generate_number
    g_number = int(input("Try guessing the number: "))  # get_guess_from_user
    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")


def difficulty_4():
    computer_number = random.randint(1000, 10000)  # generate_number
    g_number = int(input("Try guessing the number: "))  # get_guess_from_user
    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")


def difficulty_5():
    computer_number = random.randint(100000, 1000000)  # generate_number
    g_number = int(input("Try guessing the number: "))  # get_guess_from_user
    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")



