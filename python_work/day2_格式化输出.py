age = 18 
name = "Tom"
weigh = 75.5
stu_id = 1
stu_id2 = 1000

#05-	格式化输出

# %06d,表示输出的路数显示位数,不足以0补全,超出当前位数则原样输出
# %.2f,表示小数点后显示的小数位数。

#1、今年我的年龄是X岁  -- 整数 %d
print("今年我的年龄是%d" %age)

#2、我的名字是X -- 字符串 %s
print('我的名字是%s' %name)

#3、我的体重是X公斤  -- 浮点数 %f
print('体重是%.2f公斤' %weigh)

#4、我的学号是X --%d 
print('我的学号是%d' %stu_id)

#4.1 我的学号是001
print('我的学号是%03d' %stu_id)
print('我的学号是%03d' %stu_id2)

#5、我的名字是X，今年X岁了
print('我的名字是%s，今年%d岁了' %(name,age))

#5.1 我的名字是X，今年X岁了
print('我的名字是%s，明年%d岁了' %(name,age+1))

#6、名字是X，年龄是X岁，体重是X斤，学号是
print('名字是%s，年龄是%d岁，体重是%.2f斤，学号是%03d' %(name,age,weigh,stu_id))



#07-	-f格式化字符串
print(f'我的名字{name},明年{age+1}岁了')

#08-	print结束符	
#结束格式：print('输出内容'，end=‘任意符号’)
print(f'我的名字{name},明年{age+1}岁了',end="...")
print(f'我的名字{name},明年{age+1}岁了')












