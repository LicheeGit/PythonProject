# 这是传智播客2016视频DAY08-Python基础-第08天(面向对象编程)的学习
# author = Lichee

# 在类里面定义的方法的第一个参数都要定义成self


class Car:
    # 方法
    def getCarInfo(self):
        print('车轮个数：%d,颜色%s' % (self.wheelNum, self.color))

    def carMove(self):
        print("车正在移动")


class Dog:

    def __init__(self, newName, newWeight, newColor):
        # self.weight = 5
        # self.color = "黄色"
        self.weight = newWeight
        self.color = newColor
        self.name = newName

    def __str__(self):
        return "This is a return string value."

    def bark(self):
        print("汪汪汪")

    def run(self):
        print("狗在疯狂地跑")

    def eat(self):
        print("吃东西")
        self.weight += 5

    def printName(self):
        print("名字是：%s" % self.name)


# 定义一个函数
def test(temp):
    temp.printName()

# 创建一只小狗
xiaogou = Dog("大白", 5, "黄色")
# 调用小狗这个对象的一个方法
# xiaogou.printName()
# xiaogou.bark()
# xiaogou.run()
# 添加属性
# xiaogou.weight = 5
# xiaogou.color = "黄颜色"
# 获取小狗的属性
# print(xiaogou.weight)
# print(xiaogou.color)

# 创建另一条小狗
wangcai = Dog("小黑子", 10, "黑色")
# wangcai.printName()
# print(wangcai.weight)
# print(wangcai.color )

test(wangcai)
print(xiaogou)