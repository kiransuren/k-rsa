import random
import sys
import math

'''
Implementation of the RSA Cryptosystem

References:
https://en.wikipedia.org/wiki/RSA_cryptosystem#Operation
'''

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

def gcd(a,b):
    # Calculates the greatest common divisor of two integers
    # using recursive Euclidean Algorithm
    if(a % b == 0):
        return b
    return gcd(b, a % b)

def gcde(a,b):
    # Calculates the greatest common divisor of two integers
    # using Extended Euclidean Algorithm 
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1

    while (r1 != 0):
        # Calculate quotient
        q = (r0 - (r0 % r1)) / r1 # calculate quotient

        # Calculate s
        s = s0 - q*s1
        s0 = s1
        s1 = s

        # Calculate t
        t = t0 - q*t1
        t0 = t1
        t1 = t

        # Calculate new remainder
        r = r0 - q*r1
        r0 = r1
        r1 = r

    return (r0, t0, s0)



# Generate and check prime list from sieve of eratosthenes
prime_list = find_prime_list(sieve_of_eratosthenes())
for i in prime_list:
    if(not primaility_check(i)):
        print(f"Non-prime found! {i}")

# Randomly pick 2 unique prime numbers
print("=== Choose two large prime numbers p & q ===")
p = prime_list[random.randint(0,len(prime_list)-1)]
q = prime_list[random.randint(0,len(prime_list)-1)]
while p == q:
    q = prime_list[random.randint(0,len(prime_list)-1)]
print(f"p: {p}")
print(f"q: {q}")
print("")

# Compute the modulus
print("=== Compute modulus ===")
n = p*q
print(f"Modulus: {n}")
print(f"Key Length: {n.bit_length()}")
print("\n")

# Calculate Carmicheal Totient function of modulus
lambda_modulus = int(math.fabs((p-1) * (q-1)) / gcd(p-1,q-1))  # force as integer, which it should be
print(f"Lambda of modulus (SECRET): {lambda_modulus}")

# Choose public/encryption exponent e
# use the smallest and fastest value
for i in prime_list:
    if(lambda_modulus % i != 0):
        e = i
        break
print(f"Encoding Exponent: {e}")

# Determine private/decryption exponent d using
# modular mutliplicative inverse operation
print(gcde(lambda_modulus, e))
remainder, bezout1, bezout2 = gcde(lambda_modulus, e)
# Verify procedure was done correctly 
print(math.floor(bezout1 * e + bezout2 * lambda_modulus) == remainder )

if(bezout1 < 0):
    # to get result which is positive and lower than lambda_modulus
    # use fact that |bezout1| < lambda_modulus provided by algorithm
    bezout1 = bezout1 + lambda_modulus

d = int(bezout1)
print(f"PRIVATE KEY: {d}")


### Test encryption ###
# NOTE: m must be strictly less than n
m = 3233
print(f"Test Message: {m}")
c = (m**e) % n
print(f"Encrypted ciphertext: {c}")
m_unencrypted = (c**d) % n
print(f"Unencrypted Message: {m_unencrypted}")
