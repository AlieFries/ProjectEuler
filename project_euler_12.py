##first generate a list of triangle numbers, formula for tri numbers, n(n+1)/2

triangles = []

##for i in range(1,100):
##    num = 0
##    for a in range(1, i+1):
##        num += a
##    triangles.append(num)

##print triangles

##generate larger tris based on formula
largest_count = 0
most_factors = 0
for i in range(12000, 12500):
    tri = i*(i+1)/2
    count = 0
    for n in range(1, tri):
        if tri % n == 0:
            count += 1  
    if count > largest_count:
        largest_count = count
        most_factors = tri  
##now figure out how many factors each element of triangles has
##largest_count = 0
##tris_with_fact_count = []
##most_factors = 0
##for item in triangles:
##    count = 0
##    for n in range(1, item/2+1):
##        if item % n == 0:
##            count += 1
##    tris_with_fact_count.append([item, count])
##    if count > largest_count:
##        largest_count = count
##        most_factors = item

##print tris_with_fact_count
print largest_count
print most_factors

##compute number of factors using prime factorization

most_divisors = 0

for n in range(6, 100):
    count = 0
    if n % 2 == 0:
        n = n/2
        count += 1
    while n % 2 == 0:
        n = n/2
        count += 1
    divisors = count+1
    div = 3
    while n != 1:
        count = 0
        while n % div == 0:
            n = n/div
            count += 1
        divisors = divisors*(count + 1)
        div += 2
    if divisors > most_divisors:
        most_divisors = divisors
    ##print divisors

print most_divisors
