import os
import json
#from start import welcome

def clear():
    os.system('cls')


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

def getspaces(str, spaceSize, character=" "):
    spaces = character*(spaceSize-len(str))
    return spaces



def openDm(user,friend,filepath,friendfilepath):
    with open(friendfilepath,'r') as fileeee:
        user2 = json.load(fileeee)
    user = user
    msgspaces = getspaces(user2['username'],90, character="═")
    messaging = True
    if user['messages'][user2['username']][0][1] == 1:
        oldturn = 1
    elif user['messages'][user2['username']][0][1] == 2:
        oldturn = 2
    while messaging:
        print("\033[0;92;40m╔═════"+user2['username']+msgspaces+"╗")
        print("\033[0;92;40m║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║")
        print("\033[0;92;40m║  ┃                                                                                         ┃  ║")
        for mesnum in range(len(user['messages'][user2['username']])):
            if user['messages'][user2['username']][mesnum][1] == 1:
                username = user['username']
                color = "\033[0;33;40m"
                turn = 1
            elif user['messages'][user2['username']][mesnum][1] == 2:
                username = user2['username']
                color = "\033[0;34;40m"
                turn = 2
            message = user['messages'][user2['username']][mesnum][0]
            fullstr = color+"("+username+"): "+message
            spaces = getspaces(fullstr,98)
            print("\033[0;92;40m║  ┃ "+"\033[0;37;40m"+fullstr+spaces+"\033[0;92;40m"+"┃  ║")
            if turn != oldturn:
                #print("\033[0;92;40m║  ┃                                                                                         ┃  ║")
                oldturn = turn
        print("\033[0;92;40m║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║")
        print("\033[0;92;40m╚═══════════════════════════════════════════════════════════════════════════════════════════════╝")
        print("\033[0;34mType a message to send or type '$mainmenu' to return to the main menu: ")
        inputt = input()
        if inputt.lower().rstrip() == '$mainmenu':
            messaging = False
            with open(filepath, 'w') as userfile, open(friendfilepath, 'w') as friendfile:
                json.dump(user,userfile,indent=4)
                json.dump(user2,friendfile,indent=4)
            mainmenu(filepath)
            return ""
        else:
            user['messages'][user2['username']].append([inputt,1])
            user2['messages'][user['username']].append([inputt,2])
        clear()
        

def listmessages(user,filepath):

    print("\033[0;92;40m╔═════DMs═══════════════════════════════════════════════════════════════════════════════════════╗")
    print("\033[0;92;40m║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║")
    for friend in user['messages'].keys():
        spaces = getspaces(friend,89)
        print("\033[0;92;40m║  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ║")
        print("\033[0;92;40m║  ┃"+"\033[0;37;40m"+friend+spaces+"\033[0;92;40m"+"┃  ║")
        print("\033[0;92;40m║  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ║")
    print("\033[0;92;40m║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║")
    print("\033[0;92;40m╚════════View Messages[V]════View Friends[A]════Log Out[L]════Quit[Q]════Profile[P]═════════════╝")
    print("\033[0;34mPlease enter a friend name to view their direct messages or type View Messages[V] View Friends[A] Log Out[L] Quit[Q] Profile[P] mainmenu[$mainmenu]")
    inputt = input()
    if inputt.lower() .rstrip() == 'v':
        listmessages(user,filepath)
    elif inputt.lower().rstrip() == 'a':
        friends(user,filepath)
    elif inputt.lower().rstrip() == 'l':
        logout(user,filepath)
    elif inputt.lower().rstrip() == 'q':
        quitt(user,filepath)
    elif inputt.lower().rstrip() == 'p':
        profile(user,filepath)
    elif inputt.lower().rstrip() == '#mainmenu':
        mainmenu(filepath)
        return ""
    else:
        for friend in user['messages'].keys():
            print(f"friend??inputt? {friend}??{inputt},, {type(friend)} {type(inputt)}")
            if friend == inputt:
                """for userr in os.scandir('users'):
                    filename = os.path.splitext(os.path.basename(userr))[0]
                    if filename == friend:
                        frienduserfilepath = 'users/'+friend+'.json'"""
                frienduserfilepath = 'users/'+friend+'.json'
                openDm(user,friend,filepath,frienduserfilepath)
                break
    #clear()
    print(red+"The Friend you named could not be found! please enter your friend's name again with correct capitalization")
    listmessages(user,filepath)

