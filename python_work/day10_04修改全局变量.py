a = 100


def T1():
    print(a)


def T2():
    # a = 20     #如果直接修改a=20，此时的a是局部变量还是全局变量呢？  --此时a是局部变量
    # print(a)
    global a    #声明a为全局变量
    a = 20
    print(a)


T1()
T2()
T1()


"""
总结：
    1、如果在函数里面直接把变量a=200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2、函数体内部修改全局变量：先global声明a为全局变量，再变量重新赋值

"""

