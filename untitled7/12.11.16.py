k = int(input())
a = 2
s = ''
while a <= 9:
    x = a * k
    b = 'x'
    y = (str(a) + ' * '  + str(k) + ' = ' + str(x))
    s = s + ' ' + y
    a += 1
print (s)

