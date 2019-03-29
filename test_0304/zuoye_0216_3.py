x=input()
a=x[0:4:2]
print(a)
b=x[4:6]
c=x[6:8]
print(b)
if b[0]=='0':
    print("{}年{}月{}日".format(a, b[1], c[1]))
else:
    print("{}年{}月{}日".format(a, b, c))


