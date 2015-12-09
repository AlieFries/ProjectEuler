count = 0
longest_chain = 0
seed = 0

for i in range(13, 1000000):
    count = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    if count > longest_chain:
        longest_chain = count
        seed = i


print longest_chain
print seed
            
