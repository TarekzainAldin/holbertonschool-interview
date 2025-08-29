#!/usr/bin/python3
"""Prime Game - Maria and Ben"""


def isWinner(x, nums):
    """Determine the winner of each round"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    # Sieve of Eratosthenes pour compter les nombres premiers
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Pré-calcul du nombre de nombres premiers <= i
    primes_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        primes_count[i] = count

    # Simulation des parties
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
