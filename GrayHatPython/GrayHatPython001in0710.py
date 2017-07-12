# coding: utf-8
# 解决方案来自http://tieba.baidu.com/p/1242856365
from ctypes import *
'''
处理字符串过程中若遇到'\0'一般认为是结尾，python3 改为默认宽字符处理字符，
比如，一般情况下'a'是一个字节存储0x61，而宽字节用两个字节表示为0x0061，
若存储时倒叙 则为0x6100，printf函数默认单字节处理，所以只打印一个字符遇到'\0'后认为结束。
'''
'''Py3K使用的是Unicode编码，而printf不支持该编码，所以需要转码。'''


# 使用wprintf宽字符显示
msvcrt = cdll.msvcrt
message_string = "Hello World!\n"
msvcrt.wprintf("Testing: %s", message_string)
# 转为byte类型 在字符串前面加b
str = b"Lichee!"
msvcrt.printf(b"Hello %s\n", str)
# 转码为utf-8
tstr = "Lichee!"
result = "Hello " + tstr + "\n"
result = result.encode("utf-8")
msvcrt.printf(result)


# 搞定在IDLE中可以直接输出

msvcrt = cdll.msvcrt
str = b"Lichee!"
s = create_string_buffer(100)  # 必须足够长
msvcrt.sprintf(s, b'Hello %s\n', str)
print(s.value.decode('utf-8'))
'''
先使用sprintf函数把结果输出到s变量，然后再用Python自带的print方法输出s的value。
好了，通过以上的各种方法就可以解决Py3K调用C函数printf的问题了。
'''

# 结构体
class beer_recipe(Structure):
_fields_ = [
("amt_barley", c_int),
("amt_water", c_int),
]


# 联合体
class barley_amount(Union):
_fields_ = [
("barley_long", c_long),
("barley_int", c_int),
("barley_char", c_char * 8),
]
