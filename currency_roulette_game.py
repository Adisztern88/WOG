import requests
from colorama import Fore
import random
import Score

api_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json"

response = requests.get(api_url)
data = response.json()
usd_to_ils_rate = round(data["usd"]["ils"],2)


def difficulty_1():
    computer_number = random.randint(1, 10)  # generate_number
    shekel = computer_number * usd_to_ils_rate
    g_number = int(input(f"Try Convert It To USD:{shekel}: "))

    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
        Score.add_score(1)
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")


def difficulty_2():
    computer_number = random.randint(10, 100)  # generate_number
    shekel = computer_number * usd_to_ils_rate
    g_number = int(input(f"Try Convert It To USD:{shekel}: "))

    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
        Score.add_score(2)
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")

def difficulty_3():
    computer_number = random.randint(100, 1000)  # generate_number
    shekel = computer_number * usd_to_ils_rate
    g_number = int(input(f"Try Convert It To USD:{shekel}: "))

    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
        Score.add_score(3)
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")
def difficulty_4():
    computer_number = random.randint(1000, 10000)  # generate_number
    shekel = computer_number * usd_to_ils_rate
    g_number = int(input(f"Try Convert It To USD:{shekel}: "))

    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
        Score.add_score(4)
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")
def difficulty_5():
    computer_number = random.randint(10000, 1000000)  # generate_number
    shekel = computer_number * usd_to_ils_rate
    g_number = int(input(f"Try Convert It To USD:{shekel}: "))

    if g_number == computer_number:
        print(Fore.GREEN + "Good job You Win!!!")
        Score.add_score(5)
    else:
        print(Fore.RED + f"Game Over-You guessed the wrong number!!!\nThe number was:{computer_number}")

