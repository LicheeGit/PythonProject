# 这是2017/04/13关于lxml的学习，学习内容来自http://www.jianshu.com/p/f446663c970f，在此致谢

from lxml import etree

html = etree.Element('html')
body = etree.SubElement(html, 'body')
body.text = 'Text'
print(etree.tostring(html))

br = etree.SubElement(body, 'br')
print(etree.tostring(html))
# tail仅在该标签后面追加文本
br.tail = 'Tail'
print(etree.tostring(br))

print((etree.tostring(html)))
# tostring方法增加method参数，过滤单一标签，输出全部文本
print(etree.tostring(html, method='text'))


# XPath方式
# 方式一：过滤单一标签，返回文本
print(html.xpath('string()'))
# 方式二：返回列表，以单一标签为分隔
texts = html.xpath('//text()')
print(texts[0])
parent = texts[0].getparent()
print(parent.tag)
print(texts[1], texts[1].getparent().tag)  # 以上 方法二获得的列表，每个元素都会带上它所属节点及文本类型信息
print(texts[0].is_text)
print(texts[1].is_text)
print(texts[1].is_tail)  # 检查文本类型是普通文本还是tail文本


# 下面是将XML文件解析为Element对象，以及将Element对象输出为XML文件
# 1.文件解析
# 文件解析常用的有fromstring,XML,HTML三个方法。接受的参数都是字符串
xml_data = '<root>data</root>'

# fromstring方法
root1 = etree.fromstring(xml_data)
print(root1.tag)
print(etree.tostring(root1))

# XML方法, 与fromstring方法基本一样
root2 = etree.XML(xml_data)
print(root2.tag)
print(etree.tostring(root2))

# HTML方法， 如果没有<html>和<body>标签，会自动补上
root3 = etree.HTML(xml_data)
print(root3.tag)
print(etree.tostring(root3))

# 2.输出
# 输出就是tostring方法，这里补充xml_declaration和encoding两个参数,前者是XML声明，后者是指定编码
root = etree.XML('<root><a><b/></a></root>')
print(etree.tostring(root))

# XML声明
print(etree.tostring(root, xml_declaration=True))

# 指定编码,这句指定了编码方式是'iso-8859-1'
print(etree.tostring(root, encoding='iso-8859-1'))

# ElementPath
# 需要引入ElementTree类，而一个ElementTree对象可以理解为一个完整的XML树，
# 每个结点都是一个Element对象。而ElementPath则相当于XML中的XPath。用于搜索和定位Element元素

# 这里介绍两个常用方法，可以满足大部分搜索、查询需求，它们的参数都是XPath语句：
# findall():返回所有匹配的元素，返回列表
# find()：返回匹配到的第一个元素

root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")
# 查找第一个b标签
print(root.find('b'))
print(root.find('a').tag)

# 查找所有b标签，返回Element对象组成的列表
print([b.tag for b in root.findall('.//b')])
# 根据属性查询
print(root.findall('.//a[@x]')[0].tag)
print(root.findall('.//a[@y]'))


