"""Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def is_prime(n):
    for x in range(2, int(n/2)):
        if n % x == 0:
            return False
    return True

number = 600851475143

largest = 0

for n in range(0, number):
    if is_prime(n):
        largest = n

print largest
