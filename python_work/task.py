bicycles = ["trek",'cannondale','redline','specialized']

print (bicycles[0].title(),'-',bicycles[1].title())
print (bicycles[-1])

name =['zoie','max','will']

print (name[0],'早上好')
print (name[1],'早上好')
print (name[2],'早上好')

motorycles = ['honda','yamaha','suzuki']
print (motorycles)


#修改、删除和添加
motorycles[1] = 'dukadi' #修改列表里第一个元素
print (motorycles)
motorycles.append('ducati') #在列表末尾添加一个元素
print (motorycles)
del motorycles[0] #删除列表里第一个元素
print (motorycles)

#使用pop()方法删除元素
P_m = motorycles.pop()
print (motorycles)
print (P_m)

