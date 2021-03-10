start = "hello pytHon world!"
#大小写字母
print (start.title())  #首字母大写
print (start.upper())  #全大写
print (start.lower())  #全小写


#字符串存储变量
S = "13"
W = "14"
S_W = S + " " + W #方法一 使用+号拼接两个变量的字符
S_W1 = f"{S} {W}" #方法二 使用f“”的方法拼接两个变量的字符 赋值给S_W1

print (S_W1)


#删除空白
A = " Python "
print (A.rstrip()) #rstrip 踢除右边的空白
print (A.lstrip()) #lstrip 剔除左边的空白
print (A.strip()) #strio 剔除左右空白


# 