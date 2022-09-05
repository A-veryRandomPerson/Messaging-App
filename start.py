import os
import json
from usersys import login,signup
from user import mainmenu

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

def clear():
    os.system('cls')

def welcome():
    clear()
    print(blue+"░██╗░░░░░░░██╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗        ████████╗░█████╗░        ██████╗░██╗░░░██╗███╗░░░███╗░██████╗░██████╗░")
    print(blue+"░██║░░██╗░░██║██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝        ╚══██╔══╝██╔══██╗        ██╔══██╗╚██╗░██╔╝████╗░████║██╔════╝██╔════╝░")
    print(blue+"░╚██╗████╗██╔╝██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░        ░░░██║░░░██║░░██║        ██████╔╝░╚████╔╝░██╔████╔██║╚█████╗░██║░░██╗░")
    print(blue+"░░████╔═████║░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░        ░░░██║░░░██║░░██║        ██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║░╚═══██╗██║░░╚██╗")
    print(blue+"░░╚██╔╝░╚██╔╝░███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗        ░░░██║░░░╚█████╔╝        ██║░░░░░░░░██║░░░██║░╚═╝░██║██████╔╝╚██████╔╝")
    print(blue+"░░░╚═╝░░░╚═╝░░╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝        ░░░╚═╝░░░░╚════╝░        ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝╚═════╝░░╚═════╝░")
    #sleep(4)
    clear()
    print(blue+"Hello User! Do you want to Log In, Sign up, or log in as remembered user?? [L,S,R]")
    inputt = input(bright_blue)
    if inputt.lower() == "s":
        signup()
        bruh = login()
        clear()
        mainmenu(bruh)
    elif inputt.lower() == "l":
        bruh = login()
        clear()
        mainmenu(bruh)
    elif inputt.lower() == 'r':
        with open('remember','r') as file:
            path = file.readline()
        mainmenu(path)
