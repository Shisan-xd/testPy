# @Time     ：2021/10/26 15:05
# @Author   ：
# @File     ：day10_10引用当作实参.py


def rest(a):
    print(a)        #打印a参数
    print(id(a))    #打印a参数的位置

    a += a          #a和a相加赋值给a
    print(a)        #打印a参数
    print(id(a))    #打印a参数的位置



# b = 323
# rest(b)   # 计算前后id相同


c = [11, 22]
rest(c)     # 计算前后id不相同




