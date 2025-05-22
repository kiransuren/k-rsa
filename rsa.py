import random
import sys
import math

def primaility_check(num):
    if(num % 2 == 0 and num != 2):
        # Number is NOT prime as 2 is a factor
        return False

    for i in range(3, math.ceil(num**0.5), 2):
        if(num % i == 0):
            # Number is NOT prime as i is a factor
            return False
    
    # number is a prime
    return True

def generate_naive_large_prime():
    # Generate two large prime numbers 
    while True:
        num = random.randint(3,sys.maxsize)
        if(primaility_check(num)):
            return num

def sieve_of_eratosthenes():
    PRIME_NUM_LIMIT = math.ceil(1000000000)
    PRIME_NUM_LIMIT_ROOT = math.ceil(PRIME_NUM_LIMIT**0.5)

    # initialize list of all numbers in range
    # (assume numbers are all primes)
    numbers_list = [True] * PRIME_NUM_LIMIT_ROOT

    for i in range(1,PRIME_NUM_LIMIT_ROOT):
        # check if current number has already been 
        # determined as a composite
        if(not numbers_list[i]):
            continue
        x = 2
        # Mark multiples of current prime as composite
        while x*(i+1) <= PRIME_NUM_LIMIT_ROOT:
            numbers_list[(i+1)*x-1] = False
            x += 1
        
    return numbers_list

def find_prime_list(numbers_list):
    return [i+1 for i, val in enumerate(numbers_list) if val]

print(find_prime_list(sieve_of_eratosthenes()))

prime_list = find_prime_list(sieve_of_eratosthenes())
print(prime_list)
for i in prime_list:
    if(not primaility_check(i)):
        print(f"Non-prime found! {i}")