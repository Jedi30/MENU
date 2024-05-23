
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:


              
    
    playerchoice = input("\nChoose number : \n1. For Rock, \n2. For Paper, \n3. For Scissor\n\n")

    player = int(playerchoice)

    if player < 1 | player > 3:
        sys.exit("You must enter 1, 2, 3")

    computerchoice = random.choice('123')    

    computer = int(computerchoice)

    print("You chose :" + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose : " + str(RPS(computer)).replace("RPS.", "") + '.')
    print('')

    if player == 1 and computer == 3:
        print('🥳 You win!')
    elif player == 2 and computer == 1:
        print("🥳 You Win!")
    elif player == 3 and computer == 2:
        print("🥳 You win!")
    elif player == computer:
        print("😲 Tie Game")

    else :
        print("🐍 Python Win!")

    playagain = input("\nPlay again? Y for yes or \nQ to Quit \n\n")

    if playagain.lower()== "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")    
        print("Thank you for Playing!\n")
        playagain = False

sys.exit("Bye! 👋")    
