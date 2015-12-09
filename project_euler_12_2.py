def divisors(n):

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
    return divisors
largest_count = 0
most_factors = 0

for i in range(3, 20000):
    tri = i*(i+1)/2
    if divisors(tri) > largest_count:
        largest_count = divisors(tri)
        most_factors = tri  
    if divisors(tri) > 500:
        break
print largest_count
print most_factors

