##The prime factors of 13195 are 5, 7, 13 and 29.

##What is the largest prime factor of the number 600851475143 ?


largest_factor = 0
i = 1
largest_prime_factor = 0
factors = []


##let's figure out if i is prime

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True                     

##only need to check up to the sqrt of the number, because any factor below the sqrt will have a mirrored factor above it and not be prime
while i < 600851475143**0.5:
    if isprime(i) == True:
        if 600851475143 % i == 0:
            largest_factor = i
            factors.append(i)
    i += 1


print largest_factor
print factors
