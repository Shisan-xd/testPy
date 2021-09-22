# 字符串
str1 = 'aa'
str2 = 'bb'

# 列表
list1 = [10, 20]
list2 = [30, 40]

# 元组
t1 = (1, 2)
t2 = (20, 30)


# 字典
dict1 = {12, 32}
dict2 = {30, 40}
dict3 = {'S': 10, 'z': 'hah', 'q':00, 'e':'wqwq'}

# del dict3['z']
# print(dict3)


# del(list1[1])
# print(list1)


print(min(dict3))
print(min(dict1))
print(max(dict1))


# enumerater    返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个对象是原迭代对象的数据
for i, a in enumerate(dict3.items(), start=1):
    print(f'{i}{a}')