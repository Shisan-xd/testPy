# @Time     ：2021/10/11 09:16
# @Author   ：
# @File     ：day10_05返回值作为参数传递.py

# -- 函数的参数
# # 1、定义两个函数；2、函数一有返回值50；函数二把返回值50作为参数传入（定义函数二要有形参）
# def T1():
#     return 5
#
#
# def T2(num):
#     print(num)
#
#
# # 先拿到函数一的返回值，再把返回值传到函数二
# result = T1()
# # print(result)
# T2(result)


# def r_e():
#     return 10
#     return 2
# # 此处只执行了一个return，是因为return可以退出当前函数，导致return下方代码不执行
#
#
# def r_e1(num):
#     print(num)
#
#
# result1 = r_e()
# r_e1(result1)







# -- 函数多返回值
# 一个函数多个返回值的写法
def r_n():
    return 1, 2     #返回的是一个元组


result = r_n()
print(result)


# return    后面可以直接书写 元组、列表、字典
def r_a():
    # return (1, 2)    # 元组
    # return [1, 2]   # 列表
    return {'name': 'Python', 'age': '12'}   # 字典


result = r_a()
print(result)























