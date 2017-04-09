# 这是传智播客2016视频DAY08烤地瓜的练习

class SweetPotato:
    # 初始化，用来设置默认的属性
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    def __str__(self):
        msg = '您的地瓜已经处于' + self.cookedString +'的状态'
        if len(self.condiments)>0:
            msg += ',添加的佐料为：'
            for temp in self.condiments:
                msg = msg + temp + ','
            msg = msg.strip(",")
        return msg

    # 用火去烤地瓜
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤糊了"
        elif self.cookedLevel > 5:
            self.cookedString = "熟了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    def addCondiments(self, temp):
        self.condiments.append(temp)

# 创建一个地瓜对象
digua = SweetPotato()
print(digua)
# print(digua.cookedLevel)
# print(digua.cookedString)
# print(digua.condiments)
print("接下来开始烤".center(30, "s"))
print("烤两分钟".center(30,"="))
digua.cook(2)
# print(digua.cookedString)
print(digua)
digua.cook(2)
print(digua)

print("添加番茄酱".center(30,"-"))
digua.addCondiments("番茄酱")
print(digua)
print("添加芥末酱".center(30,"-"))
digua.addCondiments("芥末酱")
print(digua)
digua.cook(2)
print(digua)
