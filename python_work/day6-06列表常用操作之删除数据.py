
name_list = ['TOM', 'LILY', 'JACK', 'ROSE']

# 1、del
# del name_list
# del(name_list)

# del 可以删除指定下标的数据
# del name_list[0]


# 2、pop() --删除指定下标的数据
# 如果不指定默认删除最后1个数据，无论是按照下标还是默认删除最后一个，pop函数都会返回被删除的数据
#
# del_name = name_list.pop(2)
# print(del_name)
# print(name_list)


# 3、remove(数据)  -- 移除列表中某个数据的第一个匹配项
# name_list.remove('TOM')


# 4、clear() -- 清空列表
name_list.clear()
print(name_list)

















