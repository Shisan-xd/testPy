"""
目标
    创建集合

"""


# 创建有数据的集合
s1 = {10, 20, 30, 40}
print(s1)

s2 = {10, 20, 30, 40, 10, 20, 30, 40}
print(s2)

s3 = set("abcdefg")
print(s3)

# 创建空集合
s4 = set()
print(s4)
print(type(s4))     #set类型

s5 = {}
print(type(s5))     #dict类型



#  集合之常见增删改查

# 增加数据 add、update
s6 = {10, 20}
# 1、 集合是可变类型
# s6.add(100)
# print(s6)

# 2、 集合有去重功能，如果追加的数据是集合已有的数据，则什么事情都不做
# s6.add(100)
# print(s6)

# s6.add(['a', 'b', 'c'])   # 会报错
# print(s6)

# update    追加的是一个数据序列，不支持增加单一的数据
s6.update([12, 20, 10, 30, 40, 50])
print(s6)

# s6.update(100)  #会报错
# print(s6)

# 查找数据  in、not in
# in 判断数据在集合序列
# not in 判断数据不在集合序列

print(12 in s6)
print(12 not in s6)


# 删除数据  remove、discard
s6.remove(12)
print(s6)

s6.discard(50)
print(s6)




















