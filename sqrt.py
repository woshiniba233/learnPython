def sqrt(n):
    s = n/2.0
    for i in range(10):
        s = (s + n/s)/2.0
        print s
    return s

while 1:
    s = int(input("input s : "))
    print sqrt(s)
