# 局部变量：
def TestA():
    a = 12
    print(a)


TestA()

# 全局变量:
C = 221

def TestB():
    print(C)


def TestC():
    print(C)


TestB()
TestC()
