n = int(input())
s = 0
i = 1
x = 1
while i <= n:
   k = i * 2 - 1
   k = 1 / (k ** 2)
   x = x * -1
   s = s + (x * k)
   i += 1
print (s)
