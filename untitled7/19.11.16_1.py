n = int(input())
s = 0
i = 1
while i <= n:
   k = i * 2 - 1
   k = 1 / (k ** 2)
   i += 1
   if i % 2 != 0:
      s = s - k
   else:
      s = s + k
print (s)
