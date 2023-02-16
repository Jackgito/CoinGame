import removeCoins

def findGoodPlay(coins):
    # Check if it's possible to create odd number of piles with just 1 coin in each (win)
    pileOfMany = 0
    pileIndex = 0
    if len(coins) % 2 != 0:
        for i in coins:
            if i > 1:
                pileOfMany += 1
                pileIndex = coins.index(i)
            if pileOfMany > 1:
                break
        if pileOfMany == 1:
            coins = removeCoins.removeCoins(coins[pileIndex] - 1, pileIndex, coins)
            return coins

        # Check if two or more piles have two coins
        pilesOfTwo = 0
        for i in coins:
            if i == 2:
                pilesOfTwo += 1
            else:
                pile = coins.index(i)

        if pilesOfTwo == 2 and len(coins) == 3:
            return removeCoins.removeCoins(coins[pile], pile, coins)

        elif pilesOfTwo == 3 and len(coins) == 3:
            return removeCoins.removeCoins(2, 0, coins)

    # Check if it's possible to create 1,2,3 (win)
    coinCombination = [1,2,3]
    pile = 0

    if len(coins) == 4:
        for i in coins:
            for j in coinCombination:
                if i == j:
                    coinCombination.remove(j)
                    break

        if not coinCombination: # If coinCombination is empty, it means that there are piles with sizes of 1,2,3
            helpList = []
            for i in coins:
                if i > 3:
                    pile = coins.index(i)
                    break
                else:
                    if i in helpList:
                        pile = coins.index(i)
                        break
                    else:
                        helpList.append(i)
            coins = removeCoins.removeCoins(coins[pile], pile, coins)
            return coins

        # Check if it's possible to create 2,2,2,2 (win)
        pilesOfTwo = 0
        for i in coins:
            if i == 2:
                pilesOfTwo += 1
            elif i > 2:
                pile = coins.index(i)
        if pilesOfTwo == 3:
            coins = removeCoins.removeCoins(coins[pile] - 2, pile, coins)
            return coins

        # Check if it's possible to create 1,1,2,2 (win)
        pilesOfOne = 0
        pilesOfTwo = 0
        for i in coins:
            if i == 1:
                pilesOfOne += 1
            elif i == 2:
                pilesOfTwo += 1
            else:
                pile = coins.index(i)

        if ((0 < pilesOfOne < 3) and (0 < pilesOfTwo < 3) and (pilesOfOne + pilesOfTwo == 3)):
            if pilesOfOne == 1:
                coins = removeCoins.removeCoins(coins[pile] - 1, pile, coins)
            else:
                coins = removeCoins.removeCoins(coins[pile] - 2, pile, coins)
            return coins

    if len(coins) == 3:
        twoOutOfThree = 0
        # Check if the sum of the coin piles is more than 6
        # If it's less, it's impossible to achieve 1,2,3
        sum = 0
        for i in coins:
            sum += i
            if i in coinCombination:
                twoOutOfThree += 1
                coinCombination.remove(i)

        # If it's possible to achieve 1,2,3 check what pile needs to be changed
        helpList = []
        if sum > 5 and twoOutOfThree == 2:
            for i in coins:
                if i > 3:
                    pile = coins.index(i)
                    break
                else:
                    if i in helpList:
                        pile = coins.index(i)
                        break
                    else:
                        helpList.append(i)

            amount = coins[pile] - coinCombination[0]
            coins = removeCoins.removeCoins(amount, pile, coins)
            return coins


    # Endgame strategy
    if len(coins) == 2:
        # If pile has only 1 coin, remove all coins from the other pile
        if ((coins[0] == 1 or coins[1] == 1) and coins[0] != coins[1]):
            for i in coins:
                if i == 1 and coins.index(i) == 0:
                    coins = removeCoins.removeCoins(coins[1], 1, coins)
                    return coins
                elif i == 1 and coins.index(i) == 1:
                    coins = removeCoins.removeCoins(coins[0], 0, coins)
                    return coins

        # If one pile has 2 coins, remove coins until other pile has also 2 coins
        sum = 0
        for i in coins: # Check if coin sum is more than 4
            sum += i
        if ((coins[0] == 2 or coins[1] == 2) and coins[0] != coins[1] and sum > 4):
            for i in coins:
                if i == 2 and coins.index(i) == 0:
                    coins = removeCoins.removeCoins(coins[1] - 2, 1, coins)
                    return coins
                elif i == 2 and coins.index(i) == 1:
                    coins = removeCoins.removeCoins(coins[0] - 2, 0, coins)
                    return coins
    return None