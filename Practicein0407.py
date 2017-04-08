# 这是传智播客2016视频DAY06的学习
# author = Lichee


def add3num(a, b, c):
    result = a + b + c
    return result


def average3num(a, b, c):
    result = add3num(a, b, c)
    average = result / 3
    return average


finalresult = average3num(44, 55, 66)
print(finalresult)

num = 100


def test1():
    global num  # 通过global修改全局变量
    print(num)
    num += 2
    print(num)


def test2():
    print(num)


test1()
test2()
