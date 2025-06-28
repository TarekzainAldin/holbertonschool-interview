#!/usr/bin/python3
"""
Module: make_change
Defines a function to determine the fewest number of coins to meet a total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Arguments:
    coins -- list of coin denominations (list of integers)
    total -- target amount (int)

    Returns:
    int -- fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
