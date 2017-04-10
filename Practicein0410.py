# 这是传智播客2016视频DAY09的学习
# 如果有Object的叫新式类，原来的那种没有的叫经典类


class Person(object):
    def __init__(self, name, age):
        self.__name = name  # 定义的私有属性，私有属性不会被继承
        self.__age = age
        self.__height = 180

    def __str__(self):
        return "年龄为：" + str(self.__age)

    def setNewAge(self, newAge):
        if 0 < newAge < 80:
            self.__age = newAge

    def getAge(self):
        return self.__age

lichee = Person("Lichee", 20)
print(lichee)
# print(lichee.__name)
# print(lichee.__age)
lichee.setNewAge(21)
print(lichee)


class Animal(object):
    def __init__(self, name='动物', color='白色'):
        self.name = name  # 公有属性可以被继承
        self.color = color
        # self.__height = "18"

    def __del__(self):  # python解释器如果检测到一个对象没有任何用处了，就把这个对象kill掉
        print("this is the end.")

    def __test(self):  # 私有方法
        print("我就看看能不能调用这个方法")
        # print(self.__height)

    def newTest(self):  # 通过这个可以调用私有方法
        self.__test()

    def bark(self):
        print("这是动物的喊叫")

dog = Animal("旺财")
print("-----1------")
newDog = dog
print("-----2------")
lastDog = dog
print("-----3------")
del dog
del newDog
del lastDog
print("-----4------")


class Dog(Animal):
    # def __init__(self, name='狗', color='黑色'):
    #     self.__name = name
    #     self.__color = color
    #
    # def __del__(self):  # python解释器如果检测到一个对象没有任何用处了，就把这个对象kill掉
    #     print("this is the end.")

    def printInfo(self):
        print("名字是：%s" % self.name)
        print("颜色是：%s" % self.color)

    def bark(self):
        # Animal.bark(self)
        super().bark()  # 这种方法在python3中使用较好
        print("这是狗的喊叫")

wangcai = Dog(name="旺财")
wangcai.printInfo()
wangcai.newTest()
wangcai.bark()


class Base(object):
    def test(self):
        print("------This is Base Test --------")


class A(object):
    def test(self):
        print("------This is A Test --------")


class B(object):
    def test(self):
        print("------This is B Test --------")


class C(B, A):
    pass


class D(A, B):
    pass

c = C()
c.test()  # 优先继承B
d = D()
d.test()
print(C.__mro__)


class Horse(Animal):

    horseNum = 0  # 类属性

    def __init__(self, name, color=''):
        super().__init__(name)
        # super().__init__(name, color)
        # self.name = name  # 以上 从父类继承颜色属性
        self.setHorseNum()

    @classmethod
    def setHorseNum(cls):
        cls.horseNum += 1

horseA = Horse("白龙马")
# Horse.horseNum += 1
horseA.setHorseNum()
print(horseA.name)
print(horseA.color)
print(horseA.horseNum)

horseB = Horse("赤兔马")
horseB.setHorseNum()
# Horse.horseNum += 1
print(horseB.name)
print(horseB.color)
print(horseB.horseNum)


class People(object):
    address = '山东'  # 类属性
    #  实例方法
    def __init__(self):
        self.name = 'xiaowang'  # 实例属性
        self.age = 20  # 实例属性

    # 类方法
    @classmethod
    def setNewAddress(cls):
        cls.address = '内蒙古'

# 可以通过类名的方式来获取类属性
# 但是不能通过类名的方式获取实例属性
# print(People.address)
# print(People.name)

# 类对象可以直接调用类属性 也可以直接调用类方法
# 但是类对象不允许调用实例属性 并且不允许调用实例方法
# 如果是一个实例对象
# 可以获取实例属性和类属性的值 但是只能修改实例属性 不能修改类属性
# 还可以调用实例方法和类方法

xiaoming = People()
xiaoming.setNewAddress()
# print(xiaoming.name)
# print(xiaoming.age)
# print(xiaoming.address)
# xiaoming.address = '河北'
# print(xiaoming.address)

People.setNewAddress()
print(People.address)

# print(People.address)
# print("-"*40)
# People.address = '廊坊'
# print(People.address)

# 关于异常
try:
    num = 100
    print(num)
except (NameError, IOError) as errmsg:
    print("产生了错误%s" % errmsg)
else:
    print("没有捕获异常，真高兴")
finally:
    print("我一定会执行的哦")



