# 打印星星号（正方形）
"""
a = 1
while a <= 1:
    i = 1
    while i <= 5:
        print('*****')
        i += 1
    a += 1
"""

s = 0
while s < 5:
    # 一行星星开始
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    # 一行星星结束：换行显示下一行
    print()
    s += 1
print('------------------')

# 打印星星号（三角形） 每行星星的个数和行号数相等
# s表示行号
s = 0
while s < 5:
    # 一行星星开始
    i = 0
    # i表示每行里面星星的分数，这个数字要和行号相等所以i要和s联动
    while i <= s:
        print('*', end='')
        i += 1
    # 一行星星结束：换行显示下一行
    print()
    s += 1
print('------------------')



