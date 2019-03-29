i = 0
sum=0
while i < 2:
    age = input("请输入你的の年龄")
    sex = input("请输入你的性别")
    if (age<='12' and age>='10') and (sex=='f'):
        print("符合要求,可以加入足球队")
        sum=sum+1
    else:
        print("不符合要求,不可以加入足球队")
    #     continue
    i=i+1
print("符合要求的人数为{}".format(sum))

