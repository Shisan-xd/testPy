
# break
# 5个苹果吃了3个苹果 吃饱了 不吃了

i = 1

while i <= 5:
    if i == 3:
        print(f'准备吃第{i}个苹果 发现吃饱了 不吃了')
        break
    print(f'吃第{i}个苹果')
    i += 1

"""
# continue
# 5个苹果 吃到第二个发现一条大虫子 继续吃第三个苹果

i = 1

while i <= 5:
    if i == 3:
        print('吃出一个大虫子，这个苹果不吃了')
        #在continue之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
"""