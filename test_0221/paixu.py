a = [1, 7, 4, 89, 34, 2]
print(len(a))
for j in range(0,len(a)-1):
    for i in range(0,len(a)-1):
        if a[i] > a[i + 1]:
            a[i] ,a[i + 1]=a[i + 1],a[i]
print(a)

