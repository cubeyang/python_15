'''''''''''
for i in range(0,6):
    for j in range(0,i):
        print("*",end=' ')
    print()
'''
for i in range(1,6):
    for j in range(0,5-i):
        print(" ", end=' ')
    for m in range(0,i):
        print("*", end=' ')
        print(" ", end=' ')
    print()
