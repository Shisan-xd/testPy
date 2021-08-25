"""
# 1、多个数据元组
t1 = (10, 20, 30)
print(type(t1))


# 2、单个数据元组
t2 = (10,)
print(type(t2))

# 3、单个数据元组不加逗号

t3 = (10)
print(type(t3)) #int


t4 = ('aaa')
print(type(t4))     #str

t5 =('aaa', 'bb', 'aaa')
print(type(t5))


# 元组常见操作
# 1、按下标查找数据
print(t1[0])

# 2、index() 查找数据所在的下标
print(t1.index(30))
print(t5.index('bb'))


# 3、count()
print(t5.count('aaa'))


# 4、len()
print(len(t5))

"""

t6 = ('aa', 'bb', 'cc', 'dd')

print(t6.index('aa'))
print(type(t6))
# t6[0] = 'aaa'

t7 = ('aa', 'bb', 'cc', 'dd', [1, 2, 3])
t7[4][1] = 'haha'
print(t7)




















