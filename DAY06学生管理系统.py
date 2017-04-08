# 这是传智播客2016视频DAY06中学生管理系统的练习
import time


def showInfo():
    print("-" * 50)
    print("学生管理系统".center(30, "-"))
    print("1.添加学生的信息".center(30, "-"))
    print("2.删除学生的信息".center(30, "-"))
    print("3.修改学生的信息".center(30, "-"))
    print("4.查询学生的信息".center(30, "-"))
    print("5.遍历所有的学生信息".center(30, "-"))
    print("6.退出系统".center(30, "-"))
    print("-" * 50)


def addNewStudent(studentsTemp):
    name = input("请输入姓名：")
    stuId = input("请输入学号：")
    age = input("请输入年龄：")
    stuInfo = {}
    stuInfo['name'] = name
    stuInfo['id'] = stuId
    stuInfo['age'] = age
    studentsTemp.append(stuInfo)


def delStuInfo(students):
    delNum = int(input("请输入要删除的序号："))
    # students = [{"name":'xiaoxiao', "id":100, "age":16}]
    # del students[0]
    del students[delNum]


i = -1
students = []
while (i != 6):
    showInfo()
    key = int(input("请选择功能（相应的序号）："))
    # 定义一个列表，来存储多个学生的信息
    if key == 1:  # 完成添加学生信息的功能
        addNewStudent(students)
    elif key == 2:
        delStuInfo(students)
    elif key == 3:
        pass
    elif key == 4:
        pass
    elif key == 5:
        print("*" * 30)
        print("接下来进行遍历所有的学生信息")
    # time.sleep(1)
        print("id\t姓名\t年龄\t")
        for temp in students:
            print("%s\t%s\t\t%s\t\t" % (temp['id'], temp['name'], temp['age']))
        print("*" * 30)
    elif key == 6:
        pass
    else:
        print("您的输入有误。请重新输入")
