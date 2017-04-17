# 这是Python正则表达式的学习,等有时间将此例优化为类和方法的形式进行实现
# 学习内容参考自http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
# encoding = utf-8
# 备注一条输出格式代码：print("images, titles, descs, rates, cates, sep = "\n-*40\n"
# 2.re模块
# 2.1.开始使用re
import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
if match:
    # 使用Match获得分组信息
    print(match.group())
# X(VERBOSE)：详细模式。这个模式下正则表达式可以是多行，忽略空白字符，
# 并且可以加入注释。以下两个正则表达式是等价的：
a = re.compile(r"""\d + #the integral part
                    \.  #the decimal point
                    \d * #some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
# 上面的例子可以简写为以下形式，但是无法复用编译后的Pattern对象
m = re.match(r'hello', 'hello world!')
print(m.group(0))

# 2.2.Match部分的练习
import re
# m = re.match(r'(\w+)(\w+)(?P<sign>.*)', 'hello world!')
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
# string: 匹配时使用的文本
print("m.string:", m.string)
# re：匹配时使用的Pattern对象
print("m.re:", m.re)
# pos：文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.search()方法的同名参数相同
print("m.pos:", m.pos)
# endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.search()方法的同名参数相同。
print("m.endpos:", m.endpos)
# lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
print("m.lastindex:", m.lastindex)
# lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
print("m.lastgroup:", m.lastgroup)

# group([group1, …]): 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
print("m.group(1,2):", m.group(1, 2))
# groups([default]): 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
print("m.groups():", m.groups())
# groupdict([default]): 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。
print("m.groupdict():", m.groupdict())
# start([group]): 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
print("m.start(2):", m.start(2))
# end([group]): 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
print("m.end(2)", m.end(2))
# span([group]): 返回(start(group), end(group))。
print("m.span(2)", m.span(2))
# expand(template): 将匹配到的分组代入template中然后返回。
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

# 2.3.Pattern
'''
Pattern对象是一个编译好的正则式，通过Pattern提供的一系列方式可以对文本
进行匹配查找。Pattern不能直接实例化，必须使用re.compile()进行构造
'''
import re
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
# pattern：编译时用的表达式字符串
print("p.pattern:", p.pattern)
# flag：编译时用的匹配模式。数字形式
print("p.flags:", p.flags)
# groups：表达式中分组的数量
print("p.groups:", p.groups)
# groupindex
print("p.groupindex:", p.groupindex)

# 实例方法[|re模块方法]
'''2.search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]):
这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。
pos和endpos的默认值分别为0和len(string))；re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。 '''
import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用的match()无法成功匹配
match = pattern.search('hello world!')
if match:
    # 使用Match获得分组信息
    print(match.group())

# 3.split(string[,maxsplit])|re.split(pattern,string[,maxsplit]):
# 按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，缺省全部分割
import re
p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))
# 4.findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]):
# 搜索string，以列表形式返回全部能匹配的子串。
import re
p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))
# 5.finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]):
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
for m in p.finditer('one1two2three3four4'):
    print(m.group())
# 6.sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。
import re
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.sub(r'\2 \1', s))
def func(m):
    return m.group(1).title()+' '+m.group(2).title()
print(p.sub(func, s))
# 7.subn(repl, string[, count]) |re.sub(pattern, repl, string[, count]):
# 返回 (sub(repl, string[, count]), 替换次数)。
import re
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.subn(r'\2 \1', s))
def func(m):
    return m.group(1).title()+' '+m.group(2).title()
print(p.subn(func, s))