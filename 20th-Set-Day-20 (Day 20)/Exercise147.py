#You are going to make an on-screen version of the board game “Mastermind”. The computer will automatically generate four colours from a list of possible colours (it should be possible for the computer to randomly select the same colour more than once). For instance, the computer may choose “red”, “blue”, “red”, “green”. This sequence should notbe displayed to the user. After this is done the user should enter their choice of four colours from the same list the computer used. For instance, they may choose “pink”, “blue”, “yellow” and “red”. After the user has made their selection, the program should display how many colours they got right in the correct position and how many colours they got right but in the wrong position. In the example above, it should display the message “Correct colour in the correct place: 1” and “Correct colour but in the wrong place: 1”. The user continues guessing until they correctly enter the four colours in the order they should be in. At the end of the game it should display a suitable message and tell them how many guesses they took. 

import random

def select_colors():
    colors = {'r','g','b','o','y','p','w'}
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    c3 = random.choice(colors)
    c4 = random.choice(colors)
    data = (c1,c2,c3,c4)
    return (data)
    
        

def try_it(c1,c2,c3,c4):
    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y += num
        if y > 26:
            y -= 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")

    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y -= num
        if y < 0:
            y += 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")


loop = True

while loop == True:
    print("1) Make a code")

    print("2) Decode a message")

    print("3) Exit\n")

    choice = int(input("Enter your selection: "))

    if(choice==1):
        (mess,num) = get_data()
        make_code(mess,num)
    elif(choice==2):
        (mess,num) = get_data()
        decode(mess,num)
    elif(choice==3):
        loop = False
    else:
        print("Incorrect choice")
