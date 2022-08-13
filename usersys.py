
import os
import json

red = "\033[0;31m"
blue = "\033[0;34m"

def signupcut(str):
    number = len(str)
    number = 31-number
    string = ""
    string = " "*number
    return string

def nxtanswermode(answermode,mode=0):
    if mode == 0:
        if answermode == "username":
            return "password"
        elif answermode == "password":
            return "first name"
        elif answermode == "first name":
            return "last name"
        elif answermode == "last name":
            return "age"
        elif answermode == "age":
            return "done"
    if mode == 1:
        answermode = answermode + ' '
    if mode == 2:
        if answermode == "user":
            return "pass"
        elif answermode == "pass":
            return "done"

def clear():
    os.system('cls')

def backspace(str):
    str = str.rstrip(str[-1])
    return str


def signup():
    clear()
    print(blue+"Hello New User! Answer the questions bellow and press enter once your done to Register!")

    userspaces = "                               "
    username = ""
    passwordspaces = "                               "
    password = ""
    firstspaces = "                               "
    firstname = ""
    lastspaces = "                               "
    lastname = ""
    agespaces = "                               "
    age = ""

    answering = True
    answermode = "username"
    while answering:
        clear()
        print(blue + "Hello New User! Answer the questions below to make a new account\n")
        print(blue+"╔════SIGN UP════════════════════════════════════╗")
        print(blue+"╠═══════════════════════════════════════════════╣")
        print(blue+"║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║")
        print(blue+"║ ┃Username: "+username+userspaces+"  "+"┃ ║")
        print(blue+"║ ┃Password: "+password+passwordspaces+"  "+"┃ ║")
        print(blue+"║ ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ║")
        print(blue+"║ ┃First Name: "+firstname+firstspaces+"┃ ║")
        print(blue+"║ ┃Last Name: "+lastname+lastspaces+" "+"┃ ║")
        print(blue+"║ ┃Age: "+age+agespaces+"       "+"┃ ║")
        print(blue+"║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║")
        print(blue+"╚═══════════════════════════════════════════════╝")
        print(blue+"Please input a "+answermode.title())
        key = input()
        if answermode == "done":
            answering = False

                
        elif answermode == "username":
            username = key
            userspaces = signupcut(username)
            answermode = nxtanswermode('username')

            
        elif answermode == "password":
            password = key
            passwordspaces = signupcut(password)
            answermode = nxtanswermode('password')

        elif answermode == "first name":
            firstname = key
            firstspaces = signupcut(firstname)
            answermode = nxtanswermode('first name')
            
        elif answermode == "last name":
            lastname = key
            lastspaces = signupcut(lastname)
            answermode = nxtanswermode('last name')
            
        elif answermode == "age":
            age = key
            agespaces = signupcut(age)
            answermode = nxtanswermode('age')

    with open('users/'+username+'.json') as file:
        dict = {
            'username':username,
            'password':password,
            'first name':firstname,
            'last name': lastname,
            'age':age
        }
        json.dump(dict,file)
    clear()
    print("Successfully Made Account! [any key]")
    bruh = input()
    login()


def login():
    clear()
    userspaces = "                                 "
    username = ""
    passwordspaces = "                                 "
    password = ""
    
    answermode = "user"
    answering = True
    while answering:
        print(blue+"╔════LOG IN═════════════════════════════════════╗")
        print(blue+"╠═══════════════════════════════════════════════╣")
        print(blue+"║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║")
        print(blue+"║ ┃Username: "+username+userspaces+"┃ ║")
        print(blue+"║ ┃Password: "+password+passwordspaces+"┃ ║")
        print(blue+"║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║")
        print(blue+"╚═══════════════════════════════════════════════╝")
    
        key = getkey()
        if key == "`":
            next = nxtanswermode(answermode, mode=2)
            answermode = next
            if answermode == "done":
                answering = False

                
        elif answermode == "user":
            if key == 'Escape':
                back =backspace(username)
                username = back
                newstr = signupcut(userspaces,mode=1)
                userspaces = newstr
            else:
                username += key
                newstr = signupcut(userspaces)
                userspaces = newstr

            
        elif answermode == "pass":
            if key == 'Escape':
                back = backspace(password)
                password = back
                newstr = signupcut(passwordspaces,mode=1)
                userspaces = newstr
            else:
                password += key
                newstr = signupcut(passwordspaces)
                passwordspaces = newstr
    for file in os.scandir('users'):
        with open(file,'r') as user:
            userr = json.load(user)
            if userr['name'] == username:
                if userr['password'] == password:
                    mainmenu('users/'+username)