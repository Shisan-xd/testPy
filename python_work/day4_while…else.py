"""
循环可以和else配合一起使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码

while…else
语法：
while 条件:
    条件成立重复执行的代码
else：
    循环正常结束之后要执行的代码

"""

s = 1
while s <= 5:
    if s == 3:
        s += 1
        continue
    print("sorry")
    s += 1
else:
    print('happy')