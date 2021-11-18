# @Time     ：2021/10/19 17:03
# @Author   ：
# @File     ：day10_07元组拆包.py


# 拆包和交换变量值
# 拆包: 元组

def return_num():
    return 100, 200


num1, num2 = return_num()
print(num2)



# 拆包：字典     字典不支持下标
dict1 = {'name': 'hei', 'age': '12'}
a, b = dict1


print(a)    #取名称 key
print(dict1[a])     #取值value


