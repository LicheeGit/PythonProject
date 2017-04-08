# 这是传智播客2016视频DAY07的学习
# 列表和字典是可变类型

a = 100
print(id(a))
a = 200
print(id(a))
A = 10086
print(id(A))
B = A
print(id(B))
numbs = [11, 22, 33, 44]
print(id(numbs))
numbs2 = numbs
print(id(numbs2))
a = 100
b = a
print(id(a))
print(id(b))
b = 10086
print(id(b))
numbs[0] = 100
print(numbs[0])
print(numbs)
print(numbs2)
print(id(numbs))
print(id(numbs2))

myInfo = {"name": "lichee", "age": 18}
print(id(myInfo))
myInfo2 = myInfo
print(id(myInfo2))
myInfo2["name"] = "wang"
print(id(myInfo))
print(id(myInfo2))


def test1(numsTemp):
    numsTemp.append(44)


def test2(aTemp):
    print(id(aTemp))
    aTemp += 1
    print(id(aTemp))


nums = [11, 22, 33]
print(id(nums))
test1(nums)
print(id(nums))
print(nums)

a = 100
print(id(a))
test2(a)
print(id(a))
print(a)


# 全局列表不需要用global就可以更改
nums = [11, 22, 33]


def test():
    nums.append(44)
    print(nums)


def test2():
    print(nums)


test()
test2()


# 关于全局变量的使用
a = 200


def test():
    a = 100  # 如果是 a+=1 则不行，因为a=100可以看成定义，也可能是直接修改
    print(a)
# 如果一个全局变量和一个局部变量名字相同，那么用的是局部变量


def test2():
    print(a)


test()
test2()


def test3():
    name = input("请输入姓名：")
    age = input("请输入年龄")
    myId = input("请输入ID")
    # return name, age, id  # 这里也可以用列表，元组，字典返回 相当于是一个变量
    # info = [name, myId, age]
    # return info
    info = {"name": name, "id": myId, "age": age}
    return info


# recvData = test3()
# print(recvData.get("name"))
# a, b, c = test3()
# print(a, b, c)  # 对于字典形式的输出结果是name id age


def test(a, b="中国"):
    print(a)
    print(b)


# def test2(a=100, b): 如果函数有缺省形参必须把参数放后面，像前面这样会报错
test(11)
test(11, "其他国家")


def addAll(*a):
    result = 0
    for x in a:
        result += x
    return result


addResult = addAll(11, 22, 33, 44)
print(addResult)


def addAll2(*a, **b):
    print(a)
    print(b)


addAll2(11, 22, m=33, n=44)  # 前两个是元组，后两个是字典