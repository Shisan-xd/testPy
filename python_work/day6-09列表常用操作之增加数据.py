# 4、增加      --作用：增加指定数据到列表中
# append()：列表结尾增加数据       -- 语法：列表序列.append(数据)

name_list = ['TOM', 'LILY', 'JACK', 'ROSE']
# name_list.append(['aa', 'bb'])



# 1、列表数据可改的 -- 列表可变类型
# append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾

# extend()：列表结尾增加数据，如果是一个序列，则将这个序列的数据拆开逐一添加到列表    -- 语法：列表序列.extend(数据)
# name_list.extend('cocount')


# insert(): 指定位置新增数据    -- 语法：列表序列.insert（下标位置，数据）
name_list.insert(3, 'drink')
print(name_list)















