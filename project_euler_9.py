

for b in range(1,300):
    if 1000*(500-b)%(1000-b) == 0:
        print b
        break
a = 1000*(500-b)/(1000-b)
print a, b

c = (a**2+b**2)**.5
print c
print a*b*c
