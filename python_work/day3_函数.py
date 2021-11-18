# # help(abs)有且仅有1个参数，多给会报错
# m = max(1 , 2 , 10)  # max函数返回最大的那个
# print(m)
#
# # 调用函数
# # hex()函数把一个整数转换成十六进制表示的字符串
# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))
# print(float(n1))  # float小数
#
#
# # ------定义函数 def
# def my_abs(x):
#     if x >= 3:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(5))
#
#
# # ------定义空函数
# def nop():
#     pass  # 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#
#
# print(nop)
#
# # def my_abs(x):
# # 	if  not isinstance (x,(int,float)):
# # 		raise TypeError('bad openrand type')
# # 	if x >= 0:
# # 		return x
# # 	else:
# # 		return -x
# # print(my_abs('A'))


import math  # 导入math包，并后续代码引用sin\cos等函数


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx, ny





def hello():
    print("Hello World!")


# hello()


# def H32():
#     print("HAHAH")
#
#
# H32()
#
#
# def area(width, height):
#     return width * height
#
#
# def print_welcome(name):
#     print("Welcome" , name)
#
#
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))
#
#
# def print_me(str):
#     print(str)
#     return
#
#
# print_me("1234")
#
#
# # 可写函数说明
# def chan_game(my_list):
#     """修改传入的列表"""
#     my_list.append([1, 2, 3, 4])
#     print("函数内取值：", my_list)
#     return
#
#
# # 调用 chan_game 函数
# my_list = [10, 20, 30]
# chan_game(my_list)
# print("函数外取值：" , my_list)
#
#
# def change(a):
#     print(id(a))  # 指向的是同一个对象
#     a = 10
#     print(id(a))  # 一个新对象
#
#
# a = 1
# print(id(a))
# change(a)
#
#
# def print_info(name, age):
#     """打印任何传入的字符串"""
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用print_info函数
# print_info(age=50, name="Runoob")
#
#
# def print_info1(name, age):
#     print('名字：', name)
#     print('年龄：', age)

