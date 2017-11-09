import random
import sys

print("Hello What is your name")
playerName = input()

print("Hello " + playerName + " My Name THE GOD OF NUMBERS!!!!")

print("press 1 if you want yo play")

guess = 0
bye = 0
play =int(input())



#Start Game Function 
def playgame(p):
    if p  == 1:
        print(guessnumber(guess, playerName))
        
    

# Guess Number Function
def guessnumber(g,name):
    num = random.randint(1, 20)
    for g in range(1, 7):
        print("Guess My number between 1 and 20")
        numberguessed = int(input())
        if num < numberguessed:
            print("Your Guess is to high Please enter a new guess")
            
        elif num > numberguessed:
            print("Your Guess is to low Please enter a new guess")
            
        else:
            break
    if num == numberguessed:
        print("Your Right " + name + " my number is " + str(numberguessed) +
              " you guessed My number in " + str(g) +
              " guesses")
        print("do you want to play agian If so Press 1 Other wise press 0")  
        yes = int(input())
        if yes == 1:
            return playgame(1)
        else:
            return goodbye(0)    
    
    else:
        print("you ran out of trys " + name + " you are a turd burglar!!! HAHAHAHA!!!")
        print("do you want to play agian If so Press 1 Other wise press 0")
        yes1 = int(input())
        if yes1 == 1:
            return playgame(1)
        else:
            return goodbye(0)
        
# Exit Function
def goodbye(b):
    print("Thank you for playing press any key to exit")
    sys.exit(b)

# start game statment 
if play == 1:
    print(playgame(1))
else:
    print(goodbye(0))
