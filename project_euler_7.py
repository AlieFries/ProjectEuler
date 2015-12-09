##find the 10001st prime

##first figure out if a number is prime
def isPrime(n):
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


##now go through numbers and count how many are prime

count = 0
num = 1
largest_prime = 0
##make sure the count is less than 10001, because that will stop othe loop once you hit a count of 10001
while count < 10001:
    if isPrime(num) == True:
        if num > largest_prime:
            largest_prime = num
        count += 1
        num += 1
    else:
        num += 1

##
print largest_prime
print num
print count
