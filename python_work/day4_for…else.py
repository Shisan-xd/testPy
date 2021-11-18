"""

语法：
for 临时变量 in 序列:
    重复执行代码
else:
    循环正常结束之后要执行的代码

"""


str1 = 'xixirei'

for he in str1:
    if he == 'i':
        continue    # break
    print(str1)
else:
    print('循环正常之后执行代码')



"""
总结:
    循环的作用：控制代码重复执行 

while语法：   
while 条件：
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    
while循环嵌套语法：
    while 条件1：
        条件1成立执行的代码
        ……
        while 条件2：
            条件2成立执行的代码
            …
            
for循环语法：
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
    
"""