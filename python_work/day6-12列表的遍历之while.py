# 依次打印列表中的各个数据

name_list = ['TOM', 'LILY', 'JACK', 'ROSE']


"""
1、准备表示下标数据
2、循环while
    条件 n < 3 --循环遍历不适合写死，可以用len()表示
    遍历：依次按顺序访问到序列的每个数据
    n += 1
"""

n = 0
while n < len(name_list):
    print(name_list[n])     # 遍历时不能固定写死，填写随着程序循环推进变化的一个数据
    n += 1
