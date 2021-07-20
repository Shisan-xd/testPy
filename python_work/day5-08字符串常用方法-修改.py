
myst1 = 'Love is not a maybe thing. You know when you love someone'
op = '--------------------------'

# 1、replace()  #** replace函数有返回值，返回值是修改后的字符串
# myst11 = myst1.replace('s', 'S')
# myst11 = myst1.replace('s', 'M', 1)
# 替换次数如果超出子串出现次数，表示替换所有的子串
myst11 = myst1.replace('s', 'M', 20)
print(myst11)
print(myst11.count('s'))  # -- 统计myst11字符串序列李's'出现的字符

print('\n', op, '\n')

# **** 调用了relace函数，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# **** 说明 字符串是不可修改类型
# **** 数据是否可以改变划分为 可变类型 和 不可变类型

# 2、split() -- 分割 返回一个列表,会丢失分割符号
# list1 = (myst1.lower()).split('you')
list1 = (myst1.lower()).split('you', 1)
print(list1)

print('\n', op, '\n')

# 2、join() --合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc', 'dd']
mylist1 = '-'.join(mylist)
print(mylist1)

print('\n', op)