import random
r=random.randint(1,9)
print(r)
n=int(input("请输入一个数字："))
if n>r:
    print("bigger")
elif n<r:
    print("less")
else:
    print("equal")