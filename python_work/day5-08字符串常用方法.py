

# 字符串的常操作方法有查找、修改和判断三大类

# 查找
# 所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数
# -- find(): 检测某个子串是否包含在这个字符串中，如果子串在字符串中，则返回这个子串开始的位置下标，否则则返回-1
# -- index()：检测某个子串是否包含在这个字符串中，如果子串在字符串中，返回这个子串开始的位置下标，否则则报异常
# -- count()：返回某个子串在字符串中出现的次数
# 语法：字符串序列.find(子串，开始位置下标，结束位置下标)  -- 开始和结束位置下标可以省略，表示在整个字符串序列中查找


# 操作函数的三个学习方向 -- 记住函数的单词  --记住函数的作用  --函数传递参数的方式（函数参数的写法）

mystr = 'Love is not a maybe thing. You know when you love someone'


# 1 .find()
# print(mystr.find('a'))  # 12
# print(mystr.find('a', 13, 20))  #15
# print(mystr.find('aA'))    #-1，表示'aA'子串不存在
# print((mystr.lower()).find('l', 1, 55))     #忽略大小写查找

# 2 .index()
# print(mystr.index('not'))   # 8
# print(mystr.index('not', 2, 20))   # 8
# print(mystr.index('nott', 2, 20))   # 如果index查找子串不存在，则报错ValueError: substring not found


# 3 .count()
# print(mystr.count('n'))     #5次  -- 统计mystr字符串中所有'n'的数量
# print(mystr.count('n', 2, 30))     #2次  -- 统计mystr字符串位置在2-30中'n'的数量
# print(mystr.count('nA'))     #0次  -- 表示mystr字符串中没有'nA'

# 4 .rfind()
# print(mystr.rfind('e'))

# 4 .rindex()
print(mystr.rindex('e1'))





