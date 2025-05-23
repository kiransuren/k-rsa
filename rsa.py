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
    # generate the list of primes from 3 to PRIME_NUM_LIMIT
    PRIME_NUM_LIMIT = 10000
    PRIME_LIST_LENGTH = math.ceil(PRIME_NUM_LIMIT/2 - 1) # length of list is odd numbers from 3 to PRIME_NUM_LIMIT

    # initialize list of all numbers in range
    # (assume numbers are all primes)
    numbers_list = [True] * PRIME_LIST_LENGTH 

    for idx in range(0, PRIME_LIST_LENGTH):
        # check if current number has already been 
        # determined as a composite
        if(not numbers_list[idx]):
            continue

        x = 2
        # Mark multiples of current prime as composite
        while x*(2*idx+3) <= PRIME_NUM_LIMIT:
            if(x*(2*idx+3) % 2 != 0):
                # mark odd number multiples (ignore even numbers)
                numbers_list[int((x*(2*idx+3)-3)/2)] = False
            x += 1
    return numbers_list

def find_prime_list(numbers_list):
    return [2*i+3 for i, val in enumerate(numbers_list) if val]

# Generate and check prime list from sieve of eratosthenes
prime_list = find_prime_list(sieve_of_eratosthenes())
for i in prime_list:
    if(not primaility_check(i)):
        print(f"Non-prime found! {i}")

# Randomly pick 2 unique prime numbers 
p = prime_list[random.randint(0,len(prime_list)-1)]
q = prime_list[random.randint(0,len(prime_list)-1)]
while p == q:
    q = prime_list[random.randint(0,len(prime_list)-1)]
print(f"p: {p}")
print(f"q: {q}")


# Compute the modulus
n = p*q
print(f"Key Length: {n.bit_length()}")