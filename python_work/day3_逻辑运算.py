a = 1
b = 2
c = 3


# 逻辑运算
# 1、and ： 与： 都真才真
print((a < b) and (b < c))

# 2、or : 或 ： 一真则真，都假则假
print((a < b) or (c > b))
print((b < a) or (c < a))

# 3 not ： 非： 取反
print(not(a < b))



# 数字逻辑运算
# and运算符 ，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)


# or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
