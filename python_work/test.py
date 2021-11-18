# @Time     ：2021/10/21 16:58
# @Author   ：
# @File     ：test.py


# a = [1, 2, 3, 4, 5]
# print(a[:100])
# print(a[:])
# print(a[-1:])
# print(a[0:])


res3 = 0
res1 = []
a = [[1, 2], [2, 3], [3, 4]]

for v in a:
    res2 = 0
    for s in v:
        res2 += s
    res1.append(res2)
    res3 += res2

print(res1)
print(res3)


# res = 0
# a = [1, 2, 3]
#
# for c in a:
#     # print(f'当前第{c}次循环的值是{a[c-1]}')
#     res = res+c
# print(res)


