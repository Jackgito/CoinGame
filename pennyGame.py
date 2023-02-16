import random
from datetime import datetime

import removeCoins
import bots

# Menu is the first thing the player will see when starting the game
# Here the player can start the game against AI opponent of various skills, check the rules or end the game
def menu():
    print("Welcome to Penny Game\n")
    gameState = "mainMenu"
    rules = '''
    # In penny game, there are six coin piles of different sizes.                               #
    # The first player is chosen by random.                                                     #
    # On each turn, a player must take at least one penny from one of the piles.                #
    # For example: If you wanted to remove 1 coin from the 2nd. pile, you would write "1-2"   #
    # The game continues with the next player taking their turn.                                #
    # If a player takes the last penny from the last pile, they lose the game.                  #
    '''

    while gameState == "mainMenu":
        print("What do you want to do?")
        print("1: Start")
        print("2: How to play?")
        print("3: Quit")
        choice = input()

        if choice == "1":
            choice = 0
            gameState = "startMenu"
        elif choice == "2":
            print(rules)
        elif choice == "3":
            exit
        else:
            print("Wrong input. Type only one of the numbers shown in the menu.")
    
    while gameState == "startMenu":
        print("\nChoose the difficulty")
        print("1: Easy")
        print("2: Normal")
        print("3: Hard")
        choice = input()
        if choice == "1":
            startGame("easy")
        elif choice == "2":
            startGame("normal")
        elif choice == "3":
            startGame("hard")
        else:
            print("Wrong input. Type only one of the numbers shown in the menu.")
    return


# When the player wants to start the game, startGame is called.
# The difficulty parameter decides which bot the player is going to face
def startGame(difficulty):
    coins = [1,3,5,7,9]
    random.seed(str(datetime.now()))     # Use the current time to randomize the seed
    # Determine who goes first
    if random.randint(0,1) == 0:
        currentPlayer = "bot"
        print("\nOpponent starts!")
    else:
        currentPlayer = "player"
        print("\nYou start!")

    while True:
        if currentPlayer == "player":
            if not coins:
                print("You won!")
                return
            print(coins)
            while True:
                playerInput = input()

                # Checks if the player input is valid
                if len(playerInput) == 3 and playerInput[1] == "-":
                    if playerInput[0].isnumeric() and playerInput[2].isnumeric():
                        amount = int(playerInput[0])
                        pile = int(playerInput[2]) - 1

                        if -1 < pile < len(coins):
                            if coins[pile] < amount:
                                print("You tried to remove too many coins.")
                            elif amount == 0:
                                print("You have to remove at least 1 coin.")
                            else:
                                break
                        else:
                            print("Pile " + str(pile + 1) + " doesn't exist.")
                    else:
                        print("Wrong input. Example input: '1-2' removes 1 coin from the 2nd. pile")

                else:
                    print("Wrong input. Example input: '1-2' removes 1 coin from the 2nd. pile")

            # If player input is valid, remove coins from the chosen pile
            coins = removeCoins.removeCoins(amount, pile, coins)
            print(coins)
            #removeCoins.printRemoval(amount, pile, "player")
            currentPlayer = "bot"

        # If it's not player's turn, give the turn to bot unless there are no coins left
        else:
            if not coins:
                print("You lost!")
                return
            if difficulty == "easy":
                coins = bots.easy(coins)
            elif difficulty == "normal":
                coins = bots.normal(coins)
            else:
                coins = bots.hard(coins)
            currentPlayer = "player"

menu()