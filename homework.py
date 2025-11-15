#1.将字符串" data_processing "的首尾空白字符清除，结果存入clean_str
str1=' data_processing '
clean_str=str1.strip()
print(clean_str)
#2.已知char_list = ['H','e','l','l','o']，编写代码将其转换为字符串"Hello"
char_list = ['H','e','l','l','o']
str2=''.join(char_list)
print(str2)
#3.给定列表 domain = ['http', 'example', 'net']，编写代码生成完整网址字符串 "http://example.net"
domain = ['http', 'example', 'net']
str3='.'.join(domain)
str4=str3.replace('.','://',1)
print(str4)
#4. 已知字符串 s = "programming"，编写代码利用 s 提取子串 "rog"
s='programming'
print(s[1:4])
str5=s.find('rog',0,10)
print(str5)
#5.统计字符串 text = "HeLLoWorLD" 中o的数量
text = "HeLLoWorLD"
print(text.count('o'))
#6. 给定列表 items = ["apple", "orange", "pear"]，生成格式为 "apple-orange-pear" 的字符串，保存为 joined_str
items = ["apple", "orange", "pear"]
joined_str='-'.join(items)
print(joined_str)
#7.编写代码得到字符串“test\ntest”并保存为 mystr1，其中字符"\"不被视作转义字符
mystr1='test\\ntest'
print(mystr1)
#8.定义字符串值为" hello python "去掉里面的所有空格（使用replace）
str6=" hello python "
str7=str6.replace(' ','')
print(str7)
#9 已知列表 students = ["小明", "小红", "小刚", "小丽", "小强"]，请通过切片获取列表中从第 2 个元素到第 4 个元素（包含首尾）的子列表，打印该子列表。
students = ["小明", "小红", "小刚", "小丽", "小强"]
print(students[1:4])
#10.已知列表scores = [85, 92, 78, 90, 88, 76]，使用反向索引（负数）从后往前输出元素
scores = [85, 92, 78, 90, 88, 76]
print(scores[-1:-7:-1])

'''
自己测试几个常用函数
lower()/upper()/len()/capitalize()/swapcase()
isdigit()/isupper()/islower()/
'''
#lower()
str8='PYTHON'
print(str8.lower())
#upper()
str9='python'
print(str9.upper())
#len()
str10='python'
print(len(str10))

list1=[55,66,77]
print(len(list1))
#capitalize()
str11='PyTHon'
print(str11.capitalize())
#swapcase()
str12='pYThoN'
print(str12.swapcase())
#isdigit()
str13='python'
print(str13.isdigit())

str14='114514'
print(str14.isdigit())
#islower()
str15='python'
print(str15.islower())

str16='PyThoN'
print(str16.islower())
#isupper()
str17='python'
print(str17.isupper())

str18='PYTHON'
print(str18.isupper())

#1.控制台录入一个字符串，打印出其长度
str19='Hello,world'
print(len(str19))
#2.将字符串 "HelloWoRLd" 中的字符统一转换为小写形式
str20="HelloWoRLd"
print(str20.lower())
#3.将字符串"HelloWORLD"中第一个字母转大写后面字母转小写，结果保存为 upper_str
str21="HelloWORLD"
print(str21.capitalize())
#4.str="123"判断str是否只由数字组成
str="123"
print(str.isdigit())




