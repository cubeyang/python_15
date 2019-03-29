import random
robot = {1: '曹操', 2: '张飞', 3: '刘备'}
while 1:
    r = int(input("请输入你要选择的角色："))
    if r==1 or r==2 or r==3:
        print("你选择的是{}".format(robot[r]))
        break
    else:
        print("请重新输入")
        continue
win=0
lose=0
equal=0
while 1:
    robotselect = random.randint(1, 3)
    f = int(input("请选择你出拳的类型："))
    print("你选择的出拳为{}".format(f))
    print("电脑选择的出拳为{}".format(robotselect))
    if f == robotselect:
        print("本局对战结果:平局")
        equal=equal+1
    elif (f==1 and robotselect==2) or (f==2 and robotselect==3) or (f==3 and robotselect==2):
        print("本局对战结果:你输了")
        lose=lose+1
    elif (f==1 and robotselect==3) or (f==2 and robotselect==1) or (f==3 and robotselect==1):
        print("本局对战结果:你赢了")
        win = win + 1
    m=input("本局已结束，请选择是否继续？按y继续，按n退出")
    if m=='y':
        continue
    else:
        print("本次游戏你赢的次数为{}，输得次数为{}，平局次数为{}".format(win,lose,equal))
        break



