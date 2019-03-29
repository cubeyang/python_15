price=float((input('商品的价格是:')))
if price>100:
    print("你的折扣价是：20%%：你的の最终价格为： %.2f"%(price*0.2))
elif price<=100 and price>=50:
    print("你的折扣价是：10%%：你的の最终价格为： %.2f"%(price*0.1))
else :
    print('很遗憾，没有折扣')