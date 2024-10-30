Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
from colorama import Fore, Style, init


init(autoreset=True)

def guessing_game():
    random_number = random.randint(1, 100) 
    attempts = 0
    user_guess = None

    print(Fore.CYAN + "🎉 Welcome to the Guessing Game! 🎉")
    print(Fore.CYAN + "Try to guess the number between 1 and 100.")
    print(Fore.YELLOW + "Hint: Type 'exit' anytime to quit the game.\n")

...     while user_guess != random_number:
...         user_input = input(Fore.GREEN + "Enter your guess: ")
... 
...       
...         if user_input.lower() == "exit":
...             print(Fore.RED + "Game exited. Thank you for playing!")
...             break
... 
...       
...         if not user_input.isdigit():
...             print(Fore.RED + "🚫 Please enter a valid number!")
...             continue
... 
...         user_guess = int(user_input)
...         attempts += 1
... 
...       
...         if user_guess < random_number:
...             print(Fore.BLUE + "🔼 Too low! Try a higher number.")
...         elif user_guess > random_number:
...             print(Fore.BLUE + "🔽 Too high! Try a lower number.")
...         else:
...             print(Fore.MAGENTA + f"🎉 Congratulations! You've guessed the number in {attempts} attempts! 🎉")
...             break
... 
...    
...     if user_guess == random_number:
...         print(Fore.CYAN + "✨ Well done! Thanks for playing the Guessing Game! ✨")
...     else:
...         print(Fore.CYAN + "Thanks for playing! Come back soon!")
... 
... 
... guessing_game()
... 
... #i used chatgpt to help me with the font colours as i wanted to make mmy old code from an erlier lesson mpre user friendly but i remade this code to run better and be more userfirnedly however i couldnt figure out how to put in any music
