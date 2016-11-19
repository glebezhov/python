n = int(input())
s = 0
i = 1
while i <= n:
    k = 1 / i
    print ('k =', k)
    s = s + k
    print ('s =', s)
    i += 1
print (s)
