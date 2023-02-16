# Input coin list. Output: updated coin list.
# Easy bot chooses random amount of coins from random pile
import removeCoins
import random
import findGoodPlay

# Removes random amount of coins from a random pile
def easy(coins):
    pile = random.randint(0, len(coins) - 1)
    amount = random.randint(1, coins[pile])
    #removeCoins.printRemoval(amount, pile, "bot")
    return removeCoins.removeCoins(amount, pile, coins)

def normal(coins):
    goodPlay = findGoodPlay.findGoodPlay(coins)
    if goodPlay != None:
        return goodPlay
    else:
        return easy(coins) # If no good plays are found, choose random

# Normal but avoids losing patterns
def hard(coins):

    goodPlay = findGoodPlay.findGoodPlay(coins)

    if goodPlay != None:
        return goodPlay
    else:
        # If no good plays were found, choose random one. If it leads to losing position try again few times
        for i in range(10):
            coinsTest = list(coins)
            pile = random.randint(0, len(coins) - 1)
            amount = random.randint(1, coins[pile])
            coinsTest[pile] -= amount
            if coinsTest[pile] == 0:
                coinsTest.remove(coinsTest[pile])
            if findGoodPlay.findGoodPlay(coinsTest) == None:
                break

        #removeCoins.printRemoval(amount, pile, "bot")
        return removeCoins.removeCoins(amount, pile, coins)