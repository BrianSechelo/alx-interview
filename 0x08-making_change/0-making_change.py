#!/usr/bin/python3
"""
Minimum Number of Coins using while loops
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    i = 0
    n = len(coins)
    while i < n and total > 0:
        while total >= coins[i]:
            total -= coins[i]
            num_coins += 1
        i += 1    
    if total == 0:
        return num_coins
    else:
        return -1
