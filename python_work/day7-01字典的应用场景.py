"""
目标
- 字典的应用场景
- 创建字典的语法
- 字典的常见操作
- 字典的循环遍历

"""

# 1、字典的应用场景
# 思考：如果有多个数据，例如：'Tom','男','20'，如何快速存储

list1 = ['Tom', '男', '20']   #--这是列表
# 数据顺序发生变化，每个数据的下标也会随即变化，如何保证数据顺序变化变化前后能使用同一的标准查找数据呢？
# 字典：
#     字典里面的数据是以【键值对】形式出现，字典数据和数据顺序没有关系，即字典不支持下标，后期无论数据如何变化，
    # 只需要按照对应键的名字查找数据即可

# 字典 - 增
# 写法：字典序列[key] = 值      注意：key存在则修改这个key对应的值，不在则新增此键值对
dict1 = {'name':'Tom', 'age':18, 'gender':'男'}      #--这是字典
dict1['id'] = 1
dict1['name'] = 'Jack'
print(dict1)


# 字典 - 删    del()/del 删除字典或删除字典中指定的键值对
del dict1['gender']
print(dict1)

# 字典 - clear()清空字典
dict1.clear()
print(dict1)


# 字典 - 改










