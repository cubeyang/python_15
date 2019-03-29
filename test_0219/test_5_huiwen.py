n=input("请输入一个五位数：")
if len(n)==5:
    if n[0]==n[4] and n[3]==n[1]:
        print("是回文")
    else:
        print("不是回文")
else:
    print("你输入的不是五位数，请重新输入")