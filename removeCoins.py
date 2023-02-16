# Helper function for removing coins. Pile index starts from 0
def removeCoins(amount, pile, coins):
    coins[pile] -= amount

    # If pile is empty, remove it
    if coins[pile] == 0:
        coins.remove(coins[pile])
    return coins

# Not used
def printRemoval(amount, pile, currentPlayer):
    if amount > 1:
        if currentPlayer == "player":
            print("You removed " + str(amount) + " coins from pile " + str(pile + 1))
        else:
            print("Opponent removed " + str(amount) + " coins from pile " + str(pile + 1))
    else:
        if currentPlayer == "player":
            print("You removed " + str(amount) + " coin from pile " + str(pile + 1))
        else:
            print("Opponent removed " + str(amount) + " coin from pile " + str(pile + 1))