# 这是传智播客2016视频DAY08存放家具的学习


class Home:
    def __init__(self, area):
        self.area = area
        self.accommondateItem = []

    def __str__(self):
        msg = "家当前可用的面积为：" + str(self.area)
        return msg

    def containItem(self, item):
        bedArea = item.getBedArea()
        bedName = item.getBedName()
        if self.area > bedArea:
            self.accommondateItem.append(item)
            self.area -= bedArea
            print("当前添加%s成功" % bedName)
        else:
            print("Error:当前%s需要的面积大于家的可用面积" % bedName)


class Bed:
    def __init__(self, name, area):
        self.area = area
        self.name = name

    def __str__(self):
        msg = self.name + "占用的面积为：" + str(self.area)
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name

home = Home(180)
print(home)
bed = Bed("席梦思", 4)
print(bed)
home.containItem(bed)
print(home)
bed2 = Bed("木板床", 177)
home.containItem(bed2)
print(home)