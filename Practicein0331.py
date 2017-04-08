# 这是传智播客2016视频DAY06的学习


def add2num(a, b):
    c = a + b
    print("%d+%d=%d" % (a, b, c))


add2num(b=20, a=100)  # 如果在调用的时候，写的参数的顺序和定义的时候接收的顺序


# 不一致，那么可以在传递的时候指定是给哪个形参的


def add3num(a, b, c):
    d = a + b + c
    return d


result = add3num(11, 22, 33)
print("%d" % result)

functiondic = {"Title": "名片管理系统", "1": "添加名片", "2": "删除名片", "3": "修改名片", "4": "查询名片", "5": "退出系统"}
temp = functiondic.items()


def displaymenu():
    print("-" * 30)
    for m, n in temp:
        print("%s.%s".center(30) % (m, n))
    print("-" * 30)


def getchoice():
    selectedkey = input("请输入序号：")
    return int(selectedkey)


def printallinfo(namelisttemp):
    print("=" * 30)
    for tempname in namelisttemp:
        print(tempname)
    print("=" * 30)


nameList = []
key = 0
while not (key == 5):  # 循环十次
    displaymenu()
    key = getchoice()
    if key == 1:
        print("您选择了%s" % functiondic.get("1"))
        print("接下来是添加的详细信息：")
        newName = input("请输入姓名：")
        nameList.append(newName)
    elif key == 2:
        pass
    elif key == 3:
        pass
    elif key == 4:
        pass
    elif key == 5:
        printallinfo(nameList)
    else:
        print("输入有误，请重新输入")
print("感谢使用")
