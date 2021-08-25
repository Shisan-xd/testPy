# 需求：有三个办公室，8位老师，随机分配到三个办公室
"""
步骤
1. 准备数据
    1.1 8个老师 --列表
    1.2 3个办公室 --列表
2. 随机分配老师到办公室
    ***随机分配
    就是把老师的名字写入到办公室列表（办公室列表追加老师名字数据）
3. 验证是否分配成功
    打印办公室详情信息，每个办公室的人数和对应老师名字

"""

# 1、准备数据
import random
teachers = ['TOM', 'LILY', 'JACK', 'ROSE', 'a', 'b', 'c', 'd', 'e', 'f',
             '1', '2', '3', '4', '5', '6']
offices = [[], [], []]
"""
# 2. 随机分配老师到办公室 --取每个老师的名字放到列表里
#    遍历老师列表数据
for name in teachers:   #此处teachers的内容已经赋值给name这个临时变量
    # xx[0]不能指定是具体某个下标 --随机
    # 列表追加数据 --append（选中）extend insert
    num = random.randint(0,2)
    offices[num].append(name)
# print(num)
# print(offices)

# 3. 验证是否分配成功
    # 打印办公室详情信息，每个办公室的人数和对应老师名字
i = 1

for office in offices:
    # 打印办公室人数 -- 子列表数据的个数 len()
    print(f'办公室{i}人数是{len(office)},老师分别是:{office}')
    # 打印老师的名字
    # print()   --每个子列表里面的名字个数不一定   --可再使用遍历，遍历子列表
    # for teacher in office:
        # print(teacher)
    i += 1
"""

n = 1

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
# print(offices)
for office in offices:
    print(f'办公室人数是{len(office)}，老师分别是：{office}')
    n += 1
