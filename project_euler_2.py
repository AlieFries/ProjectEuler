##Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
##1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fibonacci = [1,2]
even_fib = [2]
total = 2
a = 1
b = 2
c = 0

while c < 4000000:
    c = a + b
    a = b
    b = c
    fibonacci.append(c)
    if c % 2 == 0:
        even_fib.append(c)
        total += c

print total
    
