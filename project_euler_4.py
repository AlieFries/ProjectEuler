

def isPalindrome(n):
    n = str(n)
    length = len(n)
##check if odd or even number of digits
    if length % 2 == 0:
        middle = length/2-1
        digits = 'even'
    else:
        middle = length/2
        digits = 'odd'
##start with cases with even number of digits
##loop through pairs of digits and check if they're the same
    if digits == 'even':
        i = 0
        while i <= middle:
            if n[i] != n[(length-1)-i]:
                return False
                break
            i += 1
        return True
    if digits == 'odd':
        i = 0
        while i < middle:
            if n[i] != n[(length-1)-i]:
                return False
                break
            i += 1
        return True

##Now, look at the numbers that are the results of any 3 digit number multiplied by any other 3 digit number.
##probably apropriate to do bitwise operations :/ Looking for the largest palindrome, so start at 999*999 and work your way down, I guess
##need two loops, one that cycles through n and one outside that cycles through m

m = 999
n = 999
largest_palindrome = 0
a = 0
b = 0
while m > 99:
    n = 999
    while n > 99:
        if isPalindrome(m*n) == True:
            if m*n > largest_palindrome:
                largest_palindrome = m*n
                a = m
                b = n
            break
        else:
            n -= 1    
    m -= 1

print largest_palindrome
print largest_palindrome, "is", a, "times", b
