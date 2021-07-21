# 转换
# capitalize():将字符串第1个字符转换成大写
# title()     # 每个单词首字母大写
# upper()     # 所有单词小写-->大写
# lower()     # 所有单词大写-->小写              语法：变量名／字符串序列.lower()


# 删除空白
# rstrip()    #rstrip 踢除右边的空白
# lstrip()    #lstrip 剔除左边的空白
# strip()     #strip 剔除左右空白


# 字符串对齐
# ljust()：返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串。
# -- 语法：字符串序列.ljust(长度，填充字符)
# rjust()：右对齐
# center()：中间对齐


# mystr = 'It’s better to be alone than to be with someone you’re not happy to be with.'
# print(mystr.ljust(15,'*'))
# print(mystr.rjust(13,'-'))
# print(mystr.center(13,'-'))


# 判断    --判断真假，返回的数据类型为布尔类型：True 和 False
# -- 语法：字符串序列.startswith(子串，开始位置下标，结束位置下标)
# startswith()：检查字符串是否是以指定子串开头，是则返回True，否则返回False。如果设置开始和结束下标，则在指定范围内查找判断
# endswith():检查字符串是否是以指定子串结尾，是则返回True，否则返回False。
# isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
# isdigit()：如果字符串只包含数字则返回True，否则返回False
# isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
# isspace()：如果字符串中只包含空格，则返回True，否则返回False。

mystrs = '43214'
# 1、.startswith()   -- 判断字符串是否已指定子串开头
# print((mystr.lower()).startswith('i'))

# 2、.endswith()     -- 判断字符串是否已指定子串结尾
# print(mystr.endswith('th.'))

# isalpha()  --都是字母，返True
# print(mystr.isalpha())

# isdigit() --都是数字，返True
# print(mystrs.isdigit())

# isalnum()：--数字、字母或组合，返True
# mystrz = 'rfgdfgfds12'
# print(mystrz.isalnum())

# isspace()：都是空白，返True
mystrz = ' '
print(mystrz.isspace())









