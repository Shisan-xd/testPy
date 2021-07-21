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

mystr = 'word'
# print(mystr.ljust(15,'*'))
# print(mystr.rjust(13,'-'))
# print(mystr.center(13,'-'))