#╚╔═║╝╗━┃┗┣┛┫┓┏
def profile(user,filepath,frienduser={},friendfilepath=""):
    bluee = "\033[0;94;40m"
    if frienduser == {}:
        spaces = [getspaces(user['username'],72),getspaces(user['password'],72),getspaces(user['first name'],70),getspaces(user['age'],77),getspaces(user['about me'],72)]

        print(bluee+"╔════Profile════════════════════════════════════════════════════════════════════════════╗")
        print(bluee+"║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║")
        print(bluee+"║ ┃Username: "+white+user['username']+spaces[0]+"┃ ║")
        print(bluee+"║ ┃Password: "+white+user['password']+spaces[1]+"┃ ║")
        print(bluee+"║ ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ║")
        print(bluee+"║ ┃First Name: "+white+user['first name']+spaces[2]+"┃ ║")
        print(bluee+"║ ┃Last Name: "+white+user['last name']+spaces[3]+"┃ ║")
        print(bluee+"║ ┃Age: "+white+user['age']+spaces[4]+"┃ ║")
        print(bluee+"║ ┃About Me: "+white+user['about me']+spaces[5]+"┃ ║")
        print(bluee+"║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║")
        print(bluee+"╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        print(red+"Change Password[#P] Change Username[#U] Add or edit About me[#A] exit to main menu[$mainmenu] view friends[$friends]")
    elif frienduser != {}:
        spaces = [getspaces(frienduser['username'],72),frienduser(user['password'],72),frienduser(user['first name'],70),frienduser(user['age'],77),frienduser(user['about me'],72)]

        print(bluee+"╔════Profile════════════════════════════════════════════════════════════════════════════╗")
        print(bluee+"║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║")
        print(bluee+"║ ┃Username: "+white+frienduser['username']+spaces[0]+"┃ ║")
        print(bluee+"║ ┃Password: "+white+frienduser['password']+spaces[1]+"┃ ║")
        print(bluee+"║ ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ║")
        print(bluee+"║ ┃First Name: "+white+frienduser['first name']+spaces[2]+"┃ ║")
        print(bluee+"║ ┃Last Name: "+white+frienduser['last name']+spaces[3]+"┃ ║")
        print(bluee+"║ ┃Age: "+white+frienduser['age']+spaces[4]+"┃ ║")
        print(bluee+"║ ┃About Me: "+white+frienduser['about me']+spaces[5]+"┃ ║")
        print(bluee+"║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║")
        print(bluee+"╚═══════════════════════════════════════════════════════════════════════════════════════╝")

        print(red+"exit to main menu[$mainmenu] view friends[$friends]")
    inputt = input(white)
    if inputt.lower()=='#P':
        print(green+"\nWhat do you want your new password to be? ($quit to return)")
        inputtt = input(white)
        if inputtt.lower()=="$quit":
            clear()
            profile(user,filepath)
        else:
            user['password'] = inputtt
            print('\n')
            print("Successfully changed password!")
            profile(user,filepath)
    elif inputt.lower()=='#U':
        print(green+"\nWhat do you want your new username to be? ($quit to return)")
        inputtt = input(white)
        if inputtt.lower()=="$quit":
            clear()
            profile(user,filepath)
        else:
            user['username'] = inputtt
            print('\n')
            print(f"Successfully changed username to {user['username']}!")
            profile(user,filepath)
    elif inputt.lower()=='#a':
        print(green+"\nWhat do you want your new about me to be? ($quit to return)")
        inputtt = input(white)
        if inputtt.lower()=="$quit":
            clear()
            profile(user,filepath)
        else:
            user['about me'] = inputtt
            print('\n')
            print(f"Successfully changed about me to {user['about me']}!")
            profile(user,filepath)
    elif inputt.lower()=="$mainmenu":
        if frienduser == {}:
            with open(filepath,'w') as file:
                json.dump(user,file,indent=4)
            clear()
            mainmenu(filepath)
        else:
            clear()
            mainmenu(filepath)
    elif inputt.lower()=="$friends":
        if frienduser == {}:
            with open(filepath,'w') as file:
                json.dump(user,file,indent=4)
            clear()
        else:
            clear()
            friends(user,filepath)





def friends(user,filepath):
    clear()
    print(blue+"Your Current Friends: ")
    for friend in user['friends']:
        print(green+friend+", ",end="")
    print()
    print(blue+"Enter the name of a friend to view their profile, enter $addfriend to add a friend or enter $mainmenu to go back to main menu")
    inputt = input(white)
    if inputt == '$mainmenu':
        mainmenu(filepath)
        return ""
    if inputt == "$addfriend":
        print(blue+"Enter the username of the person you would like to add as a friend, type $return to return")
        inputtt = input(white)
        if inputtt.lower() == '$return':
            friends(user,filepath)
        else:
            for userbruh in os.scandir('users'):
                filename = os.path.splitext(os.path.basename(userbruh))[0]
                print("filename == "+filename+" filename.type= "+ str(type(filename)))
                print(f"filename == inputt ??? {filename} = {inputtt}")
                if filename == inputtt:
                    print(f"filename == inputt == {filename} = {inputtt} SUCCESS")
                    frienduser = 0
                    user = user
                    with open('users/'+filename+'.json','r') as fruser, open(filepath,'r') as ouuser:
                        frienduser = json.load(fruser)
                        print(f'frienduser"{frienduser}')
                        print(f'user{user}')
                        print(f"frienduser 'friends' {frienduser['friends']}, frienduser 'messages' {frienduser['messages']}")
                        print(f"user 'friends' {user['friends']}, user 'messages' {user['messages']}")
                        user['friends'].append(frienduser['username'])
                        frienduser['friends'].append(user['username'])
                        user['messages'][frienduser['username']] = []
                        frienduser['messages'][user['username']] = []
                        print(f"NEW frienduser 'friends' {frienduser['friends']}, frienduser 'messages' {frienduser['messages']}")
                        print(f"NEW user 'friends' {user['friends']}, user 'messages' {user['messages']}")
                        print(blue+"Successfully added "+frienduser['username']+" as a friend")
                        print("main menu[$mainmenu] friends[$friends] message your new friend[$message]")
                    with open('users/'+ filename+'.json','w') as fruser1, open(filepath,'w') as ouuser1:
                        print(f"NEW frienduser 'friends' {frienduser['friends']}, frienduser 'messages' {frienduser['messages']}")
                        print(f"NEW user 'friends' {user['friends']}, user 'messages' {user['messages']}")
                        json.dump(frienduser,fruser1)
                        json.dump(user,ouuser1)
                        broimlitearlysocool = input()
                        if broimlitearlysocool == '$mainmenu':
                            mainmenu(filepath)
                            return ""
                        elif broimlitearlysocool == '$message':
                            openDm(user,frienduser,filepath,'users/'+filename+'.json')
                        else:
                            friends(user,filepath)
            print(red+"The username you inputed could not be found! continue[$continue] main menu[$mainmenu]")
            bruh = input(white)
            if bruh.lower() == '$mainmenu':
                mainmenu(filepath)
            else:   
                friends(user,filepath)
    else:
        for user in os.scandir('users'):
            filename = os.path.splitext(os.path.basename(user))[0]
            print("filename == "+filename+" filename.type= "+ str(type(filename)))
            print(f"filename == inputt ??? {filename} = {inputt}")
            if filename == inputt:
                with open('users/'+filename+'.json', 'r') as frienddict:
                    profile(user,filepath,frienddict,'users/'+filename+'.json')
        else:
            print(red+"User could not be found!")
            friends(user,filepath)
def logout(user,filepath):
    clear()
    print(blue+"press Q to log out, press M to go back to the main menu ")
    inputt = input()
    if inputt.lower().rstrip() == 'q':
        clear()
        print(red+"Successfully logged out!")
        welcome()
    elif inputt.lower().rstrip() == 'm':
        mainmenu(filepath)
        return ""


def quitt(user,filepath):
    clear()
    print(blue+'press Q to quit or M to return back to the main menu')
    inputt = input()
    if inputt.lower().rstrip() == 'q':
        clear()
        print(red+"Sad to see you go!")
        exit()
    elif inputt.lower().rstrip() == 'm':
        mainmenu(filepath)
        return ""


#-------------
#OUTDATED CODE
#-------------

"""
def newmessage(user,filepath):
    clear()
    print(blue+"Your Current Friends: ",end="")
    for friend in user['friends']:
        print(friend+", ",end="")
    print()
    print("With which one of your friends would you like to start a new message with? [type '$mainmenu' to go back to the main menu")
    inputt = input()
    if inputt.lower().rstrip() == '$mainmenu':
        mainmenu(filepath)
        return ""
    else:
        frienduser = ""
        for user in os.scandir('users'):
            filename = os.path.splitext(os.path.basename(__file__))[0]
            if filename == friend+'.json':
                with open('users/'+filename,'r') as user:
                    frienduser = json.load(user)
                    break
        if frienduser == "":
            print("couldent find friend,press m to return to the main menu or press c to continue")
            inputt = input()
            if inputt.lower() == 'c':
                newmessage(user,filepath)
            else:
                mainmenu(filepath)
                return ""
        for friend in user['friends']:
            if inputt == friend:
                for dm in user['messages']:
                    if dm == friend:
                        openDm(user,frienduser,filepath)
                        break
        user['messages'][frienduser['username']] = []
        clear()
        print(red+"Successfully added "+frienduser['username']+"as a friend")
        openDm(user,frienduser,filepath)
"""
#^^^^^^^^^^^^^
#OUTDATED CODE
#^^^^^^^^^^^^^




def mainmenu(filepath):
    with open(filepath, 'r') as file:
        user = json.load(file)
    spaces = [getspaces(user['username'],51)]

    print("\033[0;94;40m"+"╔═════════════════════════════════════════════════════════════════━━PYMSG━━═════════════════════════════════════════════════════════════╗")
    print("\033[0;94;40m"+"║                                                                                                                                       ║")
    print("\033[0;94;40m"+"║      _______     ____  __  _____  _____                             Welcome Back, "+user['username']+"!"+spaces[0]+"║")
    print("\033[0;94;40m"+"║     |  __ \ \   / /  \/  |/ ____|/ ____|                            What do you want to do today?                                     ║")
    print("\033[0;94;40m"+"║     | |__) \ \_/ /| \  / | (___ | |  __                                                                                               ║")
    print("\033[0;94;40m"+"║     |  ___/ \   / | |\/| |\___ \| | |_ |                            "+"\033[0;33;40m"+"(V)"+"\033[0;37;40m"+" View Messages"+"\033[0;94;40m"+"                                                 ║")
    print("\033[0;94;40m"+"║     | |      | |  | |  | |____) | |__| |                                  "+"\033[0;32;40m"+"view direct messages"+"\033[0;94;40m"+"                                        ║")
    print("\033[0;94;40m"+"║     |_|      |_|  |_|  |_|_____/ \_____|                            "+"\033[0;33;40m"+"(A)"+"\033[0;37;40m"+" View Friends"+"\033[0;94;40m"+"                                                  ║")
    print("\033[0;94;40m"+"║                                                                           "+"\033[0;32;40m"+"view and add people to your dms"+"\033[0;94;40m"+"                             ║")
    print("\033[0;94;40m"+"║                                                                     "+"\033[0;33;40m"+"(L)"+"\033[0;37;40m"+" Log Out"+"\033[0;94;40m"+"                                                       ║")
    print("\033[0;94;40m"+"║                                                                           "+"\033[0;32;40m"+"log out of your account"+"\033[0;94;40m"+"                                     ║")
    print("\033[0;94;40m"+"║                                                                     "+"\033[0;33;40m"+"(P)"+"\033[0;37;40m"+" Profile"+"\033[0;94;40m"+"                                                       ║")
    print("\033[0;94;40m"+"║                                                                           "+"\033[0;32;40m"+"View your profile and information"+"\033[0;94;40m"+"                           ║")
    print("\033[0;94;40m"+"║                                                                     "+"\033[0;33;40m"+"(Q)"+"\033[0;37;40m"+" Quit"+"\033[0;94;40m"+"                                                          ║")
    print("\033[0;94;40m"+"║                                                                           "+"\033[0;32;40m"+"close pymsg"+"\033[0;94;40m"+"                                                 ║")
    print("\033[0;94;40m"+"║                                                                                                                                       ║")
    print("\033[0;94;40m"+"╚════View Messages[V]════View Friends[A]════Log Out[L]════Quit[Q]════Profile[P]═════════════════════════════════════════════════════════╝")
    inputt = input(white)                                 
    if inputt.lower() .rstrip() == 'v':
        listmessages(user,filepath)
    elif inputt.lower().rstrip() == 'a':
        friends(user,filepath)
    elif inputt.lower().rstrip() == 'l':
        logout(user,filepath)
    elif inputt.lower().restrip() == 'q':
        quitt(user,filepath)
    elif inputt.lower().rstrip() == 'p':
        clear()
        profile(user,filepath)
    else:
        clear()
        print(red+"INVALID INPUT, Please enter a one letter input")
        mainmenu(filepath)
        return ""

    #╚╔═║╝╗━┃┗┣┛┫┓┏