# Gmail-Clone
 a gmail clone i made just for fun :/


 usersys.py is for logging and signing up
 main is the main body of the application
 menu is the main menu when a user logs in


demo user:
{
    "username": "random user",
    "password': "jj#77^#3J",
    "first name": "bob",
    "last name": "johns",
    "age": 16,
    "messages": {
        "david":[["hello", 1], ["hello, how are you?, 2], ["im good, how about you?", 1]]
        "random dude222":[["get a better username", 1], ["no u", 2]]
    }
    "friends": []
}

message structure:
"messages": {
    "<name of user>": [ ["message", 1 if the message was for you or 2 if the message was from the other person], ["message", ...]]
}