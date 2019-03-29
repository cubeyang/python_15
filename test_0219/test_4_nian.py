n = int(input())
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("%d是闰年" % n)
else:
    print("%d不是闰年" % n)

