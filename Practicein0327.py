# 这是传智播客2016视频DAY03-04的学习
# encoding = utf-8
# from datetime import time
import time

from Tools.scripts.treesync import raw_input

print("hello world")
# age = 18
print("age")
age = 19
# score = 99
score = 85.5
a = 100
b = 100.5
print(age, score, a, b)
print("my english score is %d" % score)
mathScore = 95
print("english score is %d, math score is %d" % (score, mathScore))
print("111111111\n7777777777")
password = input("请输入密码：")
print("您的密码是：%s" % password)
raw_input("提示")  # 这是python2的input操作
'''
在python3中的input是输入100+99的结果是‘100+99’
在python2中是199.
所以python2的raw_input等同于python3中的input
'''
# 下面是升级版名片打印代码
name = input("请输入您的姓名：")
qq = input("请输入您的QQ:")
phoneNumber = input("请输入您的手机号：")
# 模拟打印过程
print("系统正在打印中...3")
time.sleep(1)
print("系统正在打印中...2")
time.sleep(1)
print("系统正在打印中...1")
time.sleep(1)
print("=" * 20)
print("姓名：%s\nQQ:%s\nTel:%s\n" % (name, qq, phoneNumber))
print("=====================")

# if语句的基本使用
a = 16
if a > 18:
    print("%d>18" % a)
