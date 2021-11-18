# @Time     ：2021/10/19 17:28
# @Author   ：
# @File     ：day10_08交换变量的值.py


# 方法一
a = 10
b = 20



c = 0
c = a
a = b
b = c

print(a)
print(b)
print(c)


# 方法二
d, n = 1, 3
d, n = n, d

print(n)
print(d)
