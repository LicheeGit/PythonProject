# 这是传智播客2016视频DAY05的学习

# 列表应用：显示文件名的后缀
fileNames = ['01.py', '02.txt', '03.rar', '04.c', '05.cpp', '06.php',
             '07.java', 'index.doc']
for tempName in fileNames:
    position = tempName.rfind(".")
    print(tempName[position:])
print("---------华丽的分割线-----------")
i = 0
length = len(fileNames)
while i < length:
    tempName = fileNames[i]
    position = tempName.rfind(".")
    print(tempName[position:])
    i += 1

# 字典
info = {"name": "Lichee", "height": "180", "name": "王立志"}
print(info.keys())
print(info.values())
print(info.get("weight", "65"))
temp = info.items()
for key, value in temp:
    print(key, value)

aaa = (11, 22, 33)
a, b, c = aaa
print(b, a, c)

chars = ['a', 'b', 'c', 'd']
for i, ch in enumerate(chars):  # 枚举 可以返回一个下标
    print(i, ch)
# 下面是关于函数的学习


def hello():
    """这是hello函数的说明，可以从help(hello)中查看到"""
