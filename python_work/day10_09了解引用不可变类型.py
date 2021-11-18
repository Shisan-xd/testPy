# @Time     ：2021/10/21 15:22
# @Author   ：
# @File     ：day10_09了解引用不可变类型.py


# 在python中值是靠引用来传递的
# 我们可以yo用id()来判断两个变量是否为同一个值的引用，可以将id值理解为那块内存的地址标识

# 1. int类型 为不可变类型
a = 1
b = a

# print(id(a))
# print(id(b))

aa = [10, 20]  #列表是可变类型
bb = aa

print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(id(bb))

