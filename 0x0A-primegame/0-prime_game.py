#!/usr/bin/python3
"""Module Docs"""
def isWinner(x, nums):
    """Func Doc"""
    def sieve_of_eratosthenes(n):
        """Func Doc"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime
        primes = []
        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return primes
    
    def play_game(n):
        """Func Doc"""
        primes = sieve_of_eratosthenes(n)
        multiples_removed = set()
        turn = 0  # Maria starts first, 0 -> Maria, 1 -> Ben
        
        for prime in primes:
            if prime not in multiples_removed:
                # Remove prime and its multiples
                multiples_removed.update(range(prime, n + 1, prime))
                turn = 1 - turn  # Switch turn between Maria (0) and Ben (1)
        
        # If turn is 1, it means Ben made the last move, so Maria wins
        return turn == 1
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 1:
            ben_wins += 1  # No prime numbers to choose from, Ben wins
        elif play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
