name_list = ['TOM', 'LILY', 'JACK', 'ROSE']

# 1、修改指定下标的数据
name_list[1] = 'COCO'
print(name_list)

# 2、逆序 reverse()
list1 = [1, 4, 3, 2, 6, 5]
# list1.reverse()
# print(list1)

# 3、sort() 排序   升序(默认升序排序) 和 降序     -- 语法：列表序列.sort(key=None，reverse=False)
# 注意：reverse表示排序规则，reverse = False 升序（默认），reverse = True 降序
list1.sort(reverse=True)
print(list1)

