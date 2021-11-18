"""
1、出拳
    玩家：手动输入
    电脑：1.固定：剪刀    2.随机

2、判断输赢
    1.玩家赢
    2.平局
    3.电脑赢
"""

import random

# 1-出拳（电脑固定出拳）
# 1.玩家出拳
Player = int(input('请出拳 ：0-拳头；1-布；2-剪刀：'))
# 2.电脑出拳
computer = random.randint(0, 2)
print(computer)

# 2-判断输赢
# 1.玩家赢
if ((Player == 0) and (computer == 2)) or ((Player == 2) and (computer == 1)) or ((Player == 1) and (computer == 0)):
    print('玩家获胜')
# 2.平局
elif Player == computer:
    print('平局，再来一局')
# 3.除去前两种情况剩余，情况电脑获胜
else:
    print('电脑获胜')





