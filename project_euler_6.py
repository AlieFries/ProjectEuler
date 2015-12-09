##Difference in the sum of the squares and the square of the sums for 1-100

##first get the sum and square that 
n = 1
total = 0
while n < 101:
    total += n
    n += 1
sq_of_sums = total**2

##now get all the squares and sum them
m = 1
totes = 0
while m < 101:
    totes += m**2
    m += 1

print sq_of_sums - totes
