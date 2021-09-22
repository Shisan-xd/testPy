# 列表推导式
# 作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表.
# 列表推导式又称列表生成式

# while创建有规律的列表
# while实现循环
# 需求：创建0-10的列表
# 1、准备一个空列表

# list1 = []
#
# i = 0
# # while i < 10:
# #     list1.append(i)
# #     i += 1
# # print(list1)
#
# for i in range(10, 21):
#     list1.append(i)
# print(list1)

# a = '-'
# print(a * 40)

"""
while i in range(10, 20):
    list1.append(i)
    i += 1
print(list1)
"""

# 列表推导式实现----------------

a = '-'
print(f"列表推导式实现{a*25}")
#
# list2 = [i for i in range(20, 50)]
# print(list2)


# 带列表的if推导式----------------
# 创建0-10的偶数列表
# 简单列表推导式 range步长
list10 = [i for i in range(0, 10, 2)]
print(list10)

# for循环加if 创建有规律的列表
list11 = []
for a in range(0, 10):
    if a % 2 == 0:
        list11.append(a)
print(list11)

# 把for循环配合if的代码，改写带if的列表推导式
list12 = [a for a in range(0, 10) if a % 2 == 0]
print(list12)


# list3 = [i for i in range(20, 50) if i % 2 == 1]
# print(list3)









