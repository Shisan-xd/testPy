"""
	if 条件:
	条件成立执行的代码
	……
"""


# if False:
# 	print('条件成立之行的代码1')
# print('12')



# if……lese……
# input接收到的数据类型是str，需要用int()转换数据类型

#age = int(input('请输入您的年龄：'))
"""
	if age >= 18:
	print(f'您的年龄是{age}，已经成年，可以上网')
else:
	print(f'您的年龄是{age}，未成年哦～ 快回家写作业')
print('系统关闭')"""



"""
	多重判断
	
	if 条件:
		print（'条件成立执行的代码'）
	elif：
		pritn（'条件2成立执行的代码'）
"""


"""
题目：
如果年龄小于18，为童工，不合法
如果年龄18-60之间，为合法工作年龄
如果年龄大于60为退休年龄

步骤：
1.用户输入自己的年龄：保存变量，--str
2.if做判断
3.输出提示信息：您输入的年龄是X，合法与否
"""
"""
age = int(input('请输入您的年龄：'))

if age < 18:
	print(f'您输入的年龄是{age},为童工，不合法哦～')
elif (age >= 18) and (age <= 60):
	print(f'您输入的年龄是{age},可以工作，合法哟～')
elif age > 60:
	print(f'您输入的年龄是{age},退休咯～')
"""

#条件新写法：
age = int(input('请输入您的年龄：'))

if age < 18:
	print(f'您输入的年龄是{age},为童工，不合法哦～')
elif 18 <= age <= 60:
	print(f'您输入的年龄是{age},可以工作，合法哟～')
elif age > 60:
	print(f'您输入的年龄是{age},退休咯～')

