#1.创建列表num_list，要求包含50以内所有能被3整除的正整数，遍历
num_list=range(1,51)
for i in num_list:
    if i%3==0:
        print(i)

#2.截取num_list的第3到第7个元素（包含两端）,保存到新列表sub_list中
sub_list=num_list[2:7]
for i in sub_list:
    print(i)

#3.将sub_list中的元素进行倒序排列，生成新的列表reverse_list（使用切片）
reverse_list=sub_list[::-1]
for i in reverse_list:
    print(i)

#4.创建numbers列表包含50到200之间所有能被17整除的整数
numbers=[i for i in range(50,201) if i%17==0]
print(numbers)

#5.计算numbers中所有元素的乘积
product=1
for i in numbers:
    product*=i
print(product)

#6.录入密码,如果密码为aaa,提示登录成功;否则提示登录失败
key=input('请输入密码：')
if key=='aaa':
    print('登录成功')
else:
    print('登录失败')

#7.录入年龄，根据年龄打印出对应的信息
#年龄 < 18: 未成年
#年龄 等于18并且小于65: 成年
#年龄 >= 65: 老年
age=input('请输入年龄：')
age1=int(age)
if age1<18:
    print('未成年')
elif age1>=18 and age1<65:
    print('成年')
else:
    print('老年')

#8.统计字符串text="HeLLoWorLD"中小写字母的数量（字符串也可以使用for循环）
#这个题的思路是循环字符串，使用字符串islower函数判断是否是小写。
text="HeLLoWorLD"
num=0
for char in text:
    if char.islower():
        num+=1
print("小写字母的数量：",num)

#9.求100-999之间所有的水仙花数(水仙花数是指一个n位正整数，其各位数字的n次方之和等于它本身(常见 n = 3，如153 = 1³+5³+3³))
#这题思路是：循环这个范围的数，在循环内获取数字的个位/十位/百位，然后进行计算。
for i in range(100,1000):
    g=i%10
    s=i//10%10
    b=i//100
#    g=1%10
#    s=int(i/10)%10
#    b=int(i/100)%10
    if i==g*g*g+s*s*s+b*b*b:
        print(i)

#10.录入商品价格，录入是否是会员，如果是会员打折，如果不是原价购买。录入是否为vip会员，如果是vip会员打8折，其他打9折。
price=input('请输入商品价格：')
price1=float(price)
vip=input('是否是会员？')
if vip=='是':
    print(price1*0.8)
elif vip=='否':
    print(price1*0.9)










