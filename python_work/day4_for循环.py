str1 = 'hei sha'
"""
for i in str1:  # i是str1的另一个命名
    if i == 's':
        break   #终止打印
    print(i)
"""


for i in str1:
    if i == 's':
        continue  # 终止当前一次循环，继续下一次循环 # break
    print(i)
