#huash12
sum=0
for i in range(1, 5):
    for j in range(1, 5):
        for z in range(1, 5):
            if i != j and i != z and j != z:
                print("{}{}{}".format(i,j,z))
                sum=sum+1
print(sum)
