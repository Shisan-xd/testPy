
# in 判断指定数据在某个列表序列，在则返回True
# not in 判断指定数据不在某个列表序列，不在则返回True

name_list = ['TON', 'LILY', 'MAX', 'ROSE']

# 需求：注册邮箱，用户输入一个账号名字，判断用户名是否存在，存在提示用户，不存在可以注册
name = input('请输入名字：')

if name in name_list:
    # 提示不可以注册
    print(f'你输入的名字{name}已经存在不可以注册嗷---^-^')
else:
    # 提示可以注册
    print(f'你输入的名字{name}哇哦～ 可以注册嗷')





















