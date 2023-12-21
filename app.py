
import colorama
import guess_game
import memory_game
import currency_roulette_game
import time

def welcome(): #Enter your name
    name = input(colorama.Fore.LIGHTBLUE_EX + "Please enter your name: ")

    print(colorama.Fore.LIGHTBLUE_EX + f"Hi {name} and welcome to the World of Games: The Epic Journey\n""Here you can find many cool games to play.")

def start_play():  #game choosing
    print(colorama.Fore.LIGHTBLUE_EX + "1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
    "2. Guess Game - guess a number and see if you chose like the computer\n"
    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    user_game_input = int(input(colorama.Fore.LIGHTBLUE_EX + "Please choose a game to play from 1-3: "))
    if user_game_input == 1:
         print(colorama.Fore.LIGHTBLUE_EX + "You choose: 1.Memory Game\n",
               colorama.Fore.CYAN + "Soon sequence of numbers will appear for 1 second and you have to guess it back")

    elif user_game_input == 2:
         print(colorama.Fore.LIGHTBLUE_EX + "You choose: 2.Guess Game\n",
               colorama.Fore.CYAN + "Guess a number and see if you chose like the computer")

    elif user_game_input == 3:
         print(colorama.Fore.LIGHTBLUE_EX + "You choose: 3.Currency Roulette\n",
               colorama.Fore.CYAN + "Try and guess the value of a random amount of USD in ILS")

    else:
         print(colorama.Fore.RED + "You wrote an unknown number, please try again")
         return(start_play())

    #choose difficult
    game_difficulty = int(input(colorama.Fore.LIGHTBLUE_EX + "Please choose game difficulty from 1 to 5 to go back choose 0: "))
    if game_difficulty == 1:
        print("You choose difficult level 1\n""Good Luck")
        print("Game Is Loading... Please Wait")
        time.sleep(2)
        if user_game_input == 1:
            memory_game.difficulty_1()
        elif user_game_input == 2:
            guess_game.difficulty_1()
        elif user_game_input == 3:
            currency_roulette_game.difficulty_1()

    elif game_difficulty == 2:
        print("You choose difficult level 2\n""Good Luck")
        print("Game Is Loading... Please Wait")
        time.sleep(2)
        if user_game_input == 1:
            memory_game.difficulty_2()
        elif user_game_input == 2:
            guess_game.difficulty_2()
        elif user_game_input == 3:
            currency_roulette_game.difficulty_2()

    elif game_difficulty == 3:
        print("You choose difficult level 3\n""Good Luck")
        print("Game Is Loading... Please Wait")
        time.sleep(2)
        if user_game_input == 1:
            memory_game.difficulty_3()
        elif user_game_input == 2:
            guess_game.difficulty_3()
        elif user_game_input == 3:
            currency_roulette_game.difficulty_3()

    elif game_difficulty == 4:
        print("You choose difficult level 4\n""Good Luck")
        print("Game Is Loading... Please Wait")
        time.sleep(2)
        if user_game_input == 1:
            memory_game.difficulty_4()
        elif user_game_input == 2:
            guess_game.difficulty_4()
        elif user_game_input == 3:
            currency_roulette_game.difficulty_4()

    elif game_difficulty == 5:
        print("You choose difficult level 5\n""Good Luck")
        print("Game Is Loading... Please Wait")
        time.sleep(2)
        if user_game_input == 1:
            memory_game.difficulty_5()
        elif user_game_input == 2:
            guess_game.difficulty_5()
        elif user_game_input == 3:
            currency_roulette_game.difficulty_5()

    elif game_difficulty == 0:
        print(colorama.Fore.MAGENTA + "You choose to go back")
        return(start_play())

    elif game_difficulty != int:
        print(colorama.Fore.MAGENTA + "You choose an invalid character")
        return(start_play())

    else:
        print(colorama.Fore.RED + "You choose an invalid number")
        return(start_play())

