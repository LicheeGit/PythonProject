# 这是传智播客2016视频的学习DAY05的学习

name = "Lichee"
print(name[1:5:2])  # 切片[起始：结束：步长] 不包含结束位
print(name[-1])  # 倒着来
print(name[3:])  # 到结束
# print(name[-3:-1]) 有问题 别用了还是
print(name[::-1])
name = name[::-1]  # 倒序

# 字符串常用操作
mystr = "Lichee's Python Learning is So Happy"
mystr.find("ic")  # 返回第一次出现的下标, -1 means not found
mystr.index("ic")  # index找不存在的会报错
mystr.rfind("ic")  # r mean Right
# 找文件后缀/类型
myFileName = "Practice.in.0328.py"
index = myFileName.rfind(".")
print(myFileName[index + 1:])

mystr.count("i")
print(mystr.replace("n", "N", 2))
# 修改两次n->N,输出Lichee's PythoN LearNing is So Happy

print(mystr.split(" "))  # 分割所有的空格
print(mystr.split(" ", 2))
# 只分割前两个空格 后面的是还一个整体 ["Lichee's", 'Python', 'Learning is So Happy']

print(mystr.capitalize())  # 全小写

print(mystr.startswith("Liche"))
print(myFileName.endswith(".py"))

Ha = "haha"
print(Ha.ljust(7))
print(Ha.rjust(5))
print(Ha.center(9))

print(Ha.partition("a"))
print(Ha.rpartition("a"))
'''
('h', 'a', 'ha')
('hah', 'a', '')
'''

Ha = "ha\nha"

mm = "_"
newStr = ["Call", "me", "Lichee", "97"]
print(mm.join(newStr))
# 表示使用mm将列表里面的项串起来
