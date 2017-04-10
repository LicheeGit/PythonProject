# 这是传智播客2016视频DAY08存放家具的学习
# 在DAY09做了升级修改


class Home:
    def __init__(self, area):
        self.area = area
        self.accommondateItem = []
        # 默认灯的状态为off
        self.light = 'off'

    def __str__(self):
        msg = "家当前可用的面积为：" + str(self.area) + ",灯的状态为：" + self.light
        if len(self.accommondateItem)>0:
            msg += "\n家中当前有："
            for temp in self.accommondateItem:
                msg += temp.getBedName() + ","
            msg = msg.strip(",")
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

    def turnOn(self):
        # 把家里的灯打开了
        self.light = "On"
        # 把家里所有的家具都变成亮的状态
        for temp in self.accommondateItem:
            # 调用这个方法用来修改这个物品的亮状态
            temp.setLight()

class Bed:
    def __init__(self, name, area):
        self.area = area
        self.name = name
        self.light = "off"

    def __str__(self):
        msg = self.name + "占用的面积为：" + str(self.area) + "，当前的明暗程度为" + self.light
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name

    def setLight(self):
        self.light = "on"

    def setLightOff(self):
        self.light = "off"

home = Home(180)
print(home)
bed = Bed("席梦思", 4)
print(bed)
home.containItem(bed)
print(home)
bed2 = Bed("木板床", 177)
home.containItem(bed2)
print(home)