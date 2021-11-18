
# 函数的参数作用
# 需求：一个函数完成1和2的加法运算，如何书写程序?
# 1、函数：固定数据1 和 2加法
def add_num1():
    result = 1 + 2
    print(result)
add_num1()


# 2、参数形式传入真实数据    做加法运算
# 定义函数时，同时定义了接收用户数据的参数a和b，a和b是行参
def add_num2(a, b):
    result = a + b
    print(result)

# 调用函数时传入了真实的数据2和3，真实数据为实参
add_num2(2, 3)



