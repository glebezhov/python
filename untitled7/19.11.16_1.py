n = int(input())
s = 0
i = 1
while i <= n:
    k = i
    print ('k = ', k)
    k = k + 2
    print ('k = ', k)
    v = i ** 2
    print ('v = ', v)
    m = 1 / v
    print ('m = ', m)
    s = s + m
    print ('s = ', s)
    i += 2
print (s)
