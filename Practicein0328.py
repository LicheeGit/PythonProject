# 这是传智播客2016视频DAY04的学习
import random

import time

length = input("input length:")

if 0 < int(length) <= 10:
    print("legal")
else:
    print("illegal")

sex = int(input("your sex: "))
if sex == 0:
    print("man")
elif sex == 1:
    print("lady")
elif sex == 2:
    print("third")
else:
    print("nothing")

# 石头剪刀布
# 0剪刀 1石头 2布
playerInput = input("请输入（0剪刀  1石头 2布）：")
player = int(playerInput)
windows = random.randint(0, 2)

if (player == 0 and windows == 2) or (player == 1 and windows == 0) or (player == 2 and windows == 1):
    print("赢了真高兴")
elif windows == player:
    print("平局")
else:
    print("输了")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("\n")
    i += 1

# 乘法口诀表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d" % (j, i, j * i), end='')
        j += 1
    print("\n")
    i += 1

name = "Lichee"
for temp in name:
    print("%s" % temp)
    if temp == 'i':
        continue
    time.sleep(1)
