"""
语法：

条件成立执行表达式 if 条件 else 条件不成立执行表达式

"""

a = 8
b = 2

c = a if a > b else b   # 判断a是否大于b，a大于b则执行a变量赋值给c，否则执行b赋值给c
print(c)


# 需求：有两个变量，比较大小  如果变量1 大于 变量2 执行 变量1 - 变量2 否则 变量2 - 变量1
aa = 91
bb = 90

cc = aa - bb if aa > bb else bb - aa
print(cc)
