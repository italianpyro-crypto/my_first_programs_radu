def scene_start():
    print("you wake up in a strange room. Its dark. You have a flashlight and a teddy bear.")
    choice = input("what do you use?   >>>")
    if choice == "flashlight":
        return "Scene 1"
    elif choice == "teddybear":
        return "Scene 2"
    return "start"

def scene_1():
    print("the room lightens up. you see 3 doors, red, yellow, green.")
    choice2 = input("what door do you go?  >>>")
    if choice2 == "red":
        return "RedDoor"
    elif choice2 == "yellow":
        return "YellowDoor"
    elif choice2 == "green":
        return "GreenDoor"
    return "Scene1"
    
def scene_red():
    print("you go through the red door. You see a message, it says 'elppa rood'. there is a paper and a pencil. " \
    "You need to decrypt the message")
    choice3 = input("what do you write?  >>>")
    if choice3 == "apple door":
        return "magic door"
    return "RedDoor"
    
def scene_apple():
    print("You write the word, and a secret door has opened. You go there and you see a book." \
    "it says 'for you..'")
    choice4 = input("what do you do with the book?  >>>")
    if choice4 == "read":
        return "read"
    return "magic door"
    
def scene_read():
    print (" Dear Player, all of this is a dream. You are in a hospital, barely surviving. This?" \
        "This is a place you created, where no one is mean to you and bullies you. If you look around, " \
        "you will see all of your family members really loving you. All of your friend liking you. " \
        "I am telling the truth. WAKE UP")
    choice0 = input("what do you do?  >>>")
    if choice0 == "wake up":
        return "fuck"
    return "read"

def scene_fuck():
    print("you wake up in the hospital, you dont want to. U get out of bed and try to kill yourself. " \
    "You fail. You start to cry because you miss the word created by you. im sorry...")
    choice01 = input("want to start again?  >>>")
    if choice01 == "yes":
        return "start"
    elif choice01 == "no":
        exit
    return "fuck"

def scene_yellow():
    print("You go through the yellow door, and you see a guy. You cant remember his face. He asks you: ")
    choice5 = input("do you love yourself?")
    if choice5 == "yes":
        print("good")
        return "cooldoor"
    elif choice5 == "no":
        print("F-F-F-FUCK Y-Y-YOU")
        return "cooldoor"
    return "YellowDoor"
    
def scene_cool():
    print("A door opens behind the man. He says 'go'. You go and you see some cameras. you can watch them")
    choice6 = input("you want to watch it?>>>")
    if choice6 == "yes":
        return "camera"
    elif choice6 == "no":
        print("you say no, but the man puts a gun at your head and says 'watch.. it..'." \
        "you start to watch out of fear of death")
        return "camera"
    return "cooldoor"

def scene_camera():
    print("you watch the cameras. You see yourself in a hospital bed. your head starts to hurt like shit" \
    "a note is in the left corner. you can read it.")
    choice7 = input("what do you do?  >>>")
    if choice7 == "read":
        return "read"
    return "camera"
    
def scene_green():
    print("you go through the green door. You see a pair a glasses, but they look funny. you are too curious")
    choice8 = input("what do you do?  >>>")
    if choice8 == "yes":
        return "?"
    elif choice8 == "no":
        print("you still put the glasses on")
        return "?"
    return "GreenDoor"

def scene_huh():
    print("you put the glasses, and then you feel wierd. You wake up at a table, your whole family is here, your friends are there, even your gf is here" \
    "They love you, for the first time... In front of you is a gun. You feel the urgde to kill all of them.")
    choice9 = input("do you shoot them?  >>>")
    if choice9 == "yes":
        print("You shoot them all in the head")
        return "fuck"
    if choice9 == "no":
        return "good ending"
    return "?"

def scene_good():
    print("You dont kill them. It feels great knowing they love you. You forget all about the doors and then you start living your life. The truth?" \
    "You are dead. You were in a coma and you gave up and died.")
    choice10 = input("want to start again?  >>>")
    if choice10 == "yes":
        return "start"
    elif choice10 == "no":
        exit
    return "good ending"

scenes = {
    "start": scene_start
    "Scene1": scene_1
    "RedDoor" scene_red
    "magic door": scene_apple
    "read": scene_read
    "fuck": scene_fuck
    "YellowDoor": scene_yellow
    "cooldoor": scene_cool
    "camera": scene_camera
    "GreenDoor": scene_green
    "?": scene_huh
    "good ending": scene_good 
}
