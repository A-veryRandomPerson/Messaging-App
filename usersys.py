from user import mainmenu
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
        if answermode == "username":
            return "password"
        elif answermode == "password":
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
        if answermode == "done":
            break
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

                
        if answermode == "username":
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

    with open('users/'+username+'.json','w') as file:
        dict = {
            'username':username,
            'password':password,
            'first name':firstname,
            'last name': lastname,
            'age':age,
            'messages':{},
            'friends':[],
            'about me':""
        }
        json.dump(dict,file,indent=4)
    clear()
    print("Successfully Made Account! [any key]")
    bruh = input()


def login():
    clear()
    userspaces = "                               "
    usernamee = ""
    passwordspaces = "                               "
    passwordd = ""
    
    answermode = "username"
    answering = True
    while answering:
        clear()
        if answermode == "done":
            break
        print(blue+"╔════LOG IN═════════════════════════════════════╗") 
        print(blue+"╠═══════════════════════════════════════════════╣")
        print(blue+"║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║")
        print(blue+"║ ┃Username: "+usernamee+userspaces+"  "+"┃ ║")
        print(blue+"║ ┃Password: "+passwordd+passwordspaces+"  "+"┃ ║")
        print(blue+"║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║")
        print(blue+"╚═══════════════════════════════════════════════╝")
        print(blue+"Please input your "+answermode.title())
        key = input()
                
        if answermode == "username":
            usernamee = key
            userspaces = signupcut(usernamee)
            answermode = nxtanswermode('username',mode=2)

            
        elif answermode == "password":
            passwordd = key
            passwordspaces = signupcut(passwordd)
            answermode = nxtanswermode('password',mode=2)


    for file in os.scandir('users'):
        filename = os.path.splitext(os.path.basename(file))[0]
        if filename == usernamee:
            with open(file,'r') as user:
                userr = json.load(user)
                if userr['password'] == passwordd:
                    print(blue+"do you want the system to remember you? [Y,N]")
                    bruh = input()
                    if bruh.lower() == 'y':
                        with open('remember','w') as file:
                            file.write(f"users/{filename}.json")
                        return 'users/'+usernamee+'.json'
                    else:
                        return 'users/'+usernamee+'.json'
    print(red+"Invalid username or password, to log in again press 'L', to sign up press 'S' ")
    thing= input()
    if thing.lower() == 'l':
        login()
    elif thing.lower() == 's':
        signup()
    else:
        login()
    