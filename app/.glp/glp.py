#!/bin/python3

def generate_prime_numbers(lim):
    """
    Generates prime numbers above 100 10**100
    """
    start = 10**100
    l = []
    for num in range(start, lim):
        for n in range(2, num):
            if num % n == 0:
                print("Not found")
                break
        else:  # If the modulus is never zero, it is prime
            print(num)
    return l

test = generate_prime_numbers((10**100)+38)