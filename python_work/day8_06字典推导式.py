
dict1 = {a: a**2 for a in range(1, 5)}
dict1 = {a: a**2 for a in range(1, 5)}
print(dict1)


# 合并两个列表为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['tom', 20, '']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)

# 两个列表数据下标数值相同，len统计任何一个列表的长度都可以
# 两个列表数据下标数值不相同，len统计下标数值多的会报错（可统计下标数值小的列表）


# 提取字典中的目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'lenovo': 330, 'acer': 99}

# 1、需求:提取键值对大于等于200
# 获取所有键值对数据，判断v值大于等于200 返回字典
dict3 = {a: b for a, b in counts.items() if b >= 200}
print(dict3)













