#1.已知列表 mylist=[15, 49, 23, 78, 81, 85]，找出其中所有奇数并保存为 mylist1
mylist=[15, 49, 23, 78, 81, 85]
mylist1=[]
for i in mylist:
    if i%2==1:
        mylist1.append(i)
print(mylist1)

#2.计算 mylist1 中元素的数量和最大值
print(len(mylist1))
print(max(mylist1))

#3.将 mylist1 中的所有元素按照从小到大的升序排列，将排序结果保存为 mylist2
mylist1.sort()
print(mylist1)
mylist2=mylist1

#4.已知列表 newlist=[3,6,9]，编写代码将 newlist 中的元素插入到 mylist2 的尾部，将插入后的结果保存为 mylist3
newlist=[3,6,9]
mylist3=mylist2+newlist
print(mylist3)

#5.numbers = [num for num in range(50, 201) if num % 17 == 0]
#从 numbers 中提取数值最大的三个元素，存入新列表 top_numbers
'''
numbers = [num for num in range(50, 201) if num % 17 == 0]
numbers.sort(reverse=True)
print(numbers)
top_numbers=numbers
'''
numbers = [num for num in range(50, 201) if num % 17 == 0]
top_numbers = sorted(numbers, reverse=True)[0:3];
print(" top_numbers 列表:", top_numbers);
#6.现有集合 data_set = {5, 15, 25}，请向其中添加元素 35 和 45，并输出更新后的集合
data_set = {5, 15, 25}
data_set.update([35,45])
print(data_set)

#7.已知 setA={1,32,12,24,51}，setB={1,3,2,12}，编写代码找出仅存在于 setA 中但不存在于 setB 中的所有元素
setA={1,32,12,24,51}
setB={1,3,2,12}
new_set=setA-setB
print(new_set)

#8.计算商品库存总量stock = {"鼠标": 45, "键盘": 32, "U盘": 27}
#45为鼠标的价格
stock = {"鼠标": 45, "键盘": 32, "U盘": 27}
print(stock.values())
total_value=0
for value in stock.values():
    total_value+=value
print(total_value)

#9.某商店周销量记录为字典 sales = {1: 150, 2: 89, 3: 200, 4: 75, 5: 300}，请找出销量最低的周次  # 1表示周次，150表示销售量
sales = {1: 150, 2: 89, 3: 200, 4: 75, 5: 300}
week=min(sales,key=sales.get)
print(week)
#10学生的性别用字典 myDict2={"Zhang":"F","Wang":"M","Zhao":"F","Li":"F"}，其中“M”代表男，“F”代表女，编写代码统计 myDict2 中男女学生的数量
#思路：获取所有的性别（value），循环查找统计
myDict2={"Zhang":"F","Wang":"M","Zhao":"F","Li":"F"}
male=0
female=0
for value in myDict2.values():
    if value=="M":
        male+=1
    else:
        female+=1
print(male)
print(female)
