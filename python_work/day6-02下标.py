# 列表可以一次性储存多个数据，且可以为不同数据类型

# 列表的常用操作
# 列表的作用是一次性储存多个数据，程序员可以多这些数据进行的操作有：增、删、改、查
# １、查找 - 下标
name_list = ['Tom', 'Lily', 'Rose']
print(name_list[0])

# 2、查找 - 函数
# index():返回指定数据所在位置的下标     -- 列表序列.index(指定数据，开始位置下标，结束位置下标)
# count()：统计指定数据在当前列表中出现的次数     -- 列表序列.count(指定数据)
# len()：访问列表长度，即列表中列表的数据         -- len(列表序列)
print(name_list.count('Lily'))
print(len(name_list))

# 3、查找 - 判断是否存在
# in 判断指定数据在某个列表序列，在则返回True
# not in 判断指定数据不在某个列表序列，不在则返回True

print('Tom' in name_list)
print('To' in name_list)
print('To' not in name_list)
print('Tom' not in name_list)



















