# 函数嵌套调用---多条横线
def print_line1():
    print('-' * 40)


# def print_lines(num):
#     i = 0
#     while i < num:
#         print_line1()
#         i += 1


# print_lines(3)


def print_lines1(bu):
    a = 0
    while a < bu:
        print_line1()
        a += 1


print_lines1(5)


# 嵌套调用之函数计算
# 函数求和计算
def sum_mua(a, b, c):
    return a + b + c


result = sum_mua(1, 2, 3)
print(result)


# 任意3个数求平均值计算
def average_num(a, b, c):
    sumRsult = sum_mua(a, b, c)
    return sumRsult / 3


average_num1 = average_num(10, 20, 30)
print("平均值是：%d" %average_num1)





















